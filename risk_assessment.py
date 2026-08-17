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