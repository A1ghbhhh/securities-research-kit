from researchkit.industry import pest, porter_five_forces, research_outline


def test_outline_keys():
    o = research_outline("白酒")
    assert set(o.keys()) == {"宏观环境", "行业格局", "公司研究"}
    assert all(isinstance(v, list) and v for v in o.values())


def test_pest():
    p = pest("半导体")
    assert set(p.keys()) == {"Political", "Economic", "Social", "Technological"}


def test_porter():
    f = porter_five_forces()
    assert len(f) == 5
