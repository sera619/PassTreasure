import re

def evaluate_password_strength(password: str) -> int:
    """
    Returns password strength from 0 to 5.
    """

    score = 0

    # Length
    if len(password) >= 6:
        score += 1
    if len(password) >= 10:
        score += 1

    # Contains lowercase + uppercase
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1

    # Contains digits
    if re.search(r"\d", password):
        score += 1

    # Contains symbols
    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1

    return min(score, 5)
