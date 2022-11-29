#
# Constant-current constant-voltage charge
#
import pybamm

pybamm.set_logging_level("INFO")

# load model
model = pybamm.lithium_ion.DFN()

# load parameter values
parameter_values = pybamm.ParameterValues.create_from_bpx("example-params.json")

# define experiment
v_min = parameter_values["Lower voltage cut-off [V]"]
v_max = parameter_values["Upper voltage cut-off [V]"]
experiment = pybamm.Experiment(
    [
        (
            f"Discharge at C/5 for 10 hours or until {v_min} V",
            "Rest for 1 hour",
            f"Charge at 1 A until {v_max} V",
            f"Hold at {v_max} V until 10 mA",
            "Rest for 1 hour",
        ),
    ]
    * 2
)

# create simulation 
sim = pybamm.Simulation(model, parameter_values=parameter_values, experiment=experiment)

# solve
sim.solve()

# plot
sim.plot()
