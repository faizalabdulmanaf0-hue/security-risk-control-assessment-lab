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

    return {
        "asset": asset,
        "threat": threat,
        "risk_score": risk_score,
        "risk_level": risk_level,
        "control": control,
        "control_gap": control_gap
    }