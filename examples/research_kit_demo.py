"""离线演示：用 researchkit 完成一份简化的公司研究。"""
from researchkit.advisor import morning_note
from researchkit.financials import FinancialStatements, financial_ratios, revenue_cagr
from researchkit.industry import research_outline
from researchkit.valuation import dcf, relative_valuation
from researchkit.dupont import dupont_from_financials


def main():
    fs = FinancialStatements(
        revenue=[100, 120, 150],
        net_income=[10, 15, 20],
        gross_profit=[40, 50, 60],
        total_assets=[200, 220, 250],
        total_equity=[100, 110, 130],
        total_liabilities=[100, 110, 120],
        current_assets=[80, 90, 100],
        current_liabilities=[40, 45, 50],
    )
    print("财务指标:", financial_ratios(fs))
    print("营收 CAGR:", round(revenue_cagr(fs), 4))
    print("DCF 企业价值:", round(dcf([20, 22, 24], 0.10, 0.02), 2))
    print("相对估值(PE 均值 15 × EPS 2):", relative_valuation([14, 15, 16], 2.0))
    print("研究骨架:", list(research_outline("新能源").keys()))
    print("杜邦分解(ROE):", dupont_from_financials(fs))
    print(
        morning_note(
            "2026-08-03", "指数窄幅震荡", ["300750"], "结构性机会", ["政策不及预期"]
        )
    )


if __name__ == "__main__":
    main()
