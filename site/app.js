const state = {
  opportunities: [], prompts: [], tools: [], toolsets: [], toolsetSummary: {},
  cases: [], intelligence: [], sources: [], health: {}, artifacts: [], artifactSummary: {},
  repository: { files: [], directories: [], summary: {} }, status: {},
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

function actionRow(name, desc, meta, type, id) {
  return `<div class="row detail-row" role="button" tabindex="0" data-detail-type="${esc(type)}" data-detail-id="${esc(id)}" style="cursor:pointer"><div class="row-main"><b>${esc(name)}</b></div><div class="row-desc">${desc}</div><div class="meta">${meta}${tag('open ›')}</div></div>`;
}

function installDynamicUI() {
  if (!$('#toolsets')) {
    const workspaceChildren = $('.sidebar .tree-group .tree-children');
    if (workspaceChildren) {
      workspaceChildren.insertAdjacentHTML('beforeend', '<button data-tab="toolsets" class="tree-item">📦 <span>toolsets</span></button><button data-tab="repository" class="tree-item">▤ <span>repository-files</span></button>');
    }
    const activitySpacer = $('.activity-spacer');
    if (activitySpacer) activitySpacer.insertAdjacentHTML('beforebegin', '<button class="activity" data-tab="toolsets" title="Toolsets">▦</button><button class="activity" data-tab="repository" title="Repository files">▤</button>');
    const homeFolders = $('#home .folder-grid');
    if (homeFolders) homeFolders.insertAdjacentHTML('beforeend', '<button class="folder-card" data-open="toolsets"><span class="big-folder">📦</span><span><b>Toolsets</b><small>Reusable capability packs discovered from manifests</small></span></button><button class="folder-card" data-open="repository"><span class="big-folder">🗂️</span><span><b>Repository Files</b><small>Browse safe text files without leaving the workspace</small></span></button>');

    const editor = $('.editor');
    const statusbar = $('.statusbar');
    if (editor) {
      const toolsets = document.createElement('section');
      toolsets.id = 'toolsets'; toolsets.className = 'panel';
      toolsets.innerHTML = '<div class="panel-title"><div><span class="kicker">REPOSITORY / TOOLSETS</span><h2>Reusable Toolsets</h2></div><span>Auto-discovered from manifests and the toolset catalog. Click a toolset to inspect it.</span></div><div id="toolset-grid" class="data-list"></div>';
      const repository = document.createElement('section');
      repository.id = 'repository'; repository.className = 'panel';
      repository.innerHTML = '<div class="panel-title"><div><span class="kicker">REPOSITORY / FILE BROWSER</span><h2>Repository Files</h2></div><span>Bounded previews of public text files from operational repo lanes.</span></div><div id="repository-grid" class="data-list"></div>';
      const detail = document.createElement('section');
      detail.id = 'detail'; detail.className = 'panel';
      detail.innerHTML = '<div id="detail-content"></div>';
      const before = statusbar || null;
      editor.insertBefore(toolsets, before); editor.insertBefore(repository, before); editor.insertBefore(detail, before);
    }
  }
}

function renderStats() {
  const s = state.status;
  $('#hub-status').textContent = s.generated_at ? `snapshot ${new Date(s.generated_at).toLocaleString()}` : 'repository snapshot';
  $('#stats-grid').innerHTML = [
    ['Cases', s.active_cases || 0], ['Toolsets', s.toolsets || 0], ['Tools', s.tools || 0],
    ['Repo Files', s.repository_files || 0], ['Intel', s.intelligence || 0], ['Sources', s.intelligence_sources || 0],
    ['Evidence', s.artifacts || 0], ['Review', s.artifacts_review_before_move || 0],
  ].map(([key, value]) => `<div class="stat"><b>${esc(value)}</b><span>${esc(key)}</span></div>`).join('');
}

function filter(items, fields, catfn = () => true) {
  const q = text($('#search').value), cat = $('#category').value;
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
  const items = filter(state.tools.filter((x) => x.user_visible !== false), (x) => [x.id, x.name, x.category, x.path, x.command, x.description, x.maturity]);
  $('#tool-grid').innerHTML = items.map((x) => actionRow(x.name, `${esc(x.description)}<code>${esc(x.command)}</code>`, tag(x.category) + tag(x.maturity || 'registered'), 'tool', x.id)).join('') || '<div class="empty">No matches.</div>';
}
function renderToolsets() {
  const target = $('#toolset-grid'); if (!target) return;
  const items = filter(state.toolsets, (x) => [x.id, x.name, x.description, x.path, x.version, x.maturity, x.health, x.entrypoint, ...(x.warnings || [])], (x, c) => c === 'all' || x.maturity === c || x.health === c);
  const s = state.toolsetSummary || {};
  target.innerHTML = row(`${s.total || 0} discovered toolsets`, `${s.registered || 0} registered · ${s.healthy || 0} healthy · ${s.needs_attention || 0} need attention`, tag('auto-discovered')) +
    (items.map((x) => actionRow(x.name || x.id, esc(x.description || 'Reusable repository toolset'), tag(`v${x.version || '?'}`) + tag(x.maturity || 'unknown') + tag(x.health || 'unknown', x.health !== 'ok'), 'toolset', x.id)).join('') || '<div class="empty">No toolsets discovered.</div>');
}
function renderRepository() {
  const target = $('#repository-grid'); if (!target) return;
  const items = filter(state.repository.files || [], (x) => [x.path, x.name, x.parent, x.suffix], (x, c) => c === 'all' || x.parent === c || x.path.startsWith(`${c}/`));
  const s = state.repository.summary || {};
  target.innerHTML = row(`${s.files || 0} indexed files`, `${s.directories || 0} directories · ${s.previewable || 0} previewable text files`, tag('static index')) +
    (items.map((x) => actionRow(x.path, `${bytes(x.size)}${x.previewable ? ' · preview available' : ' · metadata only'}`, tag(x.suffix || 'file') + (x.previewable ? tag('preview') : tag('GitHub')), 'file', x.path)).join('') || '<div class="empty">No matching files.</div>');
}
function renderArtifacts() {
  const s = state.artifactSummary || {}, items = filter(state.artifacts, (x) => [x.path, x.name, x.artifact_type, x.related_case, x.migration_state, x.sha256, x.provenance, x.duplicate_group], (x, c) => c === 'all' || x.migration_state === c);
  $('#artifact-grid').innerHTML = row(`${s.total || 0} inventoried files`, `${s.orphaned || 0} without case links · ${s.duplicate_groups || 0} duplicate groups · ${bytes(s.bytes || 0)}`, tag('inventory')) + items.map((x) => row(x.name, `${esc(x.path)}${x.sha256 ? `<code>${esc(x.sha256.slice(0, 24))}…</code>` : ''}`, tag(x.migration_state, true) + tag(x.artifact_type) + (x.related_case ? tag(`case ${x.related_case}`) : tag('no case')))).join('');
}
function renderHealth() {
  const h = state.health, s = h.summary || {}, out = [row(`${s.total_sources || 0} collection sources`, `${s.due_sources || 0} due · ${s.changed_sources || 0} changed · ${s.history_entries || 0} checks`, tag('health'))];
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
  all('.prompt').forEach((el) => { el.onclick = async () => { const prompt = items[Number(el.dataset.prompt)]?.prompt; if (prompt) { await navigator.clipboard.writeText(prompt); el.querySelector('.tag').textContent = 'copied'; } }; });
}

function fileByPath(path) { return (state.repository.files || []).find((x) => x.path === path); }
function toolById(id) { return state.tools.find((x) => x.id === id); }
function toolsetById(id) { return state.toolsets.find((x) => x.id === id); }

function detailHeader(kicker, title, subtitle = '') {
  return `<div class="panel-title"><div><span class="kicker">${esc(kicker)}</span><h2>${esc(title)}</h2></div><span>${esc(subtitle)}</span></div>`;
}
function kv(label, value) {
  return `<div><b>${esc(label)}</b><span>${value}</span></div>`;
}
function fileAction(path) {
  const file = fileByPath(path);
  return actionRow(path, file ? `${bytes(file.size)}${file.previewable ? ' · preview available' : ''}` : 'Repository file', tag(file?.suffix || 'file'), 'file', path);
}

function showToolDetail(id) {
  const tool = toolById(id); if (!tool) return;
  const file = fileByPath(tool.path);
  const parentToolset = state.toolsets.find((x) => String(tool.path || '').startsWith(`${x.path}/`));
  const content = $('#detail-content');
  content.innerHTML = detailHeader('TOOLS / DETAIL', tool.name, tool.description || '') +
    `<div class="workflow">${kv('ID', `<code>${esc(tool.id)}</code>`)}${kv('Category', tag(tool.category || 'unknown'))}${kv('Maturity', tag(tool.maturity || 'unknown'))}${kv('Path', `<code>${esc(tool.path)}</code>`)}${kv('Command', `<code>${esc(tool.command || '')}</code>`)}${parentToolset ? kv('Toolset', `<button data-detail-type="toolset" data-detail-id="${esc(parentToolset.id)}" class="tree-item" style="padding-left:0">📦 ${esc(parentToolset.name)}</button>`) : ''}</div>` +
    `<div class="section-caption">FILES / SOURCE</div><div class="data-list">${file ? fileAction(tool.path) : row(tool.path || 'No source path', 'Source path not present in the browser index.', tag('metadata'))}</div>` +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid"><a href="${REPO_BASE}${esc(tool.path)}" target="_blank" rel="noopener">Open source on GitHub</a></div>`;
  openDetail(`tool: ${tool.name}`);
}

function showToolsetDetail(id) {
  const toolset = toolsetById(id); if (!toolset) return;
  const content = $('#detail-content');
  const warnings = (toolset.warnings || []).map((x) => `<div class="notice">${esc(x)}</div>`).join('');
  const tools = toolset.tools || [];
  const files = toolset.files || [];
  content.innerHTML = detailHeader('TOOLSETS / DETAIL', toolset.name || toolset.id, toolset.description || '') +
    `<div class="workflow">${kv('ID', `<code>${esc(toolset.id)}</code>`)}${kv('Version', tag(`v${toolset.version || '?'}`))}${kv('Maturity', tag(toolset.maturity || 'unknown'))}${kv('Health', tag(toolset.health || 'unknown', toolset.health !== 'ok'))}${kv('Path', `<code>${esc(toolset.path)}</code>`)}${kv('Entrypoint', `<code>${esc(toolset.entrypoint || 'none')}</code>`)}${kv('Catalog', toolset.registered ? tag('registered') : tag('unregistered', true))}</div>${warnings}` +
    `<div class="section-caption">TOOLS (${tools.length})</div><div class="data-list">${tools.length ? tools.map((x) => actionRow(x.name, esc(x.description || ''), tag(x.category || 'tool') + tag(x.maturity || 'unknown'), 'tool', x.id)).join('') : '<div class="empty">No tools registered under this toolset yet.</div>'}</div>` +
    `<div class="section-caption">FILES (${files.length})</div><div class="data-list">${files.length ? files.map(fileAction).join('') : '<div class="empty">No indexed files.</div>'}</div>` +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid"><a href="${REPO_BASE}${esc(toolset.readme_path || toolset.manifest_path)}" target="_blank" rel="noopener">Open on GitHub</a></div>`;
  openDetail(`toolset: ${toolset.name || toolset.id}`);
}

function showFileDetail(path) {
  const file = fileByPath(path); if (!file) return;
  const content = $('#detail-content');
  const preview = file.previewable ? `<pre style="white-space:pre-wrap;word-break:break-word;background:#181818;border:1px solid #333;color:#d4d4d4;padding:12px;max-height:65vh;overflow:auto;font:11px/1.5 ui-monospace,SFMono-Regular,Consolas,monospace">${esc(file.preview)}</pre>` : '<div class="notice">This file is metadata-only in the static browser. Open it on GitHub to inspect the full content.</div>';
  content.innerHTML = detailHeader('REPOSITORY / FILE', file.name, file.path) +
    `<div class="workflow">${kv('Path', `<code>${esc(file.path)}</code>`)}${kv('Directory', `<code>${esc(file.parent)}</code>`)}${kv('Size', esc(bytes(file.size)))}${kv('Type', tag(file.suffix || 'file'))}${kv('Preview', file.previewable ? tag(file.preview_truncated ? 'truncated' : 'available') : tag('not embedded'))}</div>` +
    `<div class="section-caption">PREVIEW</div>${preview}<div class="quick-grid"><a href="${REPO_BASE}${esc(file.path)}" target="_blank" rel="noopener">Open full file on GitHub</a></div>`;
  openDetail(file.path);
}

function openDetail(label) {
  current = 'detail';
  all('[data-tab]').forEach((x) => x.classList.remove('active'));
  all('.panel').forEach((x) => x.classList.toggle('active', x.id === 'detail'));
  $('#crumb').textContent = `cipher-solving-suite › ${label}`;
  $('#tab-title').textContent = label;
  $('#tab-icon').textContent = '◫';
  $('#category').style.display = 'none';
  $('#search').value = '';
  bindDetailActions();
  $('#sidebar').classList.remove('open');
}

function bindDetailActions() {
  all('[data-detail-type]').forEach((el) => {
    if (el.dataset.detailBound) return;
    const open = () => {
      const { detailType: type, detailId: id } = el.dataset;
      if (type === 'tool') showToolDetail(id);
      if (type === 'toolset') showToolsetDetail(id);
      if (type === 'file') showFileDetail(id);
    };
    el.addEventListener('click', (event) => { if (event.target.closest('a')) return; event.preventDefault(); open(); });
    el.addEventListener('keydown', (event) => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); open(); } });
    el.dataset.detailBound = '1';
  });
}

