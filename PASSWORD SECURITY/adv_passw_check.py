import re
import tkinter as tk
import os
import json
import random
import string
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

def check_strength(entry):
    password = entry.get()

    score = 0
    feedback = []

    # Counts
    total_counts = len(password)
    lowercase = len(re.findall(r"[a-z]", password))
    uppercase = len(re.findall(r"[A-Z]", password))
    digits    = len(re.findall(r"[0-9]", password))
    special   = len(re.findall(r"[^a-zA-Z0-9\s]", password))
    spaces    = len(re.findall(r"\s", password))
    letters   = lowercase + uppercase

    # Strength checks
    if len(password) >= 10:
        score += 2
    elif len(password) >= 7:
        score += 1
    else:
        feedback.append("Too short (use at least 7 characters)")

    if uppercase:
        score += 2
    else:
        feedback.append("No uppercase letters")

    if lowercase:
        score += 2
    else:
        feedback.append("No lowercase letters")

    if digits:
        score += 2
    else:
        feedback.append("No numbers")

    if special:
        score += 2
    else:
        feedback.append("No special characters")

    counts = {
        "total_counts": total_counts,
        "letters": letters,
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": special,
        "spaces": spaces
    }

    return score, feedback, counts


def response(score):
    if score <= 3:
        return "Absolutely terrible. Hackers are already inside."
    elif score <= 6:
        return "Weak. This wouldn’t survive a coffee break."
    elif score <= 8:
        return "Decent, but don’t get too confident."
    else:
        return "Strong password. Hackers aren't into you."


def on_button_click(entry, score_label, response_label, feedback_label, count_label):
    score, feedback, counts = check_strength(entry)

    score_label.config(text=f"Score: {score} / 10")
    response_label.config(text=response(score))

    if feedback:
        feedback_label.config(text="\n".join(f"- {f}" for f in feedback))
    else:
        feedback_label.config(text="No obvious weaknesses found.")

    count_label.config(
        text=(
            f"Total Chracters: {counts['total_counts']}\n"
            f"Letters: {counts['letters']}\n"
            f"  - Uppercase: {counts['uppercase']}\n"
            f"  - Lowercase: {counts['lowercase']}\n"
            f"Digits: {counts['digits']}\n"
            f"Special characters: {counts['special']}\n"
            f"Spaces: {counts['spaces']}"
        )
    )


def aes_encrypt(plaintext: str):
    key = get_random_bytes(32)   # AES-256
    iv = get_random_bytes(16)    # CBC IV

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    return {
        "cipher_text": base64.b64encode(ciphertext).decode(),
        "key_hint": base64.b64encode(key).decode(),  # stored for future use
        "iv": base64.b64encode(iv).decode()
    }

def random_folder_name(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def create_random_path(base="vault", depth=3):
    path = base
    os.makedirs(path, exist_ok=True)

    for _ in range(depth):
        candidates = []
        for _ in range(5):
            folder = random_folder_name()
            full = os.path.join(path, folder)
            os.makedirs(full, exist_ok=True)
            candidates.append(full)

        path = random.choice(candidates)

    return path

def save_password_encrypted(password, depth=5):
    encrypted = aes_encrypt(password)

    data = {
        "encryption_type": "AES",
        "mode": "CBC",
        "key_size_bits": 256,
        "padding": "PKCS7",
        "cipher_text": encrypted["cipher_text"],
        "iv": encrypted["iv"],
        "key_hint": encrypted["key_hint"],
        "note": "Decrypt using AES-256-CBC with stored IV and key"
    }

    final_dir = create_random_path(depth=depth)
    file_path = os.path.join(final_dir, "payload.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path



def main():
    root = tk.Tk()
    root.title("Advanced Password Checker")
    root.geometry("450x420")

    tk.Label(root, text="Advanced Password Checker",
             font=("Arial", 18, "bold")).pack(pady=10)

    password_entry = tk.Entry(root, show="*")
    password_entry.pack(pady=5)

    score_label = tk.Label(root, text="Score:")
    score_label.pack(pady=5)

    response_label = tk.Label(root, text="")
    response_label.pack(pady=5)

    feedback_label = tk.Label(root, text="", justify="left")
    feedback_label.pack(pady=5)

    count_label = tk.Label(root, text="", justify="left")
    count_label.pack(pady=5)

    tk.Button(
        root,
        text="Check Strength",
        command=lambda: on_button_click(
            password_entry,
            score_label,
            response_label,
            feedback_label,
            count_label
        )
    ).pack(pady=10)

    path = save_password_encrypted(
        password_entry.get(),
        depth=3
    )
    print("Encrypted password saved at:")
    print(path)

    root.mainloop()


if __name__ == "__main__":
    main()

