# scoring.py
def compute_credit_score(f):
    score = 500

    if f["repay_ratio"] > 0.8:
        score += 200
    elif f["repay_ratio"] > 0.5:
        score += 100

    if f["liquidation_count"] == 0:
        score += 100
    elif f["liquidation_count"] > 2:
        score -= 150

    if f["borrow_to_deposit_ratio"] < 0.6:
        score += 100

    if f["deposit_frequency"] > 10:
        score += 50

    if f["unique_assets"] > 3:
        score += 50

    score = max(0, min(1000, int(score)))
    return score
