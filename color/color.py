from PIL import Image, ImageDraw
from webcolors import rgb_to_hex


def get_colors(infile, outline_width, palette_length_div, outline_color, numcolors=10):
    original_image = Image.open(infile)
    image = Image.open(infile)
    small_image = image.resize((80, 80))
    result = small_image.convert('P', palette=Image.ADAPTIVE, colors=numcolors)   # image with only 10 dominating colors
    result.putalpha(0)
    colors = result.getcolors(80*80)      # array of colors in the image
    print(type(colors))
    swatchsize2 = 100

    width, height = original_image.size
    palette_height = int(height/palette_length_div)
    background = Image.new("RGB", (width, height + palette_height))   # blank canvas(original image + palette)
    pal = Image.new("RGB", (width, palette_height))
    pal2 = Image.new("RGB", (numcolors*swatchsize2, swatchsize2))
    draw = ImageDraw.Draw(pal)
    draw2 = ImageDraw.Draw(pal2)
    posx = 0
    posx2 = 0
    swatchsize = width/10
    hex_codes = []

    # making the palette
    for count, col in colors:
        draw.rectangle([posx, 0, posx + swatchsize, palette_height], fill=col, width=outline_width, outline=outline_color)
        draw2.rectangle([posx2, 0, posx2+swatchsize2, swatchsize2], fill=col)
        posx = posx + swatchsize
        posx2 = posx2 + swatchsize2
        hex_codes.append(rgb_to_hex(col[:3]))

    del draw
    del draw2
    box = (0, height, width, height + palette_height)

    # pasting image and palette on the canvas
    background.paste(original_image)
    background.paste(pal, box)


    return background, pal2, hex_codes
