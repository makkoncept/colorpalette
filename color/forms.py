from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import IntegerField
from wtforms.validators import NumberRange


class PhotoForm(FlaskForm):
    photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    palette_height = IntegerField('Palette Height', validators=[NumberRange(1, 10)])
    palette_outline_width = IntegerField('Palette Outline Width', validators=[NumberRange(1, 40)])


