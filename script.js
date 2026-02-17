// ===============================================
// Main JavaScript for Marginal Reputation Demo
// ===============================================

// Tab Navigation
document.addEventListener('DOMContentLoaded', function() {
    const tabLinks = document.querySelectorAll('.tab-link');
    const contentArea = document.getElementById('content-area');
    
    // Load initial tab
    loadTab('intro');
    
    // Tab click handlers
    tabLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const tabName = this.dataset.tab;
            
            // Update active state
            tabLinks.forEach(l => l.classList.remove('active'));
            this.classList.add('active');
            
            // Load content
            loadTab(tabName);
        });
    });
    
    async function loadTab(tabName) {
        try {
            const response = await fetch(`${tabName}.html`);
            const html = await response.text();
            contentArea.innerHTML = html;
            
            // Initialize tab-specific functionality
            if (tabName === 'original') {
                initOriginalTab();
            } else if (tabName === 'markov') {
                initMarkovTab();
            } else if (tabName === 'comparison') {
                initComparisonTab();
            } else if (tabName === 'example') {
                initExampleTab();
            } else if (tabName === 'author-review') {
                initAuthorReviewTab();
            } else if (tabName === 'revision') {
                initRevisionTab();
            } else if (tabName === 'prompt-history') {
                initPromptHistoryTab();
            }
            
            // Re-render MathJax
            if (window.MathJax) {
                MathJax.typesetPromise();
            }
        } catch (error) {
            console.error('Error loading tab:', error);
            contentArea.innerHTML = '<p>Error loading content.</p>';
        }
    }
});

// ===============================================
// Original Tab Functionality
// ===============================================

function initOriginalTab() {
    // Deterrence game parameters
    const piSlider = document.getElementById('pi-slider');
    const xSlider = document.getElementById('x-slider');
    const ySlider = document.getElementById('y-slider');
    
    const piValue = document.getElementById('pi-value');
    const xValue = document.getElementById('x-value');
    const yValue = document.getElementById('y-value');
    
    piSlider.addEventListener('input', updateOriginal);
    xSlider.addEventListener('input', updateOriginal);
    ySlider.addEventListener('input', updateOriginal);
    
    // KL bound parameters
    const mu0Slider = document.getElementById('mu0-slider');
    const etaSlider = document.getElementById('eta-slider');
    
    const mu0Value = document.getElementById('mu0-value');
    const etaValue = document.getElementById('eta-value');
    
    mu0Slider.addEventListener('input', updateKLBound);
    etaSlider.addEventListener('input', updateKLBound);
    
    function updateOriginal() {
        const pi = parseFloat(piSlider.value);
        const x = parseFloat(xSlider.value);
        const y = parseFloat(ySlider.value);
        
        piValue.textContent = pi.toFixed(2);
        xValue.textContent = x.toFixed(2);
        yValue.textContent = y.toFixed(2);
        
        document.getElementById('payoff-gf').textContent = `x = ${x.toFixed(2)}`;
        document.getElementById('payoff-ba').textContent = `y = ${y.toFixed(2)}`;
        
        // Supermodularity check
        const isSupermodular = (x + y) < 1;
        const resultText = isSupermodular
            ? `✅ <strong>Supermodular</strong> (x + y = ${(x+y).toFixed(2)} < 1): Strategy is confound-defeating. Commitment payoff V(s₁*) = π(G) = ${pi.toFixed(3)}`
            : `❌ <strong>Submodular</strong> (x + y = ${(x+y).toFixed(2)} > 1): Strategy is NOT confound-defeating. Long-run player gets minmax payoff.`;
        
        document.getElementById('result-text').innerHTML = resultText;
        
        // Plot commitment payoff
        plotCommitmentPayoff(pi, x, y);
    }
    
    function updateKLBound() {
        const mu0 = parseFloat(mu0Slider.value);
        const eta = parseFloat(etaSlider.value);
        
        mu0Value.textContent = mu0.toFixed(3);
        etaValue.textContent = eta.toFixed(2);
        
        const klBound = Math.round(-2 * Math.log(mu0) / (eta * eta));
        document.getElementById('kl-bound-value').textContent = klBound;
        
        plotKLBound(mu0, eta);
    }
    
    updateOriginal();
    updateKLBound();
}

function plotCommitmentPayoff(pi, x, y) {
    const piValues = [];
    const payoffs = [];
    
    for (let p = 0.1; p <= 0.9; p += 0.01) {
        piValues.push(p);
        payoffs.push(p); // V(s_1*) = pi(G) in supermodular case
    }
    
    const trace1 = {
        x: piValues,
        y: payoffs,
        type: 'scatter',
        mode: 'lines',
        name: 'V(s₁*) = π(G)',
        line: { color: 'blue', width: 2 }
    };
    
    const trace2 = {
        x: [pi],
        y: [pi],
        type: 'scatter',
        mode: 'markers',
        name: 'Current',
        marker: { size: 12, color: 'red' }
    };
    
    const layout = {
        title: 'Commitment Payoff vs. π(G)',
        xaxis: { title: 'π(G) (Probability of Good State)' },
        yaxis: { title: 'Commitment Payoff V(s₁*)' },
        hovermode: 'closest'
    };
    
    Plotly.newPlot('commitment-payoff-plot', [trace1, trace2], layout);
}

