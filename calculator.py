import tkinter as tk
def calculate():
    result=eval(entry.get())
    label.cconfig(text="Result:"+str(result))
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Calculate",command=calculate)
button.pack()
label=tk.label(root,text="Result:")
label.pack()
root.mainloop()
