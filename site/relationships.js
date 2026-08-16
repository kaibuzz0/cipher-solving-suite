/* Cross-linked repository detail views layered over app.js.
 * Keep this file data-driven: normal repo content changes should not require UI edits.
 */

function caseId(item) { return item.case_id || item.id || item.name; }
function caseById(id) { return state.cases.find((x) => caseId(x) === id); }
function intelById(id) { return state.intelligence.find((x) => x.id === id); }
function opportunityById(id) { return state.opportunities.find((x) => x.id === id); }
function sourceById(id) { return state.sources.find((x) => x.id === id); }
function artifactByPath(path) { return state.artifacts.find((x) => x.path === path); }
function listTags(values) { return (values || []).map((x) => tag(x)).join('') || tag('none'); }
function externalAction(url, label) { return url ? `<a href="${esc(url)}" target="_blank" rel="noopener">${esc(label)}</a>` : ''; }
function relationButton(type, id, label, icon = '↳') {
  return `<button data-detail-type="${esc(type)}" data-detail-id="${esc(id)}" class="tree-item" style="padding-left:0">${icon} <span>${esc(label)}</span></button>`;
}
function repoFileOrRow(path, description = 'Repository path') {
  if (!path) return '';
  const file = fileByPath(path);
  if (file) return fileAction(path);
  const artifact = artifactByPath(path);
  if (artifact) return actionRow(path, description, tag(artifact.artifact_type || 'artifact'), 'artifact', path);
  return row(path, description, tag('path'), `${REPO_BASE}${path}`);
}

renderOpportunities = function renderOpportunitiesLinked() {
  const items = filter(state.opportunities, (x) => [x.id, x.name, x.category, x.description, ...(x.tags || [])], (x, c) => c === 'all' || x.category === c);
  $('#opportunity-grid').innerHTML = items.map((x) => actionRow(x.name, esc(x.description), tag(x.category) + (x.authorized_only ? tag('scope required', true) : tag('open research')), 'opportunity', x.id)).join('') || '<div class="empty">No matches.</div>';
};

renderIntel = function renderIntelLinked() {
  const items = filter(state.intelligence, (x) => [x.id, x.title, x.summary, x.category, x.source_name, ...(x.tags || [])], (x, c) => c === 'all' || x.category === c);
  $('#intel-grid').innerHTML = items.map((x) => actionRow(x.title, esc(x.summary), tag(x.category) + tag(`confidence ${x.confidence || 'unknown'}`) + tag(x.relevance || 'unknown'), 'intelligence', x.id)).join('') || '<div class="empty">No matches.</div>';
};

renderCases = function renderCasesLinked() {
  const items = filter(state.cases, (x) => [caseId(x), x.name, x.title, x.type, x.status, x.owner, x.next_action, x.source, ...(x.tags || [])]);
  $('#case-grid').innerHTML = items.map((x) => actionRow(x.name || x.title || caseId(x), esc(x.next_action ? `Next: ${x.next_action}` : (x.summary || x.objective || x.source || 'Structured research case')), tag(x.type || 'case') + tag(x.status || 'active') + (x.owner ? tag(x.owner) : ''), 'case', caseId(x))).join('') || '<div class="empty">No active cases.</div>';
};

renderArtifacts = function renderArtifactsLinked() {
  const s = state.artifactSummary || {};
  const items = filter(state.artifacts, (x) => [x.path, x.name, x.artifact_type, x.related_case, x.migration_state, x.sha256, x.provenance, x.duplicate_group], (x, c) => c === 'all' || x.migration_state === c);
  $('#artifact-grid').innerHTML = row(`${s.total || 0} inventoried files`, `${s.orphaned || 0} without case links · ${s.duplicate_groups || 0} duplicate groups · ${bytes(s.bytes || 0)}`, tag('inventory')) + items.map((x) => actionRow(x.name || x.path, `${esc(x.path)}${x.sha256 ? `<code>${esc(x.sha256.slice(0, 24))}…</code>` : ''}`, tag(x.migration_state || 'unknown', String(x.migration_state || '').includes('REVIEW')) + tag(x.artifact_type || 'artifact') + (x.related_case ? tag(`case ${x.related_case}`) : tag('no case')), 'artifact', x.path)).join('');
};

renderSources = function renderSourcesLinked() {
  const items = filter(state.sources, (x) => [x.id, x.name, x.source_type, x.tier, x.assigned_agent, x.notes, x.freshness_state, ...(x.categories || [])], (x, c) => c === 'all' || (x.categories || []).includes(c));
  $('#source-grid').innerHTML = items.map((x) => actionRow(x.name, `${esc(x.notes || 'Registered source')} · agent: ${esc(x.assigned_agent || 'unassigned')}`, tag(x.freshness_state || 'unknown', ['due','never-checked'].includes(x.freshness_state)) + tag(`${x.freshness_hours || '?'}h`) + tag(x.tier || 'source'), 'source', x.id)).join('') || '<div class="empty">No matches.</div>';
};

