from tkinter import *
import math
import os
import winsound
import sys
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
checkmark = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    global checkmark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_txt.config(text = "Timer", fg=GREEN)
    reps = 0
    checkmark = ""
    checkmark_txt.config(text = checkmark)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60 
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 == 1:
        count_down(work_sec)
        timer_txt.config(text = "Work", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_txt.config(text = "Long Break", fg=PINK)
    else:
        count_down(short_break_sec)
        timer_txt.config(text = "Short Break", fg=RED)


def play_sound():
    winsound.Beep(400, 1000)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = str(count_sec)
        count_sec = "0"+count_sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        play_sound()
        start_timer()
        if reps % 2 == 0:
            global checkmark
            checkmark += "✓"
            checkmark_txt.config(text = checkmark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)




canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
image_path = resource_path("tomato.png")
tomato_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=tomato_img)
timer_text =  canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

timer_txt = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_txt.grid(column=1, row=0)


start_btn = Button(text="Start", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_btn.grid(column=2, row=2)

checkmark_txt = Label(fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
checkmark_txt.grid(column=1, row=3)

exit_btn = Button(text="Exit", command=window.quit)
exit_btn.grid(column=1, row=4)


window.mainloop()