<p align="center">
  <img height=200 src="https://github.com/makkoncept/colorpalette/blob/master/.readme_assets/color-palette.png?raw=true"><br>
  <h1 align="center">ColorPalette</h2>
  <p align="center">A simple web app to extract dominant colors from an image.<p>
  <p align="center">
    <a href="https://github.com/makkoncept/colorpalette/blob/master/LICENSE">
      <img alt="MIT License" src="https://img.shields.io/github/license/makkoncept/colorpalette.svg?color=brightgreen" />
    </a>
    <a href="https://github.com/makkoncept/colorpalette/pulls">
	    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="prs welcome">
    </a>
  </p>
</p>

# Demo
<p align="center">
  <img src="https://github.com/makkoncept/colorpalette/blob/master/.readme_assets/demo.gif?raw=true">
</p>

# Live

View it live at: https://colorpalette.xyz

An old version of the application lives on: https://colorpalettedemo.herokuapp.com/

## What it do

Extracts 10 dominating colors from the image and add the palette to the bottom of the image (inspired by [colorpalette.cinema](https://www.instagram.com/colorpalette.cinema/?hl=en)).
You can adjust the palette height, outline color and width to match your image dimension.

<img height="480" width="682.66" src="https://i.imgur.com/WuwhwOr.png">

## How it works

The `color.py` script does all the work. It uses Pillow. It takes the image and reduce the number of colors in it to 10, but the way it does this is interesting as only dominating colors are choosen as they can best resemble the original image.

_image with 10 colors_

<img width="50%" style="padding: 10px;" alt="Screenshot" src="https://user-images.githubusercontent.com/34679965/48556179-39e3ad80-e909-11e8-8671-dafe65d29fcc.png">

_original image_

<img width="50%" src="https://user-images.githubusercontent.com/34679965/48556182-3f40f800-e909-11e8-8d70-22bf311513e2.png">

To know more about the method you can read [this](http://www.aishack.in/tutorials/dominant-color/) post

## Install & run locally

Install:

```
git clone https://github.com/makkoncept/colorpalette.git
cd colorpalette
```

Create a virtualenv:

```
python3 -m venv venv
```

Activate it on Linux:

```
. venv/bin/activate
```

Or on Windows cmd:

```
venv\Scripts\activate.bat
```

Install requirements:

```
pip install -r requirements.txt
```

Run:

```
python run.py
```

View on [localhost:5000](http://127.0.0.1:5000)

## Attribution

Icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
