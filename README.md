# battery-interface-api
We made the battery interface simulation based on uinsg the PhaseTree software. Our approach to simulate the battery interface is separated for two steps - material properties explorer using cluster expansion and battery interface simulation using the phase-field simulation. The cluster expansion is a useful tool getting the material properties mostly faster than other atomic simulation tools. The material properties from the cluster expansion simulation shoud be archived for the user and can use it for the phase-field simulation. Phase-field method is a popular tool for simulating the interface of the battery using Finite Element Method (FEM) due to allowing to get clearly separated phase.

This document aims to run the phase-field simulation and how to run this application. User need to follow this simple instruction for running this simulation.
```
    1. Make the JSON file refering to below "Input file description".
    2. Submit the job using battery-interface-api.
        2-1. Check the status of the calculation until the simulation is done.
    3. Retrive the result from the simulation using the battery-interface-api if the simulation is done.
```


# Input file description
User need to make the JSON for running the simulation. The each items shows below.

* "username"
* "password"
* "no_of_cpus": 4,
* "wall_time": "1:12:00:00",
* "job_name": name of the simulation
* "size_x": mesh size of the x-axis. unit: μm
* "size_y": mesh size of the y-axis. unit: μm
* "nx": number of the quad elements along x-axis.
* "ny": number of the quad elements along y-axis.
* "max_time": maximum time to calculate. unit: s
* "interval": time to save the results of simulation. unit: s
* "calc_interval": time interval for running simulation. unit: s
* "overpotential": unit: V
* "temperature": unit: K
* "num_of_electrons": number of electrons in the system.
* "transfer_coefficient": symmetric factor for forward-backward reaction.
* "electrolyte_density": site density of the electrolyte. unit: mol/m³
* "electrode_density": site density of the electrode. unit: mol/m³
* "initial_concentration": initial ion concentration in the bulk electrolyte.
* "electrode_conductivity": conductivity of the electrode. unit: S/m
* "electrolyte_conductivity": conductivity of the electrolyte. unit: S/m
* "exchange_current_density": exchange current density along the interface. unit: mA/cm²
* "barrier_height": barrier height of chemical reaction. unit: J/m³
* "kappa": gradient coefficient for phase-field simulation. unit: J/m
* "interface_mobility": interface mobility passing through the each phases. unit: m³/J⋅s
* "surface_energy": surface energy of the electrode. unit: J/m²
* "diffusivity": ionic diffusivity. unit: m²/s
* "interface_thickness": thickness of the interface. unit: μm

"params" hold the all of the informations of parameter for running simulation. The parameters can be getting from the literature research using the experiments or density functional theory. But, It also can take the parameters from the CLEASE.

## Mesh setup
Battery-interface-api basically operate the simulation on the square domain. We can generate the mesh calculating the FEM problem if user define the size and number of element of the quad element for simulation. 
    
* "size_x" [μm]: size of the domain along x-axis.
* "size_y" [μm]: size of the domain along y-axis.
* "nx": number of the quad elements along x-axis. The element of the x-axis is limited to 100 due to the simulation time.
* "ny": number of the quad elements along y-axis. The element of the y-axis is also limited to 100 due to the simulation time.

## Time calcuation setup
User needs to define the calculation time for determining the time to stop the simulation and take the converged simulation data.

* "max_time" [s]: time to stop the calculation. highly recommend to put lower than 50 s.
* "interval" [s]: time to save the results of simulation. recommend ranges are 0.01 s < "interval" < 0.1 s.
* "calc_interval" [s]: time interval for running simulation. recommend ranges are 0.0001 s < "calc_interval" < 0.01 s.

## External parameters
External physical parameters are the crucial parameter from the outer of the system that determines the physical phenomena like dendrite growth or electrochemical reaction of the phases. We decide two external parameters for running the simulation.

* "overpotential" [V]: overpotential of the system. Highly recommend ranges are -0.30 V < "overpotential" < -0.45 V.
* "temperature" [K]: temperature of the system. Highly recommend ranges are 268 K < "temperature" < 333 K.

