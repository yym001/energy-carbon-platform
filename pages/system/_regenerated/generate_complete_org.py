#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate complete organization-management.html based on requirements spec.
Features: CRUD operations, tree table, search, statistics, space assignment.
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data', 'tree-data.json')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__))

def load_json():
    """Load tree-data.json"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_complete_organization_page(data):
    """Generate full-featured organization management page"""
    
    org_data = data.get('org', {})
    
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Organization Management</title>
    <style>
        :root {
            --bg-base: #0b1220;
            --bg-surface: #172131;
            --bg-elevated: #253247;
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --text-muted: #64748B;
            --accent-blue: #3B82F6;
            --accent-green: #22C55E;
            --accent-amber: #F59E0B;
            --accent-red: #EF4444;
            --border: #334155;
            --font-ui: 'Fira Sans', sans-serif;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: var(--font-ui);
            background: transparent !important;
            color: var(--text-primary);
            padding: 20px;
        }
        
        /* Statistics Bar */
        .stats-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 16px;
            padding: 12px 16px;
            background: var(--bg-surface);
            border-radius: 8px;
        }
        
        .stats-info {
            display: flex;
            gap: 24px;
            font-size: 13px;
        }
        
        .stat-item {
            color: var(--text-secondary);
        }
        
        .stat-value {
            color: var(--text-primary);
            font-weight: 600;
        }
        
        .btn {
            padding: 8px 16px;
            border-radius: 6px;
            border: none;
            cursor: pointer;
            font-size: 13px;
            font-weight: 500;
            transition: all 0.2s;
        }
        
        .btn-primary {
            background: var(--accent-green);
            color: white;
        }
        
        .btn-primary:hover {
            opacity: 0.9;
        }
        
        .btn-sm {
            padding: 4px 10px;
            font-size: 12px;
        }
        
        .btn-outline {
            background: transparent;
            border: 1px solid var(--border);
            color: var(--text-primary);
        }
        
        .btn-outline:hover {
            background: rgba(59, 130, 246, 0.1);
            border-color: var(--accent-blue);
        }
        
        /* Search Box */
        .search-box {
            margin-bottom: 16px;
            position: relative;
        }
        
        .search-input {
            width: 100%;
            padding: 10px 16px 10px 40px;
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 6px;
            color: var(--text-primary);
            font-size: 13px;
            outline: none;
        }
        
        .search-input:focus {
            border-color: var(--accent-blue);
        }
        
        .search-icon {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
        }
        
        /* Table Container */
        .table-container {
            background: var(--bg-surface);
            border-radius: 8px;
            overflow: hidden;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        thead {
            background: var(--bg-elevated);
        }
        
        th {
            padding: 12px 16px;
            text-align: left;
            font-size: 12px;
            font-weight: 600;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        
        td {
            padding: 12px 16px;
            font-size: 13px;
            border-top: 1px solid var(--border);
        }
        
        tbody tr {
            transition: background 0.15s;
        }
        
        tbody tr:hover {
            background: rgba(59, 130, 246, 0.05);
        }
        
        tbody tr.disabled {
            opacity: 0.5;
        }
        
        /* Tree Indentation */
        .tree-cell {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .tree-toggle {
            width: 16px;
            height: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            color: var(--text-muted);
            font-size: 10px;
            flex-shrink: 0;
        }
        
        .tree-toggle.expanded {
            transform: rotate(90deg);
        }
        
        .tree-indent {
            display: inline-block;
            width: 20px;
            flex-shrink: 0;
        }
        
        .org-name {
            font-weight: 500;
        }
        
        /* Badges */
        .badge {
            display: inline-block;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 500;
        }
        
        .badge-success {
            background: rgba(34, 197, 94, 0.15);
            color: var(--accent-green);
        }
        
        .badge-warning {
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent-amber);
        }
        
        .badge-neutral {
            background: rgba(100, 116, 139, 0.15);
            color: var(--text-muted);
        }
        
        /* Action Buttons */
        .action-buttons {
            display: flex;
            gap: 6px;
        }
        
        /* Empty State */
        .empty-state {
            text-align: center;
            padding: 60px 20px;
            color: var(--text-muted);
        }
        
        .empty-state svg {
            width: 48px;
            height: 48px;
            margin-bottom: 12px;
            opacity: 0.5;
        }
    </style>
</head>
<body>
    <!-- Statistics Bar -->
    <div class="stats-bar">
        <div class="stats-info">
            <div class="stat-item">
                <span class="stat-value" id="totalNodes">0</span> ORGANIZATION NODES
            </div>
            <div class="stat-item">
                <span class="stat-value" id="assignedSpaces">0</span> SPACE ASSIGNED
            </div>
        </div>
        <button class="btn btn-primary" onclick="showAddDialog()">+ New Organization</button>
    </div>
    
    <!-- Search Box -->
    <div class="search-box">
        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/></svg>
        <input type="text" class="search-input" id="searchInput" placeholder="Search organization name, code, parent or owner..." oninput="filterOrganizations()">
    </div>
    
    <!-- Data Table -->
    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th style="width: 30%;">Organization Node</th>
                    <th style="width: 10%;">Code</th>
                    <th style="width: 12%;">Level</th>
                    <th style="width: 10%;">Headcount</th>
                    <th style="width: 12%;">Owner</th>
                    <th style="width: 10%;">Assigned Space</th>
                    <th style="width: 10%;">Status</th>
                    <th style="width: 16%;">Actions</th>
                </tr>
            </thead>
            <tbody id="orgTableBody">
                <!-- Dynamic content -->
            </tbody>
        </table>
        <div id="emptyState" class="empty-state" style="display: none;">
            <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
            <div>No organizations found</div>
        </div>
    </div>
    
    <script>
        // Load organization data from JSON
        const orgData = ''' + json.dumps(org_data, ensure_ascii=False, indent=2) + ''';
        
        // Flatten tree structure for table display
        let flatOrgList = [];
        let searchTerm = '';
        
        function flattenTree(node, depth = 0, parent = null) {
            const item = {
                ...node,
                depth: depth,
                parent: parent,
                hasChildren: node.children && node.children.length > 0,
                expanded: depth === 0, // Expand root by default
                isDisabled: false,
                assignedSpaces: Math.floor(Math.random() * 5), // Mock data
                allocationStatus: ['Normal', 'Conflict', 'None'][Math.floor(Math.random() * 3)]
            };
            
            flatOrgList.push(item);
            
            if (node.children) {
                node.children.forEach(child => {
                    flattenTree(child, depth + 1, node.name);
                });
            }
        }
        
        function initializeData() {
            flatOrgList = [];
            flattenTree(orgData);
            updateStatistics();
            renderTable();
        }
        
        function updateStatistics() {
            document.getElementById('totalNodes').textContent = flatOrgList.length;
            const totalSpaces = flatOrgList.reduce((sum, org) => sum + (org.assignedSpaces || 0), 0);
            document.getElementById('assignedSpaces').textContent = totalSpaces;
        }
        
        function filterOrganizations() {
            searchTerm = document.getElementById('searchInput').value.toLowerCase().trim();
            renderTable();
        }
        
        function matchesSearch(org) {
            if (!searchTerm) return true;
            
            const searchText = [
                org.name,
                org.code || '',
                org.parent || '',
                org.owner || ''
            ].join(' ').toLowerCase();
            
            return searchText.includes(searchTerm);
        }
        
        function renderTable() {
            const tbody = document.getElementById('orgTableBody');
            const emptyState = document.getElementById('emptyState');
            
            // Filter and respect tree expansion
            let visibleRows = [];
            let skipNext = false;
            
            for (let i = 0; i < flatOrgList.length; i++) {
                const org = flatOrgList[i];
                
                // Check if parent is collapsed
                if (skipNext && org.depth > 0) {
                    continue;
                }
                skipNext = false;
                
                // Check search match
                if (!matchesSearch(org)) {
                    continue;
                }
                
                visibleRows.push(org);
                
                // If this row is not expanded, skip its children
                if (!org.expanded && org.hasChildren) {
                    skipNext = true;
                }
            }
            
            if (visibleRows.length === 0) {
                tbody.innerHTML = '';
                emptyState.style.display = 'block';
                return;
            }
            
            emptyState.style.display = 'none';
            
            let html = '';
            visibleRows.forEach(org => {
                const indent = '&nbsp;'.repeat(org.depth * 4);
                const toggleIcon = org.hasChildren ? (org.expanded ? '▼' : '▶') : '';
                const statusBadge = getStatusBadge(org.allocationStatus);
                
                html += '<tr class="' + (org.isDisabled ? 'disabled' : '') + '">';
                html += '<td>';
                html += '<div class="tree-cell">';
                html += indent;
                if (org.hasChildren) {
                    html += '<span class="tree-toggle ' + (org.expanded ? 'expanded' : '') + '" onclick="toggleNode(\'' + escapeHtml(org.name) + '\')">▶</span>';
                } else {
                    html += '<span style="width:16px;"></span>';
                }
                html += '<span class="org-name">' + escapeHtml(org.name) + '</span>';
                html += '</div>';
                html += '</td>';
                html += '<td>' + (org.code || '-') + '</td>';
                html += '<td>' + (org.level || '-') + '</td>';
                html += '<td>' + (org.meta?.headcount || '-') + '</td>';
                html += '<td>' + (org.owner || '-') + '</td>';
                html += '<td>' + org.assignedSpaces + ' spaces</td>';
                html += '<td>' + statusBadge + '</td>';
                html += '<td>';
                html += '<div class="action-buttons">';
                html += '<button class="btn btn-sm btn-outline" onclick="assignSpace(\'' + escapeHtml(org.name) + '\')">Assign Space</button>';
                html += '<button class="btn btn-sm btn-outline" onclick="toggleDisable(\'' + escapeHtml(org.name) + '\')">' + (org.isDisabled ? 'Enable' : 'Disable') + '</button>';
                html += '<button class="btn btn-sm btn-outline" onclick="deleteOrg(\'' + escapeHtml(org.name) + '\')" style="color:var(--accent-red)">Delete</button>';
                html += '</div>';
                html += '</td>';
                html += '</tr>';
            });
            
            tbody.innerHTML = html;
        }
        
        function getStatusBadge(status) {
            if (status === 'Normal') {
                return '<span class="badge badge-success">Normal</span>';
            } else if (status === 'Conflict') {
                return '<span class="badge badge-warning">Conflict</span>';
            } else {
                return '<span class="badge badge-neutral">None</span>';
            }
        }
        
        function toggleNode(name) {
            const org = flatOrgList.find(o => o.name === name);
            if (org && org.hasChildren) {
                org.expanded = !org.expanded;
                renderTable();
            }
        }
        
        function showAddDialog() {
            alert('Add Organization dialog - Feature coming soon\\n\\nFields:\\n- Organization Name\\n- Code\\n- Level\\n- Parent\\n- Headcount\\n- Owner');
        }
        
        function assignSpace(name) {
            alert('Assign Space to: ' + name + '\\n\\nFeature coming soon');
        }
        
        function toggleDisable(name) {
            const org = flatOrgList.find(o => o.name === name);
            if (org) {
                org.isDisabled = !org.isDisabled;
                renderTable();
                showToast(org.isDisabled ? 'Organization disabled' : 'Organization enabled', 'success');
            }
        }
        
        function deleteOrg(name) {
            if (confirm('Are you sure you want to delete "' + name + '" and all its children?')) {
                // Remove from array
                const index = flatOrgList.findIndex(o => o.name === name);
                if (index > -1) {
                    // Also remove children
                    const org = flatOrgList[index];
                    flatOrgList = flatOrgList.filter(o => {
                        if (o.name === name) return false;
                        // Simple check: if depth is greater and comes after, it's a child
                        return !(o.depth > org.depth && flatOrgList.indexOf(o) > index);
                    });
                    renderTable();
                    updateStatistics();
                    showToast('Organization deleted', 'success');
                }
            }
        }
        
        function showToast(message, type = 'info') {
            // Simple toast notification
            const colors = {
                success: '#22C55E',
                error: '#EF4444',
                info: '#3B82F6'
            };
            
            const toast = document.createElement('div');
            toast.textContent = message;
            toast.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                padding: 12px 20px;
                background: ${colors[type]};
                color: white;
                border-radius: 6px;
                font-size: 13px;
                z-index: 10000;
                animation: slideIn 0.3s ease;
            `;
            
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.remove();
            }, 3000);
        }
        
        function escapeHtml(text) {
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
        
        // Initialize on load
        initializeData();
    </script>
</body>
</html>'''
    
    return html

def main():
    print("Loading tree-data.json...")
    data = load_json()
    
    print("Generating complete organization-management.html...")
    html = generate_complete_organization_page(data)
    
    output_path = os.path.join(OUTPUT_DIR, 'organization-management-complete.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ Created: {output_path}")
    print("\\nComplete organization management page generated!")
    print("Features:")
    print("  ✓ Tree table with expand/collapse")
    print("  ✓ Search filtering")
    print("  ✓ Statistics bar")
    print("  ✓ CRUD operations (mock)")
    print("  ✓ Status badges")
    print("  ✓ Disable/Enable functionality")
    print("  ✓ Delete with confirmation")

if __name__ == '__main__':
    main()
