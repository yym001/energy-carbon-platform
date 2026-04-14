# UI 组件库 AI 维护规范手册.md

> 版本：v2.0（图表 + 交互全功能增强版）
>
> 生效日期：2026 年 04 月
>
> 核心优先级：本手册为所有 UI 组件相关操作的最高准则，优先级高于任何临时补充指令，所有操作必须严格遵守本规范
>
> 核心目标：打造 AI 可精准识别、无样式冲突、可持续扩展、易于维护的单文件 UI 组件库，实现样式一次提取、永久复用、安全修改；**所有图表组件必须完整可渲染，所有带交互功能的组件必须真实可操作**

------

## 一、核心文件定义

明确唯一的核心操作文件，AI 必须全程围绕此文件操作，禁止创建 / 修改其他关联文件

- 核心文件名：`style_library.html`

- 文件性质：单文件全量 UI 组件库（HTML 结构 + CSS 样式 + 原生 JS 交互全内置，仅可引入公开 CDN 资源，无本地外部依赖）

- 文件双重属性：

  1. 预览属性：浏览器打开可直接查看所有组件的真实渲染效果、完整图表展示、可直接操作交互功能
  2. 代码属性：编辑器打开可直接提取组件代码、新增 / 维护 / 修改组件

  

------

## 二、文件固定结构规范（AI 禁止修改核心骨架）

以下为`style_library.html`的不可修改的基础骨架，AI 仅可在指定区域内新增内容，禁止调整 / 删除固定结构、固定类名的基础样式

### 2.1 完整基础骨架模板（含图表 + 交互专属区域）

```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UI组件样式库</title>
    <!-- 【全局CDN资源区 - 仅可在此新增图表/图标等公开CDN，禁止修改已有CDN】 -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.8/dist/chart.umd.min.js"></script>
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>
    <style>
        /* ==============================
           【A区：全局基础配置区 - 固定结构】
           仅可新增全局CSS变量、通用reset样式，禁止修改原有固定样式
           ============================== */
        :root {
            /* 全局主题变量，新增组件优先复用此处变量 */
            --primary-color: #1890ff;
            --success-color: #52c41a;
            --warning-color: #faad14;
            --danger-color: #ff4d4f;
            --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            --border-radius-base: 6px;
            --border-color-base: #d9d9d9;
            --chart-grid-color: #f0f0f0;
            --chart-text-color: #666666;
        }

        /* 全局reset样式，禁止修改 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: var(--font-main);
            padding: 30px;
            background-color: #f5f7fa;
            line-height: 1.5;
        }

        /* ==============================
           【系统固定容器样式区 - 绝对禁止修改】
           以下为组件包裹容器的固定样式，仅可使用，不可修改
           ============================== */
        .section-card {
            background: #ffffff;
            padding: 24px;
            border-radius: 8px;
            margin-bottom: 40px;
            border-left: 4px solid var(--primary-color);
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }
        .component-title {
            font-size: 18px;
            font-weight: 600;
            color: #262626;
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 1px solid #f0f0f0;
        }
        .demo-area {
            border: 1px dashed #d9d9d9;
            padding: 24px;
            border-radius: 4px;
            background-color: #fafafa;
            min-height: 60px;
            display: flex;
            align-items: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        /* ==============================
           【B区：组件样式专属区 - 仅可在此新增/修改样式】
           所有组件的CSS样式必须写在此区域，按组件序号顺序排列
           格式要求：每个组件样式上方必须加「/* --- X. 组件全称 样式 --- */」的注释
           ============================== */
        
        /* --- 1. 主按钮 Primary Button 样式 --- */
        .btn-primary {
            background-color: var(--primary-color);
            color: #ffffff;
            border: none;
            padding: 10px 20px;
            border-radius: var(--border-radius-base);
            cursor: pointer;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.2s;
        }
        .btn-primary:hover {
            background-color: #40a9ff;
        }

    </style>
</head>
<body>
    <!-- ==========================================
         【C区：组件列表展示区 - 仅可在此按顺序新增组件，仅可修改指定组件的HTML结构】
         所有组件必须按序号顺序，从文件末尾依次追加，禁止调整原有组件顺序/序号
         ========================================== -->

    <!-- ========================================== -->
    <!-- 组件开始：1. 主按钮 Primary Button -->
    <!-- ========================================== -->
    <div class="section-card">
        <div class="component-title">1. 主按钮 Primary Button</div>
        <div class="demo-area">
            <!-- 组件HTML结构 仅可在此区域内写组件代码 -->
            <button class="btn-primary">确认提交</button>
        </div>
    </div>

    <!-- 【新增组件必须在此处、文件最末尾追加，禁止插入到已有组件中间】 -->

    <!-- ==========================================
         【D区：全局脚本专属区 - 固定结构】
         【系统固定脚本区 - 绝对禁止修改】
         【组件专属脚本区 - 仅可在此新增组件交互/图表渲染JS代码，按组件序号顺序排列】
         ========================================== -->
    <script>
        // ==============================
        // 【系统固定脚本区 - 绝对禁止修改】
        // ==============================
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
            console.log('UI组件库初始化成功');
        });

        // ==============================
        // 【组件专属脚本区 - 仅可在此新增代码，按组件序号顺序排列】
        // 格式要求：每个组件脚本上方必须加「/* --- X. 组件全称 脚本 --- */」的注释
        // ==============================
    </script>
</body>
</html>
```

