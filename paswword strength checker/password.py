# password strength checker
# project 1 - decodelabs internship

import tkinter as tk
import string

# colors i picked
bg_color = "#1e1e1e"
text_color = "white"


def check_password(password):
    # check if password is long enough first
    if len(password) < 8:
        return "WEAK", 0

    score = 0

    # check each condition
    has_upper = False
    has_lower = False
    has_num = False
    has_symbol = False

    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_num = True
        if c in string.punctuation:
            has_symbol = True

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_num:
        score += 1
    if has_symbol:
        score += 1

    # decide strength based on score
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score


def get_tips(password):
    tips = []

    if len(password) < 8:
        tips.append("- password too short, need at least 8 characters")
        return tips  # no point checking rest

    if len(password) < 12:
        tips.append("- try using 12 or more characters")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_num = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if not has_upper:
        tips.append("- add uppercase letters like A B C")
    if not has_lower:
        tips.append("- add lowercase letters")
    if not has_num:
        tips.append("- add some numbers")
    if not has_symbol:
        tips.append("- add symbols like ! @ # $")

    if len(tips) == 0:
        tips.append("- looks good! password is strong")

    return tips


def check_btn_clicked():
    pw = entry.get()

    if pw == "":
        result_label.config(text="please enter a password", fg="gray")
        score_label.config(text="")
        tips_label.config(text="")
        bar.config(width=0)
        return

    strength, score = check_password(pw)

    # update the strength label color
    if strength == "WEAK":
        color = "red"
    elif strength == "MEDIUM":
        color = "orange"
    else:
        color = "green"

    result_label.config(text="Strength: " + strength, fg=color)
    score_label.config(text="Score: " + str(score) + " / 6", fg="gray")

    # update bar width based on score
    bar_width = score * 60  # each point = 60px
    bar.config(width=bar_width, bg=color)

    # show tips
    tips = get_tips(pw)
    tips_text = "Tips:\n" + "\n".join(tips)
    tips_label.config(text=tips_text)


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        show_btn.config(text="hide")
    else:
        entry.config(show="*")
        show_btn.config(text="show")


# main window
window = tk.Tk()
window.title("Password Checker")
window.geometry("420x480")
window.config(bg=bg_color)
window.resizable(False, False)

# title
title = tk.Label(window, text="Password Strength Checker",
                 font=("Arial", 16, "bold"),
                 bg=bg_color, fg=text_color)
title.pack(pady=(20, 5))

subtitle = tk.Label(window, text="DecodeLabs - Project 1",
                    font=("Arial", 9),
                    bg=bg_color, fg="gray")
subtitle.pack()

# some space
tk.Label(window, bg=bg_color).pack(pady=5)

# password input area
tk.Label(window, text="Enter your password:",
         font=("Arial", 11),
         bg=bg_color, fg=text_color).pack(anchor="w", padx=30)

input_frame = tk.Frame(window, bg=bg_color)
input_frame.pack(padx=30, fill="x", pady=5)

entry = tk.Entry(input_frame, show="*", font=("Arial", 13),
                 bg="#2d2d2d", fg=text_color,
                 insertbackground="white",
                 relief="flat", bd=5)
entry.pack(side="left", fill="x", expand=True)

show_btn = tk.Button(input_frame, text="show",
                     font=("Arial", 9),
                     bg="#3a3a3a", fg="gray",
                     relief="flat", bd=0,
                     command=toggle_password,
                     cursor="hand2")
show_btn.pack(side="left", padx=(5, 0))

# check button
check_button = tk.Button(window, text="Check Password",
                         font=("Arial", 11, "bold"),
                         bg="#4f8ef7", fg="white",
                         relief="flat", bd=0,
                         padx=20, pady=8,
                         command=check_btn_clicked,
                         cursor="hand2")
check_button.pack(pady=15)

# strength bar background
tk.Label(window, text="Strength bar:", font=("Arial", 9),
         bg=bg_color, fg="gray").pack(anchor="w", padx=30)

bar_bg = tk.Frame(window, bg="#333333", height=12, width=360)
bar_bg.pack(padx=30, anchor="w")
bar_bg.pack_propagate(False)

bar = tk.Frame(bar_bg, bg="gray", height=12, width=0)
bar.pack(side="left")

# result
result_label = tk.Label(window, text="",
                        font=("Arial", 15, "bold"),
                        bg=bg_color, fg="white")
result_label.pack(pady=(15, 2))

score_label = tk.Label(window, text="",
                       font=("Arial", 10),
                       bg=bg_color, fg="gray")
score_label.pack()

# tips section
tips_label = tk.Label(window, text="",
                      font=("Arial", 10),
                      bg=bg_color, fg="#aaaaaa",
                      justify="left", anchor="w")
tips_label.pack(padx=30, pady=10, anchor="w")


window.mainloop()