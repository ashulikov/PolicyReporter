import pytest
from assignment.assignment1 import findBestConfidenceScore

# Test cases
def test_empty_input():
    input = {}
    result = findBestConfidenceScore(input)
    assert result is None

def test_single_threshold_with_high_recall():
    input = {0.5: [10, 3, 2, 20]}
    result = findBestConfidenceScore(input)
    assert result == 0.5

def test_multiple_thresholds_with_best_recall_above_09():
    input = {
        0.3: [10, 2, 2, 20],
        0.5: [8, 4, 4, 18],
        0.7: [6, 6, 6, 16]
    }
    result = findBestConfidenceScore(input)
    assert result == 0.3

def test_multiple_thresholds_with_best_recall_below_09():
    input = {
        0.3: [10, 2, 10, 13],
        0.5: [8, 4, 5, 18],
        0.7: [6, 6, 7, 16],
        0.9: [4, 8, 9, 14]
    }
    result = findBestConfidenceScore(input)
    assert result is None

def test_tie_case():
    input = {
        0.3: [10, 3, 2, 20],
        0.5: [8, 5, 2, 20], # Same recall as 0.3
        0.7: [6, 6, 7, 16],
        0.9: [4, 8, 9, 14] 
    }
    result = findBestConfidenceScore(input) # The function should return any of the thresholds with the best metric
    assert result in [0.3, 0.5]

def test_negative_thresholds():
    input = {-0.2: [10, 3, 2, 20]}
    with pytest.raises(ValueError):
        findBestConfidenceScore(input)

def test_threshold_greater_than_1():
    input = {1.2: [10, 3, 2, 20]}
    with pytest.raises(ValueError):
        findBestConfidenceScore(input)

def test_non_integer_values():
    input = {0.5: [10.5, 3.3, 2.1, 20.4]}
    with pytest.raises(TypeError):
        findBestConfidenceScore(input)

def test_invalid_metric():
    input = {0.5: [10, 3, 2, 20]}
    with pytest.raises(ValueError):
        findBestConfidenceScore(input, best="invalid_metric")

def test_invalid_matrix():
    input = {0.5: [10, 3, 2, 20, 22]}
    with pytest.raises(ValueError):
        findBestConfidenceScore(input)
        
def test_invalid_threshold():
    input = {"half": [10, 3, 2, 20]}
    with pytest.raises(ValueError):
        findBestConfidenceScore(input)

if __name__ == "__main__":
    pytest.main()