### 2.2 固定区域功能说明

|      区域标识      |     区域名称     |                           操作权限                           |                           核心规则                           |
| :----------------: | :--------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  全局 CDN 资源区   | 第三方资源引入区 | 仅可新增公开稳定的 CDN 资源（如 Chart.js、ECharts、图标库），禁止修改 / 删除已有 CDN | 仅可引入前端通用开源库的官方 CDN，禁止引入本地私有文件、不可访问的外部资源 |
|        A 区        |  全局基础配置区  |     仅可新增变量、指定变量修改，禁止修改原有 reset 样式      | 仅存放全局 CSS 变量、通用 reset 样式，所有组件优先复用全局变量，图表 / 交互通用变量必须在此定义 |
| 系统固定容器样式区 | 组件包裹容器样式 |                    绝对禁止修改、禁止重写                    | 仅可使用`.section-card`/`.component-title`/`.demo-area`三个固定类名包裹组件，不可修改其基础样式 |
|        B 区        |  组件样式专属区  | 新增组件仅可在末尾追加样式；修改仅可操作指定组件的样式，禁止修改 / 删除其他原有样式 | 每个组件的样式必须对应 HTML 组件的序号，上方必须加明确的注释标题，禁止样式乱序 |
|        C 区        |  组件列表展示区  | 新增仅可在文件最末尾按序号追加；修改仅可调整指定组件 demo-area 内的 HTML 结构，禁止修改 / 删除 / 重排序原有组件 | 每个组件必须用固定容器包裹，带明确的起止注释，序号必须连续递增，图表 / 交互组件必须完整写在此区域 |
|        D 区        |  全局脚本专属区  | 系统固定脚本区禁止修改；组件专属脚本区仅可在末尾追加对应组件的 JS 代码 | 所有组件的交互逻辑、图表渲染代码必须写在此区域，与组件序号一一对应，禁止在 HTML 内写行内脚本（事件绑定除外） |

------

## 三、CSS 样式强制规范（AI 必须严格遵守，避免样式冲突）

### 3.1 强制命名空间规则

所有组件的样式类名必须添加专属前缀，禁止使用无意义、通用类名，防止样式污染

|      组件类型      |  强制前缀   |                           正确示例                           |
| :----------------: | :---------: | :----------------------------------------------------------: |
|       按钮类       |   `btn-`    |         `.btn-primary`/`.btn-secondary`/`.btn-large`         |
|      输入框类      |  `input-`   |         `.input-base`/`.input-search`/`.input-error`         |
|     标题文本类     |  `title-`   |           `.title-h1`/`.title-card`/`.title-desc`            |
|     卡片容器类     |   `card-`   |           `.card-base`/`.card-data`/`.card-shadow`           |
|    日期选择器类    |   `date-`   |         `.date-picker`/`.date-range`/`.date-header`          |
|     图表容器类     |  `chart-`   | `.chart-container`/`.chart-line`/`.chart-bar`/`.chart-title` |
|     下拉菜单类     | `dropdown-` |    `.dropdown-container`/`.dropdown-btn`/`.dropdown-menu`    |
|    标签页切换类    |   `tab-`    |            `.tab-nav`/`.tab-item`/`.tab-content`             |
|    弹窗模态框类    |  `modal-`   |       `.modal-mask`/`.modal-container`/`.modal-header`       |
|     开关切换类     |  `switch-`  |   `.switch-container`/`.switch-checkbox`/`.switch-slider`    |
|     折叠面板类     | `collapse-` |   `.collapse-header`/`.collapse-content`/`.collapse-item`    |
|       表格类       |  `table-`   |          `.table-base`/`.table-header`/`.table-row`          |
| 后续新增实验性样式 | `v2-`/`v3-` |            `.v2-card-special`/`.v2-btn-gradient`             |

