#!/usr/bin/env python

from pylab import *
from matplotlib import pyplot as plt
import sys
fig, ax = plt.subplots()

def on_key_press(event):
    print event.key
    sys.stdout.flush()
    
fig.canvas.mpl_connect('key_press_event', on_key_press)
# disable e.g. 's' (save), 'g' (grid) key-bindings
fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
plt.show()
