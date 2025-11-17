import re
import random

def check_password_strength(password, name=""):
    lower_name = name.lower()
    score = 0
    length = len(password)

    # --- Check if name used ---
    if lower_name and lower_name in password.lower():
        feedback = random.choice([
            "പേര് തന്നെ password ആക്കിയപോളേത്തോന്നി തലേൽ ഒന്നുമില്ലെന്ന്… 🤦‍♂️",
            "ഇത് bio ആണോ password ആണോ vro?",
            "എന്നാൽ പിന്നെ നിന്റെ ration card-ഉം, ജാതകം കൂടി എടുത്തുകൊടുക്ക്. 📜😒"
        ])
        return "Weak", feedback

    # --- Easy pattern check (name-like patterns) ---
    name_pattern = re.match(r'^[A-Za-z]{3,}[0-9@$!%*?&^#_\-=]+$', password)
    if name_pattern:
        feedback = random.choice([
            "ഈ password-ന് ഒരു “Easy Access” ബോർഡ് കൂടി വെച്ചോ da! 🚪😑",
            "പേര് തന്നെ password ആക്കിയപോളേത്തോന്നി തലേൽ ഒന്നുമില്ലെന്ന്… 🤦‍♂️",
            "ഇത് bio ആണോ password ആണോ vro?",
            "എന്നാൽ പിന്നെ നിന്റെ ration card-ഉം, ജാതകം കൂടി എടുത്തുകൊടുക്ക്. 📜😒"
        ])
        return "Weak", feedback

    # --- Very long password ---
    if length >= 20:
        return "Overkill", "നീ ഇതൊക്കെ ഓർത്തിരിക്കുവോ vro...?"

    # --- Character type checks ---
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[@$!%*?&^#_]", password))

    # --- Scoring ---
    if length >= 8: score += 2
    elif length >= 6: score += 1
    if length >= 12: score += 1
    if has_lower: score += 1
    if has_upper: score += 1
    if has_digit: score += 1
    if has_symbol: score += 1

    # --- Penalties ---
    # Sequential characters
    sequential = False
    for i in range(len(password) - 2):
        if password[i].isascii() and password[i+1].isascii() and password[i+2].isascii():
            if ord(password[i+1]) == ord(password[i]) + 1 and \
               ord(password[i+2]) == ord(password[i+1]) + 1:
                sequential = True
                break
    if sequential:
        score -= 2

    # Repeated chars
    if re.search(r'(.)\1{2,}', password):
        score -= 2

    # One type only
    types = sum([has_lower, has_upper, has_digit, has_symbol])
    if types == 1:
        score -= 2

    # --- Feedback ---
    very_weak = [
        "ഇതൊക്കെ ഒരു password ആണോ vro…? 🙄",
        "അയ്യോ 😭, ഇതിട്ടാൽ login തന്നെ പേടിച്ചു പോകും.",
        "ഇതൊക്കെ കണ്ടാൽ എനിക്ക് തന്നെ നാണം ആവുന്നുണ്ട്, ഒന്ന് മാറ്റിയേക്കണേ. 😓",
        "ഇതുപോലെ password-ന് security അല്ല കിട്ടാൻ പോകുന്നത്… sympathy ആണ്. 🥲",
        "Hacking പഠിക്കാൻ പോകുന്നവർക്ക് ഒരു demotivation ആണ് ഇതുപോലുള്ള weak password. 😭"
    ]

    weak = [
        "കുറേ കഷ്ടപ്പെട്ടെന്നു തോന്നുന്നു… പക്ഷെ കൊള്ളില്ല. 😐",
        "എടാ പൊട്ടാ, ഇതൊക്കെ അവന്മാർ തൂക്കും. 🤣",
        "കുറച്ചുകൂടി ശ്രെമിക്ക് vroo, നിന്നെക്കൊണ്ട് പറ്റും. 💪🙂",
        "നിന്നെ കാണാൻ കൊള്ളാലോ… പക്ഷെ ബുദ്ധി ഇല്ലാ, അല്ലേ? 😏"
    ]

    medium = [
        "ഇങ്ങനെയൊരു middle-class password… survive cheyyum, shine cheyyില്ലാ. 🫥",
        "ശരി, ഇതൊരു password ആണ്… പക്ഷെ ‘അടിപൊളി’ എന്നു പറയാൻ പറ്റില്ല. 😶",
        "ആഹ്, ഇത് തരക്കേടില്ല… കുറച്ചുകൂടി power ആക്ക്. 🔋🙂",
        "പാതി brain use ചെയ്‌തിട്ടുണ്ട്, ബാക്കി പാതി എപ്പോൾ use ചെയ്യും..? 🤔"
    ]

    strong = [
        "അമ്പട തക്കാളി 😎, നീ ഒരു കില്ലാഡി തന്നെ!",
        "ഇതൊരു ഒന്നൊന്നര password ആണ് vro! Respect!",
        "Password നല്ലത് ആണു… അതുപോലെ നിന്റെ ബാക്കി decisions ഉം ഇങ്ങനെ തന്നെ responsible ആയിരുന്നെങ്കിലോ…? 😌👉"
    ]

    very_strong = [
        "വളരെ ശക്തമായ password… occasional brilliance! 🧠✨",
        "You deserve all my respect. 🙇‍♂️🔥",
        "നിനക്കു cybersecurity specialist ആയിക്കൂടെ! 🛡️😎",
    ]

    # --- Rating ---
    if score <= 1:
        return "Very Weak", random.choice(very_weak)
    elif score <= 3:
        return "Weak", random.choice(weak)
    elif score <= 5:
        return "Medium", random.choice(medium)
    elif score <= 7:
        return "Strong", random.choice(strong)
    else:
        return "Very Strong", random.choice(very_strong)
