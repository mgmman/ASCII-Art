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


if __name__ == '__main__':
    unittest.main()
