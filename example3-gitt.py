#
# GITT discharge
#
import pybamm

pybamm.set_logging_level("INFO")

# load model
model = pybamm.lithium_ion.DFN()

# load parameter values
parameter_values = pybamm.ParameterValues.create_from_bpx("example-params.json")

# define experiment
experiment = pybamm.Experiment(
    [("Discharge at C/20 for 1 hour", "Rest for 1 hour")] * 20,
)

# create simulation 
sim = pybamm.Simulation(model, parameter_values=parameter_values, experiment=experiment)

# solve
sim.solve()

# plot
sim.plot()
