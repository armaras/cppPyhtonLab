import tkinter as tk
import string

root = tk.Tk()


root.geometry("250x170")

T = tk.Text(root, height=10  , width=100)


l = tk.Label(root, text="File operations")
l.config(font=("Courier", 14))

f = open("C:\\Users\\C605\\Desktop\\Marvel.txt", "r")
x = f.read()
def inster_text():
    T.delete(1.0,'end')
    T.insert(tk.END, x)

def count():
    d = dict()

    with open('C:\\Users\\C605\\Desktop\\Marvel.txt', 'r') as file:
        # reading each line
        for line in file:

            # reading each word
            for word in line.split():
                # displaying the words
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1
    print(d)
    T.delete(1.0,'end')
    T.insert(tk.END,d)




print(x)

b1 = tk.Button(root, text="Read", command=inster_text)


b2 = tk.Button(root, text="Exit",
            command=root.destroy)


b3 = tk.Button(root, text="Calculate",
            command=count)

f.read()
l.pack()
T.pack()
b1.pack()
b2.pack()
b3.pack()

tk.mainloop()
