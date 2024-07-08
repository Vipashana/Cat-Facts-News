import tkinter as tk
from PIL import Image, ImageTk
root = tk.Tk()
root.title('MeoWrld. . . ')
root.geometry('1000x1000')

def every_100(text):
    final_text = ''
    for i in range(0,len(text)):
        final_text +=text[i]
        if i%100 == 0 and i != 0:
            final_text +='\n'
    return final_text

photos = []
texts = []
for i in range(0,3):
    with open(f't{i+1}.txt') as f:
        text = f.read()
        texts.append(every_100(text))

        image = Image.open(f'cat{i+1}.jpg')
        image = image.resize((225,225), Image.LANCZOS)
        photos.append(ImageTk.PhotoImage(image))


f0 = tk.Frame(root, width=800, height=70)
f0.pack()

t_label1 = tk.Label(f0, text='WELCOME TO MeoWorld!', font='lucida 33 bold')
t_label2 = tk.Label(f0, text="30 June, 2024", font='lucida 13 bold')
t_label3 = tk.Label(f0, text="Let's look at some fun cat facts!", font='lucida 18 bold')
t_label1.pack()
t_label2.pack()
t_label3.pack()

f1 = tk.Frame(root, width=900, height=200, pady=14)
tk.Label(f1, text=texts[0], padx=22, pady=22).pack(side='left')
tk.Label(f1, image = photos[0],anchor='e').pack()
f1.pack(anchor='w')

f2 = tk.Frame(root, width=900, height=200, pady=14, padx=22)
tk.Label(f2, text=texts[1], padx=22, pady=22).pack(side='right')
tk.Label(f2, image = photos[1],anchor='e').pack()
f2.pack(anchor='w')

f3 = tk.Frame(root, width=900, height=200, pady=14)
tk.Label(f3, text=texts[2], padx=22, pady=22).pack(side='left')
tk.Label(f3, image = photos[2],anchor='e').pack()
f3.pack(anchor='w')


root.mainloop()