function plotKLBound(mu0, eta) {
    const etaValues = [];
    const bounds = [];
    
    for (let e = 0.01; e <= 0.3; e += 0.005) {
        etaValues.push(e);
        bounds.push(-2 * Math.log(mu0) / (e * e));
    }
    
    const trace = {
        x: etaValues,
        y: bounds,
        type: 'scatter',
        mode: 'lines',
        name: 'T̄(η, μ₀)',
        line: { color: 'green', width: 2 }
    };
    
    const traceMarker = {
        x: [eta],
        y: [-2 * Math.log(mu0) / (eta * eta)],
        type: 'scatter',
        mode: 'markers',
        name: 'Current',
        marker: { size: 12, color: 'red' }
    };
    
    const layout = {
        title: `KL-Divergence Bound (μ₀ = ${mu0.toFixed(3)})`,
        xaxis: { title: 'Tolerance η' },
        yaxis: { title: 'Maximum Distinguishing Periods T̄', type: 'log' },
        hovermode: 'closest'
    };
    
    Plotly.newPlot('kl-bound-plot', [trace, traceMarker], layout);
}

// ===============================================
// Markov Tab Functionality
// ===============================================

function initMarkovTab() {
    const alphaSlider = document.getElementById('alpha-slider');
    const betaSlider = document.getElementById('beta-slider');
    
    const alphaValue = document.getElementById('alpha-value');
    const betaValue = document.getElementById('beta-value');
    
    alphaSlider.addEventListener('input', updateMarkov);
    betaSlider.addEventListener('input', updateMarkov);
    
    function updateMarkov() {
        const alpha = parseFloat(alphaSlider.value);
        const beta = parseFloat(betaSlider.value);
        
        alphaValue.textContent = alpha.toFixed(2);
        betaValue.textContent = beta.toFixed(2);
        
        // Update transition matrix
        document.getElementById('trans-gg').textContent = (1 - alpha).toFixed(2);
        document.getElementById('trans-gb').textContent = alpha.toFixed(2);
        document.getElementById('trans-bg').textContent = beta.toFixed(2);
        document.getElementById('trans-bb').textContent = (1 - beta).toFixed(2);
        
        // Stationary distribution
        const piG = beta / (alpha + beta);
        const piB = alpha / (alpha + beta);
        
        document.getElementById('stat-g').textContent = piG.toFixed(3);
        document.getElementById('stat-b').textContent = piB.toFixed(3);
        
        // Lifted distribution
        document.getElementById('lifted-gg').textContent = (piG * (1 - alpha)).toFixed(4);
        document.getElementById('lifted-gb').textContent = (piB * beta).toFixed(4);
        document.getElementById('lifted-bg').textContent = (piG * alpha).toFixed(4);
        document.getElementById('lifted-bb').textContent = (piB * (1 - beta)).toFixed(4);
        
        // Update displays
        document.getElementById('alpha-mix-display').textContent = alpha.toFixed(2);
        document.getElementById('beta-mix-display').textContent = beta.toFixed(2);
        
        // Plot trajectories
        plotMarkovTrajectory(alpha, beta);
        plotLiftedDistribution(alpha, beta);
        plotMixingTime(alpha, beta);
    }
    
    updateMarkov();
}

function plotMarkovTrajectory(alpha, beta) {
    // Simulate Markov chain
    const n = 100;
    const trajectory = [Math.random() < beta/(alpha+beta) ? 1 : 0];
    
    for (let i = 1; i < n; i++) {
        const prev = trajectory[i-1];
        if (prev === 1) {
            trajectory.push(Math.random() < (1-alpha) ? 1 : 0);
        } else {
            trajectory.push(Math.random() < beta ? 1 : 0);
        }
    }
    
    const trace = {
        y: trajectory,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'State (1=G, 0=B)',
        line: { color: 'purple', width: 1 },
        marker: { size: 4 }
    };
    
    const layout = {
        title: 'Sample Markov Chain Trajectory',
        xaxis: { title: 'Period t' },
        yaxis: { title: 'State (1=G, 0=B)', tickvals: [0, 1], ticktext: ['B', 'G'] },
        hovermode: 'closest'
    };
    
    Plotly.newPlot('markov-trajectory-plot', [trace], layout);
}

function plotLiftedDistribution(alpha, beta) {
    const piG = beta / (alpha + beta);
    const piB = alpha / (alpha + beta);
    
    const states = ['(G,G)', '(G,B)', '(B,G)', '(B,B)'];
    const probs = [
        piG * (1 - alpha),
        piB * beta,
        piG * alpha,
        piB * (1 - beta)
    ];
    
    const trace = {
        x: states,
        y: probs,
        type: 'bar',
        marker: { color: ['#3498db', '#9b59b6', '#e74c3c', '#f39c12'] }
    };
    
    const layout = {
        title: 'Lifted State Stationary Distribution',
        xaxis: { title: 'Lifted State θ̃ = (θₜ, θₜ₋₁)' },
        yaxis: { title: 'Probability ρ̃(θ̃)' }
    };
    
    Plotly.newPlot('lifted-distribution-plot', [trace], layout);
}

