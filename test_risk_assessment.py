from risk_assessment import (
    recommend_mitigation,
    generate_assessment
)


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


def test_generate_complete_security_assessment():
    result = generate_assessment(
        asset="Critical Web3 Transaction System",
        threat="Unauthorized Activity",
        likelihood=5,
        impact=5,
        control_name="Transaction Authorization Control",
        control_effectiveness=1
    )

    assert result["asset"] == "Critical Web3 Transaction System"
    assert result["threat"] == "Unauthorized Activity"
    assert result["risk_score"] == 25
    assert result["risk_level"] == "CRITICAL"

    assert result["control"]["control"] == "Transaction Authorization Control"
    assert result["control"]["effectiveness"] == 1
    assert result["control"]["status"] == "INEFFECTIVE"

    assert result["control_gap"] is True
    assert result["mitigation"] == "IMMEDIATE MITIGATION"