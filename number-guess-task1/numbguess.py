from tkinter import *
import random

ws = Tk()
ws.title('Python Guess Random Number Game')
ws.geometry('600x600')
ws.config(bg='green')

randnumb = random.randint(1, 500)
attempt = 5

var = IntVar()
disp = StringVar()

def check_ranum():
    global randnumb
    global attempt
    uip = var.get()
    if attempt > 0:
        if uip == randnumb:
            msg = f'You won! {randnumb} is the correct answer.'
        elif uip > randnumb:
            attempt -= 1
            msg = f'{uip} is greater. You have {attempt} attempt left.'
        elif uip < randnumb:
            attempt -= 1
            msg = f'{uip} is smaller. You have {attempt} attempt left.'
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {attempt} attempt left.Correct guess is:{randnumb}'

    disp.set(msg)
    
    


Label(
    ws,
    text='Python Number Guessing Game',
    font=('Helvetica', 30),
    fg='black',
    relief=SOLID,
    padx=30,
    pady=30,
    bg='lime'
).pack(pady=(30, 0))

Entry(
    ws,
    textvariable=var,
    bg='lawngreen',
    justify='center',
    fg='black',
    font=('Helvetica', 20)
).pack(pady=(30, 10))

Button(
    ws,
    text='Submit',
    font=('Helvetica', 18),
    bg='mediumseagreen',
    fg='black',
    command=check_ranum,
    
).pack()

Label(
    ws,
    textvariable=disp,
    bg='royalblue',
    fg='white',
    font=('Helvetica', 14)
).pack(pady=(20,0))

ws.mainloop()