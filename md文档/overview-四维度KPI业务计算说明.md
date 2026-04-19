# Overview 页面 — 四维度 KPI 业务计算说明

---

## 一、空间维度（Space）

所有空间节点拥有相同的 KPI 结构，差异在 **面积** 和 **绑定表计** 不同。父节点值 = 子节点求和。

### 层级缩放规则

```
ratio = 当前节点面积 ÷ 园区总面积(17124 m²)
电量 / 水量 / 碳排 = 园区基准值 × ratio
峰值需量 = 基准值 + (ratio − 1) × 调节因子
```

子指标（Savings / YoY / 变化率%）切换节点时不重新计算，保持园区级统计值。

### 各节点面积

| 节点 | 面积 m² |
|------|---------|
| TAR UMT（根） | 17124 |
| Bangunan Tun Tan Siew Sin | 8204 |
| Ground Floor | 1320 |
| Level 1 | 1280 |
| Level 2 | 1100 |
| Level 3 | 1050 |
| Level 4 | 1020 |
| Level 5 | 980 |
| District Cooling System Room | 1454 |

### KPI 卡片

| KPI 卡片 | 主值来源 | 主值计算 |
|----------|---------|---------|
| Total Electricity | 绑定电表累计读数差分 | 该空间绑定电表区间电量汇总 |
| Peak Demand | 功率点位时间序列 | 时间窗口内该空间总功率序列最大值 |
| Total Water | 绑定水表累计读数差分 | 该空间绑定水表区间用水汇总 |
| Peak Flow Rate | 流量点位时间序列 | 时间窗口内总流量序列最大值 |
| Carbon (est.) | 电量 × 固定因子 | 总用电 × 0.000699 tCO₂e/kWh |
| Energy Intensity | 电量 / 面积 | 总用电 ÷ 节点面积 |
| Energy Cost | 分时电价计算 | 分时电费 + 水费汇总 |
| Device Online | 设备通讯状态 | 在线设备数 ÷ 总设备数 |

### 子指标

| KPI 卡片 | 子指标 | 计算公式 |
|----------|--------|---------|
| Total Electricity | Savings X kWh | 节约量 = 实际电量 × 5.8%；节约率 = (基线电量 − 实际) ÷ 基线 × 100% |
| Peak Demand | ▲ X.X% | 环比 = (本期峰值 − 上期峰值) ÷ 上期峰值 × 100% |
| Total Water | ▼ X.X% YoY | 同比 = (本期用水 − 去年同期) ÷ 去年同期 × 100% |
| Peak Flow Rate | ▲ X.X% | 环比 = (本期峰值 − 上期峰值) ÷ 上期峰值 × 100% |
| Carbon (est.) | ▲ X.X% | 环比变化率，跟随电量变化率 |
| Energy Intensity | ▲ X.X% | 环比 = (本期强度 − 上期强度) ÷ 上期强度 × 100% |
| Energy Cost | Savings X MYR | 节约 = 实际费用 × 6.2%；节约率 = (基线费用 − 实际) ÷ 基线 × 100% |
| Device Online | X Alarms | 该空间下所有设备/表计未恢复告警数求和 |

---

## 二、组织维度（Org）

所有节点 KPI 公式一致，差异在 **人数、绑定空间、分摊比例**。组织电量 = 空间电量 × 分摊比例。父 = 子求和。

### 层级缩放规则

```
ratio = 当前组织人数 ÷ 园区总人数(140)
费用 / 碳排 = 园区基准值 × ratio
人均能耗 = 89.1 × ratio（模拟值）
```

### 各节点人数

| 节点 | 人数 |
|------|------|
| TAR UMT（根） | 140 |
| Administrative Departments | 50 |
| Registrar's Office | 8 |
| Finance Department | 12 |
| Human Resources | 20 |
| Audit Department | 10 |
| Academic Departments | 60 |
| Faculty of Computing & IT | 35 |
| Faculty of New Energy | 25 |
| Research Management Dept | 15 |
| Logistics Department | 15 |

### KPI 卡片

| KPI 卡片 | 主值来源 | 主值计算 |
|----------|---------|---------|
| Cumulative Energy Bill | 空间费用 × 分摊比例 | 绑定空间费用按比例汇总 |
| Carbon Emission Quota | 电量 × 排放因子 | 组织电量 × 0.000699 tCO₂e/kWh |
| Per Capita Energy Use | 电量 / 人数 | 组织电量 ÷ 组织人数 |
| Cost Savings vs Baseline | 基线系统参数 | 上月费用 − 本月费用 |