function plotMixingTime(alpha, beta) {
    // Approximate mixing using matrix powers
    const steps = 50;
    const times = [];
    const dists = [];
    
    const piG = beta / (alpha + beta);
    
    let dist = [1, 0]; // Start from G
    for (let t = 0; t <= steps; t++) {
        times.push(t);
        dists.push(dist[0]);
        
        // Update distribution
        const newDist = [
            dist[0] * (1 - alpha) + dist[1] * beta,
            dist[0] * alpha + dist[1] * (1 - beta)
        ];
        dist = newDist;
    }
    
    const trace1 = {
        x: times,
        y: dists,
        type: 'scatter',
        mode: 'lines',
        name: 'P(G | start from G)',
        line: { color: 'blue', width: 2 }
    };
    
    const trace2 = {
        x: times,
        y: Array(times.length).fill(piG),
        type: 'scatter',
        mode: 'lines',
        name: 'Stationary π(G)',
        line: { color: 'red', width: 2, dash: 'dash' }
    };
    
    const layout = {
        title: 'Mixing to Stationary Distribution',
        xaxis: { title: 'Time Steps' },
        yaxis: { title: 'P(State = G)' },
        hovermode: 'closest'
    };
    
    Plotly.newPlot('mixing-time-plot', [trace1, trace2], layout);
}

// ===============================================
// Comparison Tab Functionality
// ===============================================

function initComparisonTab() {
    const compPiSlider = document.getElementById('comp-pi-slider');
    const compAlphaSlider = document.getElementById('comp-alpha-slider');
    const compBetaSlider = document.getElementById('comp-beta-slider');
    
    compPiSlider.addEventListener('input', updateComparison);
    compAlphaSlider.addEventListener('input', updateComparison);
    compBetaSlider.addEventListener('input', updateComparison);
    
    function updateComparison() {
        const pi = parseFloat(compPiSlider.value);
        const alpha = parseFloat(compAlphaSlider.value);
        const beta = parseFloat(compBetaSlider.value);
        
        document.getElementById('comp-pi-value').textContent = pi.toFixed(3);
        document.getElementById('comp-alpha-value').textContent = alpha.toFixed(2);
        document.getElementById('comp-beta-value').textContent = beta.toFixed(2);
        
        const markovPi = beta / (alpha + beta);
        
        document.getElementById('comp-iid-pi').textContent = pi.toFixed(3);
        document.getElementById('comp-iid-v').textContent = pi.toFixed(3);
        document.getElementById('comp-markov-pi').textContent = markovPi.toFixed(3);
        document.getElementById('comp-markov-v').textContent = markovPi.toFixed(3);
        document.getElementById('comp-diff-pi').textContent = (markovPi - pi).toFixed(3);
        document.getElementById('comp-diff-v').textContent = (markovPi - pi).toFixed(3);
        
        plotComparisonPayoff(pi, alpha, beta);
        plotMixingComparison();
    }
    
    updateComparison();
}

function plotComparisonPayoff(pi, alpha, beta) {
    const alphaVals = [];
    const betaVals = [];
    const piMarkov = [];
    
    for (let a = 0.05; a <= 0.95; a += 0.05) {
        for (let b = 0.05; b <= 0.95; b += 0.05) {
            alphaVals.push(a);
            betaVals.push(b);
            piMarkov.push(b / (a + b));
        }
    }
    
    const trace = {
        x: alphaVals,
        y: betaVals,
        z: piMarkov,
        type: 'scatter3d',
        mode: 'markers',
        marker: {
            size: 3,
            color: piMarkov,
            colorscale: 'Viridis',
            showscale: true,
            colorbar: { title: 'π(G)' }
        }
    };
    
    const layout = {
        title: 'Stationary π(G) vs. Transition Rates',
        scene: {
            xaxis: { title: 'α (G→B)' },
            yaxis: { title: 'β (B→G)' },
            zaxis: { title: 'π(G)' }
        }
    };
    
    Plotly.newPlot('comparison-payoff-plot', [trace], layout);
}

function plotMixingComparison() {
    const persistence = [];
    const mixing = [];
    
    for (let p = 0; p <= 1; p += 0.05) {
        const alpha = 0.5 * (1 - p);
        const beta = 0.5 * (1 - p);
        const eigenval = Math.max(Math.abs(1 - alpha - beta), 0);
        const mixTime = eigenval > 0 ? -1 / Math.log(eigenval) : 1;
        
        persistence.push(p);
        mixing.push(mixTime);
    }
    
    const trace = {
        x: persistence,
        y: mixing,
        type: 'scatter',
        mode: 'lines',
        line: { color: 'orange', width: 3 }
    };
    
    const layout = {
        title: 'Mixing Time vs. Persistence',
        xaxis: { title: 'Persistence (0=i.i.d., 1=perfect)' },
        yaxis: { title: 'Mixing Time τ_mix', type: 'log' }
    };
    
    Plotly.newPlot('mixing-comparison-plot', [trace], layout);
}

// ===============================================
// Example Tab Functionality
// ===============================================

