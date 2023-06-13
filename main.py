from PIL import Image

palette = [' ', '.', ',', '-', '^', '+', 'r', '*', ';', '|', '/', ')', 'T', 'R', 'B', '4', '@']
palette.reverse()
image = Image.open('test1.png')
image = image.convert('L')
image = image.resize((200, 200))
with open("output.txt", "w") as f:
    for j in range(image.size[1]-1):
        for i in range(image.size[0]-1):
            pixel = image.getpixel((i, j))
            print(palette[int(pixel/(256/len(palette)))], end=' ', file=f)
        print(file=f)