function render() {
  renderStats(); renderOpportunities(); renderIntel(); renderCases(); renderTools(); renderToolsets(); renderRepository(); renderArtifacts(); renderHealth(); renderSources(); renderPrompts(); bindDetailActions();
}

function categories(tab) {
  const sel = $('#category'); sel.innerHTML = '<option value="all">All</option>';
  let values = [];
  if (tab === 'opportunities') values = state.opportunities.map((x) => x.category);
  if (tab === 'intelligence') values = state.intelligence.map((x) => x.category);
  if (tab === 'sources') values = state.sources.flatMap((x) => x.categories || []);
  if (tab === 'artifacts') values = state.artifacts.map((x) => x.migration_state);
  if (tab === 'toolsets') values = state.toolsets.flatMap((x) => [x.maturity, x.health]).filter(Boolean);
  if (tab === 'repository') values = state.repository.roots || [];
  [...new Set(values)].sort().forEach((x) => sel.insertAdjacentHTML('beforeend', `<option value="${esc(x)}">${esc(x)}</option>`));
  sel.style.display = values.length ? 'block' : 'none';
}

const tabIcons = { home:'⌂', opportunities:'$', intelligence:'◫', cases:'◌', tools:'⚙', toolsets:'▦', repository:'▤', artifacts:'◇', health:'◉', sources:'⌁', prompts:'⌘', workflow:'⇄' };
function openTab(tab) {
  current = tab;
  all('[data-tab]').forEach((x) => x.classList.toggle('active', x.dataset.tab === tab));
  all('.panel').forEach((x) => x.classList.toggle('active', x.id === tab));
  const label = tab === 'home' ? 'home' : tab.replace(/-/g, ' ');
  $('#crumb').textContent = `cipher-solving-suite › workspace › ${label}`;
  $('#tab-title').textContent = label; $('#tab-icon').textContent = tabIcons[tab] || '•'; $('#search').value = '';
  categories(tab); render(); $('#sidebar').classList.remove('open');
}

