import sys
import base64
from PIL import Image

with open(sys.argv[1], 'rb') as png_file:
    img=Image.open(png_file)
    w_px = img.width
    h_px = img.height

    png_file.seek(0)
    img_data_base64 = base64.b64encode(png_file.read())

print(sys.argv[1])
print("w", w_px)
print("h", h_px)
#print(img_data_base64)


with open(sys.argv[1][:-3]+"svg", 'w') as svg_out,\
     open('png-embed-template.svg', 'r') as svg_tempalte:

    svg = svg_tempalte.read()
    w_mm = w_px/3.77952744
    h_mm = h_px/3.77952744

    svg = svg.replace("<img_width_mm>", f"{w_mm:.5f}")
    svg = svg.replace("<img_height_mm>", f"{h_mm:.5f}")
    svg = svg.replace("<img_doc_name>", sys.argv[1][:-3] + "svg")
    svg = svg.replace("<img_data_base64>", img_data_base64.decode('utf-8'))

    svg_out.write(svg)



