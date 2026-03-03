def format_rupees(x):
    return f"₹{x:,.0f}"

def main():
    try:
        annual_income = float(input("Annual Income (₹): ").strip())
    except ValueError:
        print("Invalid input. Enter a number.")
        return

    if annual_income < 0:
        print("Invalid input. Income cannot be negative.")
        return

    standard_deduction = 75000
    taxable_income = annual_income - standard_deduction
    if taxable_income < 0:
        taxable_income = 0

    slabs = [
        (0, 300000, 0.00),
        (300000, 700000, 0.05),
        (700000, 1000000, 0.10),
        (1000000, 1200000, 0.15),
        (1200000, 1500000, 0.20),
        (1500000, float("inf"), 0.30),
    ]

    print("\nTax regime: New Regime FY 2024-25")
    print("Standard Deduction:", format_rupees(standard_deduction))
    print("Taxable Income:", format_rupees(taxable_income))
    print("\nBreakdown:")

    total_tax = 0.0
    breakdown_rows = []

    for lower, upper, rate in slabs:
        if taxable_income <= lower:
            continue
        income_in_slab = min(taxable_income, upper) - lower
        tax_in_slab = income_in_slab * rate
        total_tax += tax_in_slab
        breakdown_rows.append((lower, upper, income_in_slab, rate, tax_in_slab))

    if not breakdown_rows:
        print("No tax payable (taxable income is within 0 percent slab).")
    else:
        for lower, upper, income_in_slab, rate, tax_in_slab in breakdown_rows:
            slab_end = "and above" if upper == float("inf") else format_rupees(upper)
            print(
                f"Slab {format_rupees(lower)} to {slab_end} | "
                f"Income: {format_rupees(income_in_slab)} | "
                f"Rate: {int(rate*100)}% | "
                f"Tax: {format_rupees(tax_in_slab)}"
            )

    print("\nTotal Tax:", format_rupees(total_tax))

    if annual_income > 0:
        effective_rate = (total_tax / annual_income) * 100
    else:
        effective_rate = 0.0

    print(f"Effective Tax Rate: {effective_rate:.2f}%")

    print("\nNote: This calculator applies slab wise tax and standard deduction. It does not add cess or surcharge unless your assignment asks for it.")

if __name__ == "__main__":
    main()