## Internal parameters
Internal parameters are defined by material's own properties.

* "electrolyte_density" [mol/m³]: site density of the electrolyte.
* "electrode_density" [mol/m³]: site density of the electrode.
* "electrode_conductivity" [S/m]: conductivity of the electrode.
* "electrolyte_conductivity" [S/m]: conductivity of the electrolyte.
* "surface_energy" [J/m²]: surface energy of the electrode.
* "diffusivity" [m²/s]: ionic diffusivity.

## Electrochemical & phase-field parameters
This kinds of parameters are highly correleated of electrochemical reaction for each chemical phases, or mathmatical parameters describing the phase-field simulatioin.

* "num_of_electrons": number of electrons transferred.
* "transfer_coefficient": symmetric factor for forward-backward reaction.
* "initial_concentration": initial ion concentration in the bulk electrolyte.
* "exchange_current_density" [mA/cm²]: exchange current density along the interface.
* "barrier_height" [J/m³]: barrier height of chemical reaction.
* "kappa" [J/m]: gradient coefficient for phase-field simulation.
* "interface_mobility" [m³/J⋅s]: interface mobility passing through the each phases.

# Using the API

Battery Interface API can be accessed by users with granted permissions. User credentials have to be included in all requests sent to the API.

## Job Submission

Users can submit jobs via command line, e.g.:

```shell
curl -X POST "https://phasetree.ai/api/v1/products/phase-field/battery-interface-submit" -d '{"username": "my-username", ...}'
```

or by editing and then running the provided `submit.py` file in the command line:

```shell
python submit.py
```

Parameters, passed as a JSON string, are described in section [Input file description](#input-file-description).

The response is a JSON object that contains job metadata, including its name, expiration time, status, etc.:

```json
{
  "job_id": "string",
  "job_name": "string",
  "wall_time": "string",
  "status": "string"
  ...
}
```

## Getting Job Status

The status of submitted job(s) can be acquired by sending a request to API endpoint, e.g.:

```shell
curl -X POST "https://phasetree.ai/api/v1/products/phase-field/battery-interface-status" -d '{"username": "my-username", "password": "my-password", "limit": 3}'
```

or by editing and then running the provided `status.py` file in the command line:

```shell
python status.py
```

Request parameters:

```json
{
    "username": "my-username",
    "password": "my-password",
    "limit": 3, # (Optional) Show status of the last 3 jobs
    "job_name": "my-job-name", # (Optional) Show job with given name
    "job_id": "my-job-id", # (Optional) Show job with given id
}
```

The response is a JSON object that contains the same metadata as in [Job submission section](#job-submission).

## Retrieving the Results

Users can retrieve job results by sending a request to API endpoint, e.g.:

```shell
curl -X POST "https://phasetree.ai/api/v1/products/phase-field/battery-interface-retrieve" -d '{"username": "my-username", "password": "my-password", "timestep": 2, "type": "order", "job_name": "my-job-name"}'
```

or by editing and then running the provided `retrieve.py` file in the command line:

```shell
python retrieve.py
```

Request parameters:

```json
{
    "username": "my-username",
    "password": "my-password",
    "timestep": 1,
    "type": "order",
    "job_name": "my-job-name", # (Optional)
    "job_id": "my-job-id", # (Optional)
}
```

Here, `timestep` specifies the step of the time which user want to get the result. and `type` defines `order parameter`, `chemical potential`, `potential` and `coordinates`. The specific types of `order parameter`, `chemical potential` and `potential` have to specify the timestep due to depending on timestep. But `coordinates` does not need to define the timestep due to describing the information regardless of the time.

The response is a JSON object that contains arrays of the each data.

<!-- # Setup environment
The application is operated with PhaseTree software on the internet. So you must be connected on internet. Hghly recommend to install Python 3.6 or newer. -->

# Acknowledge
```
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 957189. The project is part of BATTERY 2030+, the large-scale European research initiative for inventing the sustainable batteries of the future. 
```