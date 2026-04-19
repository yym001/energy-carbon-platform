# Overview 页面 — 四维度 KPI 业务计算说明

---

## 一、空间维度（Space）

所有空间节点拥有相同的 KPI 结构，差异在 **面积** 和 **绑定表计** 不同。父节点值 = 子节点求和。

### KPI 卡片

| KPI 卡片 | 主值来源 | 主值计算 |
|----------|---------|---------|
| Total Electricity | 绑定电表累计读数差分 | 该空间绑定电表区间电量汇总（虚拟电表） |
| Peak Demand | 功率点位时间序列 | 时间窗口内该空间总功率序列最大值，根据网上电价查询，目前马来西亚电价计算需要用到月功率峰值，目前这个位置放置月峰值 |
| Total Water | 绑定水表累计读数差分 | 该空间绑定水表区间用水汇总 |
| Peak Flow Rate | 流量点位时间序列 | 时间窗口内总流量序列最大值 |
| Carbon (est.) | 电量 × 固定因子 | 总用电 × * tCO₂e/kWh |
| Energy Intensity | 电量 / 面积 | 总用电 ÷ 节点面积 |
| Energy Cost | 分时电价计算 | 分时电费 + 水费汇总 |
| Device Online | 设备通讯状态 | 在线设备数 ÷ 总设备数 |

### 子指标

| KPI 卡片 | 子指标 | 计算公式 |
|----------|--------|---------|
| Total Electricity | Savings X kWh | 基准电量 − 实际电量 |
| Peak Demand | ▲ X.X% | 环比 = (本期峰值 − 上期峰值) ÷ 上期峰值 × 100% |
| Total Water | ▼ X.X% YoY | 环比 = (本期用水 − 上期用水) ÷ 上期用水 × 100% |
| Peak Flow Rate | ▲ X.X% | 环比 = (本期峰值 − 上期峰值) ÷ 上期峰值 × 100% |
| Carbon (est.) | ▲ X.X% | 环比 = (本期排放量 − 上期排放量) ÷ 上期排放量 × 100% |
| Energy Intensity | ▲ X.X% | 环比 = (本期强度 − 上期强度) ÷ 上期强度 × 100% |
| Energy Cost | Savings X MYR | 基准费用 − 实际费用；基准费用=基准电量*电价公式；实际费用=实际电量*电价公式 |
| Device Online | X Alarms | 该空间下所有设备/表计未恢复告警数求和 |

---

## 二、组织维度（Org）

### KPI 卡片

| KPI 卡片 | 主值来源 | 主值计算 |
|----------|---------|---------|
| Cumulative Energy Bill | 绑定空间费用    | 绑定空间费用累加 |
| Carbon Emission Quota | 电量 × 排放因子 | 组织电量 × * tCO₂e/kWh；组织电量=虚拟电表读数 |
| Per Capita Energy Use | 电量 / 人数 | 组织电量 ÷ 组织人数 |
| Cost Savings vs Baseline | 基线系统参数 | 上月费用 − 本月费用 |

### 子指标

| KPI 卡片 | 子指标 | 计算公式 |
|----------|--------|---------|
| Cumulative Energy Bill | 进度条 X.X% Consumed | 累计费用 ÷ 年度预算 × 100%；年度预算：配置页面进行配置 |
| Cumulative Energy Bill | 状态标签 | 配置页面可配置年度预算，超过为红色（alarm），未超过为绿色（normal） |
| Carbon Emission Quota | 进度条 X.X% Consumed | 累计碳排 ÷ 碳配额上限× 100%；碳配额上限：配置页面进行配置 |
| Carbon Emission Quota | 状态标签 | 配置页面可配置碳配额上限，超过为红色（alarm），未超过为绿色（normal） |
| Per Capita Energy Use | X% Lower/Higher | 偏差 = (本组织人均 − 园区平均人均) ÷ 园区平均人均 × 100%；正值=Higher(红)，负值=Lower(绿) |
| Cost Savings | Compared with last month | 对比基准 = 上月同组织费用 |

---

## 三、设备维度（Device）

### 系统级节点（非叶子节点）