### 3.2 样式书写强制规则

1. 禁止在 HTML 标签内使用`style=""`行内样式，所有样式必须写在`<style>`标签的 B 区，通过类名控制
2. 组件样式必须按「组件序号」顺序排列，与 C 区的 HTML 组件顺序一一对应
3. 每个组件的样式上方必须添加明确的注释标题，格式为：`/* --- X. 组件全称 样式 --- */`
4. 优先复用 A 区定义的全局 CSS 变量，禁止重复定义相同属性的固定值
5. 禁止使用 ID 选择器写样式，所有样式必须使用类名选择器
6. 禁止使用！important 强制覆盖样式，除非特殊场景并添加明确注释说明
7. 图表、交互组件的样式必须适配响应式，禁止在`.demo-area`内出现溢出、截断、压扁问题

------

## 四、组件样式修改专属强制规范

本章节为所有组件样式修改操作的唯一执行准则，优先级高于其他通用规则，任何样式修改操作必须严格遵守以下所有要求。

### 4.1 样式修改的分级定义

根据修改范围、影响程度，将样式修改分为 4 个明确等级，AI 必须先识别用户需求对应的修改等级，再执行对应操作，禁止跨等级操作。

|      修改等级      |                           等级定义                           |                         典型场景示例                         |                           影响范围                           |
| :----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|  1 级：微调整修改  | 仅修改组件单个 / 少数 CSS 属性，不改变组件核心结构、类名、基础视觉逻辑、交互功能、图表渲染逻辑 | 1. 修改按钮的圆角数值2. 调整标题的字体大小3. 更换输入框的边框色值4. 微调组件的内边距数值5. 修改图表的配色色值 | 仅影响当前修改的指定组件，不影响其他组件，不破坏原有交互 / 图表渲染功能 |
| 2 级：属性增删修改 | 在不改变原有组件类名、核心渲染效果、基础交互功能的前提下，新增 / 删除 CSS 属性，补充组件状态、交互效果、图表配置，不重构核心样式 | 1. 给主按钮新增 hover 过渡动画2. 给输入框新增禁用状态样式3. 给卡片新增阴影效果4. 给图表新增 tooltip 样式5. 给下拉菜单新增展开动画 | 仅影响当前修改的指定组件，不改变组件原有基础用法、核心交互、图表渲染能力 |
| 3 级：全量样式重构 | 对组件的核心样式进行完整重写，改变组件的视觉风格、核心属性，保留原有组件类名、HTML 结构、核心交互 / 图表渲染入口 | 1. 将直角按钮重构为渐变圆角按钮2. 将普通卡片重构为玻璃拟态风格卡片3. 完整重写日期选择器的视觉样式4. 重构图表的整体视觉风格，保留渲染逻辑 | 影响当前组件，以及所有复用该组件类名的页面，原有 HTML 结构无需修改，原有交互 / 图表功能可正常使用 |
| 4 级：全局主题修改 | 修改 A 区【全局基础配置区】的:root 全局 CSS 变量，不修改单个组件的独立样式、交互逻辑、图表代码 | 1. 更换全局主题主色值2. 调整全局默认圆角数值3. 更换全局默认字体4. 新增全局通用 CSS 变量5. 修改图表全局通用配色变量 |        影响所有复用该全局变量的组件，范围覆盖全组件库        |

### 4.2 全等级通用强制修改规则

无论任何等级的样式修改，必须严格遵守以下通用规则：

1. **精准定位原则**：仅可修改用户明确指定的「组件序号 + 组件名称」对应的样式、脚本，禁止修改其他任何未指定的组件代码、样式、结构、序号、顺序
2. **最小改动原则**：仅可修改用户明确指定的 CSS 属性、JS 配置，禁止修改、删除、调整该组件下其他未指定的 CSS 属性、JS 逻辑
3. **类名不变原则**：修改过程中必须保留组件原有类名，禁止修改、删除原有类名，保证修改后原有复用该类名的页面无需调整 HTML 结构
4. **无冲突原则**：修改后的样式、脚本必须与组件库内其他组件样式、脚本无冲突、无覆盖，不影响其他组件的正常渲染、交互、图表展示
5. **效果可复现原则**：修改后的组件，在浏览器中打开必须正常渲染，视觉效果、交互功能、图表展示完全符合用户的修改需求
6. **变量优先原则**：修改颜色、圆角、字体等通用属性时，优先复用 A 区已定义的全局 CSS 变量，禁止重复定义固定值，确需自定义的可新增全局变量
7. **功能不破坏原则**：修改图表组件样式时，禁止破坏图表的完整渲染能力；修改交互组件样式时，禁止破坏原有交互功能的正常使用

