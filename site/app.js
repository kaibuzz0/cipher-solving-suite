const state = {
  opportunities: [],
  prompts: [],
  tools: [],
  toolsets: [],
  toolsetSummary: {},
  cases: [],
  intelligence: [],
  sources: [],
  health: {},
  artifacts: [],
  artifactSummary: {},
  status: {},
};

const REPO_BASE = 'https://github.com/kaibuzz0/cipher-solving-suite/blob/main/';
const $ = (s) => document.querySelector(s);
const all = (s) => [...document.querySelectorAll(s)];
let current = 'home';

async function loadJSON(path) {
  const response = await fetch(path, { cache: 'no-store' });
  if (!response.ok) throw new Error(`${path}: ${response.status}`);
  return response.json();
}

const text = (value) => String(value ?? '').toLowerCase();
const esc = (value) => String(value ?? '').replace(/[&<>"']/g, (c) => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
}[c]));
const bytes = (n) => n < 1024 ? `${n} B` : n < 1048576 ? `${(n / 1024).toFixed(1)} KB` : `${(n / 1048576).toFixed(1)} MB`;
const tag = (value, hot = false) => `<span class="tag${hot ? ' hot' : ''}">${esc(value)}</span>`;

function row(name, desc = '', meta = '', link = '') {
  return `<div class="row"><div class="row-main">${link
    ? `<a href="${esc(link)}" target="_blank" rel="noopener"><b>${esc(name)}</b></a>`
    : `<b>${esc(name)}</b>`}</div><div class="row-desc">${desc}</div><div class="meta">${meta}</div></div>`;
}

function installDynamicToolsetUI() {
  if ($('#toolsets')) return;

  const workspaceChildren = $('.sidebar .tree-group .tree-children');
  if (workspaceChildren) {
    workspaceChildren.insertAdjacentHTML(
      'beforeend',
      '<button data-tab="toolsets" class="tree-item">📦 <span>toolsets</span></button>',
    );
  }

  const activitySpacer = $('.activity-spacer');
  if (activitySpacer) {
    activitySpacer.insertAdjacentHTML(
      'beforebegin',
      '<button class="activity" data-tab="toolsets" title="Toolsets">▦</button>',
    );
  }

  const homeFolders = $('#home .folder-grid');
  if (homeFolders) {
    homeFolders.insertAdjacentHTML(
      'beforeend',
      '<button class="folder-card" data-open="toolsets"><span class="big-folder">📦</span><span><b>Toolsets</b><small>Reusable repo capability packs discovered from manifests</small></span></button>',
    );
  }

  const editor = $('.editor');
  const statusbar = $('.statusbar');
  if (editor) {
    const panel = document.createElement('section');
    panel.id = 'toolsets';
    panel.className = 'panel';
    panel.innerHTML = '<div class="panel-title"><div><span class="kicker">REPOSITORY / TOOLSETS</span><h2>Reusable Toolsets</h2></div><span>Generated from <code>toolsets/*/toolset.json</code> and reconciled with <code>toolsets/catalog.json</code>.</span></div><div id="toolset-grid" class="data-list"></div>';
    if (statusbar) editor.insertBefore(panel, statusbar);
    else editor.appendChild(panel);
  }
}

function renderStats() {
  const s = state.status;
  $('#hub-status').textContent = s.generated_at ? `snapshot ${new Date(s.generated_at).toLocaleString()}` : 'repository snapshot';
  $('#stats-grid').innerHTML = [
    ['Cases', s.active_cases || 0],
    ['Toolsets', s.toolsets || 0],
    ['Tools', s.tools || 0],
    ['Intel', s.intelligence || 0],
    ['Sources', s.intelligence_sources || 0],
    ['Due', s.sources_due || 0],
    ['Evidence', s.artifacts || 0],
    ['Review', s.artifacts_review_before_move || 0],
  ].map(([key, value]) => `<div class="stat"><b>${esc(value)}</b><span>${esc(key)}</span></div>`).join('');
}

function filter(items, fields, catfn = () => true) {
  const q = text($('#search').value);
  const cat = $('#category').value;
  return items.filter((x) => catfn(x, cat) && (!q || fields(x).some((v) => text(v).includes(q))));
}

function renderOpportunities() {
  const items = filter(state.opportunities, (x) => [x.name, x.category, x.description, ...(x.tags || [])], (x, c) => c === 'all' || x.category === c);
  $('#opportunity-grid').innerHTML = items.map((x) => row(x.name, esc(x.description), tag(x.category) + (x.authorized_only ? tag('scope required', true) : ''), x.url)).join('') || '<div class="empty">No matches.</div>';
}