适用节点：TAR UMT、Air Conditioning System、Chiller System、Cooling Water Pump System、Chilled Water Pump System、Cooling Tower System、AHU System、Lighting System。

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Running Units | 设备状态点位 | 子设备中 status=running 的数量； | `X Offline`(离线数)、`Y Alarmed`(有活跃告警数)；设备在线离线通过暖通系统传过来的通讯测点判断；设备告警由告警告警规则和暖通系统上送两种，目前暂无数据 |
| Current Total Power | 子设备实时功率 | 子设备功率求和 | `[设备名] · XX kW`(功率最高子设备)、`Highest now` |
| Today Energy | 子设备今日电量 | 子设备今日电量求和 | `+X.X% vs yesterday` 环比=(今日−昨日)÷昨日×100%； |
| Active Alarms | 告警系统 | 子设备未恢复告警求和 | `X Critical`(severity=critical)、`Y Major`(severity=major) |

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
| Meter Devices | 电表数量统计 | 下级全部电表数量，来自表计管理页面数据 | `X Offline`(status=off)、`Y Alert`(status=warn)；设备在线离线通过暖通系统传过来的通讯测点判断；设备告警由告警告警规则和暖通系统上送两种，目前暂无数据 |
| Current Total Power | 分表实时功率 | 全部分表功率求和 | `Peak demand · X kW`(当日功率最大值)、`Live total` |
| Today Energy | 分表今日电量 | 全部分表今日电量求和 | `+X.X% vs yesterday` 环比c |
| Monthly Energy | 分表月电量 | 全部分表月电量求和 | `+X.X% vs last`month 环比 |
| Active Alerts | 告警系统 | 全部电表告警求和 | `Demand warning X`、`Overload X` 或 `No active alerts` |

### B. TTSS Main Electric Meter（主变总表）

**Demand 面板**

