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

Extracts 10 dominating colors from the image and adds the palette to the bottom of the image (inspired by [colorpalette.cinema](https://www.instagram.com/colorpalette.cinema/?hl=en)). You can adjust the palette height, outline color, and width to match your image dimension. Another independent image of the palette with the hex codes of colors is also generated.

The app does not depend on any APIs for extracting colors. `color.py` contains the code for it with [Pillow](https://pillow.readthedocs.io/en/stable/) as the only dependency.

## Some samples

1. <span>Photo by <a href="https://unsplash.com/@lukaodak?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Luka Odak</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<p align="center">
  <img width=80% src="https://i.imgur.com/zw0SenV.jpg"><br><br>
  <img width=80% src="https://i.imgur.com/KNg06TY.jpg">
</p>

2. <span>Photo by <a href="https://unsplash.com/@goodspleen?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Alexandre Chambon</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<p align="center">
  <img width=80% src="https://i.imgur.com/ngBiV0t.jpg"><br><br>
  <img width=80% src="https://i.imgur.com/xmn52P0.jpg">
</p>

3. <span>Photo by <a href="https://unsplash.com/@federyka?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Federica Diliberto</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<p align="center">
  <img height=1000px src="https://i.imgur.com/vZTtGEb.jpg"><br><br>
  <img width=80% src="https://i.imgur.com/kvt0gNS.jpg">
</p>

4. <span>Photo by <a href="https://unsplash.com/@randomlies?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Ashim D’Silva</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>

<p align="center">
  <img width=80% src="https://i.imgur.com/QCnXUAf.jpg"><br><br>
  <img width=80% src="https://i.imgur.com/jjcv5OV.jpg">
</p>

## Directory Structure

<pre>

|-- Procfile
|-- README.md
|-- app.json
|-- colorpalette
|   |-- __init__.py
|   |-- color.py
|   |-- forms.py
|   |-- routes.py
|   |-- static
|   |   |-- css
|   |   |-- font
|   |   |-- images
|   |   |   |-- favicon
|   |   `-- js
|   `-- templates
|       |-- 413.html
|       |-- base.html
|       |-- index.html
|       `-- picture.html
|-- config.py
|-- requirements.txt
|-- run.py    
`-- LICENSE

</pre>

## Run locally

1. Clone the repostory:

```
git clone https://github.com/makkoncept/colorpalette.git
```

2. Navigate to the project root and create a virtual environment:

```
python3 -m venv venv
```

3. Activate the virtual environment:

Linux:

```
source venv/bin/activate
```

Windows cmd:

```
venv\Scripts\activate.bat
```

4. Install requirements:

```
pip install -r requirements.txt
```

5. Run the development server:

```
python run.py
```

6. View on [localhost:5000](http://127.0.0.1:5000)

## Attribution

Icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
