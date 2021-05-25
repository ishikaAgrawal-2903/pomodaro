from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if rep == 8:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif rep % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global rep
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark = ""
        for _ in range(math.floor(rep / 2)):
            checkmark += "✔"
        checkmark_label.config(text=checkmark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodaro")
window.config(padx=80, pady=80, bg=YELLOW)

timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14))
checkmark_label.grid(column=1, row=3)
window.mainloop()
