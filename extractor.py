from scipy.spatial import KDTree
import webcolors
import extcolors

class extract:
    def __init__(self) -> None:
        pass

    def extract_color(self, img):
        colors, pixels = extcolors.extract_from_image(img, tolerance = 10, limit = 3)
        
        color_names = list(webcolors.CSS3_HEX_TO_NAMES.values())
        color_vals = [webcolors.name_to_rgb(name) for name in color_names]
        kdtree = KDTree(color_vals)

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