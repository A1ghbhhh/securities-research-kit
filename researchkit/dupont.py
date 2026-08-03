"""杜邦分析（DuPont analysis）— 拆解 ROE 的 drivers。"""
from __future__ import annotations

from typing import Dict


def dupont(roe: float, net_margin: float, asset_turnover: float,
           equity_multiplier: float) -> Dict[str, float]:
    """返回杜邦三因子分解与各因子对 ROE 的贡献。

    恒等式：ROE = 净利率 × 总资产周转率 × 权益乘数。
    返回 ``contribution`` 为各因子独立相乘得到的乘积（与输入 roe 应一致，
    用于校验），``product`` 为三因子连乘值。
    """
    product = net_margin * asset_turnover * equity_multiplier
    return {
        "roe": roe,
        "net_margin": net_margin,
        "asset_turnover": asset_turnover,
        "equity_multiplier": equity_multiplier,
        "product": product,
    }


def dupont_from_financials(fs) -> Dict[str, float]:
    """从 FinancialStatements 直接计算杜邦三因子（取最新一期）。

    ``fs`` 为 financials.FinancialStatements 实例（含 revenue, net_income,
    total_assets, total_equity, total_liabilities）。
    """
    i = -1
    rev = fs.revenue[i]
    ni = fs.net_income[i]
    ta = fs.total_assets[i]
    te = fs.total_equity[i]
    tl = fs.total_liabilities[i]
    net_margin = ni / rev if rev else float("nan")
    asset_turnover = rev / ta if ta else float("nan")
    equity_multiplier = ta / te if te else float("nan")
    roe = ni / te if te else float("nan")
    return dupont(roe, net_margin, asset_turnover, equity_multiplier)
