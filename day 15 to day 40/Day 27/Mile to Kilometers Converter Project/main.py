from tkinter import *


def create_label(text, column, row):
    label = Label(text=text)
    label.grid(column=column, row=row)
    return label


def main():
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=250, height=150)
    window.config(padx=20, pady=20)

    create_label("is equal to", 0, 1)
    create_label("Miles", 2, 0)
    create_label("Km", 2, 1)
    result = create_label("", 1, 1)

    entry = Entry(width=10)
    entry.insert(END, string="0")
    entry.grid(column=1, row=0)

    def calculate():
        try:
            mile_distance = float(entry.get())
            km_distance = mile_distance/0.6214
            result.config(text=f"{km_distance}")
        except EXCEPTION as e:
            print(e)

    button = Button(text="Calculate", command=calculate)
    button.grid(column=1, row=2)

    window.mainloop()


if __name__ == '__main__':
    main()