function initExampleTab() {
    const exAlphaSlider = document.getElementById('ex-alpha-slider');
    const exBetaSlider = document.getElementById('ex-beta-slider');
    const exXSlider = document.getElementById('ex-x-slider');
    const exYSlider = document.getElementById('ex-y-slider');
    const exMu0Slider = document.getElementById('ex-mu0-slider');
    const exEtaSlider = document.getElementById('ex-eta-slider');
    
    exAlphaSlider.addEventListener('input', updateExample);
    exBetaSlider.addEventListener('input', updateExample);
    exXSlider.addEventListener('input', updateExample);
    exYSlider.addEventListener('input', updateExample);
    exMu0Slider.addEventListener('input', updateExampleKL);
    exEtaSlider.addEventListener('input', updateExampleKL);
    
    function updateExample() {
        const alpha = parseFloat(exAlphaSlider.value);
        const beta = parseFloat(exBetaSlider.value);
        const x = parseFloat(exXSlider.value);
        const y = parseFloat(exYSlider.value);
        
        document.getElementById('ex-alpha-value').textContent = alpha.toFixed(2);
        document.getElementById('ex-beta-value').textContent = beta.toFixed(2);
        document.getElementById('ex-x-value').textContent = x.toFixed(2);
        document.getElementById('ex-y-value').textContent = y.toFixed(2);
        
        document.getElementById('ex-payoff-gf').textContent = x.toFixed(2);
        document.getElementById('ex-payoff-ba').textContent = y.toFixed(2);
        
        // Supermodularity
        const isSupermodular = (x + y) < 1;
        const superText = isSupermodular
            ? `✅ <strong>Supermodular</strong> (x + y = ${(x+y).toFixed(2)} < 1): Deterrence strategy is confound-defeating.`
            : `❌ <strong>Submodular</strong> (x + y = ${(x+y).toFixed(2)} > 1): Deterrence strategy is NOT confound-defeating.`;
        document.getElementById('ex-supermodular-text').innerHTML = superText;
        
        // Stationary distribution
        const piG = beta / (alpha + beta);
        const piB = alpha / (alpha + beta);
        
        document.getElementById('ex-stat-g').textContent = piG.toFixed(3);
        document.getElementById('ex-stat-b').textContent = piB.toFixed(3);
        
        // Persistence level
        const persistence = (1 - alpha - beta) / 2;
        let persistenceText;
        if (persistence < 0.2) persistenceText = 'Low (near i.i.d.)';
        else if (persistence < 0.5) persistenceText = 'Moderate';
        else persistenceText = 'High';
        document.getElementById('ex-persistence').textContent = persistenceText;
        
        // Lifted distribution
        document.getElementById('ex-lifted-gg').textContent = (piG * (1 - alpha)).toFixed(4);
        document.getElementById('ex-lifted-gb').textContent = (piB * beta).toFixed(4);
        document.getElementById('ex-lifted-bg').textContent = (piG * alpha).toFixed(4);
        document.getElementById('ex-lifted-bb').textContent = (piB * (1 - beta)).toFixed(4);
        
        // Commitment payoff
        document.getElementById('ex-commitment-payoff').textContent = piG.toFixed(3);
        
        // Economic interpretation
        document.getElementById('ex-interp-alpha').textContent = alpha.toFixed(2);
        document.getElementById('ex-interp-beta').textContent = beta.toFixed(2);
        document.getElementById('ex-avg-calm').textContent = (1 / alpha).toFixed(1);
        document.getElementById('ex-avg-attack').textContent = (1 / beta).toFixed(1);
        
        // Plots
        plotExampleTrajectory(alpha, beta);
        plotExampleLifted(alpha, beta);
        plotExamplePersistence();
        
        updateExampleKL();
    }
    
    function updateExampleKL() {
        const mu0 = parseFloat(exMu0Slider.value);
        const eta = parseFloat(exEtaSlider.value);
        
        document.getElementById('ex-mu0-value').textContent = mu0.toFixed(3);
        document.getElementById('ex-eta-value').textContent = eta.toFixed(2);
        
        const klBound = Math.round(-2 * Math.log(mu0) / (eta * eta));
        
        document.getElementById('ex-kl-mu0').textContent = mu0.toFixed(3);
        document.getElementById('ex-kl-eta').textContent = eta.toFixed(2);
        document.getElementById('ex-kl-bound').textContent = klBound;
    }
    
    updateExample();
}

function plotExampleTrajectory(alpha, beta) {
    const n = 100;
    const piG = beta / (alpha + beta);
    const trajectory = [Math.random() < piG ? 1 : 0];
    
    for (let i = 1; i < n; i++) {
        const prev = trajectory[i-1];
        if (prev === 1) {
            trajectory.push(Math.random() < (1-alpha) ? 1 : 0);
        } else {
            trajectory.push(Math.random() < beta ? 1 : 0);
        }
    }
    
    const trace = {
        y: trajectory,
        type: 'scatter',
        mode: 'lines+markers',
        name: 'Attack State',
        line: { color: 'red', width: 1.5 },
        marker: { size: 4 },
        fill: 'tozeroy',
        fillcolor: 'rgba(231, 76, 60, 0.2)'
    };
    
    const layout = {
        title: 'Sample Attack Trajectory (1=Calm, 0=Attack)',
        xaxis: { title: 'Period t' },
        yaxis: { title: 'State', tickvals: [0, 1], ticktext: ['Attack', 'Calm'] }
    };
    
    Plotly.newPlot('ex-trajectory-plot', [trace], layout);
}

