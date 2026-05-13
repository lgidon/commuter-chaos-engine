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
