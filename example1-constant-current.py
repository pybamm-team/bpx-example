#
# Constant-current discharge
#
import pybamm

pybamm.set_logging_level("INFO")

# load model
model = pybamm.lithium_ion.DFN()

# load parameter values
parameter_values = pybamm.ParameterValues.create_from_bpx("example-params.json")

# create simulation (default is a 1C constant current discharge)
sim = pybamm.Simulation(model, parameter_values=parameter_values)

# solve for 1 hour
sim.solve([0, 3600])

# plot
sim.plot()
