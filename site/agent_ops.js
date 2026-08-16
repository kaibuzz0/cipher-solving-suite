/* Agent operations console generated from WORK_QUEUE, handoffs, current state and integration inbox. */

async function loadAgentOps() {
  const response = await fetch('data/agent-ops.json', { cache: 'no-store' });
  if (!response.ok) throw new Error(`data/agent-ops.json: ${response.status}`);
  return response.json();
}

function opsTag(value, hot = false) { return tag(value || 'unknown', hot); }

function installAgentOpsUI() {
  if ($('#operations')) return;
  const agentGroup = all('.tree-folder').find((el) => el.textContent.includes('agent-ops'))?.parentElement?.querySelector('.tree-children');
  if (agentGroup) {
    agentGroup.insertAdjacentHTML('afterbegin', '<button data-tab="operations" class="tree-item">◎ <span>operations-console</span></button>');
  }
  const activitySpacer = $('.activity-spacer');
  if (activitySpacer) activitySpacer.insertAdjacentHTML('beforebegin', '<button class="activity" data-tab="operations" title="Agent operations">◎</button>');
  const homeFolders = $('#home .folder-grid');
  if (homeFolders) homeFolders.insertAdjacentHTML('beforeend', '<button class="folder-card" data-open="operations"><span class="big-folder">🧭</span><span><b>Agent Operations</b><small>Queue, handoffs, priorities, blockers and integration inbox</small></span></button>');

  const editor = $('.editor');
  const statusbar = $('.statusbar');
  const panel = document.createElement('section');
  panel.id = 'operations';
  panel.className = 'panel';
  panel.innerHTML = '<div class="panel-title"><div><span class="kicker">AGENT NETWORK / OPERATIONS</span><h2>Agent Operations Console</h2></div><span>Generated from repository coordination state. No separate dashboard database.</span></div><div id="ops-content"></div>';
  editor.insertBefore(panel, statusbar || null);

  tabIcons.operations = '◎';
  all('[data-tab="operations"]').forEach((el) => el.addEventListener('click', (event) => { event.preventDefault(); openTab('operations'); }));
  all('[data-open="operations"]').forEach((el) => { el.onclick = () => openTab('operations'); });
}

function renderOpsSummary(ops) {
  const s = ops.summary || {};
  return `<div class="section-caption">OPERATIONS STATUS</div><div class="status-grid">
    <div class="stat"><b>${esc(s.queue_total || 0)}</b><span>queued work</span></div>
    <div class="stat"><b>${esc(s.queue_p1 || 0)}</b><span>P1 items</span></div>
    <div class="stat"><b>${esc(s.queue_claimed || 0)}</b><span>claimed items</span></div>
    <div class="stat"><b>${esc(s.integration_items || 0)}</b><span>integration inbox</span></div>
    <div class="stat"><b>${esc(s.known_debt || 0)}</b><span>known debt</span></div>
    <div class="stat"><b>${esc(s.handoffs || 0)}</b><span>handoff entries</span></div>
  </div>`;
}

function renderQueue(ops) {
  const items = ops.queue?.items || [];
  return `<div class="section-caption">WORK QUEUE (${items.length})</div><div class="data-list">${items.length ? items.map((item) => row(
    `${item.priority} · ${item.work}`,
    esc(item.next_step || ''),
    opsTag(item.state, item.state !== 'done') + opsTag(item.owner || 'unclaimed', item.owner === 'unclaimed'),
  )).join('') : '<div class="empty">No queued work.</div>'}</div>`;
}

function renderCurrentState(ops) {
  const current = ops.current_state || {};
  const priorities = current.priorities || [];
  const debt = current.known_debt || [];
  return `<div class="section-caption">CURRENT STATE</div>
    <div class="workflow">
      ${kv('Reconciled', esc(current.last_reconciled || 'unknown'))}
      ${kv('Branch', `<code>${esc(current.default_branch || 'unknown')}</code>`)}
      ${kv('Version', esc(current.version || 'unknown'))}
      ${kv('Next Handoff', esc(current.next_handoff || 'No next handoff recorded.'))}
    </div>
    <div class="section-caption">OPERATING PRIORITIES (${priorities.length})</div><div class="data-list">${priorities.length ? priorities.map((value, i) => row(`${i + 1}. ${value}`, '', opsTag(i < 2 ? 'high' : 'priority', i < 2))).join('') : '<div class="empty">No priorities recorded.</div>'}</div>
    <div class="section-caption">KNOWN DEBT (${debt.length})</div><div class="data-list">${debt.length ? debt.map((value) => row(value, '', opsTag('debt', true))).join('') : '<div class="empty">No known debt recorded.</div>'}</div>`;
}

function renderIntegrationQueue(ops) {
  const queue = ops.integration_queue || {};
  const items = queue.items || [];
  return `<div class="section-caption">INTEGRATION INBOX (${items.length})</div><div class="data-list">${items.length ? items.map((item) => {
    const title = item.name || item.path || item.id || item.type || 'integration item';
    const desc = item.notes || item.description || item.next_action || 'Awaiting integration review.';
    return row(title, esc(desc), opsTag(item.type || 'item') + opsTag(item.status || 'pending', true));
  }).join('') : '<div class="empty">Integration inbox is empty.</div>'}</div>`;
}

function renderHandoffs(ops) {
  const items = ops.recent_handoffs || [];
  return `<div class="section-caption">RECENT HANDOFFS (${items.length})</div><div class="data-list">${items.length ? items.map((item) => {
    const verification = item.verification ? `Verification: ${esc(item.verification)}` : '';
    const next = item.next_action ? `<code>Next: ${esc(item.next_action)}</code>` : '';
    return row(`${item.timestamp} · ${item.agent}`, `${esc(item.task)}${verification ? `<br>${verification}` : ''}${next}`, opsTag(item.branch_pr || 'handoff'));
  }).join('') : '<div class="empty">No handoffs parsed.</div>'}</div>`;
}

function renderAgentOps() {
  const ops = state.agentOps || {};
  const target = $('#ops-content');
  if (!target) return;
  target.innerHTML = renderOpsSummary(ops) + renderQueue(ops) + renderCurrentState(ops) + renderIntegrationQueue(ops) + renderHandoffs(ops) +
    '<div class="section-caption">SOURCE FILES</div><div class="quick-grid"><a href="docs/WORK_QUEUE.md">WORK_QUEUE.md</a><a href="docs/AGENT_HANDOFF.md">AGENT_HANDOFF.md</a><a href="ops/CURRENT_STATE.md">CURRENT_STATE.md</a><a href="data/integration_queue.json">integration_queue.json</a></div>';
}

(async () => {
  try {
    installAgentOpsUI();
    state.agentOps = await loadAgentOps();
    renderAgentOps();
  } catch (error) {
    installAgentOpsUI();
    const target = $('#ops-content');
    if (target) target.innerHTML = `<div class="notice"><strong>Agent Ops data error:</strong> ${esc(error.message)}</div>`;
  }
})();