renderHealth = function renderHealthLinked() {
  const h = state.health, s = h.summary || {};
  const out = [row(`${s.total_sources || 0} collection sources`, `${s.due_sources || 0} due · ${s.changed_sources || 0} changed · ${s.history_entries || 0} checks`, tag('health'))];
  (h.changed_sources || []).forEach((x) => out.push(actionRow(x.name || x.source_id, esc(x.note || 'Source state changed.'), tag('changed', true) + tag(x.checked_at || ''), 'source', x.source_id)));
  (h.due_sources || []).forEach((x) => out.push(actionRow(x.name, `Assigned: ${esc(x.assigned_agent || 'unassigned')} · SLA ${esc(x.freshness_hours)}h`, tag(x.freshness_state || 'due', true), 'source', x.id || x.source_id)));
  $('#health-grid').innerHTML = out.join('');
};

function showOpportunityDetail(id) {
  const item = opportunityById(id); if (!item) return;
  const relatedIntel = state.intelligence.filter((x) => x.category === item.category || (x.tags || []).some((t) => (item.tags || []).includes(t))).slice(0, 8);
  $('#detail-content').innerHTML = detailHeader('OPPORTUNITIES / DETAIL', item.name, item.description || '') +
    `<div class="workflow">${kv('ID', `<code>${esc(item.id)}</code>`)}${kv('Category', tag(item.category || 'unknown'))}${kv('Authorization', item.authorized_only ? tag('published scope required', true) : tag('standard participation'))}${kv('Tags', listTags(item.tags))}</div>` +
    `<div class="notice"><strong>Verification:</strong> Rules, eligibility, payout, deadlines and scope can change. Verify the official source before committing time or testing anything.</div>` +
    `<div class="section-caption">RELATED INTELLIGENCE (${relatedIntel.length})</div><div class="data-list">${relatedIntel.length ? relatedIntel.map((x) => actionRow(x.title, esc(x.summary), tag(x.confidence || 'unknown') + tag(x.relevance || 'unknown'), 'intelligence', x.id)).join('') : '<div class="empty">No related intelligence currently linked.</div>'}</div>` +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid">${externalAction(item.url, 'Open official source')}</div>`;
  openDetail(`opportunity: ${item.name}`);
}

function showIntelligenceDetail(id) {
  const item = intelById(id); if (!item) return;
  const source = sourceById(item.source_id);
  const relatedCase = item.related_case ? caseById(item.related_case) : null;
  $('#detail-content').innerHTML = detailHeader('INTELLIGENCE / DETAIL', item.title, item.summary || '') +
    `<div class="workflow">${kv('ID', `<code>${esc(item.id)}</code>`)}${kv('Category', tag(item.category || 'unknown'))}${kv('Confidence', tag(item.confidence || 'unknown'))}${kv('Relevance', tag(item.relevance || 'unknown'))}${kv('Published', esc(item.published_at || 'unknown'))}${kv('Checked', esc(item.checked_at || 'unknown'))}${kv('Tags', listTags(item.tags))}${source ? kv('Source', relationButton('source', source.id, source.name, '⌁')) : kv('Source', esc(item.source_name || 'unknown'))}${relatedCase ? kv('Case', relationButton('case', caseId(relatedCase), relatedCase.name || caseId(relatedCase), '◌')) : ''}</div>` +
    (item.agent_notes ? `<div class="section-caption">AGENT NOTES</div><div class="notice">${esc(item.agent_notes)}</div>` : '') +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid">${externalAction(item.source_url, 'Open source')}</div>`;
  openDetail(`intel: ${item.title}`);
}

function showCaseDetail(id) {
  const item = caseById(id); if (!item) return;
  const evidence = item.evidence || [];
  const scripts = item.analysis_scripts || [];
  const notes = item.notes || [];
  const linkedArtifacts = state.artifacts.filter((x) => x.related_case === id || (item.repo_path && String(x.path || '').startsWith(`${item.repo_path}/`)));
  const evidenceRows = evidence.map((x) => repoFileOrRow(x.path, x.role || 'case evidence')).join('');
  const extraArtifacts = linkedArtifacts.filter((x) => !evidence.some((e) => e.path === x.path)).slice(0, 50).map((x) => actionRow(x.name || x.path, esc(x.path), tag(x.artifact_type || 'artifact') + tag(x.migration_state || 'unknown'), 'artifact', x.path)).join('');
  $('#detail-content').innerHTML = detailHeader('CASES / DETAIL', item.name || item.title || id, item.next_action || '') +
    `<div class="workflow">${kv('Case ID', `<code>${esc(id)}</code>`)}${kv('Type', tag(item.type || 'case'))}${kv('Status', tag(item.status || 'unknown'))}${kv('Owner', tag(item.owner || 'unclaimed'))}${kv('Source', esc(item.source || 'unknown'))}${kv('Updated', esc(item.updated_at || 'unknown'))}${kv('Tags', listTags(item.tags))}</div>` +
    `<div class="section-caption">NEXT ACTION</div><div class="notice">${esc(item.next_action || 'No next action recorded.')}</div>` +
    `<div class="section-caption">EVIDENCE</div><div class="data-list">${evidenceRows || extraArtifacts ? evidenceRows + extraArtifacts : '<div class="empty">No evidence linked.</div>'}</div>` +
    `<div class="section-caption">ANALYSIS SCRIPTS (${scripts.length})</div><div class="data-list">${scripts.length ? scripts.map((x) => repoFileOrRow(x, 'Case analysis script')).join('') : '<div class="empty">No analysis scripts linked.</div>'}</div>` +
    `<div class="section-caption">NOTES (${notes.length})</div><div class="data-list">${notes.length ? notes.map((x) => repoFileOrRow(x, 'Case notes')).join('') : '<div class="empty">No notes linked.</div>'}</div>` +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid">${externalAction(item.source_url, 'Open source')}${item.repo_path ? `<a href="https://github.com/kaibuzz0/cipher-solving-suite/tree/main/${esc(item.repo_path)}" target="_blank" rel="noopener">Open case folder</a>` : ''}</div>`;
  openDetail(`case: ${item.name || id}`);
}

