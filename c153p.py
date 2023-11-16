from tkinter import*
root = Tk()
import random

root.title("Random Password Generator")
root.geometry("400x400")

label = Label(root)
label1 = Label(root)
label2 = Label(root)

entry = Entry(root)

array_3d = [[["1", "2", "3", "4", "5", "6"],["Head", "Tail"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]
print(array_3d [0][2][3])

def password() :
    random_1 = random.randint(0,5)
    random_2 = random.randint(0,1)
    random_3 = random.randint(0,7)
    
    letter_1 = (array_3d[0][0][random_1])
    letter_2 = (array_3d[0][1][random_2])
    letter_3 = (array_3d[0][2][random_3])
    
    generatedPassword = letter_1 + letter_2 + letter_3
    
    label1["text"]= generatedPassword
    guessedPassword = entry.get()
    
    label["text"]= guessedPassword
    
    if(generatedPassword == guessedPassword):
        label2["text"]= "Password Match"
    
    label2["text"]= "Password Incorrect"

btn = Button(root, text="Password", command=password)

entry.place(relx=0.5, rely=0.3, anchor=CENTER)
label.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()