### 4.3 分等级专属修改规则

#### 4.3.1 1 级 / 2 级修改（微调整 / 属性增删）专属规则

1. 必须在修改的 CSS 属性行后，添加单行修改注释，格式为：`/* 修改记录：[修改内容] | [修改日期] | 原属性值：[原数值] */`

2. 禁止修改组件的 HTML 核心结构、JS 核心逻辑，仅可修改对应 CSS 样式、非核心 JS 配置（如图表配色、动画时长）

3. 禁止新增新的 CSS 类名，仅可在原有类名下修改 / 新增属性

4. 合规示例：

   css

   ```
   /* --- 1. 主按钮 Primary Button 样式 --- */
   .btn-primary {
       background-color: var(--primary-color);
       color: #ffffff;
       border: none;
       padding: 10px 20px;
       border-radius: 8px; /* 修改记录：圆角从4px调整为8px | 2026-04-10 | 原属性值：4px */
       cursor: pointer;
       font-size: 14px;
       font-weight: 500;
       transition: all 0.3s; /* 新增记录：添加hover过渡动画 | 2026-04-10 */
   }
   ```

   

#### 4.3.2 3 级修改（全量样式重构）专属规则

1. 必须先将组件原有完整样式、完整脚本，以注释的形式完整保留在该组件对应区域的最上方，标注「历史版本备份」，方便后续回滚

2. 重构后的样式，必须保留原有组件的核心类名、核心 JS 入口，保证 HTML 结构无需修改即可正常使用，原有交互 / 图表功能可正常运行

3. 必须在样式区域、脚本区域的注释标题处，标注重构版本号与日期，格式为：`/* --- X. 组件全称 样式 | v2.0 重构 | 2026-04-10 --- */`

4. 重构后的样式必须遵守本手册的 CSS 命名规范，禁止使用行内样式、ID 选择器；重构后的脚本必须写在 D 区对应位置，禁止写行内脚本

5. 合规示例：

   css

   ```
   /* --- 1. 主按钮 Primary Button 样式 | v2.0 重构 | 2026-04-10 --- */
   /* 【历史版本备份 开始】
   .btn-primary {
       background-color: var(--primary-color);
       color: #ffffff;
       border: none;
       padding: 10px 20px;
       border-radius: 4px;
       cursor: pointer;
       font-size: 14px;
       font-weight: 500;
       transition: all 0.2s;
   }
   .btn-primary:hover {
       background-color: #40a9ff;
   }
   【历史版本备份 结束】 */
   .btn-primary {
       background: linear-gradient(90deg, #1890ff, #40a9ff);
       color: #ffffff;
       border: none;
       padding: 12px 24px;
       border-radius: 50px;
       cursor: pointer;
       font-size: 14px;
       font-weight: 600;
       box-shadow: 0 4px 12px rgba(24, 144, 255, 0.3);
       transition: all 0.3s ease;
   }
   .btn-primary:hover {
       transform: translateY(-2px);
       box-shadow: 0 6px 16px rgba(24, 144, 255, 0.4);
   }
   ```

   

#### 4.3.3 4 级修改（全局主题修改）专属规则

1. 仅可修改 A 区【全局基础配置区】:root 选择器内的指定变量，禁止修改:root 外的其他样式、脚本，禁止修改 reset 基础样式

2. 必须在修改的变量行后，添加单行修改注释，格式为：`/* 修改记录：[修改内容] | [修改日期] | 原属性值：[原数值] */`

3. 必须完整校验修改后，所有复用该变量的组件，渲染效果、交互功能、图表展示正常，无样式错乱、功能失效

4. 新增全局变量时，必须添加明确的注释，说明变量用途与使用场景

5. 合规示例：

   css

   ```
   :root {
       --primary-color: #1677ff; /* 修改记录：主色从#1890ff调整为#1677ff | 2026-04-10 | 原属性值：#1890ff */
       --success-color: #52c41a;
       --warning-color: #faad14;
       --danger-color: #ff4d4f;
       --font-main: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
       --border-radius-base: 8px; /* 修改记录：全局圆角从6px调整为8px | 2026-04-10 | 原属性值：6px */
       --border-color-base: #d9d9d9;
       --chart-grid-color: #f0f0f0;
       --chart-text-color: #666666;
   }
   ```

   

