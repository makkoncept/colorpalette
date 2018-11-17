# **[Live demo](https://colorpalettedemo.herokuapp.com/)**

## What it do
Extracts 10 dominating colors from the image and add the palette to the bottom of the image (inspired by [colorpalette.cinema](https://www.instagram.com/colorpalette.cinema/?hl=en)).
You can adjust the palette height, outline color and width to match your image dimension.

<img height="480" width="682.66" src="https://github.com/makkoncept/colorpalette/blob/master/color/static/images/2.png">

## How it works
The `color.py` script does all the work. It uses Pillow. It takes the image and reduce the number of colors in it to 10, but the way it does this is interesting as only dominating colors are choosen as they can best resemble the original image.

*image with 10 colors*

<img width="50%" style="padding: 10px;" alt="Screenshot" src="https://user-images.githubusercontent.com/34679965/48556179-39e3ad80-e909-11e8-8671-dafe65d29fcc.png">

*original image* 

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

## credits 
[Stackoverflow](https://stackoverflow.com/questions/1065945/how-to-reduce-color-palette-with-pil/1074680#1074680) and [script](https://gist.github.com/zollinger/1722663)
