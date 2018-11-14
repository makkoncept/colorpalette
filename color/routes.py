from color import app
from color.color import get_colors
from color.forms import PhotoForm
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from webcolors import hex_to_rgb
import os
import uuid


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhotoForm()
    if form.validate_on_submit():
        print(hex_to_rgb(request.form.get('palette_outline_color')))
        f = form.photo.data
        filename = secure_filename(f.filename)
        _, ext = os.path.splitext(filename)
        filename = uuid.uuid4().hex + ext
        print(filename)
        f = get_colors(f, palette_length_div=form.palette_height.data, outline_width=form.palette_outline_width.data,
                       outline_color=hex_to_rgb(request.form.get('palette_outline_color')))
        path = os.path.join(app.root_path, 'static/images',  filename)
        f.save(path)
        # print(path)
        # print(f.width)
        return redirect(url_for('picture', name=filename, height=f.height, width=f.width))

    return render_template('index.html', form=form, src='default')


@app.route('/picture/<name>/<height>/<width>')
def picture(name, height, width):
    src = url_for('static', filename='images/' + name)
    height, width = img_tag_size(int(height), int(width))
    print(height, width)
    return render_template('picture.html', src=src, height=height, width=width)


def img_tag_size(height, width):
    if height < 850 and width < 850:
        return height, width
    else:
        while height > 850 and width > 850:
            height = int(height/2)
            width = int(width/2)
        return height, width


@app.errorhandler(413)
def error413():
    return render_template('413.html'), 413
