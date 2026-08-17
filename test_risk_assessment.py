from risk_assessment import calculate_risk


def test_critical_risk():
    score, level = calculate_risk(4, 5)

    assert score == 20
    assert level == "CRITICAL"


def test_high_risk():
    score, level = calculate_risk(2, 5)

    assert score == 10
    assert level == "HIGH"
def test_medium_risk():
    score, level = calculate_risk(2, 3)

    assert score == 6
    assert level == "MEDIUM
def test_low_risk():
    score, level = calculate_risk(1, 2)

    assert score == 2
    assert level == "LOW"