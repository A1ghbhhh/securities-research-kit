"""财务报表分析与关键指标计算（传统基本面研究）。"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class FinancialStatements:
    """简化三张报表的输入容器。

    各序列按时间升序（最新一期在末尾）。单位保持一致即可（元 / 万元均可）。
    """

    revenue: List[float]
    net_income: List[float]
    gross_profit: List[float]
    total_assets: List[float]
    total_equity: List[float]
    total_liabilities: List[float]
    current_assets: List[float]
    current_liabilities: List[float]


def _cagr(series: List[float]) -> float:
    if len(series) < 2:
        return float("nan")
    return (series[-1] / series[0]) ** (1 / (len(series) - 1)) - 1


def financial_ratios(fs: FinancialStatements) -> Dict[str, float]:
    """返回最新一期关键财务指标。"""
    i = -1
    rev, ni, gp = fs.revenue[i], fs.net_income[i], fs.gross_profit[i]
    ta, te, tl = fs.total_assets[i], fs.total_equity[i], fs.total_liabilities[i]
    ca, cl = fs.current_assets[i], fs.current_liabilities[i]
    return {
        "roe": ni / te if te else float("nan"),
        "roa": ni / ta if ta else float("nan"),
        "gross_margin": gp / rev if rev else float("nan"),
        "net_margin": ni / rev if rev else float("nan"),
        "debt_to_assets": tl / ta if ta else float("nan"),
        "current_ratio": ca / cl if cl else float("nan"),
        "equity_multiplier": ta / te if te else float("nan"),
    }


def revenue_cagr(fs: FinancialStatements) -> float:
    return _cagr(fs.revenue)


def net_income_cagr(fs: FinancialStatements) -> float:
    return _cagr(fs.net_income)
