"""投顾晨报 / 收评报告生成（模板填充，便于批量产出）。"""
from __future__ import annotations

from typing import List, Optional


def morning_note(
    date: str,
    market_recap: str,
    watchlist: List[str],
    view: str,
    risks: Optional[List[str]] = None,
) -> str:
    """生成投顾晨报 Markdown。"""
    risks = risks or []
    wl = "\n".join(f"- {w}" for w in watchlist) or "- （无）"
    rk = "\n".join(f"- {r}" for r in risks) or "- （无）"
    return (
        f"# 投资顾问晨报 · {date}\n\n"
        f"## 一、昨日市场回顾\n{market_recap}\n\n"
        f"## 二、今日关注标的\n{wl}\n\n"
        f"## 三、市场观点\n{view}\n\n"
        f"## 四、风险提示\n{rk}\n\n"
        "> 本报告由模板自动生成，仅供内部参考，不构成投资建议。"
    )


def evening_review(
    date: str,
    summary: str,
    highlights: List[str],
    view_next: str,
) -> str:
    """生成收盘复盘 Markdown。"""
    hl = "\n".join(f"- {h}" for h in highlights) or "- （无）"
    return (
        f"# 收盘复盘 · {date}\n\n"
        f"## 一、盘面小结\n{summary}\n\n"
        f"## 二、今日亮点\n{hl}\n\n"
        f"## 三、后市展望\n{view_next}\n\n"
        "> 本报告由模板自动生成，仅供内部参考，不构成投资建议。"
    )
