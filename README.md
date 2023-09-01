# battery-interface-api
We made the battery interface simulation based on uinsg the PhaseTree software. Our approach to simulate the battery interface is separated for two steps - material properties explorer using cluster expansion and battery interface simulation using the phase-field simulation. The cluster expansion is a useful tool getting the material properties mostly faster than other atomic simulation tools. The material properties from the cluster expansion simulation shoud be archived for the user and can use it for the phase-field simulation. Phase-field method is a popular tool for simulating the interface of the battery using Finite Element Method (FEM) due to allowing to run clear phase separate simulation. 

This document aims to run the phase-field simulation and how to run this application. User need to follow this simple instruction for running this simulation.
```
    1. Make the JSON file refering to below "Input file description".
    2. Submit the job using battery-interface-api.
        2-1. Check the status of the calculation until the simulation is done.
    3. Retrive the result from the simulation using the battery-interface-api if the simulation is done.
```


# Input file description
User need to make the JSON for running the simulation. The each items shows below.
```
    - "params"
    -- "size_x": mesh size of the x-axis. unit: μm
    -- "size_y": mesh size of the y-axis. unit: μm
    -- "nx": number of the quad elements along x-axis.
    -- "ny": number of the quad elements along y-axis.
    -- "max_time": maximum time to calculate. unit: s
    -- "save_time_interval": time to save the results of simulation. unit: s
    -- "overpotential": unit: V
    -- "temperature": unit: K
    -- "num.electron": number of electrons in the system.
    -- "alpha": symmetric factor for forward-backward reaction.
    -- "interval": time interval for running simulation. unit: s
    -- "electrolyte_density": site density of the electrolyte. unit: mol/m³
    -- "Initial_concentration": initial ion concentration in the bulk electrolyte.
    -- "electrode_conductivity": conductivity of the electrode. unit: S/m
    -- "electrolyte_conductivity": conductivity of the electrolyte. unit: S/m
    -- "exchange_current_density": exchange current density along the interface. unit: mA/cm²
    -- "B": barrier height of chemical reaction. unit: J/m³
    -- "kappa": graidient coefficient for phase-field simulation. unit: J/m
    -- "m_int": interface mobility passing through the each phases. unit: m³/J⋅s
    -- "surface_e": surface energy of the electrode. unit: J/m²
    -- "diffusivity": ionic diffusivity. unit: m²/s
```
"params" hold the all of the items of parameter for running simulation. The parameters can be getting from the literature research using the experiments or density functional theory. But, It also can take the parameters from the CLEASE.

# Setup environment
The application is operated with PhaseTree software on the internet. So you must be connected on internet. Hghly recommend to install Python 3.6 or newer.

# 