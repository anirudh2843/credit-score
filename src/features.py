# features.py
import numpy as np
import datetime

def extract_wallet_features(txs):
    deposits, borrows, repays, redeems, liquidations = [], [], [], [], []
    timestamps, assets = [], set()

    for tx in txs:
        action = tx['action']
        data = tx['actionData']
        amount = float(data.get('amount', 0)) / 1e18
        price = float(data.get('assetPriceUSD', 1))
        usd_val = amount * price
        assets.add(data.get("assetSymbol", ""))

        timestamps.append(tx['timestamp'])

        if action == 'deposit': deposits.append(usd_val)
        elif action == 'borrow': borrows.append(usd_val)
        elif action == 'repay': repays.append(usd_val)
        elif action == 'redeemunderlying': redeems.append(usd_val)
        elif action == 'liquidationcall': liquidations.append(1)

    timestamps = sorted(timestamps)
    avg_interval = np.mean(np.diff(timestamps)) if len(timestamps) > 1 else 0

    return {
        "total_deposit_usd": sum(deposits),
        "total_borrow_usd": sum(borrows),
        "total_repay_usd": sum(repays),
        "repay_ratio": sum(repays) / sum(borrows) if sum(borrows) > 0 else 0,
        "borrow_to_deposit_ratio": sum(borrows) / sum(deposits) if sum(deposits) > 0 else 0,
        "deposit_frequency": len(deposits),
        "liquidation_count": len(liquidations),
        "redeem_count": len(redeems),
        "unique_assets": len(assets),
        "avg_tx_interval": avg_interval
    }
