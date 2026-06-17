from logic_utils import (
    check_guess,
    get_range_for_difficulty,
    parse_guess,
    update_score,
)


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "Go HIGHER!"


def test_string_secret_still_allows_win():
    outcome, message = check_guess(42, "42")
    assert outcome == "Win"
    assert message == "Correct!"


def test_hard_range_is_larger_than_normal():
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    assert normal_low == hard_low
    assert hard_high > normal_high


def test_parse_guess_rejects_decimal_input():
    ok, value, error = parse_guess("42.5")

    assert ok is False
    assert value is None
    assert error == "Enter a whole number."


def test_score_does_not_increase_for_wrong_guess():
    assert update_score(0, "Too High", 1) == 0
    assert update_score(10, "Too Low", 2) == 5
