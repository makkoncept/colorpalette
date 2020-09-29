from colorpalette import app
from colorpalette.color import process_uploaded_image
from colorpalette.forms import PhotoForm
from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename
from webcolors import hex_to_rgb
import os
import uuid


@app.route("/", methods=["GET", "POST"])
def index():
    form = PhotoForm()
    if form.validate_on_submit():
        image = form.photo.data

        filename = secure_filename(image.filename)  # sanitize image name
        _, ext = os.path.splitext(filename)
        new_filename = uuid.uuid4().hex + ext  # creating a random name

        image_with_palette, pallete, hex_codes = process_uploaded_image(
            image,
            pallete_division_factor=form.palette_height.data,
            outline_width=form.palette_outline_width.data,
            outline_color=hex_to_rgb(request.form.get("palette_outline_color")),
        )

        image_with_pallete_path = os.path.join(
            app.root_path, "static/images", new_filename
        )
        pallete_path = os.path.join(
            app.root_path, "static/images", "pal" + new_filename
        )

        session["hex_codes"] = hex_codes

        # saving image and pallete
        image_with_palette.save(image_with_pallete_path)
        pallete.save(pallete_path)

        return redirect(
            url_for(
                "picture",
                name=new_filename,
            )
        )

    return render_template("index.html", form=form, src="default")


@app.route("/picture/<name>")
def picture(name):
    processed_img_relative_path = url_for("static", filename="images/" + name)
    pallete_relative_path = url_for("static", filename="images/" + "pal" + name)

    return render_template(
        "picture.html",
        src=processed_img_relative_path,
        src2=pallete_relative_path,
        hex_codes=session.get("hex_codes"),
    )


@app.errorhandler(413)
def error413(e):
    return render_template("413.html"), 413
