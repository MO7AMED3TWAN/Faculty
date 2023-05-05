import tkinter as tk
# تعريف النافذة
App = tk.Tk()
App.title("تاسك عبدالمولى")
App.geometry("600x400")
# تعريف مكونات الواجهة

def on_submit():
    # استخراج النص من حقل النص وطباعته
    text = TextBox.get("1.0", tk.END)
    print(text)
    text_box.insert(tk.END, text + "\n")




label = tk.Label(App, text="أزيك يابا")

TextBox = tk.Text(App, height=5, bd=1) 
text_box= tk.Text(App, height=10)

button = tk.Button(App, text="Click me!", command=on_submit)
# ترتيب المكونات داخل النافذة
label.pack()
TextBox.pack()
button.pack()
text_box.pack()
# تشغيل النافذة
App.mainloop()