### 4.4 样式修改后的强制自检流程

AI 完成任何等级的样式修改后，必须完成以下自检步骤，全部通过后方可输出代码：

1. ✅ 自检 1：仅修改了用户指定的组件 / 变量 / 脚本，未修改任何其他未指定的内容
2. ✅ 自检 2：修改后的样式无语法错误，类名与 HTML 结构中的类名完全一致
3. ✅ 自检 3：修改后的组件在浏览器中可正常渲染，视觉效果符合需求
4. ✅ 自检 4：修改后的样式与其他组件无冲突、无覆盖，不影响其他组件的渲染
5. ✅ 自检 5：已按规范添加完整的修改记录 / 历史备份注释，无遗漏
6. ✅ 自检 6：组件原有 HTML 结构无需修改，即可正常使用修改后的样式
7. ✅ 自检 7：图表组件修改后，可完整渲染，无数据丢失、坐标轴错乱、tooltip 失效
8. ✅ 自检 8：交互组件修改后，可正常操作，无点击无响应、展开无法关闭、切换失效等问题

------

## 五、图表组件专属强制规范

本章节为所有图表类组件的唯一执行准则，任何图表组件的新增 / 修改，必须严格遵守以下所有要求，**禁止输出只有外观无渲染能力的假图表**。

### 5.1 图表组件必须包含的完整内容

所有新增的图表组件，必须完整包含以下元素，缺一不可：

1. 完整的坐标轴（X 轴 + Y 轴，含刻度、标签、单位）
2. 图例（legend），可正常识别系列名称
3. 真实模拟数据（不少于 3 组数据，禁止空数据、单条无效数据）
4. 鼠标悬浮 tooltip（可正常显示对应数据数值、系列名称）
5. 网格线（适配主题色，不突兀）
6. 图表标题 / 副标题（明确图表用途）
7. 正常配色、合理宽高比例，不压扁、不截断、不溢出`.demo-area`容器

### 5.2 支持的图表类型（必须完整渲染）

- 折线图 Line Chart
- 柱状图 Bar Chart（含横向柱状图、堆叠柱状图）
- 饼图 Pie Chart
- 环形图 Doughnut Chart
- 面积图 Area Chart
- 仪表盘 Gauge Chart
- 雷达图 Radar Chart
- 散点图 Scatter Chart
- 数据卡片 / 指标卡 Chart Card
- 复合图表（折线 + 柱状组合等）

### 5.3 图表渲染强制要求

1. **必须可直接运行**：浏览器打开`style_library.html`，图表即可自动完整渲染，无需额外操作、无控制台报错
2. **数据要求**：必须使用真实合理的模拟数据，数值范围统一，禁止出现负数、异常值、无意义数据
3. **主题适配**：必须优先复用 A 区定义的全局 CSS 变量，配色与组件库主题色保持一致，禁止使用冲突配色
4. **容器要求**：图表必须包裹在`.chart-container`类名的容器内，宽高设置合理，自适应`.demo-area`容器宽度，禁止溢出
5. **资源要求**：仅可使用已在头部引入的 Chart.js，或新增 ECharts 等官方稳定 CDN，禁止使用私有图表库、本地依赖文件
6. **脚本要求**：图表的渲染 JS 代码，必须写在 D 区【组件专属脚本区】，按组件序号顺序排列，上方必须加明确的注释标题，禁止在 HTML 内写大段脚本
7. **响应式要求**：图表必须支持窗口大小自适应，缩放窗口无错乱、无截断

### 5.4 图表组件标准结构模板（AI 必须严格按此格式编写）

#### HTML 结构（写在 C 区组件列表末尾）

```
<!-- ========================================== -->
<!-- 组件开始：2. 基础折线图 Basic Line Chart -->
<!-- ========================================== -->
<div class="section-card">
    <div class="component-title">2. 基础折线图 Basic Line Chart（完整可渲染）</div>
    <div class="demo-area">
        <div class="chart-container" style="width:100%;height:320px;">
            <canvas id="chart-line-basic"></canvas>
        </div>
    </div>
</div>
```

#### CSS 样式（写在 B 区样式末尾）

