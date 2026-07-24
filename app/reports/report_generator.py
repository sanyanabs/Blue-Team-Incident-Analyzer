from datetime import datetime


def generate_report(investigation, findings):

    report = []

    report.append("=" * 60)
    report.append("SENTINELAI INCIDENT RESPONSE REPORT")
    report.append("=" * 60)

    report.append("")
    report.append(f"Investigation ID : {investigation.id}")
    report.append(f"Title            : {investigation.title}")
    report.append(
        f"Generated        : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    report.append("")
    report.append("=" * 60)
    report.append("EXECUTIVE SUMMARY")
    report.append("=" * 60)

    report.append(
        "The uploaded authentication logs were analysed for "
        "security events. The investigation identified potential "
        "security findings requiring analyst review."
    )

    report.append("")
    report.append("=" * 60)
    report.append("INCIDENT FINDINGS")
    report.append("=" * 60)

    if not findings:

        report.append("No security findings detected.")

    else:

        for index, finding in enumerate(findings, start=1):

            report.append("")
            report.append(f"{index}. {finding.title}")
            report.append(f"Severity: {finding.severity}")
            report.append("")
            report.append("Description:")
            report.append(finding.description)

            report.append("")
            report.append("Impact:")
            report.append(finding.impact)

            report.append("")
            report.append("Recommendation:")
            report.append(finding.recommendation)

            report.append("")
            report.append("Response Action:")
            report.append(finding.response_action)

            report.append("")
            report.append("-" * 60)

    report.append("")
    report.append("=" * 60)
    report.append("INCIDENT RESPONSE WORKFLOW")
    report.append("=" * 60)

    report.append("1. Detection")
    report.append("2. Alert")
    report.append("3. Investigation")
    report.append("4. Response")
    report.append("5. Recovery")
    report.append("6. Closure")

    report.append("")
    report.append("=" * 60)
    report.append("GENERAL SECURITY RECOMMENDATIONS")
    report.append("=" * 60)

    report.append("- Enable Multi-Factor Authentication (MFA).")
    report.append("- Monitor repeated authentication failures.")
    report.append("- Restrict SSH access to trusted IP addresses.")
    report.append("- Review privileged account activity regularly.")
    report.append("- Maintain centralized logging and continuous monitoring.")

    report.append("")
    report.append("=" * 60)

    return "\n".join(report)