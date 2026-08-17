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