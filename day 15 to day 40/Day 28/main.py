from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None
COUNTING = False
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global REPS
    global COUNTING
    COUNTING = False
    REPS = 0
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_check_marks.config(text="")
    label_timer.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global REPS

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if not COUNTING:
        REPS += 1
        if REPS < 8:
            if REPS % 2 != 0:
                label_timer.config(text="Work", fg=GREEN)
                count_down(work_sec)
            else:
                label_timer.config(text="Break", fg=PINK)
                count_down(short_break_sec)
        else:
            label_timer.config(text="Break", fg=RED)
            count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global COUNTING
    hours = int(count/60)
    minutes = count % 60
    hours_str = f"{hours:02d}"
    minutes_str = f"{minutes:02d}"

    canvas.itemconfig(timer_text, text=f"{hours_str}:{minutes_str}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
        COUNTING = True
    else:
        if REPS % 2 == 0:
            label_check_marks.config(text="✔"*int(REPS/2))
        COUNTING = False
        start()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text =canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1, row=0)

label_check_marks = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
label_check_marks.grid(column=1, row=3)

button_start = Button(text="Start", command=start, highlightthickness=0)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset, highlightthickness=0)
button_reset.grid(column=2, row=2)

window.mainloop()
