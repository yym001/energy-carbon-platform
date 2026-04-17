// Navbar Configuration - Auto-generated from pages directory structure
const NAVBAR_CONFIG = {
    defaultLang: 'en',
    translations: {
        en: {
            brandName: 'RunDo',
            sysName: 'Energy Carbon Center',
            weather: 'Sunny',
            aiAssistant: 'iRun AI Assistant',
            aiPlaceholder: 'Type your question...',
            send: 'Send',
            greeting: 'Hello! I am iRun AI Assistant, how can I help you?',
            admin: 'Admin',
            role: 'Energy Manager',
            cockpit: 'Dashboard',
            modules: {
                montior: 'Monitor',
                datacenter: 'Data Center',
                'o&m': 'O&M',
                assert: 'Asset',
                system: 'System'
            },
            subMenus: {
                montior: {
                    'overview': 'Overview',
                    'settings': 'Settings'
                },
                datacenter: {
                    'comparative-analysis': 'Comparative Analysis',
                    'smart-report': 'Smart Report',
                    'statistics-query': 'Statistics Query'
                },
                'o&m': {
                    'alarm-center': 'Alarm Center',
                    'notification-center': 'Notification Center',
                    'rule-engine': 'Rule Engine'
                },
                system: {
                    'account-management': 'Account Management',
                    'benchmark-management': 'Benchmark Management',
                    'organization-management': 'Organization Management',
                    'role-management': 'Role Management',
                    'space-management': 'Space Management',
                    'tariff-management': 'Tariff Management'
                },
                assert: {
                    'device-management': 'Device Management',
                    'meter-management': 'Meter Management'
                }
            }
        },
        zh: {
            brandName: 'RundDo',
            sysName: '能源碳管理中心',
            weather: '晴',
            aiAssistant: 'iRun AI 助手',
            aiPlaceholder: '输入你的问题...',
            send: '发送',
            greeting: '你好！我是 iRun AI 助手，有什么可以帮助你的吗？',
            admin: '管理员',
            role: '能源经理',
            cockpit: '驾驶仓',
            modules: {
                montior: '监控',
                datacenter: '数据中心',
                'o&m': '运维',
                assert: '资产',
                system: '系统'
            },
            subMenus: {
                montior: {
                    'overview': '概览',
                    'settings': '设置'
                },
                datacenter: {
                    'comparative-analysis': '对比分析',
                    'smart-report': '智能报表',
                    'statistics-query': '统计查询'
                },
                'o&m': {
                    'alarm-center': '告警中心',
                    'notification-center': '通知中心',
                    'rule-engine': '规则引擎'
                },
                system: {
                    'account-management': '账号管理',
                    'benchmark-management': '基准管理',
                    'organization-management': '组织管理',
                    'role-management': '角色管理',
                    'space-management': '空间管理',
                    'tariff-management': '电价管理'
                },
                assert: {
                    'device-management': '设备管理',
                    'meter-management': '电表管理'
                }
            }
        }
    },
    navItems: [
        { 
            id: 'montior', 
            titleKey: 'modules.montior',
            icon: 'activity', 
            url: './pages/montior/overview.html', 
            subMenus: ['overview', 'settings']
        },
        { 
            id: 'datacenter', 
            titleKey: 'modules.datacenter',
            icon: 'database', 
            url: './pages/datacenter/comparative-analysis.html', 
            subMenus: ['comparative-analysis', 'smart-report', 'statistics-query']
        },
        { 
            id: 'o&m', 
            titleKey: 'modules.o&m',
            icon: 'wrench', 
            url: './pages/o&m/alarm-center.html', 
            subMenus: ['alarm-center', 'notification-center', 'rule-engine']
        },
        { 
            id: 'assert', 
            titleKey: 'modules.assert',
            icon: 'box', 
            url: './pages/assert/device-management.html', 
            subMenus: ['device-management', 'meter-management']
        },
        { 
            id: 'system', 
            titleKey: 'modules.system',
            icon: 'settings', 
            url: './pages/system/account-management.html', 
            subMenus: ['account-management', 'benchmark-management', 'organization-management', 'role-management', 'space-management', 'tariff-management']
        }
    ],
    defaultModule: 'montior'
};
