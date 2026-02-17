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