function plotExampleLifted(alpha, beta) {
    const piG = beta / (alpha + beta);
    const piB = alpha / (alpha + beta);
    
    const states = ['(G,G)<br>Calm continues', '(G,B)<br>Attack ends', '(B,G)<br>Attack begins', '(B,B)<br>Attack persists'];
    const probs = [
        piG * (1 - alpha),
        piB * beta,
        piG * alpha,
        piB * (1 - beta)
    ];
    
    const trace = {
        x: states,
        y: probs,
        type: 'bar',
        marker: { color: ['#2ecc71', '#3498db', '#e74c3c', '#e67e22'] }
    };
    
    const layout = {
        title: 'Lifted State Distribution (Transition Patterns)',
        xaxis: { title: 'Lifted State (θₜ, θₜ₋₁)' },
        yaxis: { title: 'Stationary Probability' }
    };
    
    Plotly.newPlot('ex-lifted-plot', [trace], layout);
}

function plotExamplePersistence() {
    const alphaVals = [];
    const payoffs = [];
    const mixTimes = [];
    
    for (let a = 0.05; a <= 0.95; a += 0.05) {
        const b = 0.5; // Fix beta
        alphaVals.push(a);
        payoffs.push(b / (a + b));
        
        const eigenval = Math.max(1 - a - b, 0);
        mixTimes.push(eigenval > 0 ? -1 / Math.log(eigenval) : 1);
    }
    
    const trace1 = {
        x: alphaVals,
        y: payoffs,
        type: 'scatter',
        mode: 'lines',
        name: 'Commitment Payoff',
        yaxis: 'y',
        line: { color: 'blue', width: 3 }
    };
    
    const trace2 = {
        x: alphaVals,
        y: mixTimes,
        type: 'scatter',
        mode: 'lines',
        name: 'Mixing Time',
        yaxis: 'y2',
        line: { color: 'orange', width: 3, dash: 'dash' }
    };
    
    const layout = {
        title: 'Commitment Payoff and Mixing Time vs. α (β = 0.5)',
        xaxis: { title: 'α (G→B transition rate)' },
        yaxis: { title: 'Commitment Payoff V(s₁*)', side: 'left' },
        yaxis2: { title: 'Mixing Time τ_mix', side: 'right', overlaying: 'y' }
    };
    
    Plotly.newPlot('ex-persistence-plot', [trace1, trace2], layout);
}

// ===============================================
// Prompt History Tab Functionality
// ===============================================

const PROMPT_FILES = [
    { id: '67b86cd4-146c-42a1-aa17-5d027ed88b38', size: '44K' },
    { id: 'c5083db6-e06c-42e4-80a4-80f954d8d282', size: '60K' },
    { id: '0415a79b-369d-49ea-813a-d86501b1afae', size: '24K' },
    { id: '00db3062-78f8-43af-84b0-1d7bfab41c15', size: '39K' },
    { id: '439ed1fc-6ac2-4b22-8a46-245d71b90f96', size: '66K' },
    { id: '8f39fab3-3f8d-486b-802d-8744444c6f2e', size: '86K' },
    { id: 'b540e723-991b-4036-89f9-28a860364864', size: '69K' },
    { id: '94eb98ad-3e42-4d4d-9e32-65f01fc2416d', size: '23K' },
    { id: '37c9635e-ffa1-45dc-bf2d-db130079dcbe', size: '97K' },
    { id: '05901914-1f2f-41ff-b7fc-2d454c04c8a9', size: '77K' },
    { id: 'cd01fc35-7e6d-47e9-943f-b1362eded047', size: '149K' },
    { id: 'b1f67f41-ac2c-4f9d-9fed-7201f74c8424', size: '6K' },
    { id: '5959a99a-05d9-4e23-ab48-73d96d2a3417', size: '64K' },
    { id: '14f9ea16-84d3-4de0-83bd-aeeb7b4c0098', size: '7K' },
    { id: '628e5ccb-256f-4e04-b418-ce60072c3e35', size: 'new' }
];

function initPromptHistoryTab() {
    const cardsGrid = document.getElementById('prompt-cards-grid');
    const modal = document.getElementById('transcript-modal');
    const modalClose = document.querySelector('.modal-close');
    
    if (!cardsGrid) {
        console.error('prompt-cards-grid not found');
        return;
    }

    // Update session count
    const countEl = document.getElementById('ph-total-count');
    if (countEl) countEl.textContent = PROMPT_FILES.length;
    
    // Clear existing cards
    cardsGrid.innerHTML = '';
    
    // Load each prompt file
    PROMPT_FILES.forEach((file, index) => {
        loadPromptCard(file, index, cardsGrid);
    });
    
    // Close modal handlers
    if (modalClose) {
        modalClose.addEventListener('click', () => {
            if (modal) modal.style.display = 'none';
        });
    }
    
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
}

