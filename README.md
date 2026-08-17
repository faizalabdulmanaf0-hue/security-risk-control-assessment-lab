🔐 Security Risk & Control Assessment Lab

A Python-based security risk assessment engine designed to evaluate security risks, assess control effectiveness, identify control gaps, and recommend appropriate mitigation actions.

This project demonstrates a structured security assessment workflow using deterministic risk and control logic.

---

🎯 Objective

The objective of this project is to demonstrate how security risks can be evaluated systematically by combining:

- Risk likelihood
- Risk impact
- Risk severity
- Security control effectiveness
- Control gap identification
- Mitigation recommendations
- Automated security testing

The project focuses on turning security assessment inputs into a structured and actionable result.

---

🔄 Security Assessment Pipeline

Security Scenario
       ↓
Likelihood + Impact
       ↓
Risk Score
       ↓
Risk Level
       ↓
Security Control
       ↓
Control Effectiveness
       ↓
Control Gap
       ↓
Mitigation Recommendation
       ↓
Automated Security Test
       ↓
GitHub Actions

---

🧮 Risk Calculation

The engine calculates risk using:

Risk Score = Likelihood × Impact

Risk levels are classified as:

Risk Score| Risk Level
15+| CRITICAL
10–14| HIGH
5–9| MEDIUM
0–4| LOW

Example:

Likelihood = 5
Impact = 5

Risk Score = 5 × 5
           = 25

Risk Level = CRITICAL

---

🛡️ Control Assessment

The engine evaluates security control effectiveness on a numerical scale.

Effectiveness| Control Status
4–5| EFFECTIVE
2–3| PARTIALLY EFFECTIVE
0–1| INEFFECTIVE

The assessment also identifies a control gap when:

Effectiveness < 3

---

🚨 Mitigation Recommendation

The engine maps risk severity and control gaps to a recommended action.

CRITICAL + Control Gap
        ↓
IMMEDIATE MITIGATION

HIGH + Control Gap
        ↓
PRIORITY MITIGATION

MEDIUM + Control Gap
        ↓
IMPROVE CONTROL

LOW + Control Gap
        ↓
MONITOR

No Control Gap
        ↓
CONTROL ACCEPTABLE

This allows the assessment to move beyond simply identifying risk and provide a structured mitigation decision.

---

🧠 Unified Security Assessment

The "generate_assessment()" function provides a single entry point for the complete assessment workflow.

It combines:

Risk Calculation
       +
Control Assessment
       +
Control Gap Detection
       +
Mitigation Recommendation

Example assessment:

Asset:
Critical Web3 Transaction System

Threat:
Unauthorized Activity

Likelihood:
5

Impact:
5

Risk Score:
25

Risk Level:
CRITICAL

Control:
Transaction Authorization Control

Effectiveness:
1 / 5

Control Status:
INEFFECTIVE

Control Gap:
TRUE

Mitigation:
IMMEDIATE MITIGATION

---

🔬 Security Finding

RISK-001 — Critical Risk with Control Gap

Severity: CRITICAL

This finding demonstrates a scenario where a critical risk exists together with an ineffective security control.

The assessment identifies:

Risk Score: 25
Risk Level: CRITICAL

Control Effectiveness: 1 / 5
Control Status: INEFFECTIVE

Control Gap: TRUE

Mitigation:
IMMEDIATE MITIGATION

The finding documents the risk scenario, root cause, security impact, and recommended mitigation.

See:

findings/RISK-001.md

---

🧪 Security Testing

The project uses "pytest" to validate the assessment logic.

Current tests cover:

- Critical risk mitigation
- High risk mitigation
- Medium risk mitigation
- Low risk mitigation
- No-control-gap scenarios
- Complete security assessment generation

The complete assessment test validates the entire flow:

Input
 ↓
Risk Calculation
 ↓
Risk Level
 ↓
Control Assessment
 ↓
Control Gap
 ↓
Mitigation
 ↓
Expected Security Decision

---

🤖 Continuous Integration

GitHub Actions automatically executes the security tests when changes are pushed to the repository.

Workflow:

Code Change
     ↓
GitHub Push
     ↓
GitHub Actions
     ↓
Python Environment
     ↓
Install pytest
     ↓
Run Security Tests
     ↓
Tests Passed

The CI pipeline helps detect regressions when the assessment engine is modified.

---

📁 Project Structure

security-risk-control-assessment-lab/

├── risk_assessment.py
├── test_risk_assessment.py
├── findings/
│   └── RISK-001.md
│
└── .github/
    └── workflows/
        └── tests.yml

---

🛠️ Technology

- Python
- Pytest
- Git
- GitHub
- GitHub Actions
- Security Risk Assessment
- Control Assessment
- Risk Analysis
- Security Testing
- Technical Documentation

---

🎯 Research Focus

This project focuses on demonstrating a practical security assessment process rather than simply calculating a numerical risk score.

The assessment workflow connects:

Risk → Control → Gap → Mitigation → Validation

This approach can be extended to security assessments involving applications, infrastructure, Web3 systems, governance systems, and other technology environments.

---

🚧 Current Status

Completed

- Risk score calculation
- Risk level classification
- Security control assessment
- Control gap detection
- Mitigation recommendation logic
- Unified security assessment function
- Automated Python tests
- GitHub Actions CI
- RISK-001 security finding

Future Research

Potential future extensions include:

- Additional risk findings
- More control categories
- Risk acceptance logic
- Residual risk calculation
- Security assessment reporting
- Additional automated regression scenarios

---

⚠️ Disclaimer

This project is an educational security research laboratory.

The scenarios and findings are designed for controlled security research, learning, and portfolio demonstration.

This project should not be interpreted as a security assessment of any real-world production system.