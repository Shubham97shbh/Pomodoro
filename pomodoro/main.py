from tkinter import *

pink = "#e2979c"
red = "#e7365b"
green = "#9bdeac"
yellow = "#f7f5dd"
font_name = "courier"
Work_time = 25
short_break = 5
long_break = 20
start_again = False
reps = 0
tick = 0
timer = None

window = Tk()
window.title("pomodoro")
window.config(padx=60, pady=50, bg=yellow)

lab = Label(text="Timer", fg=red, font=("Arial", 44, "bold"))
lab.grid(row=0, column=2)

check = Label(text="", fg=red, font=(font_name, 25, "bold"))
check.grid(row=2, column=2)


def count_down(count_sec, count_min):
        global tick, reps, start_again, timer,lab
        if count_min == 0 and count_sec == 0:
            canvas.itemconfig(text_pic, text=f"00:00")
            start_again = True
            reps += 1
        else:
            start_again = False
            if count_sec == 0:
                count_sec = 59
                count_min -= 1
            # display
            if count_sec < 10 and count_min < 10:
                canvas.itemconfig(text_pic, text=f"0{count_min}:0{count_sec}")
            elif count_sec < 10:
                canvas.itemconfig(text_pic, text=f"{count_min}:0{count_sec}")
            elif count_min < 10:
                canvas.itemconfig(text_pic, text=f"0{count_min}:{count_sec}")
            else:
                canvas.itemconfig(text_pic, text=f"{count_min}:{count_sec}")
            timer = window.after(100, count_down, count_sec - 1, count_min)

            # reps
        if start_again:
            if reps % 2 == 0:
                if tick !=4:
                    if reps != 0:
                        tick = int(reps / 2)
                        check.config(text="✔" * tick)
                    count_down(0, 25)
                    lab.config(text="WORK", fg=green)
                else:
                    lab.config(text="Well Done!", fg=green)
            else:
                if reps == 7:
                    count_down(0, 20)
                    lab.config(text="Break", fg=pink)
                else:
                    lab.config(text="Break", fg=red)
                    count_down(0, 5)
            start_again = False


def start():
    count_down(0, 25)
    lab.config(text="WORK", fg=green)


def reset():
    global reps, tick
    reps = 0
    tick = 0
    lab.config(text="Timer", fg=red)
    check.config(text="")
    canvas.itemconfig(text_pic, text=f"00:00")
    window.after_cancel(timer)


canvas = Canvas(width=550, height=500, bg=yellow, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(280, 250, image=tomato)
text_pic = canvas.create_text(280, 250, text="00:00", fill="white", font=("Arial", 34, "bold"))
canvas.grid(row=1, column=2)

b_start = Button(text="start", font=(font_name, 15, "bold"), command=start, highlightthickness=0)
b_start.grid(row=1, column=0)
# start_check=False
b_reset = Button(text="reset", font=(font_name, 15, "bold"), command=reset, highlightthickness=0)
b_reset.grid(row=1, column=3)

window.mainloop()