### 子指标

| KPI 卡片 | 子指标 | 计算公式 |
|----------|--------|---------|
| Cumulative Energy Bill | 进度条 X.X% Consumed | 累计费用 ÷ 年度预算(5000 MYR) × 100% |
| Cumulative Energy Bill | 状态标签 | >100% → "Over Limit"(红)；>80% → "Near Limit"(琥珀)；≤80% → "Safe Range"(绿) |
| Carbon Emission Quota | 进度条 X.X% Consumed | 累计碳排 ÷ 碳配额上限(15.0 tCO₂e/年) × 100% |
| Carbon Emission Quota | 状态标签 | >100% → "Exceeded"；>80% → "Alert"；≤80% → "Normal" |
| Per Capita Energy Use | X% Lower/Higher | 偏差 = (本组织人均 − 园区平均人均) ÷ 园区平均人均 × 100%；正值=Higher(红)，负值=Lower(绿) |
| Cost Savings | Compared with last month | 对比基准 = 上月同组织费用 |

---

## 三、设备维度（Device）

### A. 系统级节点（非叶子节点）

适用节点：TAR UMT、Air Conditioning System、Chiller System、Cooling Water Pump System、Chilled Water Pump System、Cooling Tower System、AHU System、Lighting System。

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Running Units | 设备状态点位 | 子设备中 status=running 的数量 | `X Offline`(离线数)、`Y Alarmed`(有活跃告警数) |
| Current Total Power | 子设备实时功率 | 子设备功率求和 | `[设备名] · XX kW`(功率最高子设备)、`Highest now` |
| Today Energy | 子设备今日电量 | 子设备今日电量求和 | `+X.X% vs yesterday` 环比=(今日−昨日)÷昨日×100%；昨日=今日×0.93(估算) |
| Active Alarms | 告警系统 | 子设备未恢复告警求和 | `X Critical`(severity=critical)、`Y Major`(severity=major) |

### B. 叶子节点（单设备）

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Current Status | 状态点位 | running / stopped / fault / offline | 固定描述文本 |
| Current Power | 功率点位 | 直接取功率点位值 | 特征指标：冷机→COP，水泵→频率Hz，冷却塔→进出水温差℃，AHU→送风温度℃ |
| Today Energy | 功率积分/电量差分 | 功率积分或电量点位差分 | `+X.X% vs yesterday` 环比；昨日=今日÷1.08(估算) |
| Load Rate | 功率/额定功率 | 实时功率 ÷ 额定功率 × 100% | — |
| Active Alarms | 告警系统 | 该设备未恢复告警数 | `X Active` 或 `No active alarms` |

### 各叶子设备额定功率

| 设备 | 额定功率 kW |
|------|------------|
| CH-1, CH-2 | 420 |
| CWP-1/2/3 | 55 |
| CHWP-1/2/3 | 45 |
| CT-1, CT-2 | 30 |
| GF AHU | 15 |
| L1~L5 AHU-1/2/3（共11台） | 12 |
| GF~L5 Lighting（共6个） | 8 |

### 灯光设备特殊处理

灯光设备目前仅有电量、功率、每个区域的数量数据，其余字段显示 "-"：

- 照度 → "-"
- 区域状态 → "-"
- 策略数 → "-"

---

## 四、表计维度（Meter）

### A. Electric Meter 根节点

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Meter Devices | 电表数量统计 | 下级全部电表数量 | `X Offline`(status=off)、`Y Alert`(status=warn) |
| Current Total Power | 分表实时功率 | 全部分表功率求和 | `Peak demand · X kW`(当日功率最大值)、`Live total` |
| Today Energy | 分表今日电量 | 全部分表今日电量求和 | `+X.X% vs yesterday` 环比 |
| Overall Power Factor | 功率加权平均 | Σ(Pi×PFi) ÷ ΣPi | `Target ≥0.95`；≥0.95→"Normal"，<0.95→"Below Target" |
| Active Alerts | 告警系统 | 全部电表告警求和 | `Demand warning X`、`Overload X` 或 `No active alerts` |

### B. TTSS Main Electric Meter（主变总表）

**Demand 面板**

