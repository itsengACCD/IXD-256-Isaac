import js as p5
from js import document

data_string = None
data_list = None
angle_val = None
light_val = None
button_val = None

# load image data and assign it to variable:
valley_img = p5.loadImage('valley.png')
cloud_img = p5.loadImage('cloud.png')

def setup():
  p5.createCanvas(800, 400)

def draw():
  global data_string, data_list
  global angle_val, button_val, light_val

  # assign content of "data" div on index.html page to variable:
  data_string = document.getElementById("data").innerText
  # split data_string by comma, making a list:
  data_list = data_string.split(',')
  # make sure to change initial string in html file to reflect list:
  angle_val = int(data_list[0])
  light_val = int(data_list[1])
  button_val = int(data_list[2])

  p5.fill(0)
  p5.noStroke()
  p5.text('sensor_val = ' + str(angle_val), 10, 20)
  p5.text('light_val = ' + str(light_val), 10, 35)
  p5.text('button_val = ' + str(button_val), 10, 50)

  # change fill color with button value:
  if(button_val == 0):
    p5.fill(255, 200, 0)  # yellow fill
    p5.background(angle_val-100, angle_val-55, angle_val+100)

  else:
    p5.fill(255, 255, 180)  # pale yellow fill
    p5.background(0-angle_val, 0-angle_val, 100-angle_val)

  # change sun height with sensor value:
  p5.ellipse(400, 355-angle_val, 150, 150)
  # control opacity on cloud_img with tint:
  p5.tint(255, 255, 255, light_val)
  p5.image(cloud_img, 0, 0, 800, 400)
  # disable tint on valley_img:
  p5.noTint()
  p5.image(valley_img, 0, 0, 800, 400)
