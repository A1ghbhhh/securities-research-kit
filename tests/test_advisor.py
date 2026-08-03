from researchkit.advisor import evening_review, morning_note


def test_morning_note():
    note = morning_note(
        "2026-08-03", "沪指缩量震荡", ["600519", "000858"], "震荡偏多", ["外围波动"]
    )
    assert "投资顾问晨报" in note
    assert "600519" in note
    assert "外围波动" in note


def test_evening_review():
    r = evening_review("2026-08-03", "成交放大", ["券商异动"], "关注量能持续性")
    assert "收盘复盘" in r
    assert "券商异动" in r
