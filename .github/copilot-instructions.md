# RunDo Energy Carbon Platform - AI Agent Instructions

## Project Overview

RunDo Energy Carbon Platform is a dark-themed energy and carbon management dashboard built with vanilla HTML/CSS/JavaScript. The platform provides monitoring, data analytics, operations & maintenance, asset management, and system administration capabilities for zero-carbon campus initiatives.

**Tech Stack:** Vanilla HTML5, CSS3 (with CSS Variables), JavaScript (ES6+), Chart.js 4.x, Lucide Icons  
**Architecture:** Multi-page application with iframe-based content loading  
**Theme:** Dark mode only (#0b1220 base background)  
**Language Support:** Bilingual (English/Chinese) with dynamic switching  

---

## Essential Commands

### Local Development
```powershell
# No build step required - static files served directly
# Open index.html in browser or use any static file server

# Example: Using Python HTTP server
python -m http.server 8080

# Or using Node.js http-server
npx http-server -p 8080
```

### File Generation Scripts
```powershell
# Generate device management page
.\generate-device-page.ps1

# Replace device data
.\replace-device-data.ps1
```

---

## Architecture & Component Boundaries

### Core Framework Files (DO NOT MODIFY)

| File | Purpose | Modification Rules |
|------|---------|-------------------|
| `index.html` | Main frame with topbar, sidebar, content iframe, AI panel | **Never modify** DOM structure, core styles, or iframe container |
| `app.js` | Framework logic: language switching, routing, menu rendering, iframe injection | Only append code in designated functions (language broadcast, iframe script injection). **Never modify** existing routing/menu/language core logic |
| `navbar-config.js` | Navigation & translation configuration | Only append new translations/module configs. **Never delete/modify** existing config items or object structures |
| `pages/` | Business pages directory | Only create new module folders/pages per spec. **Never modify/delete/move** existing modules |

### Page Structure Pattern

All business pages follow this structure:
```
pages/[module-id]/[page-name].html
```

**Module IDs:** `montior`, `datacenter`, `o&m`, `assert`, `system`  
**Naming Convention:** kebab-case only (e.g., `device-management.html`)  
**Menu Identifier:** Must match filename without `.html` extension exactly

### Data Flow

1. **Navigation:** User clicks sidebar → `app.js` loads page into `<iframe id="contentFrame">`
2. **Language Switching:** `toggleLanguage()` broadcasts `LANGUAGE_CHANGED` message to iframe
3. **Page Translation:** Pages listen for postMessage and update text via `t()` function
4. **Data Sources:** Static JSON files in `/data/` directory (e.g., `tree-data.json`)

---

## Project-Specific Conventions

### Naming Conventions (MANDATORY)

- **Folders/Files:** kebab-case only (`energy-prediction.html`, NOT `EnergyPrediction.html`)
- **Menu IDs:** Exact match with filename (without `.html`)
- **Module IDs:** Match folder name under `pages/`
- **CSS Classes:** Use descriptive prefixes (`.drawer-`, `.btn-`, `.form-`)
- **Variables:** camelCase for JS, kebab-case for CSS custom properties
- **NO Chinese/Pinyin naming** - English semantic names only

### Styling Standards

#### CSS Variables (Always Reuse)
```css
:root {
    --bg-base: #0b1220;           /* Base background */
    --bg-surface: #172131;        /* Surface level */
    --bg-elevated: #253247;       /* Elevated elements */
    --bg-content: #111a28;        /* Content areas */
    --text-primary: #F8FAFC;      /* Primary text */
    --text-secondary: #94A3B8;    /* Secondary text */
    --text-muted: #64748B;        /* Muted text */
    --accent-green: #22C55E;      /* Success/active states */
    --accent-blue: #3B82F6;       /* Primary actions */
    --accent-cyan: #06B6D4;       /* Info highlights */
    --accent-amber: #F59E0B;      /* Warnings */
    --accent-red: #EF4444;        /* Errors/danger */
    --border: #334155;            /* Borders */
    --font-ui: 'Fira Sans', sans-serif;
    --font-data: 'Fira Code', monospace;
}
```

#### Critical Style Rules
- **Page Background:** MUST be `background: transparent !important;` (framework handles background)
- **No Custom Topbars/Sidebars:** Framework provides these globally
- **Scrollbar Styling:** Use standard webkit scrollbar rules (6px width)
- **Font Families:** Fira Sans for UI, Fira Code for data/code

### Interaction Patterns

#### Drawer Components (PRIMARY interaction method)
**Use drawers for:** Forms, details, configurations, multi-field operations  
**Dimensions:** Small (360px), Medium (560px default), Large (720px)  
**Structure:** Fixed header + scrollable body + fixed footer

```html
<div class="drawer-mask" id="drawerMask"></div>
<div class="drawer-container" id="targetDrawer">
    <div class="drawer-header">
        <div class="drawer-title">Title</div>
        <button class="drawer-close-btn"><i data-lucide="x"></i></button>
    </div>
    <div class="drawer-body"><!-- Content --></div>
    <div class="drawer-footer">
        <button class="btn-secondary">Cancel</button>
        <button class="btn-primary">Confirm</button>
    </div>
</div>
```

#### Modal Dialogs (ONLY for confirmations)
**Use modals ONLY for:** Delete confirmations, risk warnings, success/failure notifications  
**NEVER use for:** Forms, details, business content

#### Toast Notifications
- Position: Top-right corner
- Auto-dismiss: 3 seconds
- Types: success (green), warning (amber), error (red), info (blue)

### Internationalization (i18n)

#### In Business Pages
Pages must support dynamic language switching via parent frame communication:

```javascript
// Listen for language changes from parent
window.addEventListener('message', (event) => {
    if (event.data.type === 'LANGUAGE_CHANGED') {
        currentLang = event.data.lang;
        updatePageTexts();
    }
});

// Translation helper
function t(key) {
    const keys = key.split('.');
    let value = translations[currentLang];
    for (const k of keys) {
        value = value?.[k];
    }
    return value || key;
}
```

#### Adding New Translations
In `navbar-config.js`:
```javascript
// English
translations.en.subMenus['module-id']['page-name'] = 'Page Name';

// Chinese
translations.zh.subMenus['module-id']['page-name'] = '页面名称';
```

### Data Management

#### JSON Data Sources
- Location: `/data/tree-data.json`
- Contains: Space hierarchy, organization structure, device metadata
- Usage: Load via `fetch('./data/tree-data.json')` in pages
- **ALWAYS use existing JSON data** - never hardcode sample data that conflicts

#### localStorage for CRUD Operations
```javascript
// Store mock data persistently
localStorage.setItem('devices', JSON.stringify(devices));
const devices = JSON.parse(localStorage.getItem('devices')) || [];
```

---

## Common Pitfalls & Solutions

### ❌ DON'T Do This

1. **Modify core framework files** (`index.html`, `app.js`, `navbar-config.js` core logic)
2. **Hardcode text strings** - always use i18n mechanism
3. **Create custom themes/colors** - reuse CSS variables only
4. **Mix drawer and modal usage** - follow strict interaction guidelines
5. **Use Chinese/Pinyin in filenames** - kebab-case English only
6. **Set opaque backgrounds on pages** - must be transparent
7. **Duplicate navigation components** - framework provides these
8. **Ignore existing JSON data** - always reference `/data/` files

### ✅ DO This Instead

1. **Extend safely** - append to arrays/objects, don't replace
2. **Use translation keys** - `t('modules.assert')` not `'Asset'`
3. **Reference CSS variables** - `var(--accent-green)` not `#22C55E`
4. **Drawers for business content** - forms, details, configs
5. **Semantic English names** - `device-management.html`
6. **Transparent backgrounds** - `background: transparent !important`
7. **Trust the framework** - focus on page content only
8. **Load from JSON** - `fetch('./data/tree-data.json')`

### Debugging Tips

#### Language Switching Not Working
- Check if page listens for `postMessage` events
- Verify `currentLang` variable updates correctly
- Ensure translation keys exist in `navbar-config.js`

#### Styles Not Applying
- Confirm page background is transparent
- Check CSS specificity (avoid overriding framework styles)
- Verify CSS variables are referenced correctly

#### Menu Item Not Appearing
- Filename must match menu ID exactly (case-sensitive)
- Module must exist in `navItems` array
- Submenu entry added to correct module's `subMenus` array

#### Data Loading Issues
- Use relative paths: `./data/tree-data.json` (not absolute)
- Handle async properly with `async/await` or `.then()`
- Provide fallback sample data for development

---

## Key Reference Files

### Documentation
- [`md文档/平台新增页面AI 开发执行手册.md`](md文档/平台新增页面AI%20开发执行手册.md) - Page creation workflow (MANDATORY reading)
- [`md文档/UI 组件库 AI 维护规范手册.md`](md文档/UI%20组件库%20AI%20维护规范手册.md) - UI component standards
- [`md文档/AI 前端原型功能要求规范手册.md`](md文档/AI%20前端原型功能要求规范手册.md) - Interaction patterns & prototypes
- [`md文档/JavaScript变量声明顺序规范-避坑指南.md`](md文档/JavaScript变量声明顺序规范-避坑指南.md) - JS declaration order

### Template Pages
- [`pages/system/account-management.html`](pages/system/account-management.html) - Standard CRUD page template
- [`pages/assert/device-management.html`](pages/assert/device-management.html) - Complex data management example

### Configuration
- [`navbar-config.js`](navbar-config.js) - All navigation & translation definitions
- [`data/tree-data.json`](data/tree-data.json) - Hierarchical data source

---

## Quick Start: Adding a New Page

### Scenario: Add "Energy Prediction" to Data Center Module

1. **Create page file**
   ```
   pages/datacenter/energy-prediction.html
   ```
   Use mandatory template from development manual

2. **Update navbar-config.js** (3 places)
   ```javascript
   // English translation
   translations.en.subMenus.datacenter['energy-prediction'] = 'Energy Prediction';
   
   // Chinese translation
   translations.zh.subMenus.datacenter['energy-prediction'] = '能耗预测';
   
   // Menu config
   { 
       id: 'datacenter',
       subMenus: ['comparative-analysis', 'smart-report', 'statistics-query', 'energy-prediction']
   }
   ```

3. **Verify app.js has language broadcast**
   ```javascript
   // In toggleLanguage() function
   const iframe = document.getElementById('contentFrame');
   if (iframe && iframe.contentWindow) {
       iframe.contentWindow.postMessage({
           type: 'LANGUAGE_CHANGED',
           lang: currentLang
       }, '*');
   }
   ```

4. **Test thoroughly**
   - Page loads in iframe
   - Language switching works
   - Menu appears in correct position
   - No console errors

---

## Related Skills & Extensions

For specialized tasks, consider creating:

- **Testing Skill**: Unit test patterns for vanilla JS components
- **Performance Skill**: Optimization techniques for large datasets
- **Accessibility Skill**: WCAG compliance for dark theme interfaces
- **Chart Configuration Skill**: Chart.js best practices for energy dashboards

---

## Version Information

- **Platform Version:** v1.0
- **Last Updated:** 2026-04-14
- **Framework Type:** Static multi-page with iframe content loading
- **Browser Support:** Modern browsers (Chrome 90+, Firefox 88+, Safari 14+)
