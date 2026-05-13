from app.sniffer import calculate_chaos_score


def test_chaos_score_calculation():
    # Scenario: One line is fine, one has minor delays
    mock_data = [
        {
            "name": "District",
            "lineStatuses": [{"statusSeverityDescription": "Good Service"}],
        },
        {
            "name": "Central",
            "lineStatuses": [{"statusSeverityDescription": "Minor Delays"}],
        },
    ]
    assert calculate_chaos_score(mock_data) == 5


def test_chaos_score_severe():
    # Scenario: A major disruption
    mock_data = [
        {
            "name": "Jubilee",
            "lineStatuses": [{"statusSeverityDescription": "Suspended"}],
        }
    ]
    assert calculate_chaos_score(mock_data) == 20


def test_chaos_score_empty():
    assert calculate_chaos_score([]) == 0
    assert calculate_chaos_score(None) == 0
