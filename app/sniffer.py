import requests


def get_chaos_data(url="https://api.tfl.gov.uk/Line/mode/tube/Status"):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def calculate_simple_score(data):
    """Returns total number of lines not in 'Good Service'"""
    if not data:
        return 0

    bad_lines = [
        line
        for line in data
        if line["lineStatuses"][0]["statusSeverityDescription"] != "Good Service"
    ]
    return len(bad_lines)


def fetch_transport_data(url="https://api.tfl.gov.uk/Line/mode/tube/Status"):
    """Fetches raw status data from TfL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def calculate_chaos_score(data):
    """
    Analyzes the data and returns a 'Chaos Score'.
    Good Service = 0 points
    Minor Delays = 5 points
    Severe Delays/Suspended = 20 points
    """
    if not data:
        return 0

    total_score = 0
    for line in data:
        # Navigate the TfL JSON structure
        status = line.get("lineStatuses", [{}])[0].get(
            "statusSeverityDescription", "Unknown"
        )

        if status == "Minor Delays":
            total_score += 5
        elif status in ["Severe Delays", "Part Suspended", "Suspended"]:
            total_score += 20

    return total_score
