import re
import random

def check_password_strength(password, name=""):
    score = 0
    lower_name = name.lower()

    # --- Check if name used ---
    if lower_name and lower_name in password.lower():
        feedback = random.choice([
            "ഈ password-ന് ഒരു 'Easy Access' ബോർഡ് കൂടി വെച്ചോ da! 😂",
            "ഇത് bio ആണോ password ആണോ vro?",
            "എന്നാൽ പിന്നെ നിന്റെ ജാതകംകൂടി എടുത്തുകൊടുക്ക്! 🤦‍♂️"
        ])
        return "Weak", feedback


    name_pattern = re.match(r'^[A-Za-z]{3,}[0-9@$!%*?&^#_\-=]+$', password)
    if name_pattern:
        feedback = random.choice([
            "ഈ password-ന് ഒരു 'Easy Access' ബോർഡ് കൂടി വെച്ചോ da! 😂",
            "ഇത് bio ആണോ password ആണോ vro?",
            "എന്നാൽ പിന്നെ നിന്റെ ജാതകംകൂടി എടുത്തുകൊടുക്ക്! 🤦‍♂️"
        ])
        return "Weak", feedback

    # --- Overkill check (very long passwords) ---
    if len(password) >= 20:
        return "Overkill", "നീ ഇതൊക്കെ ഓർത്തിരിക്കുവോ vro...?"

    # --- Basic checks ---
    if len(password) >= 8: score += 1
    if len(password) >= 12: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[@$!%*?&^#_]", password): score += 1

    # --- Local slang feedback sets ---
    very_weak = [
        "ഇതൊക്കെ ഒരു password ആണോ vro...", 
        "അയ്യോ 😭, ഇതിട്ടാൽ login തന്നെ പേടിച്ചു പോകും!",
        "ഇതൊക്കെ കണ്ടാൽ എനിക്ക് തന്നെ നാണം ആവുന്നുണ്ട്, ഒന്ന് മാറ്റിക്കേ da!"
    ]
    weak = [
    "എടാ പൊട്ടാ, ഇതൊക്കെ അവന്മാർ തൂക്കും da!", 
    "കുറച്ചുകൂടി ശ്രെമിക്ക് vroo, നിന്നെക്കൊണ്ട് പറ്റും", 
    "Vroo, ഇത് കണ്ടാൽ ഹാക്കർമാർ ചായയും പരിപ്പുവടയും കഴിച്ചു ചിരിക്കും."
    ]
    medium = [
        "ആഹ്, ഇത് തരക്കേടില്ല",
        "ഇത് Bad അല്ല. പക്ഷേ, ഒരു 'Next level' ആക്കാൻ ഇനിയും പറ്റും vro!",
        "ഇതൊരു good start ആണ്! പക്ഷേ കുറച്ചുകൂടി power ആക്ക് !"
    ]
    strong = [
        "അമ്പട തക്കാളി 😎, നീ ഒരു കില്ലാഡി തന്നെ!",
        "ഇതൊരു ഒന്നൊന്നര password ആണ് vro! Respect!",
        "ഈ password സെറ്റാണ്. നീ ധൈര്യമായി ഉറങ്ങിക്കോ !"
    ]
    very_strong = [
        "vrooo... ഇതൊക്കെ കണ്ടുപിടിക്കുമ്പോളേക്ക് അവന്മാർ തട്ടിപോകും!",
        "ഇതു കിടുക്കി, തിമിർത്തു, കലക്കി!",
        "നിനക്കു ഒരു cybersecurity specialist ആയിക്കൂടെ!",
    ]

    # --- Strength rating ---
    if score <= 2:
        strength = "Very Weak"
        feedback = random.choice(very_weak)
    elif score == 3:
        strength = "Weak"
        feedback = random.choice(weak)
    elif score == 4:
        strength = "Medium"
        feedback = random.choice(medium)
    elif score == 5:
        strength = "Strong"
        feedback = random.choice(strong)
    else:
        strength = "Very Strong"
        feedback = random.choice(very_strong)

    return strength, feedback



if __name__ == "__main__":
    print("🛡️ Password Strength Checker - Ithokke oru password anoda..? 🛡️\n")
    name = input("പേര് (optional): ")
    password = input("പാസ്സ്‌വേർഡ് നൽകൂ: ")

    strength, feedback = check_password_strength(password, name)
    print(f"\n🔐 Password Strength: {strength}")
    print(f"💬 Feedback: {feedback}")
