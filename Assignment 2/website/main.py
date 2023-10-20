import js as p5
from js import document

data = None

def setup():
  p5.createCanvas(500, 500)
  print('update')

def draw():
  p5.background(255)

  global data
  data_string = document.getElementById("data").innerText
  data_list = data_string.split(',')
  data = data_list[0]
  button_val = int(data_list[1])
  p5.text(int(data), 10, 20)
  p5.text(button_val, 10, 30)

  p5.noStroke()
  p5.push()
  # move to middle of canvas:
  p5.translate(p5.width/2, p5.height/2)
 
  if(button_val == 0):
    # set angle variable to integer of data:
    angle = int(data)
    # rotate canvas with angle converted from degrees to radians:
    p5.rotate(p5.radians(angle))
     # fill with gray responding to data:
    p5.fill(int(data))
    # change mode to draw rectangle from center:
    p5.rectMode(p5.CENTER)
    # draw rectangle at coordinate 0, 0 and 100 width and height and 20 radius:
    p5.rect(0, 0, 100, 100, 20)
  else:
    circle_size = int(data)
    p5.ellipse(0, 0, circle_size, circle_size)
    # fill with blue color:
    p5.fill(0, 0, 255)
  # restore graphical transformation:
  p5.pop()
  

def print_test(x):
  print(x)