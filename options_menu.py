# 3rd party modules
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui


class OptionsMenu(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # Create the "Lotka-Volterra Coefficients" options
        self.a_sb = QtGui.QDoubleSpinBox()
        self.b_sb = QtGui.QDoubleSpinBox()
        self.c_sb = QtGui.QDoubleSpinBox()
        self.d_sb = QtGui.QDoubleSpinBox()

        for widget in (self.a_sb, self.b_sb, self.c_sb, self.d_sb):
            widget.setRange(0, 10)
            widget.setSingleStep(0.1)

        coeff_grid = QtGui.QGridLayout()
        coeff_grid.addWidget(QtGui.QLabel('Prey Growth Rate'), 0, 0)
        coeff_grid.addWidget(self.a_sb, 0, 1)
        coeff_grid.addWidget(QtGui.QLabel('Predation Death Rate'), 1, 0)
        coeff_grid.addWidget(self.b_sb, 1, 1)
        coeff_grid.addWidget(QtGui.QLabel('Predator Death Rate'), 2, 0)
        coeff_grid.addWidget(self.c_sb, 2, 1)
        coeff_grid.addWidget(QtGui.QLabel('Predator Reproduction Rate'), 3, 0)
        coeff_grid.addWidget(self.d_sb, 3, 1)

        coeff_gb = QtGui.QGroupBox('Lotka-Volterra Coefficients:')
        coeff_gb.setLayout(coeff_grid)

        # Create the "Other Parameters" options
        self.predator_sb = QtGui.QDoubleSpinBox()
        self.predator_sb.setRange(0, 100000)
        self.predator_sb.setSingleStep(1)

        self.prey_sb = QtGui.QDoubleSpinBox()
        self.prey_sb.setRange(0, 100000)
        self.prey_sb.setSingleStep(1)

        self.iterations_sb = QtGui.QSpinBox()
        self.iterations_sb.setRange(0, 100000)
        self.iterations_sb.setSingleStep(100)

        self.timedelta_sb = QtGui.QDoubleSpinBox()
        self.timedelta_sb.setRange(0, 100)
        self.timedelta_sb.setSingleStep(0.05)

        other_grid = QtGui.QGridLayout()
        other_grid.addWidget(QtGui.QLabel('Predator Population'), 0, 0)
        other_grid.addWidget(self.predator_sb, 0, 1)
        other_grid.addWidget(QtGui.QLabel('Prey Population'), 1, 0)
        other_grid.addWidget(self.prey_sb, 1, 1)
        other_grid.addWidget(QtGui.QLabel('Iterations'), 2, 0)
        other_grid.addWidget(self.iterations_sb, 2, 1)
        other_grid.addWidget(QtGui.QLabel('Time Delta'), 3, 0)
        other_grid.addWidget(self.timedelta_sb, 3, 1)

        other_gb = QtGui.QGroupBox('Other Parameters:')
        other_gb.setLayout(other_grid)

        # Create the "Graph Options" options
        self.legend_cb = QtGui.QCheckBox('Show Legend')
        self.legend_cb.setChecked(True)
        self.connect(self.legend_cb, QtCore.SIGNAL(
            'stateChanged(int)'),
            self.legend_change,
        )
        self.grid_cb = QtGui.QCheckBox('Show Grid')
        self.grid_cb.setChecked(True)
        self.legend_loc_lbl = QtGui.QLabel('Legend Location')
        self.legend_loc_cb = QtGui.QComboBox()
        self.legend_loc_cb.addItems([x.title() for x in [
            'right',
            'center',
            'lower left',
            'center right',
            'upper left',
            'center left',
            'upper right',
            'lower right',
            'upper center',
            'lower center',
            'best',
        ]])
        self.legend_loc_cb.setCurrentIndex(6)

        cb_box = QtGui.QHBoxLayout()
        cb_box.addWidget(self.legend_cb)
        cb_box.addWidget(self.grid_cb)

        legend_box = QtGui.QHBoxLayout()
        legend_box.addWidget(self.legend_loc_cb)
        legend_box.addStretch()

        graph_box = QtGui.QVBoxLayout()
        graph_box.addLayout(cb_box)
        graph_box.addWidget(self.legend_loc_lbl)
        graph_box.addLayout(legend_box)

        graph_gb = QtGui.QGroupBox('Graph Options:')
        graph_gb.setLayout(graph_box)

        # Create the update/reset buttons
        self.update_btn = QtGui.QPushButton(
            QtGui.QIcon(':/resources/calculator.png'),
            'Run Iterations',
        )
        self.reset_values_btn = QtGui.QPushButton(
            QtGui.QIcon(':/resources/arrow_undo.png'),
            'Reset Values',
        )
        self.clear_graph_btn = QtGui.QPushButton(
            QtGui.QIcon(':/resources/chart_line_delete.png'),
            'Clear Graph',
        )
        self.connect(self.reset_values_btn, QtCore.SIGNAL(
            'clicked()'),
            self.reset_values,
        )

        # Create the main layout
        container = QtGui.QVBoxLayout()
        container.addWidget(coeff_gb)
        container.addWidget(other_gb)
        container.addWidget(graph_gb)
        container.addWidget(self.update_btn)
        container.addStretch()
        container.addWidget(self.reset_values_btn)
        container.addWidget(self.clear_graph_btn)
        self.setLayout(container)

        # Populate the widgets with values
        self.reset_values()

    def reset_values(self):
        """
        Sets the default values of the option widgets.
        """
        self.a_sb.setValue(1.0)
        self.b_sb.setValue(0.1)
        self.c_sb.setValue(1.0)
        self.d_sb.setValue(0.075)
        self.predator_sb.setValue(5)
        self.prey_sb.setValue(10)
        self.iterations_sb.setValue(1000)
        self.timedelta_sb.setValue(0.02)

    def legend_change(self):
        self.legend_loc_cb.setEnabled(self.legend_cb.isChecked())
        self.legend_loc_lbl.setEnabled(self.legend_cb.isChecked())
