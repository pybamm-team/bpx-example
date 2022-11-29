# 🔋 PyBaMM BPX example
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pybamm-team/bpx-example/blob/main/)

An example repository showing how to import parameters defined using the [BPX standard](https://github.com/pybamm-team/BPX). To try out the examples locally on your own machine follow the installation instructions below.


## 💻 About PyBaMM
The example simulations use the package [PyBaMM](www.pybamm.org) (Python Battery Mathematical Modelling). PyBaMM solves physics-based electrochemical DAE models by using state-of-the-art automatic differentiation and numerical solvers. The Doyle-Fuller-Newman model can be solved in under 0.1 seconds, while the reduced-order Single Particle Model and Single Particle Model with electrolyte can be solved in just a few milliseconds. Additional physics can easily be included such as thermal effects, fast particle diffusion, 3D effects, and more. All models are implemented in a flexible manner, and a wide range of models and parameter sets (NCA, NMC, LiCoO2, ...) are available. There is also functionality to simulate any set of experimental instructions, such as CCCV or GITT, or specify drive cycles.

## 🚀 Installation
In order to run the examples in this repository you will need to install [PyBaMM](https://github.com/pybamm-team/PyBaMM) and [BPX](https://github.com/pybamm-team/BPX). Note that at present the functionality to load in BPX parameters is not included in the latest release of PyBaMM, so for now we must install from a specific branch as specified in `requirements.txt`.

We recommend installing within a [virtual environment](https://docs.python.org/3/tutorial/venv.html) in order to not alter any python distribution files on your machine.

PyBaMM is available on GNU/Linux, MacOS and Windows. For more detailed instructions on how to install PyBaMM, see [the PyBaMM documentation](https://pybamm.readthedocs.io/en/latest/install/GNU-linux.html#user-install).

### Linux/Mac OS
To install the requirements on Linux/Mac OS use the following terminal commands:

1. Clone the repository
```bash
https://github.com/pybamm-team/bpx-example
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
https://github.com/pybamm-team/bpx-example
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
