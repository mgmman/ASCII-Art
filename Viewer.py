import tkinter
from tkinter import ttk
from main import ASCIIArtConvertor


class Viewer:
    def __init__(self):
        root = tkinter.Tk()
        root.title('ASCII art convertor')
        file_name_hint = ttk.Label(text='enter file name')
        file_name_hint.pack()
        self.file_name_input = ttk.Entry()
        self.file_name_input.pack()
        size_hint = ttk.Label(text='enter width and height separated with comma')
        size_hint.pack()
        self.size_input = ttk.Entry()
        self.size_input.pack()
        self.text_output = tkinter.Text()
        self.text_output.pack()
        self.generate_button = tkinter.Button(text='generate')
        self.generate_button.pack()
        self.save_button = tkinter.Button(text='save')
        self.save_button.pack()

        root.mainloop()


if __name__ == '__main__':
    Viewer()