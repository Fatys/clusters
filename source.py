
# coding: utf-8

# In[ ]:

get_ipython().magic(u'matplotlib inline')
import os, sys
import numpy as np
import struct
from matplotlib import pyplot as plt
#from ipywidgets import widgets
from ipywidgets import interact, interactive, fixed
#from IPython.display import display, clear_output


# In[ ]:

def load_outs(filename):
    data = []
    with open(filename, 'r') as fin:
        for line in fin:
            row = line.split()
            ast1_id = str(row[0])
            ast2_id = str(row[1])
            t = float(row[2])
            dist = float(row[3])
            vel = float(row[4])

            data.append([t, dist, vel, ast1_id, ast2_id])
    return data


def histogram(data=None, d_max=10000, v_max=5, c='b'):
    hills_rad = 1859
    v_esc = 5.2
    # c = 'b'
    bins = range(0, 1010, 10)

    x = []
    for point in data:
        if (point[1] < d_max) and (point[2] < v_max):
            x.append((point[0] * 1000))
    ast_id = data[0][3].split('_')[0] + ' - ' + data[0][4].split('_')[0] + ' (%i)' % len(x)
    print('(%i points plotted)' % len(x))
    
    plt.figure(figsize=(10, 6))
    plt.hist(x, bins=bins, color=c, label= '' + ast_id)
    
    #title = "ast. %s: Hill's rad = %i km, Escape vel. = %.1f m/s\n" % (data[0][3].split('_')[0], hills_rad, v_esc)
    title = 'Number of orbital clones with rel. distance < %i km and with rel. velocity < %.1f m/s' % (d_max, v_max)
    plt.title(title)
    plt.xlabel('t [kyr]')
    plt.xlim(0, max(bins))
    plt.ylabel('Number of orbital clones')
    plt.legend()
    plt.show()


def histogram_multi(data=None, d_max=10000, v_max=5):
    # import matplotlib.pyplot as plt
    # plt.interactive(False)
    plt.figure(figsize=(10, 6))

    bins = range(0, 1010, 10)

    for res in data:
        x = []
        for point in res:
            if (point[1] < d_max) and (point[2] < v_max):
                x.append((point[0] * 1000))
        ast_id = res[0][3].split('_')[0] + ' - ' + res[0][4].split('_')[0] + ' (%i)' % len(x)
        # print('(%i points plotted)' % len(x))
        plt.hist(x, bins=bins, alpha=0.7, label=ast_id)

    plt.xlabel('t [kyr]')
    plt.xlim(0, max(bins))
    plt.ylabel('Number of orbital clones')
    plt.legend()
    title = 'Number of orbital clones with rel. distance < %i km and with rel. velocity < %.1f m/s' % (d_max, v_max)

    # title2 = 'Number of orbital clones with rel. distance < %i km and with rel. velocity < %.1f m/s' % (d_max, v_max)
    # title += title2
    # # plt.title('Number of orbital clones with distance < %.0f km and with velocity < %.2f m/s' % (d_max, v_max))
    plt.title(title)
    plt.show()
