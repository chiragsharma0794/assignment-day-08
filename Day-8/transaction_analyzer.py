from typing import Dict, List, Tuple


def read_transaction() -> Tuple[float, str, str]:
    raw_amount = input("Amount: ").strip()
    amount = float(raw_amount)

    ttype = input("Type credit or debit: ").strip().lower()
    if ttype not in {"credit", "debit"}:
        raise ValueError("Type must be credit or debit.")

    category = input("Category food, travel, bills, other: ").strip().lower()
    if category not in {"food", "travel", "bills", "other"}:
        category = "other"

    return amount, ttype, category


def bar_for_amount(amount: float) -> str:
    stars = int(amount // 1000)
    if stars <= 0:
        stars = 1
    out = []
    for _ in range(stars):
        out.append("*")
    return "".join(out)


def main() -> None:
    transactions: List[Dict[str, object]] = []

    print("Enter transactions. Type done to finish.")
    while True:
        cmd = input("Add transaction or done: ").strip().lower()
        if cmd == "done":
            break

        try:
            amount, ttype, category = read_transaction()
        except Exception as e:
            print("Invalid input:", e)
            continue

        high_value = amount > 10000
        if high_value:
            print("High value transaction flagged.")

        transactions.append(
            {"amount": amount, "type": ttype, "category": category, "high_value": high_value}
        )

    total_credits = 0.0
    total_debits = 0.0
    highest = 0.0
    total_amount = 0.0

    spending_by_category: Dict[str, float] = {"food": 0.0, "travel": 0.0, "bills": 0.0, "other": 0.0}

    for tx in transactions:
        amount = float(tx["amount"])
        ttype = str(tx["type"])
        category = str(tx["category"])

        total_amount += amount
        if amount > highest:
            highest = amount

        if ttype == "credit":
            total_credits += amount
        else:
            total_debits += amount
            spending_by_category[category] += amount

    net_balance = total_credits - total_debits
    count = len(transactions)
    avg = (total_amount / count) if count > 0 else 0.0

    print()
    print("Bar chart for last 10 transactions. One star per 1000.")
    last_ten = transactions[-10:]
    for tx in last_ten:
        amount = float(tx["amount"])
        ttype = str(tx["type"])
        flag = " HIGH" if bool(tx["high_value"]) else ""
        print(f"{ttype} {amount:.2f} {bar_for_amount(amount)}{flag}")

    print()
    print("Summary")
    print("Total transactions:", count)
    print("Total credits:", f"{total_credits:.2f}")
    print("Total debits:", f"{total_debits:.2f}")
    print("Net balance:", f"{net_balance:.2f}")
    print("Highest transaction:", f"{highest:.2f}")
    print("Average amount:", f"{avg:.2f}")

    print()
    print("Spending breakdown by category for debits")
    for cat, amt in spending_by_category.items():
        print(cat, f"{amt:.2f}")


if __name__ == "__main__":
    main()