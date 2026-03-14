from logic_utils import check_guess, update_score
# FIX: Updated import to use refactored check_guess from logic_utils.py.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    # FIX: Updated to unpack tuple (outcome, message) since check_guess now returns both, fixed via Copilot test debugging.
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    # FIX: Updated to unpack tuple.
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    # FIX: Updated to unpack tuple.
    assert outcome == "Too Low"

def test_update_score_win():
    # Test the corrected win points formula: 100 - 10*(attempt_number - 1)
    # FIX: Added test to verify fixed win scoring formula, ensuring 100 points for 1st attempt win, targeting the original bug.
    assert update_score(0, "Win", 1) == 100  # 1st attempt: 100 - 0 = 100
    assert update_score(0, "Win", 2) == 90   # 2nd attempt: 100 - 10 = 90
    assert update_score(0, "Win", 3) == 80   # 3rd attempt: 100 - 20 = 80