| 参数 | 来源 | 计算 |
|------|------|------|
| Today Peak Demand | 需量点位序列 | 当日所有时刻中的最大需量值 |
| Contract Demand | 系统配置 | 固定值（如 1200 kW） |
| Demand Utilization | 计算值 | 当前需量 ÷ 合同需量 × 100% |
| Month Peak Demand | 需量点位序列 | 本月所有时刻中的最大需量值 |

**Energy Consumption 面板**

| 参数 | 来源 | 计算 |
|------|------|------|
| Today Avg kWh/h | 电量/时间 | 今日电量 ÷ 已运行小时数 |
| Today vs yesterday | 电量差分 | (今日 − 昨日) ÷ 昨日 × 100% |
| Yesterday Avg kWh/h | 电量/时间 | 昨日电量 ÷ 24 |
| This Month Est. | 累计推算 | 本月累计 × (月总天数 ÷ 已过天数) |
| Last Month RM | 费用记录 | 上月总费用 |

**TTSS 虚拟表（Power Quality / Load Trend）**

TTSS 为虚拟表计无物理设备，Power Quality 12项全部显示 "-"；Load Trend 中电压/电流/功率因数显示 "Virtual meter — No data available for this metric"，仅功率有数据。

### C. 电表叶子（分表）

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Real-time Power | 有功功率点位 | 直接取值 | `Current X A`(实时电流)、`Voltage X V`(实时电压) |
| Today Energy | 累计电量差分 | 00:00→now 差值 | `Avg X kWh/h`(电量÷小时数)、`Peak X kW`(今日峰值) |
| This Month | 累计电量差分 | 月初→now 差值 | `21 days`(已过天数)、`Est. X.X MWh`(累计×1.42 推算系数) |

**灯光表计特殊处理：** Current A/B/C 和 Voltage A/B/C 显示 "-"。

### D. Water Meter 根节点

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Water Meters | 水表数量统计 | 下级水表数量 | `Online X · Offline Y` |
| Real-time Total Flow | 子水表流量点位 | 子水表实时流量求和 | `Campus inlet + branch loops` |
| Today Water Usage | 子水表累计差分 | 子水表累计差分求和 | `vs yesterday +X.X%` 环比 |
| Average Pressure | 子水表压力点位 | 子水表压力平均值 | `Target 2.8 - 3.5 bar` |
| Water Alerts | 告警系统 | 水系统异常事件统计 | `X offline · Y leakage watch` |

### E. 水表叶子

| KPI | 来源 | 计算 |
|-----|------|------|
| 实时流量 | 流量点位 | 直接取值 |
| 今日用水 | 累计读数差分 | 00:00→now 差值 |
| 本月用水 | 累计读数差分 | 月初→now 差值 |
| 实时压力 | 压力点位 | 直接取值 |
| 供回水温差 | 温度点位 | 进水温 − 回水温 |

---

## 通用公式速查

| 公式 | 表达式 | 适用场景 |
|------|--------|---------|
| 环比 MoM | (本期 − 上期) ÷ 上期 × 100% | 所有 vs yesterday / vs previous |
| 同比 YoY | (本期 − 去年同期) ÷ 去年同期 × 100% | Water Total 等 |
| 节约量 | 基线 − 实际 | Space 电量/费用 |
| 节约率 | (基线 − 实际) ÷ 基线 × 100% | 电量 5.8%、费用 6.2% |
| 预算消耗比 | 累计 ÷ 年度预算 × 100% | Org 费用/碳配额 |
| 面积缩放 | 园区值 × (节点面积 ÷ 17124) | Space 层级切换 |
| 人头缩放 | 园区值 × (节点人数 ÷ 140) | Org 层级切换 |
| 月预估 | 累计 × (月总天数 ÷ 已过天数) | Meter 月电量 |
| 碳排放 | 电量 × 0.000699 tCO₂e/kWh | 所有碳排计算 |
| 负载率 | 实时功率 ÷ 额定功率 | Device / Meter 叶子 |
| 加权功率因数 | Σ(Pi × PFi) ÷ ΣPi | Meter 综合 PF |

---

## 时间范围（Day/Week/Month/Year）对数据的影响

### 时间乘数 `getTimeMultiplier()`

| 时间范围 | 乘数 (mult) | 说明 |
|----------|------------|------|
| Today | 1 | 基准日值 |
| This Week | 7 | 日值 × 7 |
| This Month | 30 | 日值 × 30 |
| This Year | 365 | 日值 × 365 |
| Custom | N | 自定义区间天数 |

### 各维度受时间范围影响的数据

#### 空间维度（Space）

