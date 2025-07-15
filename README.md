# DeFi Wallet Credit Scoring (Aave V2)

This project develops a machine learning pipeline to assign **credit scores (0–1000)** to wallets interacting with the **Aave V2 protocol on Polygon**.  
The goal is to identify trustworthy, responsible DeFi users and detect risky, bot-like, or exploitative behavior — using only on-chain transaction data.

---

## 📁 Project Structure
credit-score/
├── data/
│ └── user_transactions.json # Input JSON transaction data
├── score_output.csv # Final wallet scores
├── plots/
│ └── score_distribution.png # Score histogram
├── src/
│ ├── features.py # Feature engineering functions
│ └── scoring.py # Rule-based scoring logic
├── main.py # Entry point: full pipeline
├── view_scores.py # Preview score_output.csv
├── plot_distribution.py # Generate histogram
├── requirements.txt # All dependencies
├── README.md # This file
└── analysis.md # Score distribution analysis

## 🔍 Problem Statement

Given raw DeFi transaction-level data from Aave V2, assign each wallet a **credit score from 0 to 1000** based on historical behaviors such as:

- Deposits
- Borrows
- Repayments
- Redemptions
- Liquidations

### 🎯 Objective

- Encourage responsible DeFi behavior
- Detect malicious, bot-like, or Sybil behavior
- Provide an on-chain signal for creditworthiness

---

## ⚙️ Features Engineered

| Feature | Description |
|--------|-------------|
| `total_deposit_usd` | Total deposit amount in USD |
| `total_borrow_usd` | Total borrow amount |
| `total_repay_usd` | Amount repaid |
| `repay_ratio` | Repay / Borrow ratio |
| `borrow_to_deposit_ratio` | Risk measure |
| `deposit_frequency` | Number of deposit actions |
| `liquidation_count` | Times wallet was liquidated |
| `redeem_count` | Number of redemptions |
| `unique_assets` | Asset diversity |
| `avg_tx_interval` | Time between transactions |

---

## 🧠 Scoring Logic (Rule-Based Model)

Each wallet is scored based on a combination of risk and reliability indicators:

- ✅ High **repay ratio** (>80%) → +200
- ✅ Low **borrow-to-deposit ratio** → +100
- ✅ No **liquidations** → +100
- ✅ Higher **deposit frequency** & **asset diversity** → +50
- 🚫 Frequent liquidations or no repays → heavy penalties
- ✅ Score is scaled to a range between **0–1000**

This logic ensures reliable users (who borrow responsibly and repay) are rewarded with high scores, while risky/bot wallets score low.


## ▶️ How to Run

1. **Install dependencies**  
```bash
pip install -r requirements.txt

2. **Run scoring pipeline**

python main.py

3. **Preview results**
python view_scores.py

4. **Generate score histogram**
python plot_distribution.py
