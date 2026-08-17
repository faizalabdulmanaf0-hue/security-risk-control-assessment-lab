def calculate_risk(likelihood, impact):
    score = likelihood * impact

    if score >= 15:
        return score, "CRITICAL"
    elif score >= 10:
        return score, "HIGH"
    elif score >= 5:
        return score, "MEDIUM"
    else:
        return score, "LOW"


def assess_control(control_name, effectiveness):
    if effectiveness >= 4:
        status = "EFFECTIVE"
    elif effectiveness >= 2:
        status = "PARTIALLY EFFECTIVE"
    else:
        status = "INEFFECTIVE"

    return {
        "control": control_name,
        "effectiveness": effectiveness,
        "status": status
    }


def identify_control_gap(effectiveness):
    return effectiveness < 3


def recommend_mitigation(risk_level, control_gap):
    if risk_level == "CRITICAL" and control_gap:
        return "IMMEDIATE MITIGATION"

    elif risk_level == "HIGH" and control_gap:
        return "PRIORITY MITIGATION"

    elif risk_level == "MEDIUM" and control_gap:
        return "IMPROVE CONTROL"

    elif risk_level == "LOW" and control_gap:
        return "MONITOR"

    else:
        return "CONTROL ACCEPTABLE"


def assess_security_risk(
    asset,
    threat,
    likelihood,
    impact,
    control_name,
    control_effectiveness
):
    risk_score, risk_level = calculate_risk(
        likelihood,
        impact
    )

    control = assess_control(
        control_name,
        control_effectiveness
    )

    control_gap = identify_control_gap(
        control_effectiveness
    )

    mitigation = recommend_mitigation(
        risk_level,
        control_gap
    )

    return {
        "asset": asset,
        "threat": threat,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "control": control,
        "control_gap": control_gap,
        "mitigation": mitigation
    }


def generate_assessment(
    asset,
    threat,
    likelihood,
    impact,
    control_name,
    control_effectiveness
):
    return assess_security_risk(
        asset,
        threat,
        likelihood,
        impact,
        control_name,
        control_effectiveness
    )