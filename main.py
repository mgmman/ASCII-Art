from PIL import Image

palette = [' ', '.', ',', '-', '^', '+', 'r', '*', ';', '|', '/', ')', 'T', 'R', 'B', '4', '@']
image = Image.open('test1.png')
image = image.convert('L')
image = image.resize((image.size[0] // 8, image.size[1]//8))
with open("output.txt", "w") as f:
    for i in range(image.size[1]-1):
        for j in range(image.size[0]-1):
            pixel = image.getpixel((j, i))
            print(palette[int(pixel/(256/len(palette)))], end=' ', file=f)
        print(file=f)