function showArtifactDetail(path) {
  const item = artifactByPath(path); if (!item) { showFileDetail(path); return; }
  const linkedCase = item.related_case ? caseById(item.related_case) : null;
  const file = fileByPath(path);
  $('#detail-content').innerHTML = detailHeader('EVIDENCE / DETAIL', item.name || path, path) +
    `<div class="workflow">${kv('Type', tag(item.artifact_type || 'artifact'))}${kv('Migration', tag(item.migration_state || 'unknown', String(item.migration_state || '').includes('REVIEW')))}${kv('SHA-256', item.sha256 ? `<code>${esc(item.sha256)}</code>` : tag('not recorded'))}${kv('Provenance', esc(item.provenance || 'unknown'))}${item.duplicate_group ? kv('Duplicate Group', `<code>${esc(item.duplicate_group)}</code>`) : ''}${linkedCase ? kv('Case', relationButton('case', caseId(linkedCase), linkedCase.name || caseId(linkedCase), '◌')) : ''}</div>` +
    `<div class="section-caption">FILE</div><div class="data-list">${file ? fileAction(path) : row(path, 'Artifact path; preview not embedded in repository browser.', tag('evidence'), `${REPO_BASE}${path}`)}</div>`;
  openDetail(`evidence: ${item.name || path}`);
}

function showSourceDetail(id) {
  const item = sourceById(id); if (!item) return;
  const intel = state.intelligence.filter((x) => x.source_id === id);
  $('#detail-content').innerHTML = detailHeader('INTELLIGENCE / SOURCE', item.name, item.notes || '') +
    `<div class="workflow">${kv('ID', `<code>${esc(item.id)}</code>`)}${kv('Type', tag(item.source_type || 'source'))}${kv('Tier', tag(item.tier || 'unknown'))}${kv('Freshness', tag(item.freshness_state || 'unknown', ['due','never-checked'].includes(item.freshness_state)))}${kv('SLA', `${esc(item.freshness_hours || '?')} hours`)}${kv('Agent', tag(item.assigned_agent || 'unassigned'))}${kv('Categories', listTags(item.categories))}${kv('Last Checked', esc(item.last_checked_at || 'never'))}</div>` +
    `<div class="section-caption">INTELLIGENCE FROM THIS SOURCE (${intel.length})</div><div class="data-list">${intel.length ? intel.map((x) => actionRow(x.title, esc(x.summary), tag(x.confidence || 'unknown') + tag(x.relevance || 'unknown'), 'intelligence', x.id)).join('') : '<div class="empty">No published intelligence from this source yet.</div>'}</div>` +
    `<div class="section-caption">ACTIONS</div><div class="quick-grid">${externalAction(item.url, 'Open source')}</div>`;
  openDetail(`source: ${item.name}`);
}

bindDetailActions = function bindAllDetailActions() {
  all('[data-detail-type]').forEach((el) => {
    if (el.dataset.detailBound) return;
    const open = () => {
      const { detailType: type, detailId: id } = el.dataset;
      if (type === 'tool') showToolDetail(id);
      else if (type === 'toolset') showToolsetDetail(id);
      else if (type === 'file') showFileDetail(id);
      else if (type === 'opportunity') showOpportunityDetail(id);
      else if (type === 'intelligence') showIntelligenceDetail(id);
      else if (type === 'case') showCaseDetail(id);
      else if (type === 'artifact') showArtifactDetail(id);
      else if (type === 'source') showSourceDetail(id);
    };
    el.addEventListener('click', (event) => { if (event.target.closest('a')) return; event.preventDefault(); open(); });
    el.addEventListener('keydown', (event) => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); open(); } });
    el.dataset.detailBound = '1';
  });
};

render();
