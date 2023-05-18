from picamera import PiCamera
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from time import sleep
import numpy
from gpiozero import CPUTemperature

def Init():
    photo_width = 1920
    photo_height = 1080
    
    global buf_height
    global buf_width

    if (int(photo_height/16)*16<photo_height):
        buf_height = (int(photo_height/16)+1)*16
    else:
        buf_height = photo_height
    if (int(photo_width/16)*16<photo_width):
        buf_height = (int(photo_wdith/16)+1)*16
    else:
        buf_width = photo_width
        
    global a
    a = numpy.zeros((buf_height,buf_width,4), dtype=numpy.uint8)
    a[0:photo_height, 0:photo_width, 3] = 0x00
    
    half_width = int(photo_width / 2)
    half_height = int(photo_height / 2)

    a[((half_height)-1):((half_height)+1), ((half_width)-5):((half_width)+5), [0,1,3]] = 0xff #0:2 yellow
    a[((half_height)-5):((half_height)+5), ((half_width)-1):((half_width)+1), [0,1,3]] = 0xff #0:2 yellow
    
    global fnt
    fnt = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf", 40)
    
    global camera
    camera = PiCamera()
    camera.resolution = (photo_width,photo_height)
    camera.framerate = 60
    camera.start_preview(vflip=True)
    
    
    b = Image.fromarray(a)
    global b1
    b1 = b.copy()
    
    c = ImageDraw.Draw(b)

    c.text((100,100), "CPU Temperature:",font = fnt, fill = (255,255,0,255))
    d = numpy.array(b)
    d.reshape((buf_height,buf_width,4))
    
    global o
    o = camera.add_overlay(d.tobytes(),layer=3)
    
    sleep(1)


def UpdateOverlay():
    b = b1.copy()
    c = ImageDraw.Draw(b)
    
    temperature = CPUTemperature().temperature;
    
    c.text((100,100), "CPU Temperature:\n" + str(temperature),font = fnt, fill = (255,255,0,255))
    
    d = numpy.array(b)
    d.reshape((buf_height,buf_width,4))
    
    o.update(d.tobytes()) # This line of code causes the error: 


def End():
    camera.remove_overlay(o)
    camera.stop_preview()
    