async function loadPromptCard(file, index, container) {
    try {
        const response = await fetch(`promptHistory/${file.id}.md`);
        const content = await response.text();
        
        // Extract summary and metadata
        const metadata = extractMetadata(content, file.id);
        
        // Create card
        const card = document.createElement('div');
        card.className = 'prompt-card';
        card.innerHTML = `
            <div class="prompt-card-header">
                <div>
                    <div class="prompt-card-title">Agent Session ${index + 1}</div>
                    <div class="prompt-card-id">${file.id.substring(0, 8)}...</div>
                </div>
                <div class="prompt-card-size">${file.size}</div>
            </div>
            <div class="prompt-card-summary">${metadata.summary}</div>
            <div class="prompt-card-meta">
                <div class="prompt-card-stat">
                    <span class="prompt-card-stat-icon">💬</span>
                    <span>${metadata.messageCount} messages</span>
                </div>
                <div class="prompt-card-stat">
                    <span class="prompt-card-stat-icon">🔧</span>
                    <span>${metadata.toolCalls} tool calls</span>
                </div>
                <div class="prompt-card-stat">
                    <span class="prompt-card-stat-icon">📝</span>
                    <span>${metadata.filesChanged} files</span>
                </div>
            </div>
        `;
        
        card.addEventListener('click', () => {
            openTranscriptModal(file, content, index);
        });
        
        container.appendChild(card);
    } catch (error) {
        console.error(`Error loading prompt file ${file.id}:`, error);
    }
}

function extractMetadata(content, fileId) {
    // Count messages
    const userMatches = content.match(/^user:/gm) || [];
    const assistantMatches = content.match(/^assistant:/gm) || [];
    const messageCount = userMatches.length + assistantMatches.length;
    
    // Count tool calls
    const toolCallMatches = content.match(/\[Tool call\]/g) || [];
    const toolCalls = toolCallMatches.length;
    
    // Extract files changed (look for Write, StrReplace, etc.)
    const writeMatches = content.match(/path: ([^\n]+)/g) || [];
    const uniqueFiles = new Set(writeMatches.map(m => m.replace('path: ', '').trim()));
    const filesChanged = uniqueFiles.size;
    
    // Extract summary from first user message
    const firstUserMatch = content.match(/user:\s*\n?(.*?)(?=\nassistant:|$)/s);
    let summary = 'Agent chat transcript';
    
    if (firstUserMatch) {
        const userContent = firstUserMatch[1].trim();
        // Remove image tags and other metadata
        const cleanContent = userContent
            .replace(/<image_files>[\s\S]*?<\/image_files>/g, '')
            .replace(/<user_query>([\s\S]*?)<\/user_query>/g, '$1')
            .replace(/\[Image\]/g, '')
            .replace(/\n{2,}/g, ' ')
            .trim();
        
        // Get first meaningful text (up to 200 chars)
        if (cleanContent.length > 0) {
            summary = cleanContent.substring(0, 200) + (cleanContent.length > 200 ? '...' : '');
        }
    }
    
    // Determine agent name if present
    const agentMatch = content.match(/You are agent (\d+)/i);
    if (agentMatch) {
        summary = `Agent ${agentMatch[1]}: ${summary}`;
    }
    
    return {
        summary,
        messageCount,
        toolCalls,
        filesChanged
    };
}

function openTranscriptModal(file, content, index) {
    const modal = document.getElementById('transcript-modal');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    
    if (!modal || !modalTitle || !modalBody) return;
    
    modalTitle.textContent = `Agent Session ${index + 1} - ${file.id.substring(0, 8)}...`;
    
    // Parse and format the transcript
    const formattedContent = formatTranscript(content);
    modalBody.innerHTML = formattedContent;
    
    modal.style.display = 'block';
}

function formatTranscript(content) {
    let html = '';
    
    // Split by user/assistant messages
    const lines = content.split('\n');
    let currentRole = null;
    let currentContent = [];
    let inThinking = false;
    let inToolCall = false;
    let inToolResult = false;
    let filesChanged = new Set();
    
    function flushMessage() {
        if (currentRole && currentContent.length > 0) {
            const messageContent = currentContent.join('\n').trim();
            if (messageContent) {
                html += formatMessage(currentRole, messageContent);
            }
            currentContent = [];
        }
    }
    
    for (let line of lines) {
        // Detect role changes
        if (line === 'user:') {
            flushMessage();
            currentRole = 'user';
            continue;
        } else if (line === 'assistant:') {
            flushMessage();
            currentRole = 'assistant';
            continue;
        }
        
        currentContent.push(line);
        
        // Track file changes
        if (line.includes('path:')) {
            const pathMatch = line.match(/path: (.+)/);
            if (pathMatch) {
                filesChanged.add(pathMatch[1].trim());
            }
        }
    }
    
    flushMessage();
    
    // Add files changed summary at the top
    if (filesChanged.size > 0) {
        html = formatFilesChanged(Array.from(filesChanged)) + html;
    }
    
    return html;
}

