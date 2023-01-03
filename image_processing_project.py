import sys
import os
from PIL import Image, ImageFilter

input_folder=sys.argv[1]
output_folder=sys.argv[2]
print(input_folder)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for image_file in os.listdir(input_folder):
    img=Image.open(f'{input_folder}/{image_file}')
    clean_name=os.path.splitext(image_file)
    img.save(f'{output_folder}/{clean_name[0]}.pdf','pdf')


img=Image.open(f'{input_folder}/killer_joker.jpg')
se=img.filter(ImageFilter.FIND_EDGES)
se.save('killer_joker2.png','png')
se.show()



