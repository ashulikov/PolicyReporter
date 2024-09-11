import pytest
from assignment.assignment2 import FSM, Modulo3

@pytest.fixture
def fsm():
    return FSM([0, 1, 2], ["0", "1"], 0, [0, 1])

def test_initialization(fsm):
    assert fsm.get_current_state() == 0
    assert set(fsm.transitions.keys()) == {0, 1, 2}

def test_add_transition_with_existing_transition(fsm):
    fsm.add_transition(0, "0", 1)
    with pytest.raises(ValueError):
        fsm.add_transition(0, "0", 1)  # Overwriting existing transition

def test_add_transitions_with_empty_list(fsm):
    fsm.add_transitions([])  # No changes

def test_transition_with_multiple_transitions(fsm):
    fsm.add_transitions([[0, "0", 1], [1, "0", 2]])
    fsm.transition("0")
    fsm.transition("0")
    assert fsm.get_current_state() == 2

def test_finalize_with_non_final_state(fsm):
    fsm.add_transition(0, "0", 2)  # Add a non-final state
    fsm.transition("0")
    assert fsm.get_current_state() == 2
    with pytest.raises(Exception):
        fsm.finalize()

def test_get_current_state_after_invalid_transition(fsm):
    with pytest.raises(ValueError):
        fsm.transition("2")  # Invalid symbol
    assert fsm.get_current_state() == 0  # Current state remains unchanged

def test_add_transitions_with_invalid_transition(fsm):
    with pytest.raises(ValueError):
        fsm.add_transitions([[0, "0", 3]])  # Invalid state

def test_add_transitions_with_duplicate_transitions(fsm):
    with pytest.raises(ValueError):
        fsm.add_transitions([[0, "0", 1], [0, "0", 2]])  # Duplicate transition

def test_transition_with_empty_input(fsm):
    with pytest.raises(ValueError):
        fsm.transition("")  # Empty input

@pytest.fixture
def modulo3():
    return Modulo3()

def test_calc_with_empty_input(modulo3):
    with pytest.raises(Exception):
        modulo3.calc("")  # Empty input

def test_calc_with_invalid_character(modulo3):
    with pytest.raises(ValueError):
        modulo3.calc("012")  # Invalid character

def test_calc_with_large_numbers(modulo3):
    assert modulo3.calc("10000000000000000000000000000000000000000000000000") == 2