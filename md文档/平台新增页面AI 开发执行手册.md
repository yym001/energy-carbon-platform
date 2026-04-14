# 平台 新增页面 AI 开发执行手册

**文档版本**：v1.0

**适用系统**：RunDo Energy Carbon Platform v1.0

**核心用途**：本手册为 AI 执行平台新增页面 / 模块开发的**唯一标准化操作指南**，AI 必须严格按照本手册的步骤、规范、约束规则执行开发任务，不得擅自修改核心框架文件、不得突破规范要求、不得遗漏校验环节。

------

## 一、AI 执行前置认知与硬约束规则

### 1.1 核心框架文件认知（AI 必须牢记，禁止擅自修改）

AI 必须明确以下核心文件的作用，仅可在本手册指定的范围内修改，**禁止修改文件内的原有核心逻辑**



|            文件路径             |                          核心作用                           |                        AI 可修改范围                         |                  绝对禁止操作                   |
| :-----------------------------: | :---------------------------------------------------------: | :----------------------------------------------------------: | :---------------------------------------------: |
|    工作 / 导航栏 /index.html    |    主框架入口，承载顶部栏、侧边栏、内容 iframe、AI 面板     |                              无                              |    禁止修改 DOM 结构、核心样式、iframe 容器     |
|      工作 / 导航栏 /app.js      | 框架核心逻辑，实现语言切换、路由加载、菜单渲染、iframe 注入 | 仅可在本手册指定的函数内追加代码（语言切换消息广播、iframe 脚本注入） |  禁止修改原有路由、菜单渲染、语言切换核心逻辑   |
| 工作 / 导航栏 /navbar-config.js |       导航与翻译核心配置，定义模块、菜单、多语言文本        |        仅可按本手册规则追加翻译文本、模块 / 菜单配置         | 禁止修改 / 删除原有配置项、禁止修改配置对象结构 |
|      工作 / 导航栏 /pages/      |                      业务页面存放目录                       |           仅可按规范创建模块文件夹、新增 HTML 页面           | 禁止修改 / 删除 / 移动原有模块文件夹和页面文件  |

### 1.2 命名规范强制约束（AI 必须 100% 遵守）

1. 文件夹 / 文件名：必须使用**kebab-case**（全小写，单词间用连字符分隔），禁止使用大写字母、空格、下划线、特殊字符；
2. 菜单标识符：必须与 HTML 文件名（不含.html 后缀）**完全一致**，禁止出现拼写偏差；
3. 模块 ID：必须与 pages 下的模块文件夹名**完全一致**；
4. 禁止使用中文、拼音命名，必须使用英文语义化命名（如`energy-prediction.html`，禁止`nenghao-yuce.html`）。

### 1.3 页面开发硬约束

1. 所有新增页面必须使用本手册提供的**强制模板**开发，禁止自定义页面骨架；
2. 页面 body 背景必须设置为`background: transparent !important;`，禁止设置不透明背景色；
3. 页面禁止自行实现顶部栏、侧边栏、语言切换按钮，框架已统一提供；
4. 页面必须兼容父框架的多语言切换机制，禁止硬编码文本；
5. 页面样式必须使用框架统一定义的 CSS 变量，禁止自定义主题色变量。

------

## 二、开发任务前置校验与拆解（AI 接到需求后第一步必须执行）

AI 在开始写代码前，必须先完成需求拆解与前置校验，输出《开发任务拆解清单》，确认所有信息无缺失后再开始开发。

### 2.1 需求核心信息拆解

AI 必须从需求中提取以下必填信息，无信息时必须向用户确认，禁止自行假设：

