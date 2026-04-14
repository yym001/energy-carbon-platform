// Application Logic
let currentLang = NAVBAR_CONFIG.defaultLang;
let currentModule = NAVBAR_CONFIG.defaultModule;
let activeSubMenu = null;

function t(key) {
    const keys = key.split('.');
    let value = NAVBAR_CONFIG.translations[currentLang];
    for (const k of keys) {
        if (value && typeof value === 'object') {
            value = value[k];
        } else {
            return key;
        }
    }
    return value || key;
}

function updateClock() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    document.getElementById('clockText').textContent = `${hours}:${minutes}`;
}

function renderSidebar() {
    const nav = document.getElementById('rightNav');
    nav.innerHTML = '';
    
    NAVBAR_CONFIG.navItems.forEach(item => {
        const groupDiv = document.createElement('div');
        groupDiv.className = 'nav-item-group';
        groupDiv.dataset.moduleId = item.id;
        
        const navItem = document.createElement('div');
        navItem.className = 'nav-item';
        navItem.innerHTML = `
            <i data-lucide="${item.icon}" class="nav-icon"></i>
            <span>${t(item.titleKey)}</span>
        `;
        
        if (item.subMenus && item.subMenus.length > 0) {
            const flyout = document.createElement('div');
            flyout.className = 'nav-flyout';
            const subMenuTranslations = NAVBAR_CONFIG.translations[currentLang].subMenus[item.id] || {};
            flyout.innerHTML = `
                <div class="nav-flyout-title">${t(item.titleKey)}</div>
                ${item.subMenus.map(sub => {
                    const label = subMenuTranslations[sub] || sub;
                    return `
                    <div class="nav-flyout-item" data-submenu="${sub}">
                        <span>${label}</span>
                    </div>
                    `;
                }).join('')}
            `;
            
            groupDiv.appendChild(navItem);
            groupDiv.appendChild(flyout);
            
            // Click to toggle flyout
            navItem.addEventListener('click', (e) => {
                e.stopPropagation();
                // Close other flyouts
                document.querySelectorAll('.nav-item-group').forEach(g => {
                    if (g !== groupDiv) g.classList.remove('show-flyout');
                });
                groupDiv.classList.toggle('show-flyout');
            });
            
            // Click on flyout item
            flyout.addEventListener('click', (e) => {
                const flyoutItem = e.target.closest('.nav-flyout-item');
                if (flyoutItem) {
                    selectSubMenu(item.id, flyoutItem.dataset.submenu);
                    // Close flyout after selection
                    groupDiv.classList.remove('show-flyout');
                }
            });
        } else {
            groupDiv.appendChild(navItem);
            navItem.addEventListener('click', () => selectModule(item.id));
        }
        
        nav.appendChild(groupDiv);
    });
    
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    // Close flyouts when clicking outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-item-group')) {
            document.querySelectorAll('.nav-item-group').forEach(g => {
                g.classList.remove('show-flyout');
            });
        }
    });
}

function selectModule(moduleId) {
    currentModule = moduleId;
    activeSubMenu = null;
    
    document.querySelectorAll('.nav-item-group').forEach(group => {
        const isActive = group.dataset.moduleId === moduleId;
        group.classList.remove('show-flyout');
        const navItem = group.querySelector('.nav-item');
        if (navItem) {
            navItem.classList.toggle('active', isActive);
        }
    });
    
    updateTopBar();
    loadModulePage(moduleId);
}

function selectSubMenu(moduleId, subMenuName) {
    currentModule = moduleId;
    activeSubMenu = subMenuName;
    
    document.querySelectorAll('.nav-item-group').forEach(group => {
        const isActive = group.dataset.moduleId === moduleId;
        const navItem = group.querySelector('.nav-item');
        if (navItem) {
            navItem.classList.toggle('active', isActive);
        }
        
        const flyoutItems = group.querySelectorAll('.nav-flyout-item');
        flyoutItems.forEach(item => {
            item.classList.toggle('active', item.dataset.submenu === subMenuName);
        });
    });
    
    updateTopBar();
    loadSubMenuPage(moduleId, subMenuName);
}

