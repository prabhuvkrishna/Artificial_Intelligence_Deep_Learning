import tkinter as tk
from tkinter import ttk

# =========================
# Window Setup
# =========================
root = tk.Tk()
root.title("Recipe Remix Fiesta!")
root.geometry("1200x700")
root.configure(bg="#101c3b")

# =========================
# Header
# =========================
header = tk.Label(
    root,
    text="🍽️ Recipe Remix Fiesta! — Unusual Kitchen Adventures Await!",
    bg="#142144",
    fg="#ffeb59",
    font=("Segoe UI", 22, "bold"),
    pady=15
)
header.pack(fill="x")

# =========================
# Main Container
# =========================
container = tk.Frame(root, bg="#101c3b")
container.pack(fill="both", expand=True, padx=20, pady=20)

# =========================
# LEFT SIDE — FORM
# =========================
form_frame = tk.Frame(container, bg="#182a55", bd=3, relief="ridge")
form_frame.pack(side="left", fill="y", padx=20)

def create_label(text):
    return tk.Label(form_frame, text=text, bg="#182a55", fg="#ffd700",
                    font=("Segoe UI", 11, "bold"))

def create_entry():
    return tk.Entry(form_frame, bg="#25335b", fg="white",
                    insertbackground="white", width=35)

def create_text():
    return tk.Text(form_frame, height=3, bg="#25335b",
                   fg="white", insertbackground="white", width=35)

# Fields
create_label("Dish Name").pack(anchor="w", pady=(10,0))
dish_entry = create_entry()
dish_entry.pack(pady=5)

create_label("Ingredients").pack(anchor="w")
ingredients_text = create_text()
ingredients_text.pack(pady=5)

create_label("Equipment Used").pack(anchor="w")
equipment_entry = create_entry()
equipment_entry.pack(pady=5)

create_label("Instructions").pack(anchor="w")
instructions_text = create_text()
instructions_text.pack(pady=5)

create_label("Prep Time").pack(anchor="w")
preptime_entry = create_entry()
preptime_entry.pack(pady=5)

create_label("Number of Servings").pack(anchor="w")
servings_entry = create_entry()
servings_entry.pack(pady=5)

# =========================
# RIGHT SIDE — RECIPES
# =========================
recipes_frame = tk.Frame(container, bg="#101c3b")
recipes_frame.pack(side="right", fill="both", expand=True)

canvas = tk.Canvas(recipes_frame, bg="#101c3b", highlightthickness=0)
scrollbar = ttk.Scrollbar(recipes_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#101c3b")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# =========================
# Recipe Creation
# =========================
def create_recipe():
    dish = dish_entry.get().strip() or "Mystery Dish"
    ingredients = ingredients_text.get("1.0", tk.END).strip()
    equipment = equipment_entry.get().strip()
    instructions = instructions_text.get("1.0", tk.END).strip()
    preptime = preptime_entry.get().strip()
    servings = servings_entry.get().strip() or "1"

    card = tk.Frame(
        scrollable_frame,
        bg="#223c73",
        bd=5,
        relief="groove"
    )
    card.pack(fill="x", pady=15, padx=20)

    # Title
    tk.Label(
        card,
        text=f"✨ {dish}",
        bg="#223c73",
        fg="#ffd700",
        font=("Segoe UI", 14, "bold")
    ).pack(anchor="w", pady=5)

    def section(title, content):
        tk.Label(
            card,
            text=f"{title}: {content}",
            bg="#223c73",
            fg="white",
            wraplength=600,
            justify="left"
        ).pack(anchor="w", pady=3)

    section("Ingredients", ingredients)
    section("Equipment", equipment)
    section("Instructions", instructions)
    section("Prep Time", preptime)
    section("Serves", f"{servings} hungry {'soul' if servings=='1' else 'folks'}")

    tk.Label(
        card,
        text="--------------------------------------------",
        bg="#223c73",
        fg="#ffd700"
    ).pack(pady=5)

    chef_remark = (
        f"Chef’s Remark:\n"
        f"Ready your {equipment}, summon your inner chef, and let {dish} shine! "
        f"This dish, prepared in just {preptime}, will delight "
        f"{'a solitary gourmet' if servings=='1' else servings + ' eager diners'}!"
    )

    tk.Label(
        card,
        text=chef_remark,
        bg="#223c73",
        fg="#ffeb59",
        wraplength=600,
        justify="left",
        font=("Segoe UI", 10, "italic")
    ).pack(anchor="w", pady=5)

    # Clear form
    dish_entry.delete(0, tk.END)
    ingredients_text.delete("1.0", tk.END)
    equipment_entry.delete(0, tk.END)
    instructions_text.delete("1.0", tk.END)
    preptime_entry.delete(0, tk.END)
    servings_entry.delete(0, tk.END)

# Button
tk.Button(
    form_frame,
    text="Print Recipe 🍳",
    command=create_recipe,
    bg="#fc85a7",
    fg="#101c3b",
    font=("Segoe UI", 12, "bold"),
    pady=8
).pack(pady=20)

root.mainloop()
