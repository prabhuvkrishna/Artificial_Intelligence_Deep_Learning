import tkinter as tk
import random

# =========================
# Window Setup
# =========================
root = tk.Tk()
root.title("Table Tennis Game with Settings")

WIDTH = 900
HEIGHT = 600

root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="black")

# =========================
# Settings Variables
# =========================
difficulty = tk.StringVar(value="easy")
points_to_win = tk.IntVar(value=5)

AI_SPEEDS = {
    "easy": 3,
    "medium": 5,
    "hard": 8
}

PADDLE_SPEED = 7

# =========================
# Layout Frames
# =========================
top_frame = tk.Frame(root, bg="black")
top_frame.pack(pady=10)

game_frame = tk.Frame(root)
game_frame.pack()

score_label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 18))
score_label.pack(pady=10)

# =========================
# Difficulty Buttons
# =========================
tk.Label(top_frame, text="Difficulty:", fg="white", bg="black", font=("Arial", 14)).pack(side="left")

def set_difficulty(level):
    difficulty.set(level)
    reset_game()

for level in ["easy", "medium", "hard"]:
    tk.Button(
        top_frame,
        text=level.capitalize(),
        command=lambda l=level: set_difficulty(l),
        width=8
    ).pack(side="left", padx=5)

tk.Label(top_frame, text="Points to Win:", fg="white", bg="black", font=("Arial", 14)).pack(side="left", padx=10)

tk.Entry(top_frame, textvariable=points_to_win, width=5).pack(side="left")

# =========================
# Canvas
# =========================
canvas = tk.Canvas(game_frame, width=800, height=450, bg="#228B22")
canvas.pack()

# =========================
# Game Objects
# =========================
PADDLE_WIDTH = 12
PADDLE_HEIGHT = 80
BALL_SIZE = 20

player_score = 0
comp_score = 0
game_over = False

player = canvas.create_rectangle(30, 180, 30 + PADDLE_WIDTH, 180 + PADDLE_HEIGHT, fill="#f5deb3")
computer = canvas.create_rectangle(760, 180, 760 + PADDLE_WIDTH, 180 + PADDLE_HEIGHT, fill="#f5deb3")
ball = canvas.create_oval(390, 215, 390 + BALL_SIZE, 215 + BALL_SIZE, fill="white")

ball_vx = random.choice([-5, 5])
ball_vy = random.uniform(-4, 4)

up_pressed = False
down_pressed = False

# =========================
# Controls
# =========================
def key_press(event):
    global up_pressed, down_pressed
    if event.keysym == "Up":
        up_pressed = True
    if event.keysym == "Down":
        down_pressed = True

def key_release(event):
    global up_pressed, down_pressed
    if event.keysym == "Up":
        up_pressed = False
    if event.keysym == "Down":
        down_pressed = False

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

# =========================
# Game Functions
# =========================
def move_paddles():
    global up_pressed, down_pressed
    
    x1, y1, x2, y2 = canvas.coords(player)

    if up_pressed and y1 > 0:
        canvas.move(player, 0, -PADDLE_SPEED)
    if down_pressed and y2 < 450:
        canvas.move(player, 0, PADDLE_SPEED)

    # AI movement
    comp_x1, comp_y1, comp_x2, comp_y2 = canvas.coords(computer)
    ball_x1, ball_y1, ball_x2, ball_y2 = canvas.coords(ball)
    ball_center = (ball_y1 + ball_y2) / 2

    ai_speed = AI_SPEEDS[difficulty.get()]

    if ball_center < (comp_y1 + PADDLE_HEIGHT / 2):
        canvas.move(computer, 0, -ai_speed)
    elif ball_center > (comp_y1 + PADDLE_HEIGHT / 2):
        canvas.move(computer, 0, ai_speed)

def move_ball():
    global ball_vx, ball_vy, player_score, comp_score, game_over

    if game_over:
        return

    canvas.move(ball, ball_vx, ball_vy)
    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce top/bottom
    if y1 <= 0 or y2 >= 450:
        ball_vy *= -1

    # Paddle collision
    if check_collision(player):
        ball_vx = abs(ball_vx) * 1.05
    if check_collision(computer):
        ball_vx = -abs(ball_vx) * 1.05

    # Score
    if x1 <= 0:
        comp_score += 1
        check_game_over()
        reset_ball()

    if x2 >= 800:
        player_score += 1
        check_game_over()
        reset_ball()

def check_collision(paddle):
    px1, py1, px2, py2 = canvas.coords(paddle)
    bx1, by1, bx2, by2 = canvas.coords(ball)

    return bx1 < px2 and bx2 > px1 and by1 < py2 and by2 > py1

def reset_ball():
    global ball_vx, ball_vy
    canvas.coords(ball, 390, 215, 390 + BALL_SIZE, 215 + BALL_SIZE)
    ball_vx = random.choice([-5, 5])
    ball_vy = random.uniform(-4, 4)

def check_game_over():
    global game_over
    if player_score >= points_to_win.get():
        game_over = True
        show_winner("You Win! 🚀")
    elif comp_score >= points_to_win.get():
        game_over = True
        show_winner("Computer Wins!")

def show_winner(text):
    canvas.create_text(400, 225, text=text, fill="white", font=("Arial", 32, "bold"))

def update_score():
    score_label.config(
        text=f"Player: {player_score}  |  Computer: {comp_score}  |  First to {points_to_win.get()} wins"
    )

def reset_game():
    global player_score, comp_score, game_over
    player_score = 0
    comp_score = 0
    game_over = False
    canvas.delete("all")
    recreate_objects()

def recreate_objects():
    global player, computer, ball
    player = canvas.create_rectangle(30, 180, 42, 260, fill="#f5deb3")
    computer = canvas.create_rectangle(760, 180, 772, 260, fill="#f5deb3")
    ball = canvas.create_oval(390, 215, 410, 235, fill="white")

# =========================
# Game Loop
# =========================
def game_loop():
    move_paddles()
    move_ball()
    update_score()
    root.after(16, game_loop)

game_loop()
root.mainloop()