```
/* --- 2. 基础折线图 Basic Line Chart 样式 --- */
.chart-container {
    width: 100%;
    height: 320px;
    position: relative;
    background: #ffffff;
    border-radius: var(--border-radius-base);
    padding: 16px;
}
```

#### JS 脚本（写在 D 区组件专属脚本区末尾）

```
/* --- 2. 基础折线图 Basic Line Chart 脚本 --- */
document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('chart-line-basic');
    if (ctx) {
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['1月', '2月', '3月', '4月', '5月', '6月'],
                datasets: [
                    {
                        label: '用电量',
                        data: [120, 190, 160, 210, 180, 240],
                        borderColor: var(--primary-color),
                        backgroundColor: 'rgba(24, 144, 255, 0.1)',
                        tension: 0.3,
                        fill: true
                    },
                    {
                        label: '发电量',
                        data: [80, 150, 200, 180, 220, 260],
                        borderColor: var(--success-color),
                        backgroundColor: 'rgba(82, 196, 26, 0.1)',
                        tension: 0.3,
                        fill: true
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            color: var(--chart-text-color)
                        }
                    },
                    tooltip: {
                        mode: 'index',
                        intersect: false
                    }
                },
                scales: {
                    x: {
                        grid: {
                            color: var(--chart-grid-color)
                        },
                        ticks: {
                            color: var(--chart-text-color)
                        }
                    },
                    y: {
                        beginAtZero: true,
                        grid: {
                            color: var(--chart-grid-color)
                        },
                        ticks: {
                            color: var(--chart-text-color)
                        }
                    }
                }
            }
        });
    }
});
```

------

## 六、交互组件专属强制规范

本章节为所有带交互功能组件的唯一执行准则，任何交互组件的新增 / 修改，必须严格遵守以下所有要求，**禁止输出只有外观无操作能力的假交互**。

### 6.1 必须实现的真实交互效果

所有标注可交互的组件，必须实现对应的真实操作效果，包括但不限于：

- 按钮：hover/active/ 禁用状态切换、点击事件响应
- 下拉菜单：点击展开 / 收起、点击选项可选中、点击外部自动关闭
- 标签页：点击切换标签、对应内容区同步切换、选中状态高亮
- 折叠面板：点击展开 / 收起内容、动画过渡、状态切换
- 单选 / 复选框：点击勾选 / 取消勾选、选中状态高亮、禁用状态
- 输入框：聚焦 / 失焦状态、输入内容响应、清空功能、禁用状态
- 日期选择器：点击弹出面板、选择日期、日期回填、面板关闭
- 弹窗模态框：点击打开 / 关闭、点击蒙层关闭、关闭动画
- 开关切换：点击切换开 / 关状态、状态同步、动画过渡
- 表格：单选 / 多选、排序、hover 行高亮、分页切换
- 侧边导航：展开 / 收起、选中高亮、二级菜单展开 / 收起

### 6.2 交互实现强制规则

1. **必须真实可操作**：浏览器打开`style_library.html`，即可直接操作交互功能，无报错、无卡顿、无逻辑异常
2. **脚本规范**：交互逻辑必须使用原生 JS 实现，写在 D 区【组件专属脚本区】，按组件序号顺序排列，上方必须加明确的注释标题，禁止使用未引入的第三方框架
3. **命名规范**：交互组件的类名必须遵守 3.1 的强制命名空间规则，使用专属前缀，禁止使用通用类名造成样式污染
4. **无冲突原则**：交互逻辑必须独立，禁止影响其他组件的交互功能、图表渲染，禁止全局事件污染、禁止重复绑定事件
5. **状态闭环**：所有交互必须形成状态闭环，展开可关闭、打开可隐藏、选中可取消，禁止出现状态卡死、无法回退的问题
6. **无障碍适配**：基础交互必须支持键盘操作（如 Tab 聚焦、Enter 触发），hover / 选中状态有明确的视觉反馈
7. **动画过渡**：交互状态切换必须添加平滑的过渡动画，时长 0.2s-0.3s，适配全局主题风格

### 6.3 交互组件标准结构模板（AI 必须严格按此格式编写）

#### HTML 结构（写在 C 区组件列表末尾）

