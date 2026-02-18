/**
 * ExRNA Research Platform - Alpine.js Components
 */

const API_BASE = '/api';

// Navigation store
document.addEventListener('alpine:init', () => {
    Alpine.store('nav', { tab: 'campaigns' });

    // Bind nav buttons to store
    document.querySelectorAll('nav button').forEach(btn => {
        btn.addEventListener('click', () => {
            Alpine.store('nav').tab = btn.textContent.trim().toLowerCase().replace(/\s+/g, '_');
        });
    });
});

// Sync nav buttons with tab names
document.addEventListener('alpine:init', () => {
    const tabMap = {
        'Campaigns': 'campaigns',
        'Knowledge Explorer': 'knowledge',
        'Semantic Search': 'search',
        'Budget Tracker': 'budget',
        'Literature Alerts': 'literature',
    };
    document.querySelectorAll('nav button').forEach(btn => {
        const tab = tabMap[btn.textContent.trim()];
        if (tab) {
            btn.setAttribute('x-on:click', `$store.nav.tab = '${tab}'`);
            btn.setAttribute(':class', `{ active: $store.nav.tab === '${tab}' }`);
        }
    });
});

// --- Health Check ---
function healthCheck() {
    return {
        status: 'unknown',
        statusText: 'Checking...',
        async check() {
            try {
                const res = await fetch(`${API_BASE}/monitoring/health`);
                if (res.ok) {
                    this.status = 'ok';
                    this.statusText = 'Online';
                } else {
                    this.status = 'warning';
                    this.statusText = 'Degraded';
                }
            } catch {
                this.status = 'error';
                this.statusText = 'Offline';
            }
            // Re-check every 30s
            setTimeout(() => this.check(), 30000);
        }
    };
}

// --- Campaign Manager ---
function campaignManager() {
    return {
        campaigns: [],
        showCreate: false,
        form: {
            name: '',
            campaign_type: 'full_crop_analysis',
            crop: 'spinach',
        },
        async load() {
            try {
                const res = await fetch(`${API_BASE}/campaigns/`);
                if (res.ok) {
                    const data = await res.json();
                    this.campaigns = data.campaigns || [];
                }
            } catch (e) {
                console.error('Failed to load campaigns:', e);
            }
            // Auto-refresh every 10s
            setTimeout(() => this.load(), 10000);
        },
        async create() {
            try {
                const res = await fetch(`${API_BASE}/campaigns/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(this.form),
                });
                if (res.ok) {
                    this.showCreate = false;
                    this.form.name = '';
                    await this.load();
                }
            } catch (e) {
                console.error('Failed to create campaign:', e);
            }
        }
    };
}

// --- Knowledge Explorer ---
function knowledgeExplorer() {
    return {
        genes: [],
        filter: { pathway: '', priority: '' },
        async loadGenes() {
            try {
                const params = new URLSearchParams();
                if (this.filter.pathway) params.set('pathway', this.filter.pathway);
                if (this.filter.priority) params.set('priority', this.filter.priority);
                const res = await fetch(`${API_BASE}/knowledge/genes?${params}`);
                if (res.ok) {
                    const data = await res.json();
                    this.genes = data.records || data;
                }
            } catch (e) {
                console.error('Failed to load genes:', e);
            }
        }
    };
}

// --- Semantic Search ---
function semanticSearch() {
    return {
        query: '',
        collection: 'gene_narratives',
        results: [],
        searched: false,
        async search() {
            if (!this.query.trim()) return;
            this.searched = true;
            try {
                const res = await fetch(`${API_BASE}/search/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        query: this.query,
                        collection: this.collection,
                        n_results: 10,
                    }),
                });
                if (res.ok) {
                    const data = await res.json();
                    this.results = data.results || [];
                }
            } catch (e) {
                console.error('Search failed:', e);
                this.results = [];
            }
        }
    };
}

// --- Budget Tracker ---
function budgetTracker() {
    return {
        budget: {
            total_spend: 0,
            gemini_spend: 0,
            claude_spend: 0,
            budget_limit: 5000,
            fraction: 0,
        },
        async load() {
            try {
                const res = await fetch(`${API_BASE}/budget/`);
                if (res.ok) {
                    this.budget = await res.json();
                    this.renderChart();
                }
            } catch (e) {
                console.error('Failed to load budget:', e);
            }
        },
        renderChart() {
            const ctx = document.getElementById('costChart');
            if (!ctx) return;
            new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Gemini', 'Claude', 'Remaining'],
                    datasets: [{
                        data: [
                            this.budget.gemini_spend,
                            this.budget.claude_spend,
                            Math.max(0, this.budget.budget_limit - this.budget.total_spend),
                        ],
                        backgroundColor: ['#4ecdc4', '#6c5ce7', '#e0e0e0'],
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'bottom' },
                    }
                }
            });
        }
    };
}

// --- Literature Alerts ---
function literatureAlerts() {
    return {
        alerts: [],
        showReviewed: false,
        async load() {
            try {
                const params = new URLSearchParams();
                if (!this.showReviewed) params.set('reviewed', 'false');
                const res = await fetch(`${API_BASE}/monitoring/literature-alerts?${params}`);
                if (res.ok) {
                    const data = await res.json();
                    this.alerts = data.alerts || data || [];
                }
            } catch (e) {
                console.error('Failed to load alerts:', e);
            }
        }
    };
}
