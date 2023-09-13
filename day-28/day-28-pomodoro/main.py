import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    start_button.config(state="normal")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = 1 * WORK_MIN
    short_break_sec = 1 * SHORT_BREAK_MIN
    long_break_sec = 2 * LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count: int):
    minutes = count // 60
    seconds = count % 60
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds:02d}")
        start_button.config(state="disabled")
    else:
        check_marks.config(text="✔" * (reps // 2))
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
image = tk.PhotoImage(file="./tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer Label
timer_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# Start Button
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Marks
check_marks = tk.Label(text="", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# Mainloop
window.mainloop()
