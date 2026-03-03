def validate_inputs(entrance_score, gpa, has_recommendation, category, extracurricular_score):
    errors = []
    if not (0 <= entrance_score <= 100):
        errors.append("Entrance score must be between 0 and 100.")
    if not (0 <= gpa <= 10):
        errors.append("GPA must be between 0 and 10.")
    if has_recommendation not in ("yes", "no"):
        errors.append("Recommendation must be yes or no.")
    if category not in ("general", "obc", "sc_st"):
        errors.append("Category must be general, obc, or sc_st.")
    if not (0 <= extracurricular_score <= 10):
        errors.append("Extracurricular score must be between 0 and 10.")
    return errors

def category_cutoff(category):
    return {"general": 75, "obc": 65, "sc_st": 55}[category]

def decide(entrance_score, gpa, has_recommendation, category, extracurricular_score):
    errors = validate_inputs(entrance_score, gpa, has_recommendation, category, extracurricular_score)
    if errors:
        return "INVALID INPUT", " | ".join(errors), None, None

    if entrance_score >= 95:
        return "ADMITTED (Scholarship)", "Merit rule applied: entrance score is 95 or more.", entrance_score, "No bonus applied"

    bonus_parts = []
    bonus = 0
    if has_recommendation == "yes":
        bonus += 5
        bonus_parts.append("+5 (recommendation)")
    if extracurricular_score > 8:
        bonus += 3
        bonus_parts.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus
    bonus_text = " + ".join(bonus_parts) if bonus_parts else "No bonus applied"

    if gpa < 7.0:
        return "REJECTED", f"GPA below requirement: {gpa} < 7.0", effective_score, bonus_text

    cutoff = category_cutoff(category)

    if effective_score >= cutoff:
        return "ADMITTED (Regular)", f"Meets {category} cutoff ({effective_score} >= {cutoff}) and GPA requirement ({gpa} >= 7.0)", effective_score, bonus_text

    if cutoff - 5 <= effective_score < cutoff:
        return "WAITLISTED", f"Close to {category} cutoff: {effective_score} is below {cutoff} by {cutoff - effective_score} points", effective_score, bonus_text

    return "REJECTED", f"Below {category} cutoff: {effective_score} < {cutoff}", effective_score, bonus_text

def main():
    entrance_score = float(input("Entrance Score: ").strip())
    gpa = float(input("GPA: ").strip())
    has_recommendation = input("Recommendation (yes/no): ").strip().lower()
    category = input("Category (general/obc/sc_st): ").strip().lower()
    extracurricular_score = float(input("Extracurricular Score: ").strip())

    result, reason, effective_score, bonus_text = decide(
        entrance_score, gpa, has_recommendation, category, extracurricular_score
    )

    if effective_score is not None:
        print(f"Bonus Applied: {bonus_text}")
        print(f"Effective Score: {effective_score}")

    print("\nResult:")
    print(result)
    print("Reason:", reason)

if __name__ == "__main__":
    main()