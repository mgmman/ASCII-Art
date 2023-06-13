from PIL import Image

palette = [' ', '.', ',', '-', '^', '+', 'r', '*', ';', '|', '/', ')', 'T', 'R', 'B', '4', '@']
palette.reverse()
image = Image.open('test1.png')
image = image.convert('L')
image = image.resize((200, 200))


class ASCIIArtConvertor:
    def __init__(self):
        self.palette = [' ', '.', ',', '-', '^', '+', 'r', '*', ';', '|', '/', ')', 'T', 'R', 'B', '4', '@']
        self.palette.reverse()

    def convert_to_ascii_art(self, image, output_file):
        with open(output_file, "w") as f:
            for j in range(image.size[1] - 1):
                for i in range(image.size[0] - 1):
                    pixel = image.getpixel((i, j))
                    print(self.palette[int(pixel / (256 / len(self.palette)))], end=' ', file=f)
                print(file=f)

    def convert_to_greyscale(self, image: Image):
        for j in range(image.size[1] - 1):
            for i in range(image.size[0] - 1):
                pixel = image.getpixel((i, j))
                image.putpixel()