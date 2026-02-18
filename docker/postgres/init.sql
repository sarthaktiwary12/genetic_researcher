-- ExRNA Platform PostgreSQL Schema
-- This runs on first container startup to initialize the database.

-- Campaigns
CREATE TABLE IF NOT EXISTS campaigns (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    campaign_type VARCHAR(50) NOT NULL,
    crop VARCHAR(100),
    status VARCHAR(20) DEFAULT 'pending',
    progress FLOAT DEFAULT 0.0,
    current_stage VARCHAR(50),
    config JSONB,
    budget_limit FLOAT,
    total_cost FLOAT DEFAULT 0.0,
    error_message TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    completed_at TIMESTAMPTZ
);
CREATE INDEX IF NOT EXISTS ix_campaigns_status ON campaigns(status);
CREATE INDEX IF NOT EXISTS ix_campaigns_crop ON campaigns(crop);

-- API Cost Log
CREATE TABLE IF NOT EXISTS api_costs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    campaign_id UUID REFERENCES campaigns(id),
    provider VARCHAR(20) NOT NULL,
    model VARCHAR(100) NOT NULL,
    input_tokens INTEGER DEFAULT 0,
    output_tokens INTEGER DEFAULT 0,
    cost_usd FLOAT NOT NULL,
    task_category VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS ix_api_costs_provider ON api_costs(provider);
CREATE INDEX IF NOT EXISTS ix_api_costs_created ON api_costs(created_at);

-- Monthly Budget Aggregation
CREATE TABLE IF NOT EXISTS monthly_budget (
    id SERIAL PRIMARY KEY,
    year_month VARCHAR(7) UNIQUE NOT NULL,
    total_spend FLOAT DEFAULT 0.0,
    gemini_spend FLOAT DEFAULT 0.0,
    claude_spend FLOAT DEFAULT 0.0,
    budget_limit FLOAT DEFAULT 5000.0,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Cost tracking trigger: auto-update monthly_budget on api_costs INSERT
CREATE OR REPLACE FUNCTION update_monthly_budget()
RETURNS TRIGGER AS $$
DECLARE
    ym VARCHAR(7);
BEGIN
    ym := TO_CHAR(NEW.created_at, 'YYYY-MM');

    INSERT INTO monthly_budget (year_month, total_spend, gemini_spend, claude_spend)
    VALUES (ym, NEW.cost_usd,
            CASE WHEN NEW.provider = 'gemini' THEN NEW.cost_usd ELSE 0 END,
            CASE WHEN NEW.provider = 'claude' THEN NEW.cost_usd ELSE 0 END)
    ON CONFLICT (year_month) DO UPDATE SET
        total_spend = monthly_budget.total_spend + NEW.cost_usd,
        gemini_spend = monthly_budget.gemini_spend +
            CASE WHEN NEW.provider = 'gemini' THEN NEW.cost_usd ELSE 0 END,
        claude_spend = monthly_budget.claude_spend +
            CASE WHEN NEW.provider = 'claude' THEN NEW.cost_usd ELSE 0 END,
        updated_at = NOW();

    -- Also update campaign total_cost
    IF NEW.campaign_id IS NOT NULL THEN
        UPDATE campaigns
        SET total_cost = total_cost + NEW.cost_usd,
            updated_at = NOW()
        WHERE id = NEW.campaign_id;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_update_monthly_budget ON api_costs;
CREATE TRIGGER trg_update_monthly_budget
    AFTER INSERT ON api_costs
    FOR EACH ROW
    EXECUTE FUNCTION update_monthly_budget();

-- Experiments
CREATE TABLE IF NOT EXISTS experiments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    crop VARCHAR(100) NOT NULL,
    experiment_type VARCHAR(50),
    target_genes JSONB,
    protocol JSONB,
    status VARCHAR(20) DEFAULT 'planned',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Experiment Results
CREATE TABLE IF NOT EXISTS experiment_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    experiment_id UUID REFERENCES experiments(id),
    gene_id VARCHAR(100),
    measurement VARCHAR(100),
    value FLOAT,
    unit VARCHAR(50),
    conditions JSONB,
    notes TEXT,
    recorded_at TIMESTAMPTZ DEFAULT NOW()
);

-- Hypotheses
CREATE TABLE IF NOT EXISTS hypotheses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    text TEXT NOT NULL,
    crop VARCHAR(100),
    target_genes JSONB,
    evidence_level VARCHAR(20) DEFAULT 'inferred',
    source_campaign UUID,
    supporting_papers JSONB,
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Literature Alerts
CREATE TABLE IF NOT EXISTS literature_alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    pmid VARCHAR(20) UNIQUE NOT NULL,
    title TEXT NOT NULL,
    authors TEXT,
    journal VARCHAR(255),
    pub_date DATE,
    abstract TEXT,
    relevance_score FLOAT DEFAULT 0.0,
    relevance_reason TEXT,
    matched_keywords JSONB,
    matched_genes JSONB,
    claims_extracted JSONB,
    reviewed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS ix_literature_alerts_relevance ON literature_alerts(relevance_score);
CREATE INDEX IF NOT EXISTS ix_literature_alerts_reviewed ON literature_alerts(reviewed);

-- Initialize current month budget
INSERT INTO monthly_budget (year_month, budget_limit)
VALUES (TO_CHAR(NOW(), 'YYYY-MM'), 5000.0)
ON CONFLICT (year_month) DO NOTHING;
