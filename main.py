from tkinter import *

root = Tk()
root.title("Крестики-нолики")
root.geometry("300x250")

fields = []

fieldValues = [
    [StringVar(), StringVar(), StringVar()],
    [StringVar(), StringVar(), StringVar()],
    [StringVar(), StringVar(), StringVar()]
]

mark = ''
currentTurnVar = StringVar()

def switchMark():
    global mark, currentTurnVar
    if mark == 'x':
        mark = 'o'
    else:
        mark = 'x'

    currentTurnVar.set('Сейчас ход ' + mark)


def buttonClickFunctionConstructor(i, j):
    def onButtonClick():
        global mark
        if fieldValues[i][j].get() != '':
            return
        fieldValues[i][j].set(mark)
        switchMark()

    return onButtonClick

for i in range(3):
    fields.append([])
    for j in range(3):
        fields[i].append(Button(
            textvariable=fieldValues[i][j],
            background="#555",
            foreground="#ccc",
            padx="14",
            pady="7",
            font="13",
            command=buttonClickFunctionConstructor(i, j)
        ))
        fields[i][j].grid(row=i, column=j, ipadx=10, ipady=6, padx=10, pady=10)

currentTurnLabel = Label(textvariable=currentTurnVar, fg="#eee", bg="#333")
currentTurnLabel.grid(row=4, column=2)
switchMark()

root.mainloop()