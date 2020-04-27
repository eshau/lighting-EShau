from display import *
from draw import *
from parser import *
from matrix import *
import math


# # lighting values
# view = [0,
#         0,
#         1];
# ambient = [170,
#            170,
#            170]
# light = [[0,
#           0,
#           1],
#          [0,
#           255,
#           255]]
# areflect = [1,
#             1,
#             1]
# dreflect = [0.9,
#             0.9,
#             0.9]
# sreflect = [0.25,
#             0.25,
#             0.25]

# lighting values
view = [0,
        0,
        1];
ambient = [50,
           50,
           50]
light = [[0.5,
          0.75,
          1],
         [0,
          255,
          255]]
areflect = [0.1,
            0.1,
            0.1]
dreflect = [0.5,
            0.5,
            0.5]
sreflect = [0.5,
            0.5,
            0.5]

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]


parse_file( 'script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
# parse_file( 'my_script', edges, polygons, csystems, screen, zbuffer, color, view, ambient, light, areflect, dreflect, sreflect)