|        必填项        |                         说明                         |              示例              |
| :------------------: | :--------------------------------------------------: | :----------------------------: |
|       开发类型       | 「已有模块新增子页面」/「新增全新顶级模块 + 子页面」 |       已有模块新增子页面       |
|     归属模块 ID      |          新增子页面需确认归属的顶级模块 ID           |     datacenter（数据中心）     |
|      页面文件名      |           不含.html 后缀的 kebab-case 命名           |       energy-prediction        |
|     页面中文名称     |                  菜单显示的中文名称                  |            能耗预测            |
|     页面英文名称     |                  菜单显示的英文名称                  |       Energy Prediction        |
|     页面核心功能     |         页面的业务用途，用于生成页面基础内容         | 展示能耗预测趋势、预测模型配置 |
| 是否需要页面内多语言 |            页面内是否有需要切换语言的文本            |               是               |

### 2.2 前置环境校验

AI 必须先确认以下环境信息，避免开发错误：

1. 确认归属模块是否已存在于`navbar-config.js`的`navItems`数组中；
2. 确认 pages 目录下是否存在对应模块的文件夹；
3. 确认现有页面的 CSS 变量、字体、图标库引用规范，确保新增页面与现有规范一致。

------

## 三、标准化开发执行流程

AI 必须严格按照对应场景的步骤执行开发，禁止跳步、禁止遗漏步骤。

### 场景一：已有模块下新增子页面（最常用场景）

#### 步骤 1：按规范创建页面 HTML 文件

1. 进入`pages/[归属模块文件夹]/`目录；
2. 创建`[页面文件名].html`文件；
3. 必须使用本手册「第四章 强制开发模板」编写页面完整代码，禁止自定义骨架；
4. 页面内的功能代码必须写在模板指定的区域内，禁止修改模板的强制配置项。

#### 步骤 2：修改 navbar-config.js（核心步骤，必须 3 处配置无遗漏）

AI 必须在`NAVBAR_CONFIG`对象中，按以下顺序追加 3 处配置，**禁止修改原有配置**：

##### 2.1 追加英文翻译

找到`translations.en.subMenus.[归属模块ID]`对象，追加键值对：

```
// 键必须与页面文件名完全一致，值为页面英文名称
'energy-prediction': 'Energy Prediction'
```

##### 2.2 追加中文翻译

找到`translations.zh.subMenus.[归属模块ID]`对象，追加键值对：

```
// 键必须与页面文件名完全一致，值为页面中文名称
'energy-prediction': '能耗预测'
```

##### 2.3 追加菜单渲染配置

找到`navItems`数组中对应归属模块的配置项，在其`subMenus`数组的末尾，追加页面文件名（不含.html）：

```
{ 
    id: 'datacenter', 
    titleKey: 'modules.datacenter',
    icon: 'database', 
    url: './pages/datacenter/comparative-analysis.html', 
    // 必须与文件名完全一致，顺序决定菜单显示顺序
    subMenus: ['comparative-analysis', 'smart-report', 'statistics-query', 'energy-prediction']
}
```

#### 步骤 3：校验并补充 app.js 的语言切换广播机制

AI 必须检查`app.js`中的`toggleLanguage`函数，确认末尾是否已添加 iframe 语言变更消息广播代码，如无则必须追加：

```
function toggleLanguage() {
    currentLang = currentLang === 'en' ? 'zh' : 'en';
    
    // 原有框架核心代码，禁止修改
    renderSidebar();
    updateTopBar();
    
    // 必须追加的代码：向子页面iframe广播语言变更事件
    const iframe = document.getElementById('contentFrame');
    if (iframe && iframe.contentWindow) {
        iframe.contentWindow.postMessage({
            type: 'LANGUAGE_CHANGED',
            lang: currentLang
        }, '*');
    }
}
```

#### 步骤 4：执行「第六章 全量校验清单」，逐项确认通过

------

### 场景二：新增全新顶级模块 + 子页面

#### 步骤 1：创建模块文件夹与页面文件