function formatMessage(role, content) {
    let html = `<div class="chat-message ${role}">`;
    html += `<div class="chat-message-header">`;
    html += `<span class="chat-role">${role === 'user' ? '👤 User' : '🤖 Assistant'}</span>`;
    html += `</div>`;
    html += `<div class="chat-content">`;
    
    // Parse special sections
    const sections = parseMessageContent(content);
    sections.forEach(section => {
        if (section.type === 'thinking') {
            html += `<div class="chat-thinking">
                <div class="chat-thinking-header">💭 Thinking</div>
                ${escapeHtml(section.content || '')}
            </div>`;
        } else if (section.type === 'tool-call') {
            html += `<div class="chat-tool-call">
                <div class="tool-call-header">🔧 Tool Call: ${section.tool || 'Unknown'}</div>
                <div class="tool-call-params">${formatToolParams(section.params || '')}</div>
            </div>`;
        } else if (section.type === 'tool-result') {
            const resultContent = section.content || '';
            const preview = resultContent.length > 200 ? resultContent.substring(0, 200) + '...' : resultContent;
            html += `<div class="chat-tool-result">
                <div class="tool-result-header">📋 Tool Result</div>
                ${preview ? escapeHtml(preview) : '<em>No output</em>'}
            </div>`;
        } else {
            const textContent = section.content || '';
            if (textContent.trim()) {
                html += `<p>${formatText(textContent)}</p>`;
            }
        }
    });
    
    html += `</div></div>`;
    return html;
}

function parseMessageContent(content) {
    const sections = [];
    const lines = content.split('\n');
    let currentSection = { type: 'text', content: '' };
    
    for (let line of lines) {
        if (line.startsWith('[Thinking]')) {
            if (currentSection.content && currentSection.content.trim()) {
                sections.push(currentSection);
            }
            currentSection = { type: 'thinking', content: line.replace('[Thinking]', '').trim() };
        } else if (line.startsWith('[Tool call]')) {
            if (currentSection.content && currentSection.content.trim()) {
                sections.push(currentSection);
            } else if (currentSection.type === 'tool-call') {
                sections.push(currentSection);
            }
            const toolMatch = line.match(/\[Tool call\] (\w+)/);
            currentSection = { 
                type: 'tool-call', 
                tool: toolMatch ? toolMatch[1] : 'Unknown',
                params: '',
                content: '' // Add content property
            };
        } else if (line.startsWith('  ') && currentSection.type === 'tool-call') {
            currentSection.params += line.trim() + '\n';
        } else if (line.startsWith('[Tool result]')) {
            if ((currentSection.content && currentSection.content.trim()) || currentSection.type === 'tool-call') {
                sections.push(currentSection);
            }
            currentSection = { type: 'tool-result', content: '' };
        } else if (line.startsWith('<user_query>') || line.startsWith('<image_files>')) {
            // Skip metadata tags
            continue;
        } else {
            if (currentSection.type === 'thinking' || currentSection.type === 'tool-result') {
                currentSection.content += line + '\n';
            } else if (currentSection.type === 'text') {
                currentSection.content += line + '\n';
            } else if (currentSection.type === 'tool-call') {
                // Continue accumulating params for tool calls
                currentSection.params += line.trim() + '\n';
            } else {
                if (currentSection.content && currentSection.content.trim()) {
                    sections.push(currentSection);
                }
                currentSection = { type: 'text', content: line + '\n' };
            }
        }
    }
    
    // Final flush - check content exists before calling trim
    if (currentSection.type === 'tool-call' || (currentSection.content && currentSection.content.trim())) {
        sections.push(currentSection);
    }
    
    return sections;
}

function formatToolParams(params) {
    return `<pre style="margin: 0.5rem 0; white-space: pre-wrap; word-wrap: break-word;">${escapeHtml(params)}</pre>`;
}

function formatFilesChanged(files) {
    if (files.length === 0) return '';
    
    let html = '<div class="files-changed-section">';
    html += '<div class="files-changed-title">📁 Files Accessed in This Session:</div>';
    html += '<div>';
    
    files.forEach(file => {
        // Determine file operation type
        let badgeClass = 'file-read';
        if (file.includes('Write') || file.includes('output')) {
            badgeClass = 'file-created';
        } else if (file.includes('StrReplace') || file.includes('Edit')) {
            badgeClass = 'file-modified';
        }
        
        html += `<span class="file-change-badge ${badgeClass}">${escapeHtml(file)}</span>`;
    });
    
    html += '</div></div>';
    return html;
}

function formatText(text) {
    if (!text) return '';
    return escapeHtml(text)
        .replace(/\n\n+/g, '</p><p>')
        .replace(/\n/g, '<br>');
}

function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = String(text);
    return div.innerHTML;
}

// ===============================================
// Author Review Tab
// ===============================================
function initAuthorReviewTab() {
    // Static content — no interactive elements needed.
    // MathJax re-render is handled by the main loadTab function.
}

// ===============================================
// Revision Tab — Interactive Plotly Visualizations
// ===============================================
function initRevisionTab() {
    setupBeliefGapExplorer();
    setupPayoffComparison();
}

