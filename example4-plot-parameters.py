#
# Plot (some) parameters from BPX
#
import matplotlib.pyplot as plt
import numpy as np
import pybamm

# load parameter values
parameter_values = pybamm.ParameterValues.create_from_bpx("example-params.json")

# define stoichiometry ranges
xLi_n_max = parameter_values["Negative electrode maximum stoichiometry"]
xLi_n_min = parameter_values["Negative electrode minimum stoichiometry"]
xLi_n = pybamm.linspace(xLi_n_min, xLi_n_max, 200)
xLi_p_max = parameter_values["Positive electrode maximum stoichiometry"]
xLi_p_min = parameter_values["Positive electrode minimum stoichiometry"]
xLi_p = pybamm.linspace(xLi_p_min, xLi_p_max, 200)

# define concentration ranges
c_n_max = parameter_values["Maximum concentration in negative electrode [mol.m-3]"]
c_p_max = parameter_values["Maximum concentration in positive electrode [mol.m-3]"]
c_n = xLi_n * c_n_max
c_p = xLi_p * c_p_max
c_e = pybamm.linspace(0, 2000, 200)

c_e_ref = parameter_values["Typical electrolyte concentration [mol.m-3]"]
T = parameter_values["Reference temperature [K]"]

# create figure
fig, ax = plt.subplots(4, 2, figsize=(16, 12))

ax[0, 0].plot(
    c_e.entries,
    parameter_values.evaluate(
        parameter_values["Electrolyte conductivity [S.m-1]"](c_e, T)
    ),
)
ax[0, 0].set(xlabel="$c_e$ [mol/m3]", ylabel="$\kappa$ [S.m-1]")
ax[0, 1].plot(
    c_e.entries,
    parameter_values.evaluate(
        parameter_values["Electrolyte diffusivity [m2.s-1]"](c_e, T)
    ),
)
ax[0, 1].set(xlabel="$c_e$ [mol/m3]", ylabel="$D_e$ [S.m-1]")
ax[1, 0].plot(
    xLi_n.entries,
    parameter_values.evaluate(
        parameter_values["Negative electrode diffusivity [m2.s-1]"](xLi_n, T)
    )
    * np.ones_like(xLi_n.entries),
)
ax[1, 0].set(xlabel="sto [-]", ylabel="$D_n$ [S.m-1]")
ax[1, 1].plot(
    xLi_p.entries,
    parameter_values.evaluate(
        parameter_values["Positive electrode diffusivity [m2.s-1]"](xLi_p, T)
    )
    * np.ones_like(xLi_p.entries),
)
ax[1, 1].set(xlabel="sto [-]", ylabel="$D_n$ [S.m-1]")
ax[2, 0].plot(
    xLi_n.entries,
    parameter_values.evaluate(
        parameter_values["Negative electrode exchange-current density [A.m-2]"](
            c_e_ref, c_n, c_n_max, T
        )
    ),
)
ax[2, 0].set(xlabel="sto [-]", ylabel="$j_n$ [A.m-2]")
ax[2, 1].plot(
    xLi_p.entries,
    parameter_values.evaluate(
        parameter_values["Positive electrode exchange-current density [A.m-2]"](
            c_e_ref, c_p, c_p_max, T
        )
    ),
)
ax[2, 1].set(xlabel="sto [-]", ylabel="$j_p$ [A.m-2]")
ax[3, 0].plot(
    xLi_n.entries, parameter_values["Negative electrode OCP [V]"](xLi_n).entries
)
ax[3, 0].set(xlabel="sto [-]", ylabel="$U_n$ [V]")
ax[3, 1].plot(
    xLi_p.entries, parameter_values["Positive electrode OCP [V]"](xLi_p).entries
)
ax[3, 1].set(xlabel="sto [-]", ylabel="$U_p$ [V]")

plt.tight_layout()
plt.show()
