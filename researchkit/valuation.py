"""估值模型：DCF（现金流折现）与可比公司相对估值。"""
from __future__ import annotations

from typing import List


def dcf(
    free_cash_flows: List[float],
    discount_rate: float,
    terminal_growth: float,
    terminal_year: Optional[int] = None,
) -> float:
    """两阶段 DCF 估算企业价值（EV）。

    free_cash_flows: 显式预测期各年自由现金流（升序）
    discount_rate:    折现率（WACC）
    terminal_growth:  永续增长率
    terminal_year:    终端价值折现期数（默认 = 预测期长度）
    """
    if discount_rate <= terminal_growth:
        raise ValueError("discount_rate 必须严格大于 terminal_growth")
    if not free_cash_flows:
        raise ValueError("free_cash_flows 不能为空")

    pv = sum(fcf / (1 + discount_rate) ** (t + 1) for t, fcf in enumerate(free_cash_flows))
    ty = terminal_year if terminal_year is not None else len(free_cash_flows)
    last = free_cash_flows[-1]
    terminal_value = last * (1 + terminal_growth) / (discount_rate - terminal_growth)
    pv_terminal = terminal_value / (1 + discount_rate) ** ty
    return pv + pv_terminal


def relative_valuation(
    peer_multiples: List[float],
    target_metric: float,
    method: str = "mean",
) -> float:
    """可比公司相对估值：同业可比倍数 × 目标公司对应指标。

    peer_multiples: 同业公司的估值倍数（如 PE / PS）
    target_metric:  目标公司对应指标（如 EPS / 营收）
    method:         "mean" 或 "median"
    """
    if not peer_multiples:
        raise ValueError("peer_multiples 不能为空")
    if method == "mean":
        mult = sum(peer_multiples) / len(peer_multiples)
    elif method == "median":
        s = sorted(peer_multiples)
        m = len(s) // 2
        mult = s[m] if len(s) % 2 else (s[m - 1] + s[m]) / 2
    else:
        raise ValueError("method 仅支持 mean / median")
    return mult * target_metric
