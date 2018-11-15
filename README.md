**[Live demo](http://colorpalette.ml)**

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

## Run Locally

- `git clone https://github.com/makkoncept/colorpalette.git`
- `cd colorpalette`
- `python3 -m venv venv`
- `source venv/bin/activate`  for linux
- `venv\Scripts\activate.bat` for windows
- `pip install -r requirements.txt`
- `python run.py`

View on `localhost:5000`

## credits 
[Stackoverflow]() and [script]()
