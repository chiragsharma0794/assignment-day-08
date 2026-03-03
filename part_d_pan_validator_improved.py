def main():
    pan = input("Enter PAN: ").strip()

    if len(pan) != 10:
        print("INVALID")
        print("Reason: PAN must be exactly 10 characters.")
        return

    first5 = pan[0:5]
    mid4 = pan[5:9]
    last1 = pan[9]
    taxpayer_code = pan[3]

    if not first5.isalpha():
        print("INVALID")
        print("Reason: First 5 characters must be letters.")
        return
    if first5 != first5.upper():
        print("INVALID")
        print("Reason: First 5 letters must be uppercase.")
        return
    if not mid4.isdigit():
        print("INVALID")
        print("Reason: Characters 6 to 9 must be digits.")
        return
    if not last1.isalpha() or last1 != last1.upper():
        print("INVALID")
        print("Reason: Last character must be an uppercase letter.")
        return

    taxpayer_types = {
        "P": "Person or Individual",
        "C": "Company",
        "H": "HUF",
        "F": "Firm",
        "A": "Association of Persons",
        "T": "Trust",
        "B": "Body of Individuals",
        "L": "Local Authority",
        "J": "Artificial Juridical Person",
        "G": "Government",
    }

    if taxpayer_code not in taxpayer_types:
        print("INVALID")
        print("Reason: 4th character is not a valid taxpayer type code.")
        return

    print("VALID")
    print("Taxpayer Type:", taxpayer_types[taxpayer_code])
    print("Type Code:", taxpayer_code)

if __name__ == "__main__":
    main()