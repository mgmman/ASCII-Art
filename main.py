from PIL import Image


class ASCIIArtConvertor:
    def __init__(self):
        self.palette = [' ', '.', ',', '-', '^', '+', 'r', '*', ';', '|', '/', ')', 'T', 'R', 'B', '4', '@']
        self.palette.reverse()

    def load_image(self, file_name):
        return Image.open(file_name)

    def convert_to_ascii_art(self, image):
        res = ''
        for j in range(len(image[0])):
            for i in range(len(image)):
                pixel = image[i][j]
                res += self.palette[int(pixel / (256 / len(self.palette)))]
            res += '\n'
        return res

    def convert_to_greyscale(self, image: Image):
        res = [[0] * image.size[0] for _ in range(image.size[1])]
        for j in range(image.size[1]):
            for i in range(image.size[0]):
                pixel = image.getpixel((i, j))
                res[j][i] = (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
        return res

    def resize(self, image, width, height):
        return image.resize((width, height))


if __name__ == '__main__':
    image = Image.open('heart 600-600.png')
    convertor = ASCIIArtConvertor()
    with open('output.txt', 'w') as f:
        image = convertor.resize(image, 600, 600)
        print(convertor.convert_to_ascii_art(convertor.convert_to_greyscale(image)), file=f)
