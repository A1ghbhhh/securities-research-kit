from researchkit import dupont, dupont_from_financials, FinancialStatements


def test_dupont_identity():
    # ROE = 15%, NM=5%, AT=1.0, EM=3.0 -> 0.05*1.0*3.0 = 0.15
    out = dupont(0.15, 0.05, 1.0, 3.0)
    assert abs(out["product"] - 0.15) < 1e-9
    assert abs(out["roe"] - out["product"]) < 1e-9


def test_dupont_from_financials():
    fs = FinancialStatements(
        revenue=[1000.0, 1200.0],
        net_income=[50.0, 60.0],
        gross_profit=[400.0, 480.0],
        total_assets=[600.0, 800.0],
        total_equity=[200.0, 300.0],
        total_liabilities=[400.0, 500.0],
        current_assets=[300.0, 400.0],
        current_liabilities=[200.0, 250.0],
    )
    out = dupont_from_financials(fs)
    # latest: NM=60/1200=0.05, AT=1200/800=1.5, EM=800/300=2.667
    assert abs(out["net_margin"] - 0.05) < 1e-9
    assert abs(out["asset_turnover"] - 1.5) < 1e-9
    assert abs(out["equity_multiplier"] - (800/300)) < 1e-9
    # product == roe = 60/300 = 0.2
    assert abs(out["roe"] - 0.2) < 1e-9
    assert abs(out["product"] - 0.2) < 1e-9
