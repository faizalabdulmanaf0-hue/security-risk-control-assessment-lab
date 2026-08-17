from risk_assessment import calculate_risk


def test_critical_risk():
    score, level = calculate_risk(4, 5)

    assert score == 20
    assert level == "CRITICAL"