| 参数 | 来源 | 计算 |
|------|------|------|
| Today Peak Demand | 需量点位序列 | 当日所有时刻中的最大需量值 |
| Contract Demand | 基准功率 | 基准功率 |
| Demand Utilization | 计算值 | 当前需量 ÷ 配置需量 × 100% |
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
| Real-time Power | 有功功率点位 | 电表功率测点 | `Current X A`(实时电流测点)、`Voltage X V`(实时电压测点) |
| Today Energy | 累计电量差分 | 00:00→now 差值 | `Avg X kWh/h`(电量÷小时数)、`Peak X kW`(今日峰值) |
| This Month | 累计电量差分 | 月初→now 差值 | `21 days`(已过天数)、`Est. X.X MWh`(目前计算公式暂时定为：至今电量/当前天数*当月天数，后续会根据现场实际运行情况修改优化） |

**灯光表计特殊处理：** Current A/B/C 和 Voltage A/B/C 显示 "-"。

### D. Water Meter 根节点

| KPI 卡片 | 主值来源 | 主值计算 | 子指标 |
|----------|---------|---------|--------|
| Water Meters | 水表数量统计 | 下级水表数量 | `Online X · Offline Y` |
| Real-time Total Flow | 子水表流量点位 | 子水表实时流量求和 | `Campus inlet + branch loops` |
| Today Water Usage | 子水表累计差分 | 子水表累计差分求和 | `vs yesterday +X.X%` 环比； |
| Average Pressure | 子水表压力点位 | 子水表压力平均值 | `Target 2.8 - 3.5 bar`，没有就用-表示 |
| Water Alerts | 告警系统 | 水系统异常事件统计 | `X offline · Y leakage watch`；离线来自厂家传过来的通讯测点，告警来自厂家传输和系统告警规则产生，目前暂无告警； |

### E. 水表叶子

| KPI | 来源 | 计算 |
|-----|------|------|
| 实时流量 | 流量点位 | 直接取值 |
| 今日用水 | 累计读数差分 | 00:00→now 差值 |
| 本月用水 | 累计读数差分 | 月初→now 差值 |
| 实时压力 | 压力点位 | 直接取值，无数据用-表示 |
| 供回水温差 | 温度点位 | 进水温 − 回水温，无数据用-表示 |

---

## 通用公式速查

| 公式 | 表达式 | 适用场景 |
|------|--------|---------|
| 环比 MoM | (本期 − 上期) ÷ 上期 × 100% | 所有 vs yesterday / vs previous |
| 同比 YoY | (本期 − 去年同期) ÷ 去年同期 × 100% | Water Total 等 |

### 环比/同比在不同时间粒度下的对比基准

#### 环比（MoM / vs previous）

| 时间范围 | 本期 | 上期（对比基准） | 子指标文本示例 |
|----------|------|----------------|---------------|
| Today | 今日（00:00 ~ now） | 昨日（同时段） | +2.1% vs yesterday |
| This Week | 本周（周一 ~ now） | 上周（同时段） | +1.8% vs last week |
| This Month | 本月（1日 ~ now） | 上月（同时段） | −0.5% vs last month |
| This Year | 本年（1月 ~ now） | 去年（同时段） | +3.2% vs last year |
| Custom | 自定义区间 | 紧邻的等长前段 | +1.5% vs previous period |

#### 同比（YoY / Year-over-Year）

| 时间范围 | 本期 | 去年同期（对比基准） | 子指标文本示例 |
|----------|------|-------------------|---------------|
| Today | 今日 | 去年同日 | ▼ 1.5% YoY |
| This Week | 本周 | 去年同一周 | ▼ 2.0% YoY |
| This Month | 本月 | 去年同月 | ▼ 1.8% YoY |
| This Year | 本年 | 去年全年 | ▼ 3.1% YoY |

---

## 通用计算逻辑（系统级）

### 1. 基准电量计算

**数据来源：** 三种运行场景实测数据

| 场景 | 条件 | 实测数据 |
|------|------|---------|
| 场景1 | 办公区域正常使用 + 礼堂举办活动 | 1小时功率 P1，用电量 MD1 |
| 场景2 | 办公区域停止使用 + 礼堂举办活动 | 1小时功率 P2，用电量 MD2 |
| 场景3 | 办公区域正常使用 + 礼堂不举办活动 | 1小时功率 P3，用电量 MD3 |

（需要现场给出具体数据）

**计算逻辑：** 一天之内场景1/2/3分别的时间为 H1、H2、H3（需要现场给出具体数据）

- 天基准电量 = MD1 × H1 + MD2 × H2 + MD3 × H3
- 天基准功率 = P1 × H1 + P2 × H2 + P3 × H3
- 基准电价 = 由基准电量结合电价计算逻辑计算

### 2. 电价计算逻辑

由马来西亚实际电价规则配置（还在研究中）。

### 3. 不同空间/组织用电量计算

通过 **虚拟电表** 实现：为每个组织、每个空间建立虚拟电表，虚拟电表可选择不同的物理电表进行数学运算。

**示例（第一层空间）：**

1. 建立虚拟表
2. 绑定第一层的照明电表和风柜电表，逻辑为相加

### 4. 空间费用计算

根据总用电量计算总费用，再按各空间用电占比进行费用分配：

**步骤：**

1. **计算园区总费用**：园区总电量按电价公式计算出总费用 Total_Cost
2. **计算各空间用电占比**：空间用电占比 = 该空间虚拟电表电量 ÷ 园区总电量
3. **分配费用**：空间费用 = Total_Cost × 空间用电占比

**示例：**

| 空间 | 电量 (kWh) | 用电占比 | 分配费用 (MYR) |
|------|-----------|---------|---------------|
| Ground Floor | 1,800 | 14.4% | Total_Cost × 14.4% |
| Level 1 | 2,100 | 16.8% | Total_Cost × 16.8% |
| Level 2 | 1,950 | 15.6% | Total_Cost × 15.6% |
| ... | ... | ... | ... |
| 合计 | 12,480 | 100% | Total_Cost |

5. 空间与组织逻辑关系

组织可以绑定一个或多个空间，支持按比例分配。与组织相关的数据根据绑定空间得出。

**绑定规则：**

- 一个组织可绑定多个空间，每个绑定关系带有 **分摊比例**（0~100%）
- 同一空间可被多个组织绑定，各组织分摊比例之和应 = 100%
- 分摊比例在「系统管理 → 组织管理」页面配置

**数据推算流程：**

1. **组织电量** = Σ(绑定空间电量 × 该空间的分摊比例)
2. **组织费用** = Σ(绑定空间费用 × 该空间的分摊比例)
3. **组织碳排** = 组织电量 × 碳排放因子
4. **组织人均能耗** = 组织电量 ÷ 组织人数

**示例：**

Finance Department 绑定 Level 2（分摊比例 40%）+ Level 3（分摊比例 20%）：

- Finance 电量 = Level 2 电量 × 40% + Level 3 电量 × 20%
- Finance 费用 = Level 2 费用 × 40% + Level 3 费用 × 20%

**父子组织关系：** 父组织值 = 子组织值求和。
