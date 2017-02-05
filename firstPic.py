import math

def fibonacciGreen(XRES, YRES):
    square_size = 20
    green = []
    g0 = 11
    g1 = 17
    x = XRES//square_size #assume it divides evenly
    y = YRES//square_size
    for i in range(y):
        line = []
        for j in range(x):
            line.append(g1)
            g0, g1 = g1 % 64, g0 + g1 % 64
        green.append(line)
    return square_size, green

#print fibonacciGreen(30,30)

f = open("firstPic.ppm", 'w')

XRES = 500
YRES = 1000
MAX_COLOR_VALUE = 255
header = "P3" + " " + str(XRES) + " " + str(YRES) + " " + str(MAX_COLOR_VALUE) + "\n"

f.write(header)

square_size, green = fibonacciGreen(XRES, YRES)
print square_size

for i in range(YRES):
    for j in range(XRES):
        r = 204
        b = int(200 + 32 * math.sin(3 * (j // square_size) + (i // square_size )))
        g = green[i // square_size][j // square_size]
        pixel = "" + str(r) + " " + str(g) + " " + str(b) + "\n"
        f.write(pixel)

f.close()
