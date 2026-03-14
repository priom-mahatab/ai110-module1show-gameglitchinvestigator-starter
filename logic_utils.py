def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # FIX: Refactored from app.py and updated Hard range to 1-1000 for better difficulty scaling, using Copilot to identify and implement.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 1000
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # FIX: Refactored from app.py without changes, as it was functional.
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # FIX: Fixed swapped hint messages and emojis, removed buggy TypeError handling for string comparisons, using Copilot to debug and correct logic.
    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Too high! Try a lower number."
    else:
        return "Too Low", "📈 Too low! Try a higher number."


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # FIX: Corrected win points formula to 100 - 10*(attempt_number-1) for fairer scoring, keeping glitchy wrong-guess logic as intentional, via Copilot analysis.
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)  # fix: attempt_number starts from 1
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