```
<!-- ========================================== -->
<!-- 组件开始：3. 下拉菜单 Dropdown Menu（完整可交互） -->
<!-- ========================================== -->
<div class="section-card">
    <div class="component-title">3. 下拉菜单 Dropdown Menu（完整可交互）</div>
    <div class="demo-area">
        <div class="dropdown-container">
            <button class="dropdown-btn">
                <span>选择选项</span>
                <i data-lucide="chevron-down" class="dropdown-icon"></i>
            </button>
            <div class="dropdown-menu">
                <div class="dropdown-item" data-value="1">选项1</div>
                <div class="dropdown-item" data-value="2">选项2</div>
                <div class="dropdown-item" data-value="3">选项3</div>
                <div class="dropdown-item" data-value="4" disabled>禁用选项</div>
            </div>
        </div>
    </div>
</div>
```

#### CSS 样式（写在 B 区样式末尾）

```
/* --- 3. 下拉菜单 Dropdown Menu 样式 --- */
.dropdown-container {
    position: relative;
    width: 200px;
}
.dropdown-btn {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px 16px;
    background-color: #ffffff;
    border: 1px solid var(--border-color-base);
    border-radius: var(--border-radius-base);
    cursor: pointer;
    font-size: 14px;
    color: #333333;
    transition: all 0.2s;
}
.dropdown-btn:hover {
    border-color: var(--primary-color);
}
.dropdown-btn:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 2px rgba(24, 144, 255, 0.2);
}
.dropdown-icon {
    width: 16px;
    height: 16px;
    transition: transform 0.2s;
}
.dropdown-container.open .dropdown-icon {
    transform: rotate(180deg);
}
.dropdown-menu {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    width: 100%;
    background-color: #ffffff;
    border: 1px solid var(--border-color-base);
    border-radius: var(--border-radius-base);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    padding: 4px 0;
    z-index: 999;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-4px);
    transition: all 0.2s;
}
.dropdown-container.open .dropdown-menu {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
}
.dropdown-item {
    padding: 8px 16px;
    font-size: 14px;
    color: #333333;
    cursor: pointer;
    transition: background-color 0.2s;
}
.dropdown-item:hover {
    background-color: rgba(24, 144, 255, 0.06);
}
.dropdown-item.disabled {
    color: #cccccc;
    cursor: not-allowed;
    background-color: transparent;
}
```

#### JS 脚本（写在 D 区组件专属脚本区末尾）

javascript

```
/* --- 3. 下拉菜单 Dropdown Menu 脚本 --- */
document.addEventListener('DOMContentLoaded', () => {
    // 初始化所有下拉菜单
    const dropdownContainers = document.querySelectorAll('.dropdown-container');
    
    dropdownContainers.forEach(container => {
        const btn = container.querySelector('.dropdown-btn');
        const menu = container.querySelector('.dropdown-menu');
        const items = container.querySelectorAll('.dropdown-item:not(.disabled)');
        
        // 点击按钮切换展开/收起
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            // 关闭其他下拉菜单
            document.querySelectorAll('.dropdown-container').forEach(other => {
                if (other !== container) other.classList.remove('open');
            });
            // 切换当前菜单
            container.classList.toggle('open');
        });
        
        // 点击选项
        items.forEach(item => {
            item.addEventListener('click', () => {
                const value = item.dataset.value;
                const label = item.textContent;
                // 回填按钮文本
                btn.querySelector('span').textContent = label;
                // 关闭菜单
                container.classList.remove('open');
                console.log('选中选项：', value, label);
            });
        });
    });
    
    // 点击外部关闭所有下拉菜单
    document.addEventListener('click', () => {
        document.querySelectorAll('.dropdown-container').forEach(container => {
            container.classList.remove('open');
        });
    });
});
```

------

## 七、AI 分场景操作标准 SOP（必须严格按步骤执行）

### 7.1 场景 1：从现有 HTML 页面提取样式，初始化组件库

**执行步骤：**

1. 先完整阅读本手册，确认所有规范
2. 分析用户提供的目标 HTML 页面，拆解出独立的 UI 组件（如标题、按钮、输入框、卡片、日期选择器、图表容器、表格等）
3. 按照本手册 2.1 的基础骨架，创建`style_library.html`文件
4. 为每个拆解后的组件分配连续递增的序号，编写明确的组件标题（中文名 + 英文名）
5. 将组件的 CSS 样式按序号顺序写入 B 区，遵守 3.1 的命名空间规则
6. 将组件的 HTML 结构按序号顺序写入 C 区，使用固定容器包裹，添加明确的起止注释
7. 将组件的交互 / 图表 JS 代码按序号顺序写入 D 区，添加明确的注释标题
8. 确保组件在浏览器中渲染效果与原页面完全一致，无样式丢失、无冲突，交互功能正常、图表完整渲染

