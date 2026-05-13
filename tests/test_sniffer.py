import pytest
from app.sniffer import calculate_simple_score

def test_calculate_score_logic():
    # Mock data: 1 Good line, 1 Delayed line
    mock_data = [
        {'name': 'Central', 'lineStatuses': [{'statusSeverityDescription': 'Good Service'}]},
        {'name': 'Victoria', 'lineStatuses': [{'statusSeverityDescription': 'Minor Delays'}]}
    ]
    score = calculate_simple_score(mock_data)
    assert score == 1

def test_calculate_score_empty():
    assert calculate_simple_score([]) == 0
