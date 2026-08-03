from researchkit.financials import FinancialStatements, financial_ratios, revenue_cagr


def _fs():
    return FinancialStatements(
        revenue=[100, 120, 150],
        net_income=[10, 15, 20],
        gross_profit=[40, 50, 60],
        total_assets=[200, 220, 250],
        total_equity=[100, 110, 130],
        total_liabilities=[100, 110, 120],
        current_assets=[80, 90, 100],
        current_liabilities=[40, 45, 50],
    )


def test_financial_ratios_basic():
    r = financial_ratios(_fs())
    assert abs(r["roe"] - 20 / 130) < 1e-9
    assert abs(r["gross_margin"] - 60 / 150) < 1e-9
    assert abs(r["net_margin"] - 20 / 150) < 1e-9
    assert abs(r["debt_to_assets"] - 120 / 250) < 1e-9
    assert abs(r["current_ratio"] - 100 / 50) < 1e-9


def test_revenue_cagr():
    assert abs(revenue_cagr(_fs()) - 0.224744871) < 1e-6
