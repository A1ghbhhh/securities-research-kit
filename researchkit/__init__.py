"""securities-research-kit：传统证券研究工具箱。

覆盖财报指标、行业研究框架、估值（DCF / 可比公司）与投顾报告生成，
面向券商研究所、投资顾问与交易员日常研究的轻量 Python 工具。
"""

from .advisor import evening_review, morning_note
from .financials import FinancialStatements, financial_ratios, net_income_cagr, revenue_cagr
from .industry import pest, porter_five_forces, research_outline
from .valuation import dcf, relative_valuation

__all__ = [
    "FinancialStatements",
    "financial_ratios",
    "revenue_cagr",
    "net_income_cagr",
    "research_outline",
    "pest",
    "porter_five_forces",
    "dcf",
    "relative_valuation",
    "morning_note",
    "evening_review",
]
