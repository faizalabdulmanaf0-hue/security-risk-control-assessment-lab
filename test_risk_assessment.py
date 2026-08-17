from risk_assessment import recommend_mitigation


def test_critical_risk_with_control_gap():
    result = recommend_mitigation("CRITICAL", True)
    assert result == "IMMEDIATE MITIGATION"


def test_high_risk_with_control_gap():
    result = recommend_mitigation("HIGH", True)
    assert result == "PRIORITY MITIGATION"


def test_medium_risk_with_control_gap():
    result = recommend_mitigation("MEDIUM", True)
    assert result == "IMPROVE CONTROL"


def test_low_risk_with_control_gap():
    result = recommend_mitigation("LOW", True)
    assert result == "MONITOR"


def test_no_control_gap():
    result = recommend_mitigation("CRITICAL", False)
    assert result == "CONTROL ACCEPTABLE"