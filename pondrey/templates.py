# Pondrey

class Template:
  stri = ""
  def __init__(str):
    stri = str
  def sub(*vars):
    for k,v in *vars.items():
      if stri == "":
        print("Please provide a string to substitute with.")
      else:
        d = stri.split("$" + k + "")                         # Variables example: "$hello"
        return v.join(d)
