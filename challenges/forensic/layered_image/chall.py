import os
import base64
from PIL import Image

data = base64.b64encode(open("flag.png", "rb").read()).decode("utf-8")

temp = ""
for i, x in enumerate(data[::-1]):
    _ = os.popen(f'convert -gravity center -background white -fill black -size 400x300 -font /usr/share/fonts/truetype/roboto/unhinted/RobotoCondensed-Regular.ttf caption:"{x}" -background white -extent 500x500 temp.png').read()
    
    temp = base64.b64encode(open("temp.png", "rb").read()).decode("utf-8")
    
_ = os.popen(f'exiftool -Comment="{temp}" excalibur.png').read()