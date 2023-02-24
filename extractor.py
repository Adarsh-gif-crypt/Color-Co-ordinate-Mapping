from scipy.spatial import KDTree
import webcolors
import extcolors

class extract:
    def __init__(self) -> None:
        pass

    def extract_color(self, img):
        colors, pixels = extcolors.extract_from_image(img, tolerance = 10, limit = 3)
        
        color_names = []
        with open(r'colorlist/colorlist.txt','r') as fp:
            for line in fp:
                x = line[:-1]

                color_names.append(x)
        
        rgb_vals = [(255,87,51),(248,131,121),(255,255,255),(128,0,0),(255,219,88),
                    (230,232,250),(128,128,128),(255,255,0),(194,178,128),(0,255,0),
                    (221,160,221),(128,0,128),(255,215,0),(250,249,246),(255,0,0),
                    (0,0,128),(0,0,0),(255,192,203),(128,128,0),(224,176,255),
                    (165,42,42),(255,253,208),(192,192,192),(255,229,180),(245,245,220),
                    (0,128,128),(255,165,0),(0,0,255),(184,115,51)]
        kdtree = KDTree(rgb_vals)

        extract_colors = []

        for color in colors:

            rgb = color[0]

            closest_color_idx = kdtree.query(rgb)[1]
            closest_color = color_names[closest_color_idx]
            extract_colors.append(closest_color)

        if len(extract_colors)>2:
            return extract_colors[-2:]
        else:
            return extract_colors