from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TEXT = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def stop_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    label_check["text"] = ""
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer["text"] = "Long Break"
        label_timer["fg"] = GREEN
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer["text"] = "Short Break"
        label_timer["fg"] = PINK
    else:
        count_down(work_sec)
        label_timer["text"] = "Work"
        label_timer["fg"] = RED

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = int(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    elif reps % 2 != 0:
        label_check["text"] += TEXT
        start_timer()
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study help tool")
window.config(pady=50, padx=90, bg=YELLOW)

canvas = Canvas(height=230, width=250, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(124, 112, image=photo) # puting a photo in we need a photo from PhotoImage
timer_text = canvas.create_text(124, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

button_start = Button(text="Start", font=(FONT_NAME, 12), width=5, highlightthickness=0, command=start_timer)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", font=(FONT_NAME, 12), width=5, highlightthickness=0, command=stop_timer)
button_reset.grid(row=2, column=2)

label_timer = Label(text="Timer", font=(FONT_NAME, 40), bg=YELLOW, foreground=GREEN)
label_timer.grid(row=0, column=1)

label_check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24))
label_check.grid(row=3, column=1)

window.mainloop()