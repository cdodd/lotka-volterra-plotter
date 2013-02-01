#!/usr/bin/env python

# Python standard library modules
import sys

# 3rd party modules
import matplotlib
import matplotlib.backends.backend_qt4agg as backend_qt4agg
from matplotlib.figure import Figure
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

# Local application modules
from growth_calculator import GrowthCalculator
from options_menu import OptionsMenu
import resources

APP_NAME = 'Lotka-Volterra Plotter'
AUTHOR = 'Craig Dodd'


class AppForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        # Set the window title
        self.setWindowTitle(APP_NAME)

        # Create the options menu in a dock widget
        self.options_menu = OptionsMenu()
        dock = QtGui.QDockWidget('Options', self)
        dock.setFeatures(
            QtGui.QDockWidget.NoDockWidgetFeatures |
            QtGui.QDockWidget.DockWidgetMovable |
            QtGui.QDockWidget.DockWidgetFloatable
        )
        dock.setAllowedAreas(
            QtCore.Qt.LeftDockWidgetArea | QtCore.Qt.RightDockWidgetArea,
        )
        dock.setWidget(self.options_menu)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)

        # Connect the signals from the options menu
        self.connect(self.options_menu.update_btn, QtCore.SIGNAL(
            'clicked()'),
            self.calculate_data,
        )
        self.connect(self.options_menu.clear_graph_btn, QtCore.SIGNAL(
            'clicked()'),
            self.clear_graph,
        )
        self.connect(self.options_menu.legend_cb, QtCore.SIGNAL(
            'stateChanged(int)'),
            self.redraw_graph,
        )
        self.connect(self.options_menu.grid_cb, QtCore.SIGNAL(
            'stateChanged(int)'),
            self.redraw_graph,
        )
        self.connect(self.options_menu.legend_loc_cb, QtCore.SIGNAL(
            'currentIndexChanged(int)'),
            self.redraw_graph,
        )

        # Create the graph plot
        fig = Figure((7.0, 3.0), dpi=100)
        self.canvas = backend_qt4agg.FigureCanvasQTAgg(fig)
        self.canvas.setParent(self)
        self.axes = fig.add_subplot(111)
        backend_qt4agg.NavigationToolbar2QTAgg(self.canvas, self.canvas)

        # Initialize the graph
        self.clear_graph()

        # Set the graph as the main window widget
        self.setCentralWidget(self.canvas)

        # Create menubar actions
        file_exit_action = QtGui.QAction('E&xit', self)
        file_exit_action.setToolTip('Exit')
        file_exit_action.setIcon(QtGui.QIcon(':/resources/door_open.png'))
        self.connect(
            file_exit_action,
            QtCore.SIGNAL('triggered()'),
            self.close,
        )

        about_action = QtGui.QAction('&About', self)
        about_action.setToolTip('About')
        about_action.setIcon(QtGui.QIcon(':/resources/icon_info.gif'))
        self.connect(
            about_action,
            QtCore.SIGNAL('triggered()'),
            self.show_about,
        )

        # Create the menubar
        file_menu = self.menuBar().addMenu('&File')
        file_menu.addAction(file_exit_action)

        help_menu = self.menuBar().addMenu('&Help')
        help_menu.addAction(about_action)

    def calculate_data(self):
        # Create a GrowthCalculator object
        growth = GrowthCalculator()

        # Update the GrowthCalculator parameters from the GUI options
        growth.a = self.options_menu.a_sb.value()
        growth.b = self.options_menu.b_sb.value()
        growth.c = self.options_menu.c_sb.value()
        growth.d = self.options_menu.d_sb.value()
        growth.predators = self.options_menu.predator_sb.value()
        growth.prey = self.options_menu.prey_sb.value()
        growth.iterations = self.options_menu.iterations_sb.value()
        growth.dt = self.options_menu.timedelta_sb.value()

        # Calculate the population growths
        results = growth.calculate()
        self.predator_history.extend(results['predator'])
        self.prey_history.extend(results['prey'])

        # Put the latest population sizes into the options toolbar
        self.options_menu.predator_sb.setValue(self.predator_history[-1])
        self.options_menu.prey_sb.setValue(self.prey_history[-1])

        # Redraw the graph
        self.redraw_graph()

    def clear_graph(self):
        # Clear the population histories
        self.predator_history = []
        self.prey_history = []

        # Redraw the graph
        self.redraw_graph()

    def redraw_graph(self):
        # Clear the graph
        self.axes.clear()

        # Create the graph labels
        self.axes.set_title('Predator & Prey Growth Cycles')
        self.axes.set_xlabel('Iterations')
        self.axes.set_ylabel('Population Size')

        # Plot the current population data
        if self.predator_history:
            self.axes.plot(self.predator_history, 'r-', label='Predator')
        if self.prey_history:
            self.axes.plot(self.prey_history, 'b-', label='Prey')

        # Create the legend if necessary
        if self.options_menu.legend_cb.isChecked():
            if self.predator_history or self.prey_history:
                legend_loc = str(
                    self.options_menu.legend_loc_cb.currentText()
                ).lower()
                legend = matplotlib.font_manager.FontProperties(size=10)
                self.axes.legend(loc=legend_loc, prop=legend)

        # Set the grid lines if necessary
        self.axes.grid(self.options_menu.grid_cb.isChecked())

        # Draw the graph
        self.canvas.draw()

    def show_about(self):
        """
        Display the "about" dialog box.
        """
        message = '''<font size="+2">%s</font>
            <p>A Lotka-Volterra Plotter written in Python.
            <p>Written by %s,
            <a href="http://opensource.org/licenses/MIT">MIT Licensed</a>
            <p>Icons from <a href="http://www.famfamfam.com/">famfamfam</a> and
            <a href="http://commons.wikimedia.org/">Wikimedia
            Commons</a>.''' % (APP_NAME, AUTHOR)

        QtGui.QMessageBox.about(self, 'About ' + APP_NAME, message)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/resources/icon.svg'))
    form = AppForm()
    form.show()
    app.exec_()
