# main.py
import json
from src.features import extract_wallet_features
from src.scoring import compute_credit_score
import pandas as pd

# Load JSON
with open("data/user_transactions.json") as f:
    txs = json.load(f)

# Group by wallet
from collections import defaultdict
wallet_data = defaultdict(list)
for tx in txs:
    wallet_data[tx["userWallet"]].append(tx)

# Extract features and score
wallet_scores = []
for wallet, txs in wallet_data.items():
    features = extract_wallet_features(txs)
    score = compute_credit_score(features)
    wallet_scores.append({
        "wallet": wallet,
        **features,
        "score": score
    })

# Save result
df = pd.DataFrame(wallet_scores)
df.to_csv("score_output.csv", index=False)
