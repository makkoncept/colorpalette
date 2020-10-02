from PIL import Image, ImageDraw, ImageFont
from webcolors import rgb_to_hex
import os


def get_dominant_colors(infile):
    image = Image.open(infile)
    small_image = image.resize((80, 80))
    result = small_image.convert(
        "P", palette=Image.ADAPTIVE, colors=10
    )  # image with only 10 dominating colors

    # Find dominant colors
    palette = result.getpalette()
    color_counts = sorted(result.getcolors(), reverse=True)
    colors = list()

    for i in range(10):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]
        colors.append(tuple(dominant_color))

    # print(colors)
    return colors


def process_uploaded_image(
    infile, outline_width, pallete_division_factor, outline_color, numcolors=10
):
    # width of the pallete that will be an independent image itself
    independent_pallete_width = 100

    original_image = Image.open(infile)
    width, height = original_image.size

    # height for the pallete that will be pasted under the image
    img_palette_height = int(height / pallete_division_factor)
    img_palette_width = width / 10

    processed_image = Image.new(
        "RGB", (width, height + img_palette_height)
    )  # blank canvas(original image + palette)

    pallete_under_image = Image.new("RGB", (width, img_palette_height))

    # blank canvas for pallete. <mode, size, color>
    independent_pallete = Image.new(
        "RGB",
        (numcolors * independent_pallete_width, independent_pallete_width + 20),
        color="rgb(255, 255, 255)",
    )

    draw = ImageDraw.Draw(pallete_under_image)
    draw2 = ImageDraw.Draw(independent_pallete)

    posx = 0
    posx2 = 0

    fonts_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "colorpalette/static/font/Roboto-Bold.ttf",
    )
    # create font object with the font file
    font = ImageFont.truetype(fonts_path, size=16)

    colors = get_dominant_colors(infile)
    # making the palettes
    for color in colors:
        draw.rectangle(
            [posx, 0, posx + img_palette_width, img_palette_height],
            fill=color,
            width=outline_width,
            outline=outline_color,
        )

        # drawing one pallete at a time on independent pallete canvas
        draw2.rectangle(
            [posx2, 0, posx2 + independent_pallete_width, independent_pallete_width],
            fill=color,
        )

        # write the hex code under the pallete
        draw2.text(
            (posx2 + 20, independent_pallete_width),
            rgb_to_hex(color[:3]),
            fill="rgb(0, 0, 0)",
            font=font,
        )

        # move the pointer to the beginning of next pallete color
        posx = posx + img_palette_width
        posx2 = posx2 + independent_pallete_width

    del draw
    del draw2
    box = (0, height, width, height + img_palette_height)

    # pasting image and palette on the canvas
    processed_image.paste(original_image)
    processed_image.paste(pallete_under_image, box)

    return processed_image, independent_pallete