function bindNavigation() {
  all('[data-tab]').forEach((x) => x.addEventListener('click', (event) => { if (x.tagName === 'A') return; event.preventDefault(); openTab(x.dataset.tab); }));
  all('[data-open]').forEach((x) => { x.onclick = () => openTab(x.dataset.open); });
  $('#menu').onclick = () => $('#sidebar').classList.toggle('open');
  $('#search').addEventListener('input', render); $('#category').addEventListener('change', render);
}

async function init() {
  installDynamicUI(); bindNavigation();
  try {
    const names = ['opportunities','prompts','tools','toolsets','repository','cases','status','intelligence','sources','collection-health','artifacts'];
    const [ops,prompts,tools,toolsets,repository,cases,status,intel,sources,health,artifacts] = await Promise.all(names.map((name) => loadJSON(`data/${name}.json`)));
    state.opportunities=ops.items||[]; state.prompts=prompts.prompts||[]; state.tools=tools.items||[];
    state.toolsets=toolsets.items||[]; state.toolsetSummary=toolsets.summary||{}; state.repository=repository||{files:[],directories:[],summary:{}};
    state.cases=cases.items||[]; state.status=status||{}; state.intelligence=intel.items||[]; state.sources=sources.sources||[];
    state.health=health||{}; state.artifacts=artifacts.items||[]; state.artifactSummary=artifacts.summary||{};
    $('#catalog-meta').textContent = `${state.toolsets.length} toolsets · ${state.tools.length} tools · ${state.repository.files.length} repo files · ${state.opportunities.length} opportunities · ${state.intelligence.length} intel · ${state.cases.length} cases`;
    categories('home'); render();
  } catch (error) {
    $('#hub-status').textContent='data error'; $('#catalog-meta').textContent=`Dashboard data error: ${error.message}`;
  }
}

init();