| 数据项 | 受 mult 影响 | 计算方式 |
|--------|:-----------:|---------|
| Total Electricity | ✅ | 12480 × mult × ratio |
| Total Water | ✅ | 385 × mult × ratio |
| Energy Cost | ✅ | 4368 × mult（电）/ 481 × mult（水） |
| Savings (kWh) | ✅ | 跟随电量值，节约量 = 电量 × 5.8% |
| Savings (MYR) | ✅ | 跟随费用值，节约额 = 费用 × 6.2% |
| Peak Demand | ❌ | today=156 kW；非 today=156 × 1.15（仅区分"当日"和"非当日"） |
| Peak Flow Rate | ❌ | 按面积比缩放，不乘时间系数 |
| Carbon (est.) | ❌ | 按面积比缩放，不乘时间系数 |
| Energy Intensity | ❌ | 固定值 1.52 kWh/m²，不随时间变化 |
| Device Online | ❌ | 固定值 96%，实时状态不随时间变化 |
| Sub-space 对比柱状图 | ✅ | 基准值 × mult |
| Detailed 明细表 | ✅ | 基准值 × mult |
| Structure 环形图 | ❌ | 仅微调比例（seed%5），不随时间线性变化 |
| 趋势图 | 独立数据 | 按时间粒度切换独立数据集（today=24h, week=7d, month=30d, year=12mo） |

#### 组织维度（Org）

**限制：Org 维度不支持 Today 和 Week，自动强制切为 This Month。**

| 数据项 | 受 mult 影响 | 计算方式 |
|--------|:-----------:|---------|
| Cumulative Energy Bill | ✅ | 基准值 × mult × ratio |
| Carbon Emission Quota | ✅ | 跟随费用缩放 |
| Per Capita Energy Use | ❌ | 89.1 × ratio，不乘时间系数 |
| Cost Savings | ✅ | 1240 × ratio，受 mult 影响 |
| 费用对比图 | ✅ | (headcount × 35 + seed) × mult |

#### 设备维度（Device）

| 数据项 | 受 mult 影响 | 说明 |
|--------|:-----------:|------|
| Running Units | ❌ | 实时状态 |
| Current Power | ❌ | 实时功率 |
| Today Energy | ❌ | 固定取当日电量，不随时间范围缩放 |
| Load Rate | ❌ | 实时功率 ÷ 额定功率 |
| Active Alarms | ❌ | 实时告警 |

#### 表计维度（Meter）

| 数据项 | 受 mult 影响 | 说明 |
|--------|:-----------:|------|
| 全部 KPI | ❌ | 表计维度不使用 getTimeMultiplier()，KPI 值固定 |
| TTSS Demand 面板 | ❌ | 固定取当日/当月数据 |
| TTSS Energy 面板 | ❌ | 分 Today/Yesterday/ThisMonth/LastMonth 四行展示 |

### 趋势图数据粒度

趋势图不使用时间乘数，而是为每个时间范围预定义独立的数据集：

| 时间范围 | 横轴标签 | 数据点数 | 粒度 |
|----------|---------|---------|------|
| Today | 00:00 ~ 23:00 | 24 | 每小时 |
| This Week | Mon ~ Sun | 7 | 每天 |
| This Month | 1 ~ 30 | 30 | 每天 |
| This Year | Jan ~ Dec | 12 | 每月 |

---

## 水页面特殊规则

### 项目仅有一只水表

当前项目只有一只水表（Campus Inlet），因此：

- **空间维度**：仅根节点（TAR UMT）显示水 Tab，选择任何子空间节点时水 Tab 自动隐藏
- **组织维度 / 设备维度 / 表计维度**：水 Tab 不可见

### 水模式下的 UI 变化（仅根节点）

| 变化项 | 电模式 | 水模式 |
|--------|--------|--------|
| KPI 卡片 | 显示电力相关卡片 | 隐藏电力卡片，显示水相关卡片 |
| Energy Intensity → Water Intensity | 1.52 kWh/m² | 0.02 m³/m² |
| Elec Cost → Water Cost | 4368 × mult MYR | 481 × mult MYR |
| Device Online → Meter Online | 96% | 同值 |
| Sub-space 对比柱状图 | 显示 | 隐藏 |
| Detailed 明细表 | 显示 | 隐藏 |
| 趋势图 Baseline 线 | 显示（有节能基线） | 隐藏（无基线） |
| 趋势图数据 | 原始值 | 原始值 × 0.35 |
