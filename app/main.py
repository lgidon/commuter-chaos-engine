import time

import requests

TFL_API_URL = "https://api.tfl.gov.uk/Line/mode/tube/Status"


def fetch_tube_status():
    response = requests.get(TFL_API_URL)
    if response.status_code == 200:
        data = response.json()
        for line in data:
            name = line["name"]
            status = line["lineStatuses"][0]["statusSeverityDescription"]
            print(f"Line: {name} | Status: {status}")
    else:
        print(f"Error fetching data: {response.status_code}")


if __name__ == "__main__":
    while True:
        fetch_tube_status()
        time.sleep(60)  # Poll every minute
