# Lotka-Volterra Plotter

[![Build Status](https://travis-ci.org/cdodd/lotka-volterra-plotter.svg?branch=master)](https://travis-ci.org/cdodd/lotka-volterra-plotter)

## So, what is it?
This is a simple graphing tool that plots the [Lotka-Volterra equation](http://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation),
with adjustable coeffecients.

I wrote this as an exercise when learning the matplotlib module.

## Installation
This program uses Python with the PyQt4 and matplotlib modules. It has been
tested to work on Ubuntu 13.10, running Python 2.7.5 (stock Ubuntu Python),
PyQt4 4.10.3 and matplotlib 1.2.1.

It has also been tested to work on Ubuntu 13.10, running Python 3.3.2, PyQt4
4.10.3 and matplotlib 1.2.1.

To download and run the program on Ubuntu (assuming you alredy have Git
installed) run the following commands:

```
sudo apt-get install -y python-qt4 python-matplotlib
git clone https://github.com/cdodd/lotka-volterra-plotter.git
lotka-volterra-plotter/lotka_volterra_plotter.py &
```

## Screenshot
![](https://raw.github.com/cdodd/Lotka-Volterra-Plotter/master/screenshot.png)
