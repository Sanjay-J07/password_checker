import re

print("=== Advanced Password Strength Checker ===\n")

while True:
    password = input("Enter your password (or type 'exit' to quit): ")

    if password.lower() == "exit":
        print("👋 Exiting program...")
        break

    score = 0

    # Conditions
    length = len(password) >= 8
    lower = re.search("[a-z]", password)
    upper = re.search("[A-Z]", password)
    digit = re.search("[0-9]", password)
    special = re.search("[!@#$%^&*(),.?\":{}|<>]", password)

    # Scoring
    if length:
        score += 1
    if lower:
        score += 1
    if upper:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    print("\n🔍 Password Analysis:")

    # Strength Level
    if score == 5:
        print("✅ Strength: Strong Password")
    elif score >= 3:
        print("⚠️ Strength: Medium Password")
    else:
        print("❌ Strength: Weak Password")

    # Suggestions
    print("\n📌 Suggestions to improve:")
    
    if not length:
        print("- Use at least 8 characters")
    if not lower:
        print("- Add lowercase letters")
    if not upper:
        print("- Add uppercase letters")
    if not digit:
        print("- Include numbers")
    if not special:
        print("- Add special characters")

    if score == 5:
        print("🎉 Your password is secure!")

    print("\n" + "-"*40)