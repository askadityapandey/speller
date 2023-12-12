import tkinter
from tkinter import*
from textblob import TextBlob

root = Tk()
root.title("Speller")
root.geometry("700x400")
root.config(background="#0a0908")


def check_spelling():
    word =enter_text.get()
    a =TextBlob(word)
    right=str(a.correct())

    cs=Label(root,text="Correct text is:" ,font=("poppins", 20),bg="#0a0908", fg="white")
    cs.place(x=100, y=250)
    spell.config(text=right)
heading= Label(root,text="Speller", font=("Trebuchet MS",35,"bold"),bg="#0a0908",fg="white")
heading.pack(pady=(50,0))

enter_text=Entry(root, justify="center", width=30,font=("poppins",25), bg="white",border=1)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root, text="Check!", font=("arial",20,"bold"),fg="white",bg="black", command=check_spelling)
button.pack()
spell=Label(root, font=("poppins",20),bg="#0a0908", fg="white")
spell.place(x=350,y=250)

root.mainloop()