function renderIntel() {
  const items = filter(state.intelligence, (x) => [x.title, x.summary, x.category, x.source_name, ...(x.tags || [])], (x, c) => c === 'all' || x.category === c);
  $('#intel-grid').innerHTML = items.map((x) => row(x.title, esc(x.summary), tag(x.category) + tag(`confidence ${x.confidence}`) + tag(x.relevance), x.source_url)).join('') || '<div class="empty">No matches.</div>';
}

function renderCases() {
  const items = filter(state.cases, (x) => [x.id, x.name, x.title, x.type, x.status, x.owner, x.next_action, x.source]);
  $('#case-grid').innerHTML = items.map((x) => row(x.name || x.title || x.id, esc(x.next_action ? `Next: ${x.next_action}` : (x.summary || x.objective || x.source || 'Structured research case')), tag(x.type || 'case') + tag(x.status || 'active'))).join('') || '<div class="empty">No active cases.</div>';
}

function renderTools() {
  const items = filter(state.tools.filter((x) => x.user_visible !== false), (x) => [x.name, x.category, x.path, x.command, x.description, x.maturity]);
  $('#tool-grid').innerHTML = items.map((x) => row(x.name, `${esc(x.description)}<code>${esc(x.command)}</code>`, tag(x.category) + tag(x.maturity || 'registered'))).join('') || '<div class="empty">No matches.</div>';
}

function renderToolsets() {
  const target = $('#toolset-grid');
  if (!target) return;
  const items = filter(
    state.toolsets,
    (x) => [x.id, x.name, x.description, x.path, x.version, x.maturity, x.health, x.entrypoint, ...(x.warnings || [])],
    (x, c) => c === 'all' || x.maturity === c || x.health === c,
  );
  const summary = state.toolsetSummary || {};
  const summaryRow = row(
    `${summary.total || 0} discovered toolsets`,
    `${summary.registered || 0} registered · ${summary.healthy || 0} healthy · ${summary.needs_attention || 0} need attention`,
    tag('auto-discovered'),
  );
  target.innerHTML = summaryRow + (items.map((x) => {
    const warnings = (x.warnings || []).length ? ` · ${esc(x.warnings.join('; '))}` : '';
    const command = x.entrypoint ? `<code>python ${esc(x.path)}/${esc(x.entrypoint)}</code>` : '';
    const description = `${esc(x.description || 'Reusable repository toolset')}${warnings}${command}`;
    const linkPath = x.readme_path || x.manifest_path || `${x.path}/toolset.json`;
    return row(
      x.name || x.id,
      description,
      tag(`v${x.version || '?'}`) + tag(x.maturity || 'unknown') + tag(x.health || 'unknown', x.health !== 'ok') + (x.registered ? tag('cataloged') : tag('unregistered', true)),
      `${REPO_BASE}${linkPath}`,
    );
  }).join('') || '<div class="empty">No toolsets discovered.</div>');
}

function renderArtifacts() {
  const s = state.artifactSummary || {};
  const items = filter(state.artifacts, (x) => [x.path, x.name, x.artifact_type, x.related_case, x.migration_state, x.sha256, x.provenance, x.duplicate_group], (x, c) => c === 'all' || x.migration_state === c);
  const summary = row(`${s.total || 0} inventoried files`, `${s.orphaned || 0} without case links · ${s.duplicate_groups || 0} duplicate groups · ${bytes(s.bytes || 0)}`, tag('inventory'));
  $('#artifact-grid').innerHTML = summary + items.map((x) => row(x.name, `${esc(x.path)}${x.sha256 ? `<code>${esc(x.sha256.slice(0, 24))}…</code>` : ''}`, tag(x.migration_state, true) + tag(x.artifact_type) + (x.related_case ? tag(`case ${x.related_case}`) : tag('no case')))).join('');
}

function renderHealth() {
  const h = state.health;
  const s = h.summary || {};
  const out = [row(`${s.total_sources || 0} collection sources`, `${s.due_sources || 0} due · ${s.changed_sources || 0} changed · ${s.history_entries || 0} checks`, tag('health'))];
  (h.changed_sources || []).forEach((x) => out.push(row(x.name || x.source_id, esc(x.note || 'Source state changed.'), tag('changed', true) + tag(x.checked_at || ''))));
  (h.due_sources || []).forEach((x) => out.push(row(x.name, `Assigned: ${esc(x.assigned_agent)} · SLA ${esc(x.freshness_hours)}h`, tag(x.freshness_state, true), x.url)));
  $('#health-grid').innerHTML = out.join('');
}

function renderSources() {
  const items = filter(state.sources, (x) => [x.id, x.name, x.source_type, x.tier, x.assigned_agent, x.notes, x.freshness_state, ...(x.categories || [])], (x, c) => c === 'all' || (x.categories || []).includes(c));
  $('#source-grid').innerHTML = items.map((x) => row(x.name, `${esc(x.notes || 'Registered source')} · agent: ${esc(x.assigned_agent)}`, tag(x.freshness_state || 'unknown', x.freshness_state === 'due') + tag(`${x.freshness_hours}h`) + tag(x.tier), x.url)).join('') || '<div class="empty">No matches.</div>';
}

