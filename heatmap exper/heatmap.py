from pynput.mouse import Listener
import logging
import pandas as pd
import csv
  

logging.basicConfig(filename="mouse_cod.csv",level=logging.DEBUG, format = "%(message)s")
headerList = ['x', 'y']

with open("mouse_cod.csv", 'w') as file:
    dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=headerList)
    dw.writeheader()

def on_click (x, y, button, pressed):
    logging.info ("({0},{1})".format((float(x)),(float(1080-y))))
    print ("({0},{1})".format(x,1080-y))



with Listener (on_click = on_click) as listener:
    listener.join ()