1. 在`pages/`目录下，创建与模块 ID 同名的文件夹（kebab-case）；
2. 在新模块文件夹中，创建至少 1 个默认页面 HTML 文件，使用「第四章 强制开发模板」开发；
3. 模块默认页面的文件名，必须与`navItems`中该模块的`url`配置路径完全一致。

#### 步骤 2：修改 navbar-config.js（4 处配置无遗漏）

AI 必须在`NAVBAR_CONFIG`对象中，按以下顺序追加配置，**禁止修改原有配置**：

##### 2.1 追加模块英文名称

找到`translations.en.modules`对象，追加模块 ID 与英文名称：

```
'reporting': 'Reporting Center'
```

##### 2.2 追加模块中文名称

找到`translations.zh.modules`对象，追加模块 ID 与中文名称：

```
'reporting': '报表中心'
```

##### 2.3 追加子页面的中英文翻译

分别在`translations.en.subMenus`和`translations.zh.subMenus`中，追加以模块 ID 为键的对象，配置所有子页面的翻译：

```
// 英文翻译
subMenus: {
    // 原有其他模块配置，禁止修改
    reporting: {
        'daily-report': 'Daily Report',
        'monthly-summary': 'Monthly Summary'
    }
}

// 中文翻译
subMenus: {
    // 原有其他模块配置，禁止修改
    reporting: {
        'daily-report': '日报表',
        'monthly-summary': '月汇总'
    }
}
```

##### 2.4 追加顶级模块菜单配置

在`navItems`数组中，追加完整的模块配置对象，**配置项必须完整无缺**：

```
{ 
    // 模块ID，必须与pages下的文件夹名完全一致
    id: 'reporting',
    // 必须与translations中的modules键名完全匹配
    titleKey: 'modules.reporting',
    // Lucide图标名，必须从https://lucide.dev/icons/中选择有效名称
    icon: 'file-text',
    // 模块默认页面路径，必须是有效存在的文件路径
    url: './pages/reporting/daily-report.html',
    // 子菜单数组，必须与子页面文件名完全一致
    subMenus: ['daily-report', 'monthly-summary']
}
```

#### 步骤 3：同场景一步骤 3，校验并补充 app.js 的语言切换广播机制

#### 步骤 4：执行「第六章 全量校验清单」，逐项确认通过

------

## 四、页面开发强制模板（AI 必须 100% 使用，禁止修改核心配置）

AI 必须使用以下模板开发页面，仅可在标注「自定义区域」的位置编写业务代码，禁止修改模板中的强制配置项。

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 页面标题必须与英文菜单名一致 -->
    <title>Energy Prediction</title>
    <!-- 强制字体引入，禁止修改 -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Fira+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- 强制图标库引入，禁止修改版本 -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        /* 强制主题变量，必须与框架保持一致，禁止自定义主题色 */
        :root {
            --bg-base: #0b1220;
            --bg-surface: #172131;
            --bg-card: #1e293b;
            --text-primary: #F8FAFC;
            --text-secondary: #94A3B8;
            --text-disabled: #64748B;
            --accent-green: #22C55E;
            --accent-blue: #3B82F6;
            --accent-orange: #F59E0B;
            --accent-red: #EF4444;
            --border-color: rgba(71, 85, 105, 0.5);
            --border-radius-sm: 6px;
            --border-radius-md: 8px;
            --border-radius-lg: 12px;
        }

        /* 全局样式重置，禁止修改 */
        * { margin: 0; padding: 0; box-sizing: border-box; }

        /* body强制样式，禁止修改background属性 */
        body {
            font-family: 'Fira Sans', sans-serif;
            background: transparent !important;
            color: var(--text-primary);
            padding: 24px;
            line-height: 1.5;
        }

        /* ==================== 自定义页面样式区域 开始 ==================== */
        /* 仅可在此处编写页面自定义样式，禁止修改上方样式 */
        .page-container {
            max-width: 1400px;
            margin: 0 auto;
            width: 100%;
        }

        .page-title {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 24px;
            color: var(--accent-green);
        }

        .card {
            background: var(--bg-surface);
            border-radius: var(--border-radius-lg);
            padding: 20px;
            margin-bottom: 16px;
            border: 1px solid var(--border-color);
            transition: border-color 0.2s;
        }

        .card:hover {
            border-color: var(--accent-blue);
        }
        /* ==================== 自定义页面样式区域 结束 ==================== */
    </style>
