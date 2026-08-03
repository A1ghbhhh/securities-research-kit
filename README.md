# securities-research-kit

![tests](https://github.com/A1ghbhhh/securities-research-kit/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![pytest](https://img.shields.io/badge/tests-pytest-0A8A4A?logo=pytest&logoColor=white)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)

**传统证券研究工具箱** —— 面向券商研究所、投资顾问与交易员的轻量 Python 工具：财报指标、行业研究框架、估值（DCF / 可比公司）与投顾报告生成。零第三方依赖，纯标准库，开箱即跑。

## ✨ 功能

- **财报指标** (`financials`)：ROE / ROA / 毛利率 / 净利率 / 资产负债率 / 流动比率，以及营收、净利 CAGR。
- **行业研究框架** (`industry`)：标准化行研骨架（宏观 → 行业 → 公司）、PEST、波特五力模板。
- **估值模型** (`valuation`)：两阶段 DCF 企业价值估算、可比公司相对估值（均值 / 中位数）。
- **投顾报告** (`advisor`)：晨报 / 收盘复盘 Markdown 模板，支持批量产出。

## 📦 安装

```bash
pip install -e .
# 或仅用于开发测试
pip install pytest
```

## 🚀 快速开始

```python
from researchkit.financials import FinancialStatements, financial_ratios
from researchkit.valuation import dcf, relative_valuation
from researchkit.industry import research_outline
from researchkit.advisor import morning_note

fs = FinancialStatements(
    revenue=[100, 120, 150], net_income=[10, 15, 20], gross_profit=[40, 50, 60],
    total_assets=[200, 220, 250], total_equity=[100, 110, 130],
    total_liabilities=[100, 110, 120], current_assets=[80, 90, 100],
    current_liabilities=[40, 45, 50],
)
print(financial_ratios(fs))                       # ROE / 毛利率 / 负债率 ...
print(dcf([20, 22, 24], 0.10, 0.02))              # DCF 企业价值
print(relative_valuation([14, 15, 16], 2.0))      # 可比公司估值
print(list(research_outline("新能源").keys()))     # 行研骨架
print(morning_note("2026-08-03", "指数窄幅震荡", ["300750"], "结构性机会"))
```

离线演示见 [`examples/research_kit_demo.py`](examples/research_kit_demo.py)。

## 🧪 测试

```bash
pytest -q
```

| 模块 | 覆盖点 |
|------|--------|
| `financials` | 比率计算、CAGR |
| `valuation`  | DCF 折现、参数校验、相对估值 mean/median |
| `industry`   | 骨架 / PEST / 五力 |
| `advisor`    | 晨报 / 收评字段完整性 |

## 🗂 目录

```
researchkit/
├── financials.py   # 财报三表指标
├── valuation.py    # DCF / 可比公司
├── industry.py     # 行研框架模板
└── advisor.py      # 投顾报告生成
tests/              # pytest 用例
examples/           # 离线演示
```

> 与作者的量化工程仓库（回测引擎、定价实验室、实时行情监控等）形成「量化 + 传统证券」双轨能力闭环。