function loadSubMenuPage(moduleId, subMenuName) {
    // Construct the URL based on module and submenu
    const url = `./pages/${moduleId}/${subMenuName}.html`;
    const iframe = document.getElementById('contentFrame');
    iframe.src = url;
    console.log(`Loading page: ${url}`);
}

function updateTopBar() {
    const module = NAVBAR_CONFIG.navItems.find(m => m.id === currentModule);
    if (!module) return;
    
    document.getElementById('moduleNameDisplay').textContent = t(module.titleKey);
    
    const container = document.getElementById('topMenuContainer');
    const sep = document.getElementById('topMenuSep');
    
    // Show submodule navigation in top bar (synced with sidebar)
    if (module.subMenus && module.subMenus.length > 0) {
        sep.style.display = 'inline';
        container.style.display = 'flex';
        const subMenuTranslations = NAVBAR_CONFIG.translations[currentLang].subMenus[module.id] || {};
        container.innerHTML = module.subMenus.map(sub => {
            const label = subMenuTranslations[sub] || sub;
            return `
            <div class="sub-menu ${activeSubMenu === sub ? 'active' : ''}" 
                 data-submenu="${sub}">
                ${label}
            </div>
            `;
        }).join('');
        
        container.querySelectorAll('.sub-menu').forEach(item => {
            item.addEventListener('click', () => {
                selectSubMenu(currentModule, item.dataset.submenu);
            });
        });
    } else {
        sep.style.display = 'none';
        container.style.display = 'none';
    }
}

function loadModulePage(moduleId) {
    const module = NAVBAR_CONFIG.navItems.find(m => m.id === moduleId);
    if (module && module.url) {
        const iframe = document.getElementById('contentFrame');
        iframe.src = module.url;
    }
}

function toggleLanguage() {
    currentLang = currentLang === 'en' ? 'zh' : 'en';
    
    document.getElementById('langEn').classList.toggle('active', currentLang === 'en');
    document.getElementById('langCn').classList.toggle('active', currentLang === 'zh');
    
    document.getElementById('brandName').textContent = t('brandName');
    document.getElementById('sysName').textContent = t('sysName');
    document.getElementById('weatherText').textContent = `32°C ${t('weather')}`;
    document.getElementById('userName').textContent = t('admin');
    document.getElementById('userRole').textContent = t('role');
    document.getElementById('aiTitle').textContent = t('aiAssistant');
    document.getElementById('aiGreeting').textContent = t('greeting');
    document.getElementById('aiInput').placeholder = t('aiPlaceholder');
    document.getElementById('sendBtnText').textContent = t('send');
    
    renderSidebar();
    updateTopBar();
    
    // Notify iframe content pages about language change
    const iframe = document.getElementById('contentFrame');
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage({
            type: 'LANGUAGE_CHANGED',
            lang: currentLang
        }, '*');
    }
}

function init() {
    renderSidebar();
    selectModule(NAVBAR_CONFIG.defaultModule);
    
    document.getElementById('langToggle').addEventListener('click', toggleLanguage);
    
    document.getElementById('aiToggleBtn').addEventListener('click', () => {
        document.getElementById('mainWrap').classList.toggle('ai-open');
        document.getElementById('aiToggleBtn').classList.toggle('active');
    });
    
    document.getElementById('aiCloseBtn').addEventListener('click', () => {
        document.getElementById('mainWrap').classList.remove('ai-open');
        document.getElementById('aiToggleBtn').classList.remove('active');
    });
    
    document.getElementById('aiSendBtn').addEventListener('click', () => {
        const input = document.getElementById('aiInput');
        const message = input.value.trim();
        if (message) {
            console.log('AI Message:', message);
            input.value = '';
        }
    });
    
    updateClock();
    setInterval(updateClock, 1000);
    
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }
    
    console.log('Navbar initialized successfully!');
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
