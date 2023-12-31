import unittest
from PIL import Image
from main import ASCIIArtConvertor


class ASCIIArtConvertorTests(unittest.TestCase):
    def setUp(self):
        self.convertor = ASCIIArtConvertor()

    def test_load_image(self):
        image = self.convertor.load_image('test2.png')
        self.assertIsInstance(image, Image.Image)
        self.assertEqual(image.size, (300, 300))

    def test_resize(self):
        image = Image.open('test2.png')
        new_image = self.convertor.resize(image, 100, 100)
        self.assertIsInstance(new_image, Image.Image)
        self.assertEqual(new_image.size, (100, 100))

    def test_convert_to_greyscale(self):
        image = Image.open('test2.png')
        greyscale_image = self.convertor.convert_to_greyscale(image)

    def test_convert_to_ascii_art(self):
        greyscale_image = [[50, 70, 90], [100, 120, 140], [160, 180, 200]]
        ascii_art = self.convertor.convert_to_ascii_art(greyscale_image)
        expected_result = "R/r\nT|+\n)*-\n"
        self.assertEqual(ascii_art, expected_result)

    def test_resize2(self):
        image = Image.new('RGB', (100, 100), (255, 0, 0))

        resized_image = self.convertor.resize(image, 50, 50)

        self.assertEqual(resized_image.size, (50, 50))

        for i in range(resized_image.size[0]):
            for j in range(resized_image.size[1]):
                pixel = resized_image.getpixel((i, j))
                self.assertEqual(pixel, (255, 0, 0))


if __name__ == '__main__':
    unittest.main()
