from PIL import Image , ImageFilter
img = Image.open('./images/rocky.jpg')
print(img)
# filtered_img=img.filter(ImageFilter.BLUR)            // making image blur
# filtered_img.save("Blur.png",'png')


# filtered_img=img.filter(ImageFilter.SMOOTH)      #making image smooth
# filtered_img.save("smooth.png",'png')



# filtered_img=img.filter(ImageFilter.Color3DLUT)
# filtered_img.save("color3DLUT.png",'png')

filtered_img=img.convert('L')
filtered_img.rotate(109)
filtered_img.save("Black&white.png",'png')

filtered_img.show()