function setupBeliefGapExplorer() {
    const alphaSlider = document.getElementById('belief-alpha-slider');
    const betaSlider = document.getElementById('belief-beta-slider');
    const mustarSlider = document.getElementById('belief-mustar-slider');

    if (!alphaSlider || !betaSlider || !mustarSlider) return;

    function update() {
        const a = parseFloat(alphaSlider.value);
        const b = parseFloat(betaSlider.value);
        const mustar = parseFloat(mustarSlider.value);

        document.getElementById('belief-alpha-display').textContent = a.toFixed(2);
        document.getElementById('belief-beta-display').textContent = b.toFixed(2);
        document.getElementById('belief-mustar-display').textContent = mustar.toFixed(2);

        const piG = b / (a + b);
        const gap = (2 * a * b * Math.abs(1 - a - b)) / Math.pow(a + b, 2);
        const FGG = 1 - a;
        const FGB = b;

        document.getElementById('belief-piG-val').textContent = piG.toFixed(4);
        document.getElementById('belief-FGG-val').textContent = FGG.toFixed(4);
        document.getElementById('belief-FGB-val').textContent = FGB.toFixed(4);
        document.getElementById('belief-gap-val').textContent = gap.toFixed(4);

        const isRobust = mustar < FGB || mustar > FGG;
        const robustEl = document.getElementById('belief-robust-val');
        if (isRobust) {
            robustEl.textContent = 'Yes — μ* is outside [β, 1−α], so cooperation is belief-robust';
            robustEl.style.color = '#28a745';
        } else {
            robustEl.textContent = 'No — μ* ∈ [β, 1−α], so SR cooperation depends on beliefs';
            robustEl.style.color = '#dc3545';
        }

        const barColors = ['#2ecc71', '#3498db', '#e67e22', '#e74c3c'];
        const barData = [{
            x: ['F(G|G) = 1−α', 'π(G)', 'F(G|B) = β', 'μ*'],
            y: [FGG, piG, FGB, mustar],
            type: 'bar',
            marker: { color: barColors },
            text: [FGG.toFixed(3), piG.toFixed(3), FGB.toFixed(3), mustar.toFixed(3)],
            textposition: 'outside'
        }];

        const layout = {
            title: 'Belief Thresholds and Stationary Distribution',
            yaxis: { title: 'Probability', range: [0, 1.15] },
            xaxis: { title: '' },
            plot_bgcolor: '#fafafa',
            paper_bgcolor: 'white',
            font: { family: 'Helvetica, Arial, sans-serif' },
            shapes: [{
                type: 'line',
                x0: -0.5, x1: 3.5,
                y0: mustar, y1: mustar,
                line: { color: '#e74c3c', width: 2, dash: 'dash' }
            }],
            annotations: [{
                x: 3.5, y: mustar,
                text: 'μ* threshold',
                showarrow: false,
                xanchor: 'right',
                yanchor: 'bottom',
                font: { color: '#e74c3c', size: 11 }
            }],
            margin: { t: 50, b: 60, l: 60, r: 30 }
        };

        Plotly.newPlot('belief-gap-plot', barData, layout, { responsive: true });
    }

    alphaSlider.addEventListener('input', update);
    betaSlider.addEventListener('input', update);
    mustarSlider.addEventListener('input', update);
    update();
}

function setupPayoffComparison() {
    const alphaSlider = document.getElementById('belief-alpha-slider');
    const betaSlider = document.getElementById('belief-beta-slider');
    const mustarSlider = document.getElementById('belief-mustar-slider');

    if (!alphaSlider || !betaSlider || !mustarSlider) return;

    const uGAC = 2;
    const uBFD = -1;
    const uGAD = 0;
    const uBFC = 1;

    function updatePayoff() {
        const a = parseFloat(alphaSlider.value);
        const b = parseFloat(betaSlider.value);
        const mustar = parseFloat(mustarSlider.value);

        const piG = b / (a + b);
        const piB = a / (a + b);

        const V = piG * uGAC + piB * uBFD;

        const FGG = 1 - a;
        const FGB = b;

        let VM;
        if (mustar <= FGB) {
            VM = piG * uGAC + piB * uBFC;
        } else if (mustar >= FGG) {
            VM = piG * uGAD + piB * uBFD;
        } else {
            VM = piG * uGAC + piB * uBFD;
        }

        const gapVal = V - VM;

        document.getElementById('payoff-V-val').textContent = V.toFixed(4);
        document.getElementById('payoff-VM-val').textContent = VM.toFixed(4);
        document.getElementById('payoff-gap-val').textContent = gapVal.toFixed(4);

        const barData = [{
            x: ['Stationary V', 'Markov-filtered V_Markov', 'Gap (V − V_Markov)'],
            y: [V, VM, gapVal],
            type: 'bar',
            marker: {
                color: ['#3498db', '#2ecc71', gapVal >= 0 ? '#e67e22' : '#e74c3c']
            },
            text: [V.toFixed(3), VM.toFixed(3), gapVal.toFixed(3)],
            textposition: 'outside'
        }];

        const yMin = Math.min(V, VM, gapVal, 0) - 0.5;
        const yMax = Math.max(V, VM, gapVal, 0) + 0.5;

        const layout = {
            title: 'Stationary vs. Markov-Filtered Payoff',
            yaxis: { title: 'Payoff', range: [yMin, yMax] },
            xaxis: { title: '' },
            plot_bgcolor: '#fafafa',
            paper_bgcolor: 'white',
            font: { family: 'Helvetica, Arial, sans-serif' },
            shapes: [{
                type: 'line',
                x0: -0.5, x1: 2.5,
                y0: 0, y1: 0,
                line: { color: '#999', width: 1, dash: 'dot' }
            }],
            margin: { t: 50, b: 60, l: 60, r: 30 }
        };

        Plotly.newPlot('payoff-comparison-plot', barData, layout, { responsive: true });
    }

    alphaSlider.addEventListener('input', updatePayoff);
    betaSlider.addEventListener('input', updatePayoff);
    mustarSlider.addEventListener('input', updatePayoff);
    updatePayoff();
}