### 7.2 场景 2：新增新的 UI 组件到现有组件库

**执行步骤：**

1. 先完整阅读本手册，确认所有规范，完整读取现有`style_library.html`文件
2. 确认现有组件的最大序号，新组件序号为「最大序号 + 1」，保证序号连续递增
3. 在`<style>`标签的 B 区**最末尾**，按规范添加新组件的 CSS 样式，带明确的注释标题，遵守命名空间规则
4. 在 HTML 文件的 C 区**最末尾**（所有已有组件的后面），按固定容器格式添加新组件的 HTML 结构，带明确的起止注释
5. 若为交互 / 图表组件，在 D 区**最末尾**添加对应的 JS 脚本，带明确的注释标题
6. 禁止修改、删除、调整现有任何组件的代码、顺序、序号、样式、脚本
7. 确保新增组件的样式与现有组件无冲突，可正常渲染、交互功能正常、图表完整渲染

### 7.3 场景 3：基于现有组件库，生成新的 HTML 页面

**执行步骤：**

1. 先完整阅读本手册，完整读取现有`style_library.html`文件的所有组件
2. 严格复用组件库中已定义的类名，禁止创建新的 CSS 类名、禁止新增 CSS 样式
3. 新页面仅可使用组件库中已有的组件 HTML 结构，可调整组件的排列布局，不可修改组件的核心样式、交互逻辑
4. 新页面必须完整引入组件库的全局样式、CDN 资源与组件脚本，保证渲染效果、交互功能、图表展示与组件库完全一致

### 7.4 场景 4：修改现有组件的样式 / 交互 / 图表

**执行步骤：**

1. 先完整阅读本手册，尤其是「四、组件样式修改专属强制规范」的所有内容，完整读取现有`style_library.html`文件
2. 识别用户的修改需求，匹配对应的修改等级，严格遵守对应等级的专属修改规则
3. 精准定位用户指定的「组件序号 + 组件名称」，仅可修改该组件对应的 CSS 样式、JS 脚本，禁止修改其他任何未指定的内容
4. 按规范添加完整的修改记录注释，3 级重构修改必须添加历史版本备份
5. 完成修改后，严格执行「4.4 样式修改后的强制自检流程」，全部通过后方可输出
6. 输出修改后的完整`style_library.html`全量代码

------

## 八、绝对禁止行为红线（AI 违反任何一条均为无效操作）

1. ❌ 禁止修改、删除、重排序组件库中已有的非指定组件代码、序号、顺序、样式、脚本
2. ❌ 禁止修改系统固定容器`.section-card`/`.component-title`/`.demo-area`的基础样式、系统固定脚本区的代码
3. ❌ 禁止拆分组件库为多个 HTML/CSS/JS 文件，所有内容必须保留在`style_library.html`单文件中
4. ❌ 禁止使用行内样式、ID 选择器、!important 强制覆盖样式（特殊情况除外）
5. ❌ 禁止新增组件时插入到已有组件中间，必须在文件最末尾追加
6. ❌ 禁止使用无命名空间的通用类名，造成样式污染
7. ❌ 禁止引入任何本地私有文件、不可访问的外部资源，仅可使用开源库官方稳定 CDN
8. ❌ 禁止在未明确用户修改需求的等级、修改范围的情况下，擅自修改组件样式、脚本
9. ❌ 禁止修改组件样式 / 脚本时，删除、修改原有类名、核心入口，导致原有复用该组件的页面失效
10. ❌ 禁止修改样式 / 脚本时，不按规范添加修改记录、历史备份注释
11. ❌ 禁止跨等级修改，比如用户仅要求微调整圆角，擅自重构组件全量样式、交互逻辑
12. ❌ 禁止修改全局变量时，擅自修改非指定的其他全局变量，或修改 reset 基础样式
13. ❌ 禁止修改样式 / 脚本后，未完成自检流程就输出代码，导致样式冲突、渲染异常、功能失效
14. ❌ 禁止输出**只有外观没有渲染能力**的假图表，图表必须完整展示坐标轴、图例、数据、tooltip，可正常渲染
15. ❌ 禁止输出**只有样式没有操作能力**的假交互，交互组件必须可真实点击、切换、展开、关闭，形成状态闭环
16. ❌ 禁止图表组件无数据、无坐标轴、无图例，出现溢出、截断、压扁、控制台报错
17. ❌ 禁止交互组件出现点击无响应、展开无法关闭、切换失效、事件污染、影响其他组件功能的问题