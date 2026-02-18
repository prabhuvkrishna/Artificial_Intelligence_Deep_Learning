import tkinter as tk
from tkinter import ttk
import random

# Create main window
root = tk.Tk()
root.title("🎂✨ The Super Silly Birthday Card Machine ✨🎂")
root.configure(bg="red")
root.geometry("1000x600")

# Main Title
title = tk.Label(
    root,
    text="🎉 Ultimate Birthday Card Generator 🎉",
    font=("Arial", 28, "bold"),
    bg="red",
    fg="blue"
)
title.pack(pady=20)

# Create main container frame
container = tk.Frame(root, bg="red")
container.pack(fill="both", expand=True, padx=20)

# Left side (Form)
form_frame = tk.Frame(container, bg="red")
form_frame.pack(side="left", fill="y", padx=20)

# Right side (Cards display)
cards_frame = tk.Frame(container, bg="red")
cards_frame.pack(side="right", fill="both", expand=True)

# Scrollable canvas for cards
canvas = tk.Canvas(cards_frame, bg="red", highlightthickness=0)
scrollbar = ttk.Scrollbar(cards_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="red")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Form fields
tk.Label(form_frame, text="Name:", bg="red", fg="blue", font=("Arial", 14)).pack()
name_entry = tk.Entry(form_frame, font=("Arial", 14))
name_entry.pack(pady=10)

tk.Label(form_frame, text="Age:", bg="red", fg="blue", font=("Arial", 14)).pack()
age_entry = tk.Entry(form_frame, font=("Arial", 14))
age_entry.pack(pady=10)

tk.Label(form_frame, text="Hobby:", bg="red", fg="blue", font=("Arial", 14)).pack()
hobby_entry = tk.Entry(form_frame, font=("Arial", 14))
hobby_entry.pack(pady=10)

def generate_funny_message(name, age, hobby):
    jokes = [
        f"Wow {name}, you're {age} already? At this rate, you'll be vintage soon! Keep rocking that {hobby} like a legend!",
        f"{age} years old and still obsessed with {hobby}? Respect. Never grow up, {name}!",
        f"Congratulations {name}! You're now level {age}! Unlocking new skills in {hobby} and dad jokes!",
        f"{name}, at {age}, you're not old — you're just a classic edition! Especially when doing {hobby}!",
        f"They say age is just a number, {name}. But {age}? That's a BIG number! Celebrate with lots of {hobby}!"
    ]
    return random.choice(jokes)

def create_card():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()

    if not name or not age or not hobby:
        return

    message = generate_funny_message(name, age, hobby)

    # Create card frame
    card = tk.Frame(
        scrollable_frame,
        bg="pink",
        bd=4,
        relief="ridge"
    )
    card.pack(fill="x", pady=10, padx=10)

    header = tk.Label(
        card,
        text=f"🎈 Happy Birthday {name}! 🎈",
        font=("Arial", 16, "bold"),
        bg="pink",
        fg="blue"
    )
    header.pack(pady=5)

    divider = tk.Frame(card, height=2, bg="blue")
    divider.pack(fill="x", padx=10, pady=5)

    inside = tk.Label(
        card,
        text=message,
        font=("Arial", 12, "italic"),
        bg="pink",
        fg="blue",
        wraplength=400,
        justify="left"
    )
    inside.pack(padx=10, pady=10)

    # Clear fields after generating
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    hobby_entry.delete(0, tk.END)

generate_button = tk.Button(
    form_frame,
    text="Generate Birthday Magic 🎉",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="blue",
    command=create_card
)
generate_button.pack(pady=20)

root.mainloop()
