from PIL import ImageFont, ImageDraw, Image
txt= "sending love..."

def string_to_image(filename = 'message.png', text = txt, size = 12, txtcolor = "white", height = 2):
    font = ImageFont.truetype('arial.ttf', size)
    # creates the image
    # size is modified depending on length of the string (length, height)
    image = Image.new(mode = "RGB", size = (int(size/2)*len(text), size+height), color = "black") 
    draw = ImageDraw.Draw(image)
    # draws out the text
    draw.text((10,10), txt, font = font, fill = txtcolor, align = "center")
    #saves the image file
    image.save(filename)


string_to_image(filename = 'todelete.bmp', text = txt, size = 300, txtcolor = "white", height = 50)