</head>
<body>
    <!-- ==================== 自定义页面内容区域 开始 ==================== -->
    <!-- 仅可在此处编写页面HTML内容，必须使用data-i18n标记多语言文本 -->
    <div class="page-container">
        <h1 class="page-title" data-i18n="pageTitle">Energy Consumption Prediction</h1>
        
        <div class="card">
            <p data-i18n="description">This page shows predicted energy consumption trends and model configuration.</p>
        </div>
    </div>
    <!-- ==================== 自定义页面内容区域 结束 ==================== -->

    <!-- 强制脚本区域，禁止修改、删除核心逻辑，仅可追加自定义业务脚本 -->
    <script>
        // ==================== 强制多语言配置区域 开始 ====================
        // 页面内所有文本必须在此处配置中英文翻译，禁止硬编码文本
        const PAGE_TRANSLATIONS = {
            en: {
                pageTitle: 'Energy Consumption Prediction',
                description: 'This page shows predicted energy consumption trends and model configuration.'
                // 在此处追加更多翻译键值对
            },
            zh: {
                pageTitle: '能耗预测',
                description: '此页面展示预测的能耗趋势与模型配置。'
                // 在此处追加更多翻译键值对，必须与英文键名完全一致
            }
        };

        // 强制语言更新函数，禁止修改核心逻辑
        function updatePageLanguage(targetLang) {
            // 优先使用传入的语言，其次读取父框架语言，兜底为英文
            const lang = targetLang || (() => {
                try {
                    return window.parent.currentLang || 'en';
                } catch(e) {
                    return 'en';
                }
            })();
            const texts = PAGE_TRANSLATIONS[lang] || PAGE_TRANSLATIONS.en;
            
            // 批量更新所有带data-i18n属性的元素
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (texts[key]) {
                    el.textContent = texts[key];
                }
            });

            // 在此处追加自定义语言更新逻辑（如图表标题、动态内容）
        }

        // 页面初始加载执行语言渲染
        (() => {
            try {
                const initLang = window.parent.currentLang || 'en';
                updatePageLanguage(initLang);
            } catch(e) {
                updatePageLanguage('en');
            }
        })();

        // 强制监听父框架语言切换事件，禁止删除
        window.addEventListener('message', (event) => {
            if (event.data && event.data.type === 'LANGUAGE_CHANGED') {
                updatePageLanguage(event.data.lang);
            }
        });
        // ==================== 强制多语言配置区域 结束 ====================

        // 强制Lucide图标初始化，禁止删除
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }

        // ==================== 自定义业务脚本区域 开始 ====================
        // 仅可在此处编写页面的业务逻辑、图表渲染、接口请求等代码
        console.log('Page loaded successfully');
        // ==================== 自定义业务脚本区域 结束 ====================
    </script>
