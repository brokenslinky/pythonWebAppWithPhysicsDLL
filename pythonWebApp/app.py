

rate = 49033.
dampingRatio = 0.
mass = 272.2

import os
import json

from flask import Flask, Response, flash, request, render_template
app = Flask(__name__)
app._static_folder = os.path.abspath('./static')


@app.route('/dampingRatio', methods= ['POST', 'GET'])
def changeDamping():
    print(request)
    global dampingRatio
    dampingRatio = float(request.form.get('ratio'))
    return str(dampingRatio)

@app.route('/rate', methods = ['POST', 'GET'])
def changeRate():
    global rate
    rate = float(request.form.get('rate'))
    return str(rate)

@app.route('/mass', methods = ['POST', 'GET'])
def changeMass():
    global mass
    mass = float(request.form.get('mass'))
    return str(mass)

import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import sys
import clr
clr.AddReference(os.path.dirname(os.path.abspath( __file__ )) + "/Physics.dll")
from Physics import *
clr.AddReference('System.Collections')
from System.Collections.Generic import List
@app.route('/plot.png')
def test():
    mass = float(request.args.get('mass'))
    rate = float(request.args.get('rate'))
    dampingRatio = float(request.args.get('ratio'))

    particle = Particle(Mass(mass))
    earth = Particle(Mass(5.972E24))
    tmpList = List[float]()
    tmpList.Add(1.)
    tmpList.Add(0.)
    tmpList.Add(0.)
    particle.position = Displacement(tmpList)

    spring = Spring(particle, earth, rate)
    damper = Damper(particle, earth, dampingRatio, rate)
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

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/Oscillator')
def oscillator():
    return render_template('getInputs.html')

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 1337)