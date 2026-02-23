<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloud Monitoring Dashboard</title>
<meta http-equiv="refresh" content="5">
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<style>
  :root {
    --bg: #090c10;
    --surface: #0d1117;
    --surface2: #161b22;
    --border: #21262d;
    --accent-green: #39d353;
    --accent-blue: #58a6ff;
    --accent-purple: #bc8cff;
    --accent-orange: #f0883e;
    --text: #e6edf3;
    --muted: #8b949e;
    --danger: #f85149;
    --warn: #d29922;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    font-family: 'Rajdhani', sans-serif;
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Subtle grid background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(88,166,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(88,166,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  .wrapper { position: relative; z-index: 1; }

  /* ── HEADER ─────────────────────────────────────────── */
  header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 40px;
    border-bottom: 1px solid var(--border);
    background: rgba(13,17,23,0.95);
    backdrop-filter: blur(10px);
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .logo-icon {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #58a6ff 0%, #bc8cff 100%);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
  }

  .header-title {
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--text);
  }

  .header-title span {
    color: var(--accent-blue);
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 24px;
  }

  .live-badge {
    display: flex;
    align-items: center;
    gap: 7px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--accent-green);
    letter-spacing: 1px;
  }

  .live-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--accent-green);
    animation: pulse-dot 1.5s ease-in-out infinite;
  }

  @keyframes pulse-dot {
    0%, 100% { opacity: 1; box-shadow: 0 0 0 0 rgba(57,211,83,0.5); }
    50% { opacity: 0.8; box-shadow: 0 0 0 6px rgba(57,211,83,0); }
  }

  .timestamp {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--muted);
  }

  /* ── MAIN CONTENT ───────────────────────────────────── */
  main { padding: 36px 40px; }

  .section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
  }

  /* ── GAUGE CARDS ────────────────────────────────────── */
  .gauges {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 36px;
  }

  .gauge-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, transform 0.2s;
  }

  .gauge-card:hover {
    border-color: var(--accent-blue);
    transform: translateY(-3px);
  }

  .gauge-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--card-accent, var(--accent-blue));
    opacity: 0.8;
  }

  .gauge-card.cpu { --card-accent: var(--accent-green); }
  .gauge-card.mem { --card-accent: var(--accent-blue); }
  .gauge-card.disk { --card-accent: var(--accent-purple); }

  .gauge-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }

  .gauge-title {
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .gauge-status {
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 4px;
    background: rgba(57,211,83,0.1);
    color: var(--accent-green);
    border: 1px solid rgba(57,211,83,0.2);
  }

  .gauge-status.warn {
    background: rgba(210,153,34,0.1);
    color: var(--warn);
    border-color: rgba(210,153,34,0.2);
  }

  .gauge-status.danger {
    background: rgba(248,81,73,0.1);
    color: var(--danger);
    border-color: rgba(248,81,73,0.2);
  }

  /* ── PROGRESS BAR GAUGE ─────────────────────────────── */
  .gauge-value {
    font-size: 56px;
    font-weight: 700;
    line-height: 1;
    margin: 12px 0 6px;
    font-family: 'Share Tech Mono', monospace;
    color: var(--card-accent, var(--accent-blue));
  }

  .gauge-value .unit {
    font-size: 20px;
    color: var(--muted);
    font-weight: 400;
  }

  .progress-track {
    width: 100%;
    height: 6px;
    background: var(--border);
    border-radius: 3px;
    overflow: hidden;
    margin-top: 14px;
  }

  .progress-fill {
    height: 100%;
    border-radius: 3px;
    background: var(--card-accent, var(--accent-blue));
    transition: width 0.5s ease;
    position: relative;
  }

  .progress-fill::after {
    content: '';
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 20px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3));
  }

  .gauge-sublabel {
    margin-top: 8px;
    font-size: 12px;
    color: var(--muted);
    font-family: 'Share Tech Mono', monospace;
  }

  /* ── SPARKLINE ──────────────────────────────────────── */
  .sparkline-row {
    display: flex;
    gap: 4px;
    align-items: flex-end;
    height: 28px;
    margin-top: 12px;
  }

  .spark-bar {
    flex: 1;
    border-radius: 2px 2px 0 0;
    background: var(--card-accent, var(--accent-blue));
    opacity: 0.4;
    transition: opacity 0.2s;
  }

  .spark-bar:last-child { opacity: 1; }

  /* ── INFO GRID ──────────────────────────────────────── */
  .info-grid {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 16px;
    margin-bottom: 36px;
  }

  .info-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    transition: border-color 0.3s;
  }

  .info-card:hover { border-color: var(--accent-blue); }

  .info-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 8px;
    font-family: 'Share Tech Mono', monospace;
  }

  .info-value {
    font-size: 16px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.3;
  }

  .info-value.ok { color: var(--accent-green); }
  .info-value.warn { color: var(--warn); }

  /* ── ACTIVITY LOG ───────────────────────────────────── */
  .bottom-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
  }

  .panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }

  .panel-header {
    padding: 14px 20px;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: var(--surface2);
  }

  .panel-title {
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
  }

  .panel-body { padding: 16px 20px; }

  .log-entry {
    display: flex;
    gap: 12px;
    align-items: flex-start;
    padding: 8px 0;
    border-bottom: 1px solid rgba(33,38,45,0.6);
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    animation: fadeIn 0.4s ease;
  }

  @keyframes fadeIn { from { opacity: 0; transform: translateX(-6px); } to { opacity: 1; } }

  .log-time { color: var(--muted); white-space: nowrap; }
  .log-level { width: 52px; text-align: center; padding: 1px 4px; border-radius: 3px; font-size: 10px; font-weight: 700; flex-shrink: 0; }
  .log-level.info { background: rgba(88,166,255,0.12); color: var(--accent-blue); }
  .log-level.warn { background: rgba(210,153,34,0.12); color: var(--warn); }
  .log-level.error { background: rgba(248,81,73,0.12); color: var(--danger); }
  .log-msg { color: var(--text); }

  /* ── METRIC BARS ────────────────────────────────────── */
  .metric-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 0;
    border-bottom: 1px solid rgba(33,38,45,0.6);
  }

  .metric-name {
    width: 110px;
    font-size: 12px;
    color: var(--muted);
    font-family: 'Share Tech Mono', monospace;
    flex-shrink: 0;
  }

  .metric-bar-track {
    flex: 1;
    height: 4px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
  }

  .metric-bar-fill {
    height: 100%;
    border-radius: 2px;
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  }

  .metric-val {
    width: 44px;
    text-align: right;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--text);
  }

  @media (max-width: 1100px) {
    .gauges { grid-template-columns: 1fr 1fr; }
    .info-grid { grid-template-columns: repeat(3, 1fr); }
    .bottom-row { grid-template-columns: 1fr; }
  }

  @media (max-width: 700px) {
    main { padding: 20px; }
    header { padding: 14px 20px; }
    .gauges { grid-template-columns: 1fr; }
    .info-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HEADER -->
  <header>
    <div class="header-left">
      <div class="logo-icon">☁</div>
      <div class="header-title">Cloud<span>OPS</span> Monitor</div>
    </div>
    <div class="header-right">
      <div class="live-badge"><div class="live-dot"></div> LIVE</div>
      <div class="timestamp" id="clock">--:--:--</div>
    </div>
  </header>

  <main>

    <!-- GAUGE SECTION -->
    <div class="section-label">Resource Utilization</div>
    <div class="gauges">

      <!-- CPU -->
      <div class="gauge-card cpu">
        <div class="gauge-header">
          <span class="gauge-title">CPU</span>
          <span class="gauge-status ok" id="cpu-status">NOMINAL</span>
        </div>
        <div class="gauge-value"><span id="cpu-val">{{ cpu_metric }}</span><span class="unit">%</span></div>
        <div class="progress-track">
          <div class="progress-fill" id="cpu-bar" style="width: {{ cpu_metric }}%"></div>
        </div>
        <div class="gauge-sublabel">8-core · avg across all threads</div>
        <div class="sparkline-row" id="cpu-spark"></div>
      </div>

      <!-- MEMORY -->
      <div class="gauge-card mem">
        <div class="gauge-header">
          <span class="gauge-title">Memory</span>
          <span class="gauge-status ok" id="mem-status">NOMINAL</span>
        </div>
        <div class="gauge-value"><span id="mem-val">{{ mem_metric }}</span><span class="unit">%</span></div>
        <div class="progress-track">
          <div class="progress-fill" id="mem-bar" style="width: {{ mem_metric }}%"></div>
        </div>
        <div class="gauge-sublabel">RAM · heap + resident set</div>
        <div class="sparkline-row" id="mem-spark"></div>
      </div>

      <!-- DISK -->
      <div class="gauge-card disk">
        <div class="gauge-header">
          <span class="gauge-title">Disk</span>
          <span class="gauge-status ok" id="disk-status">NOMINAL</span>
        </div>
        <div class="gauge-value"><span id="disk-val">{{ disk_metric }}</span><span class="unit">%</span></div>
        <div class="progress-track">
          <div class="progress-fill" id="disk-bar" style="width: {{ disk_metric }}%"></div>
        </div>
        <div class="gauge-sublabel">SSD · primary volume</div>
        <div class="sparkline-row" id="disk-spark"></div>
      </div>

    </div>

    <!-- INFO SECTION -->
    <div class="section-label">System Info</div>
    <div class="info-grid">
      <div class="info-card">
        <div class="info-label">Pod Status</div>
        <div class="info-value ok">{{ pod_status }}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Restart Count</div>
        <div class="info-value">{{ restart }}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Node Status</div>
        <div class="info-value ok">{{ node }}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Uptime</div>
        <div class="info-value">{{ uptime }}</div>
      </div>
      <div class="info-card">
        <div class="info-label">Net Sent</div>
        <div class="info-value">{{ bytes_sent }} <span style="font-size:12px;color:var(--muted)">MB</span></div>
      </div>
      <div class="info-card">
        <div class="info-label">Net Recv</div>
        <div class="info-value">{{ bytes_recv }} <span style="font-size:12px;color:var(--muted)">MB</span></div>
      </div>
    </div>

    <!-- BOTTOM ROW -->
    <div class="section-label">Diagnostics</div>
    <div class="bottom-row">

      <!-- Event Log -->
      <div class="panel">
        <div class="panel-header">
          <span class="panel-title">Event Log</span>
          <span style="font-family:'Share Tech Mono',monospace;font-size:11px;color:var(--muted)">TAIL -F</span>
        </div>
        <div class="panel-body" id="log-panel">
          <div class="log-entry">
            <span class="log-time">12:00:01</span>
            <span class="log-level info">INFO</span>
            <span class="log-msg">System health check passed</span>
          </div>
          <div class="log-entry">
            <span class="log-time">12:00:00</span>
            <span class="log-level info">INFO</span>
            <span class="log-msg">Monitoring agent started</span>
          </div>
        </div>
      </div>

      <!-- Service Breakdown -->
      <div class="panel">
        <div class="panel-header">
          <span class="panel-title">Service Metrics</span>
        </div>
        <div class="panel-body">
          <div class="metric-row">
            <span class="metric-name">api-gateway</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:72%"></div></div>
            <span class="metric-val">72%</span>
          </div>
          <div class="metric-row">
            <span class="metric-name">auth-service</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:38%"></div></div>
            <span class="metric-val">38%</span>
          </div>
          <div class="metric-row">
            <span class="metric-name">data-pipeline</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:85%"></div></div>
            <span class="metric-val">85%</span>
          </div>
          <div class="metric-row">
            <span class="metric-name">cache-layer</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:21%"></div></div>
            <span class="metric-val">21%</span>
          </div>
          <div class="metric-row">
            <span class="metric-name">search-index</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:55%"></div></div>
            <span class="metric-val">55%</span>
          </div>
          <div class="metric-row">
            <span class="metric-name">log-aggregator</span>
            <div class="metric-bar-track"><div class="metric-bar-fill" style="width:44%"></div></div>
            <span class="metric-val">44%</span>
          </div>
        </div>
      </div>

    </div>

  </main>
</div>

<script>
  // Clock
  function tick() {
    const now = new Date();
    document.getElementById('clock').textContent =
      now.toTimeString().slice(0,8);
  }
  tick();
  setInterval(tick, 1000);

  // Status badge helper
  function setStatus(elId, val) {
    const el = document.getElementById(elId);
    el.className = 'gauge-status';
    if (val >= 80) { el.classList.add('danger'); el.textContent = 'CRITICAL'; }
    else if (val >= 50) { el.classList.add('warn'); el.textContent = 'WARNING'; }
    else { el.classList.add('ok'); el.textContent = 'NOMINAL'; }
  }

  const cpuV = {{ cpu_metric }};
  const memV = {{ mem_metric }};
  const diskV = {{ disk_metric }};

  setStatus('cpu-status', cpuV);
  setStatus('mem-status', memV);
  setStatus('disk-status', diskV);

  // Sparklines (fake history — in real use, pass array from backend)
  function buildSpark(containerId, currentVal, color) {
    const el = document.getElementById(containerId);
    const count = 20;
    // generate plausible history ending at currentVal
    const vals = [];
    let v = Math.max(5, currentVal - Math.random() * 20);
    for (let i = 0; i < count - 1; i++) {
      v = Math.min(100, Math.max(2, v + (Math.random() - 0.48) * 8));
      vals.push(v);
    }
    vals.push(currentVal);
    const max = Math.max(...vals);
    el.innerHTML = vals.map(v => {
      const h = Math.max(4, (v / Math.max(max, 1)) * 28);
      return `<div class="spark-bar" style="height:${h}px;background:${color}"></div>`;
    }).join('');
  }

  buildSpark('cpu-spark', cpuV, 'var(--accent-green)');
  buildSpark('mem-spark', memV, 'var(--accent-blue)');
  buildSpark('disk-spark', diskV, 'var(--accent-purple)');

  // Simulated live log entries
  const messages = [
    ['INFO',  'Heartbeat OK — all pods responding'],
    ['INFO',  'Autoscaler evaluated: no action'],
    ['WARN',  'P99 latency spike: api-gateway (210ms)'],
    ['INFO',  'Backup snapshot completed successfully'],
    ['INFO',  'Certificate renewal check passed'],
    ['WARN',  'Memory pressure detected on worker-3'],
    ['INFO',  'Log rotation triggered'],
    ['ERROR', 'Connection timeout: db-replica-2'],
    ['INFO',  'Replica re-connected after 3.2s'],
    ['INFO',  'Scheduled job: metrics-export done'],
  ];
  let logIdx = 0;

  function addLog() {
    const panel = document.getElementById('log-panel');
    const [lvl, msg] = messages[logIdx % messages.length];
    logIdx++;
    const now = new Date().toTimeString().slice(0,8);
    const cls = lvl === 'ERROR' ? 'error' : lvl === 'WARN' ? 'warn' : 'info';
    const entry = document.createElement('div');
    entry.className = 'log-entry';
    entry.innerHTML = `
      <span class="log-time">${now}</span>
      <span class="log-level ${cls}">${lvl}</span>
      <span class="log-msg">${msg}</span>`;
    panel.insertBefore(entry, panel.firstChild);
    if (panel.children.length > 8) panel.removeChild(panel.lastChild);
  }

  setInterval(addLog, 2400);
</script>

</body>
</html>