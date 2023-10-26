import colorgram

colour_list = []
colors = colorgram.extract("image.png", 20)
for i in range(len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    rgb_col = (r, g, b)
    colour_list.append(rgb_col)

print(colour_list)