</body>
</html>
```

------

## 五、Lucide 图标使用规范

AI 在配置模块图标时，必须使用 Lucide 官方提供的有效图标名称，禁止使用自定义图标、无效图标名。

1. 图标查询地址：https://lucide.dev/icons/

2. 常用图标映射（AI 优先使用）：

   |     业务场景      | 推荐图标名  |
   | :---------------: | :---------: |
   |    监控 / 概览    |  activity   |
   | 数据中心 / 数据库 |  database   |
   |    运维 / 工具    |   wrench    |
   |     资产管理      |     box     |
   |     系统管理      |  settings   |
   |    报表 / 文件    |  file-text  |
   |     告警中心      |    bell     |
   |    用户 / 组织    |    users    |
   |    能源 / 电力    |     zap     |
   |    图表 / 统计    | bar-chart-3 |

   

------

## 六、开发完成后 AI 必须执行的全量校验清单

AI 完成开发后，必须逐项校验以下内容，**所有项必须校验通过**，方可交付开发结果，禁止遗漏：

### 6.1 文件与路径校验

-  页面 HTML 文件已放置在正确的模块文件夹中，路径与配置完全一致
-  文件名严格遵循 kebab-case 规范，无大写、空格、特殊字符
-  文件名与 navbar-config.js 中的菜单标识符完全一致
-  模块文件夹名与 navItems 中的模块 ID 完全一致

### 6.2 配置文件校验

-  navbar-config.js 中已追加页面 / 模块的英文翻译，键名无错误
-  navbar-config.js 中已追加页面 / 模块的中文翻译，键名无错误
-  navItems 数组中已追加正确的菜单标识符，顺序符合需求
-  新增模块的 navItems 配置项完整，id、titleKey、icon、url、subMenus 无缺失
-  app.js 中已添加语言切换的 postMessage 广播代码，无语法错误

### 6.3 页面规范校验

-  页面使用了本手册提供的强制模板，核心配置未修改
-  页面 body 背景设置为`background: transparent !important;`
-  页面所有文本均已配置多语言翻译，无硬编码中文 / 英文
-  页面已实现 updatePageLanguage 函数，并正确监听 message 事件
-  页面已正确引入 lucide 图标库，并执行了 createIcons 初始化
-  页面 CSS 使用了框架统一的 CSS 变量，未自定义主题色
-  HTML 语法完整，无标签未闭合、语法错误

### 6.4 功能校验

-  左侧导航栏可正常显示新增的模块 / 子菜单
-  点击菜单后，iframe 可正常加载页面，无 404 错误、无空白页面
-  页面加载后，浏览器控制台无 JavaScript 报错
-  点击右上角语言切换按钮，导航栏、页面内文本可正常切换中英文
-  页面样式与框架整体主题一致，无样式冲突、溢出问题

------

## 八、AI 交付输出规范

AI 完成开发并通过全量校验后，必须按以下规范输出结果，禁止只输出代码片段、不标注修改位置：

### 8.1 输出结构

1. **开发结果说明**：简要说明完成的开发内容（如：已完成数据中心模块下「能耗预测」页面的新增开发，包含页面开发、配置修改、多语言适配）；
2. **新增文件完整代码**：分文件输出所有新增的 HTML 文件，标注文件完整路径；
3. **修改文件变更内容**：对修改的 navbar-config.js、app.js，必须标注「修改位置」+「完整的修改后代码块」，禁止只输出新增的单行代码；
4. **校验结果说明**：明确说明已通过第六章的全量校验清单，无异常。

### 8.2 输出示例

```
## 开发结果说明
已完成「数据中心」模块下新增「能耗预测」子页面的全流程开发，包含：
1.  创建pages/datacenter/energy-prediction.html页面，实现基础功能与多语言适配
2.  完成navbar-config.js的翻译与菜单配置追加
3.  补充app.js的语言切换广播机制
4.  已通过全量校验清单，所有功能正常
## 一、新增文件完整代码
### 文件路径：工作/导航栏/pages/datacenter/energy-prediction.html
[此处粘贴完整的HTML代码]
## 二、修改文件变更内容
### 1. 修改文件：工作/导航栏/navbar-config.js
#### 变更位置1：translations.en.subMenus.datacenter 追加翻译
修改后完整代码块：
```javascript
subMenus: {
    datacenter: {
        'comparative-analysis': 'Comparative Analysis',
        'smart-report': 'Smart Report',
        'statistics-query': 'Statistics Query',
        'energy-prediction': 'Energy Prediction'
    },
    // 其他原有模块配置保持不变
}
```

