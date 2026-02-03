from PIL import Image
file = '/home/husniddin/Projects/invoice/photo_2025-11-05_07-57-36.jpg'
im = Image.open(file)

print(im.format, im.size, im.mode)
