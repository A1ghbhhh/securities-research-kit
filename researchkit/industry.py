"""行业研究框架模板（卖方研究 / 行研风格）。"""
from __future__ import annotations

from typing import Dict, List


def research_outline(sector: str) -> Dict[str, List[str]]:
    """生成标准行业研究报告骨架：宏观 → 行业 → 公司。"""
    return {
        "宏观环境": ["宏观经济周期与流动性", "产业政策与监管导向", "上下游价格与成本传导"],
        "行业格局": [
            "市场规模与增速",
            "竞争格局与集中度 (CRn)",
            "产业链上下游与议价能力",
            "技术迭代与壁垒",
        ],
        "公司研究": [
            "商业模式与盈利驱动",
            "财务质量 (ROE / 现金流)",
            "成长性 vs 估值匹配度",
            "催化剂与风险提示",
        ],
    }


def pest(sector: str) -> Dict[str, str]:
    return {
        "Political": f"{sector} 相关政策、监管与贸易环境",
        "Economic": f"利率、通胀与需求景气对 {sector} 的影响",
        "Social": f"人口结构与消费习惯变迁对 {sector} 的拉动",
        "Technological": f"技术演进对 {sector} 生产 / 交付方式的重塑",
    }


def porter_five_forces() -> Dict[str, str]:
    return {
        "现有竞争者": "行业内对手数量、份额与价格战强度",
        "潜在进入者": "壁垒（牌照 / 规模 / 技术）阻挡新进入者的程度",
        "替代品": "替代产品 / 模式对需求的侵蚀风险",
        "供应商议价": "上游集中度与对成本的把控力",
        "购买方议价": "下游客户集中度与压价能力",
    }