function renderPrompts() {
  const items = filter(state.prompts, (x) => [x.title, x.purpose, x.prompt]);
  $('#prompt-grid').innerHTML = items.map((x, i) => `<div class="row prompt" data-prompt="${i}"><div class="row-main"><b>${esc(x.title)}</b></div><div class="row-desc">${esc(x.purpose)}</div><div class="meta">${tag('copy prompt')}</div></div>`).join('') || '<div class="empty">No matches.</div>';
  all('.prompt').forEach((el) => {
    el.onclick = async () => {
      const prompt = items[Number(el.dataset.prompt)]?.prompt;
      if (prompt) {
        await navigator.clipboard.writeText(prompt);
        el.querySelector('.tag').textContent = 'copied';
      }
    };
  });
}

function render() {
  renderStats();
  renderOpportunities();
  renderIntel();
  renderCases();
  renderTools();
  renderToolsets();
  renderArtifacts();
  renderHealth();
  renderSources();
  renderPrompts();
}

function categories(tab) {
  const sel = $('#category');
  sel.innerHTML = '<option value="all">All</option>';
  let values = [];
  if (tab === 'opportunities') values = state.opportunities.map((x) => x.category);
  if (tab === 'intelligence') values = state.intelligence.map((x) => x.category);
  if (tab === 'sources') values = state.sources.flatMap((x) => x.categories || []);
  if (tab === 'artifacts') values = state.artifacts.map((x) => x.migration_state);
  if (tab === 'toolsets') values = state.toolsets.flatMap((x) => [x.maturity, x.health]).filter(Boolean);
  [...new Set(values)].sort().forEach((x) => sel.insertAdjacentHTML('beforeend', `<option value="${esc(x)}">${esc(x)}</option>`));
  sel.style.display = values.length ? 'block' : 'none';
}

const tabIcons = {
  home: '⌂', opportunities: '$', intelligence: '◫', cases: '◌', tools: '⚙', toolsets: '▦', artifacts: '◇', health: '◉', sources: '⌁', prompts: '⌘', workflow: '⇄',
};

function openTab(tab) {
  current = tab;
  all('[data-tab]').forEach((x) => x.classList.toggle('active', x.dataset.tab === tab));
  all('.panel').forEach((x) => x.classList.toggle('active', x.id === tab));
  const label = tab === 'home' ? 'home' : tab.replace(/-/g, ' ');
  $('#crumb').textContent = `cipher-solving-suite › workspace › ${label}`;
  $('#tab-title').textContent = label;
  $('#tab-icon').textContent = tabIcons[tab] || '•';
  $('#search').value = '';
  categories(tab);
  render();
  $('#sidebar').classList.remove('open');
}

function bindNavigation() {
  all('[data-tab]').forEach((x) => x.addEventListener('click', (event) => {
    if (x.tagName === 'A') return;
    event.preventDefault();
    openTab(x.dataset.tab);
  }));
  all('[data-open]').forEach((x) => { x.onclick = () => openTab(x.dataset.open); });
  $('#menu').onclick = () => $('#sidebar').classList.toggle('open');
  $('#search').addEventListener('input', render);
  $('#category').addEventListener('change', render);
}

async function init() {
  installDynamicToolsetUI();
  bindNavigation();
  try {
    const names = ['opportunities', 'prompts', 'tools', 'toolsets', 'cases', 'status', 'intelligence', 'sources', 'collection-health', 'artifacts'];
    const [ops, prompts, tools, toolsets, cases, status, intel, sources, health, artifacts] = await Promise.all(names.map((name) => loadJSON(`data/${name}.json`)));
    state.opportunities = ops.items || [];
    state.prompts = prompts.prompts || [];
    state.tools = tools.items || [];
    state.toolsets = toolsets.items || [];
    state.toolsetSummary = toolsets.summary || {};
    state.cases = cases.items || [];
    state.status = status || {};
    state.intelligence = intel.items || [];
    state.sources = sources.sources || [];
    state.health = health || {};
    state.artifacts = artifacts.items || [];
    state.artifactSummary = artifacts.summary || {};
    $('#catalog-meta').textContent = `${state.toolsets.length} toolsets · ${state.tools.length} tools · ${state.opportunities.length} opportunities · ${state.intelligence.length} intel · ${state.sources.length} sources · ${state.artifacts.length} evidence files · ${state.cases.length} cases`;
    categories('home');
    render();
  } catch (error) {
    $('#hub-status').textContent = 'data error';
    $('#catalog-meta').textContent = `Dashboard data error: ${error.message}`;
  }
}

init();
