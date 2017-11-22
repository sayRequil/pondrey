import version
import sys

routed = False

y = []

arg = sys.argv[0]

def yield(str):
  y.append(str)

class Pondrey:
  conf = {
    app="",
    version=version.vers()
  }
  def __init__(app="My Application."):
    conf.app = app
  def route(route):
    if arg == route:
      print-yields()
      
def print-yields():
  i = 0
  while i < len(y):
    print(y[i])
    i += 1
