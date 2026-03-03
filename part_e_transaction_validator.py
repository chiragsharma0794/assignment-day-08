def main():
    try:
        amount = float(input("Transaction amount (Rs): ").strip())
        category = input("Category (food/travel/electronics/other): ").strip().lower()
        hour = int(input("Hour of transaction (0-23): ").strip())
        daily_spent = float(input("Amount already spent today (Rs): ").strip())
        vip = input("VIP customer (yes/no): ").strip().lower()
    except ValueError:
        print("BLOCKED: invalid numeric input")
        return

    if amount <= 0:
        print("BLOCKED: amount must be positive")
        return
    if hour < 0 or hour > 23:
        print("BLOCKED: hour must be between 0 and 23")
        return
    if daily_spent < 0:
        print("BLOCKED: daily_spent_so_far cannot be negative")
        return
    if category not in ("food", "travel", "electronics", "other"):
        print("BLOCKED: invalid category")
        return
    if vip not in ("yes", "no"):
        print("BLOCKED: VIP must be yes or no")
        return

    multiplier = 2 if vip == "yes" else 1

    single_txn_limit = 50000 * multiplier
    daily_limit = 100000 * multiplier
    food_limit = 5000 * multiplier
    electronics_limit = 30000 * multiplier

    if amount > single_txn_limit:
        print("BLOCKED: exceeds single transaction limit")
        return

    if daily_spent + amount > daily_limit:
        print("BLOCKED: exceeds daily spending limit")
        return

    if category == "food" and amount >= food_limit:
        print("BLOCKED: exceeds food category limit")
        return

    if category == "electronics" and amount >= electronics_limit:
        print("BLOCKED: exceeds electronics category limit")
        return

    if hour < 6 or hour >= 23:
    print("FLAGGED: unusual transaction time")
    	return

    print("APPROVED")

if __name__ == "__main__":
    main()