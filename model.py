import numpy as np
import matplotlib.pyplot as plt
# import inspect
# inspect.getsource(<function>)

xd = np.array([  0. ,   0.5,   1. ,   1.5,   2. ,   2.5,   3. ,   3.5,   4. ,
         4.5,   5. ,   5.5,   6. ,   6.5,   7. ,   7.5,   8. ,   8.5,
         9. ,   9.5,  10. ])

yd = np.array([ 161.78587909,  132.72560763,  210.81767421,  179.6837026 ,
        181.98528167,  234.67907351,  246.48971034,  221.58691239,
        250.3924093 ,  206.43287615,  303.75089312,  312.29865056,
        323.8331032 ,  261.9686295 ,  316.64806585,  337.55295912,
        360.13633529,  369.72729852,  408.0289548 ,  348.82736117,
        394.93384188])

def plot_data(x, y):
    fig, axis = plt.subplots(figsize=(8, 6))
    axis.plot(x, y, color='black', linestyle=' ', marker='o')
    axis.grid(True, which='both')
    axis.axhline(0, color='black')
    axis.axvline(0, color='black')
    axis.set_ylim([-5*50, 15*50])
    axis.set_xlim([-5, 15])
    # and more
    return fig

def model(x, a0=3, a1=2, a2=0):
    return a0 + (a1*x) + (a2*x**2)

def plot_data_with_model(xd, yd, ym):
    fig = plot_data(xd, yd)
    fig.axes[0].plot(xd, ym, color='red')
    plt.show()
    return fig

a0 = 150
a1 = 25
ym = model(xd, a0, a1)

fig = plot_data_with_model(xd, yd, ym)