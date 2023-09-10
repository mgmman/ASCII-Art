import tkinter
from tkinter import ttk
from tkinter import font
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
        out_name_hint = ttk.Label(text='enter output file name')
        out_name_hint.pack()
        self.out_name_input = ttk.Entry()
        self.out_name_input.pack()
        self.out_font = font.Font(family='Consolas', size=1)
        self.text_output = ttk.Label(font=self.out_font)
        self.text_output.pack()
        self.generate_button = tkinter.Button(text='generate', command=self.generate)
        self.generate_button.pack()
        self.save_button = tkinter.Button(text='save', command=self.save)
        self.save_button.pack()
        self.convertor = ASCIIArtConvertor()
        root.mainloop()

    def generate(self):
        width, height = 600, 600
        if self.size_input.get() != '':
            width, height = map(int, self.size_input.get().split(','))
        image = self.convertor.load_image(self.file_name_input.get())
        result = self.convertor.convert_to_ascii_art(
            self.convertor.convert_to_greyscale(
                self.convertor.resize(image, width, height)
            ))
        self.text_output['text'] = result

    def save(self):
        with open(self.out_name_input.get(), 'w') as f:
            f.write(self.text_output['text'])


if __name__ == '__main__':
    Viewer()