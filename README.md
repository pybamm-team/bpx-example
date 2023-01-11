# 🔋 PyBaMM BPX example
An example repository showing how to import parameters defined using the [BPX standard](https://github.com/pybamm-team/BPX). To try out the examples locally on your own machine follow the installation instructions below.

The simplest way to use BPX parameters in PyBaMM is to run a 1C constant-current discharge with a model of your choice with all the default settings and load the BPX JSON file:
```python3
import pybamm
model = pybamm.lithium_ion.DFN()  # Doyle-Fuller-Newman model
parameter_values = pybamm.ParameterValues.create_from_bpx("example-params.json")
sim = pybamm.Simulation(model, parameter_values=parameter_values)
sim.solve([0, 3600])  # solve for 1 hour
sim.plot()
```

## 💻 About PyBaMM
The example simulations use the package [PyBaMM](www.pybamm.org) (Python Battery Mathematical Modelling). PyBaMM (Python Battery Mathematical Modelling) is an open-source battery simulation package
written in Python. Our mission is to accelerate battery modelling research by
providing open-source tools for multi-institutional, interdisciplinary collaboration.
Broadly, PyBaMM consists of
(i) a framework for writing and solving systems
of differential equations,
(ii) a library of battery models and parameters, and
(iii) specialized tools for simulating battery-specific experiments and visualizing the results.
Together, these enable flexible model definitions and fast battery simulations, allowing users to
explore the effect of different battery designs and modeling assumptions under a variety of operating scenarios.

## 🚀 Installation
In order to run the examples in this repository you will need to install [PyBaMM](https://github.com/pybamm-team/PyBaMM) (version 22.12 or newer) and [BPX](https://github.com/pybamm-team/BPX). 

We recommend installing within a [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to not alter any python distribution files on your machine.

PyBaMM is available on GNU/Linux, MacOS and Windows. For more detailed instructions on how to install PyBaMM, see [the PyBaMM documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#user-install).

### Linux/Mac OS
To install the requirements on Linux/Mac OS use the following terminal commands:

1. Clone the repository
```bash
git clone https://github.com/pybamm-team/bpx-example
```
2. Change into the `bpx-example` directory 
```bash
cd bpx-example
```
3. Create a virtual environment
```bash
virtualenv env
```
4. Activate the virtual environment 
```bash
source env/bin/activate
```
5. Install the required packages
```bash 
pip install -r requirements.txt
```

### Windows
To install the requirements on Windows use the following commands:

1. Clone the repository
```bash
git clone https://github.com/pybamm-team/bpx-example
```
2. Change into the `bpx-example` directory 
```bash
cd bpx-example
```
3. Create a virtual environment
```bash
python -m virtualenv env
```
4. Activate the virtual environment 
```bash
\path\to\env\Scripts\activate
```
where `\path\to\env` is the path to the environment created in step 3 (e.g. `C:\Users\'Username'\env\Scripts\activate.bat`).

5. Install the required packages
```bash 
pip install -r requirements.txt
```

As an alternative, you can set up [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about). This allows you to run a full Linux distribution within Windows.

### Troubleshooting

**Problem:** `ModuleNotFoundError: No module named 'wheel'`.

**Solution:** Use the command `pip install wheel` before installing the requirements.

**Problem:** error: unable to create file "...": Filename too long. fatal: unable to checkout working tree

**Solution:** 1. [Configure Windows to accept long file paths](https://thegeekpage.com/make-windows-11-accept-file-paths-over-260-characters/). 2. Configure git client to accept long paths: `git config --global core.longpaths true`
