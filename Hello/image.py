#coding=utf-8
from PIL import Image

im = Image.open('/Users/kang/Desktop/text.png')
print(im.format,im.size,im.mode)

im.thumbnail((200,100))
im.save('/Users/kang/Desktop/thumb.png','PNG')

import sys

print(sys.path)