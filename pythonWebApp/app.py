from flask import Flask, Response
app = Flask(__name__)

import os
import clr
clr.AddReference(os.path.dirname(os.path.abspath( __file__ )) + "/Physics.dll")

import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from Physics import *
clr.AddReference('System.Collections')
from System.Collections.Generic import List

@app.route('/plot.png')
@app.route('/')
def test():
    particle = Particle(Mass(272.2))
    earth = Particle(Mass(5.972E24))
    tmpList = List[float]()
    tmpList.Add(1.)
    tmpList.Add(0.)
    tmpList.Add(0.)
    particle.position = Displacement(tmpList)

    spring = Spring(particle, earth, 49033.)
    damper = Damper(particle, earth, 0.25, 49033.)
    tmpList = List[Interaction]()
    tmpList.Add(spring)
    tmpList.Add(damper)
    particle.interactions = tmpList
    tmpList = List[Particle]()
    tmpList.Add(particle)
    tmpList.Add(earth)
    syst = PhysicalSystem(tmpList)

    t = [0.]
    y = [particle.position.values[0]]
    timestep = 0.001
    for step in range(1000):
        syst.Iterate(Time(timestep))
        t.append(step * timestep)
        y.append(syst.particles[0].position.values[0])

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(t, y)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)