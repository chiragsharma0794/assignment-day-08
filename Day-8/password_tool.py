import random
import string


SPECIAL_SET = set("!@#$%^&*")


def analyze_password(pw: str) -> dict:
    score = 0
    missing = []

    length = len(pw)
    length_points = 0
    if length >= 16:
        length_points = 3
    elif length >= 12:
        length_points = 2
    elif length >= 8:
        length_points = 1
    score += length_points

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    no_repeat_more_than_two = True
    run_count = 1
    prev = ""

    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        if ch in SPECIAL_SET:
            has_special = True

        if ch == prev:
            run_count += 1
            if run_count > 2:
                no_repeat_more_than_two = False
        else:
            prev = ch
            run_count = 1

    if has_upper:
        score += 1
    else:
        missing.append("uppercase")

    if has_lower:
        score += 1
    else:
        missing.append("lowercase")

    if has_digit:
        score += 1
    else:
        missing.append("digit")

    if has_special:
        score += 1
    else:
        missing.append("special char from !@#$%^&*")

    if no_repeat_more_than_two:
        score += 1
    else:
        missing.append("repeated char more than 2 in a row")

    if length < 8:
        missing.append("too short, minimum 8")

    rating = get_rating(score)

    return {
        "score": score,
        "rating": rating,
        "missing": missing,
        "length": length,
    }


def get_rating(score: int) -> str:
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    if score <= 6:
        return "Strong"
    return "Very Strong"


def generate_password(length: int) -> str:
    if length <= 0:
        return ""
    pool = string.ascii_letters + string.digits + string.punctuation
    out = []
    for _ in range(length):
        out.append(random.choice(pool))
    return "".join(out)


def print_analysis(pw: str) -> int:
    result = analyze_password(pw)
    score = result["score"]
    rating = result["rating"]
    missing = result["missing"]

    print(f">> Strength: {score}/7 ({rating})")
    if missing:
        print(">> Missing:", ", ".join(missing))
    else:
        print(">> Missing: none")
    return score


def main() -> None:
    print("Password Strength Analyzer")
    print("Scoring out of 7. Minimum accepted is 5.")

    while True:
        pw = input("Enter password: ")
        score = print_analysis(pw)
        if score >= 5:
            print(">> Password accepted!")
            break
        print(">> Try again...")

    print()
    print("Password Generator")
    while True:
        raw = input("Enter length to generate: ").strip()
        if raw.isdigit():
            length = int(raw)
            break
        print("Please enter a valid positive integer length.")

    gen_pw = generate_password(length)
    print("Generated password:", gen_pw)
    print_analysis(gen_pw)


if __name__ == "__main__":
    main()