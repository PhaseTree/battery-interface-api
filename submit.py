from json import dumps
from urllib import request

params = {
    "username": "my-username",
    "password": "my-password",
    "job_name": "my-job-name",
    "no_of_cpus": 4,
    "wall_time": "1:12:00:00",
    "size_x": 30,
    "size_y": 30,
    "nx": 30,
    "ny": 30,
    "calc_interval": 0.001,
    "max_time": 1,
    "interval": 0.1,
    "num_of_electrons": 1,
    "electrolyte_density": 76400,
    "electrode_density": 14400,
    "initial_concentration": 0.07,
    "electrode_conductivity": 11000000,
    "electrolyte_conductivity": 1.0,
    "exchange_current_density": 6,
    "kappa": 0.8,
    "diffusivity": 30000000,
    "overpotential": -0.4,
    "temperature": 300,
    "interface_mobility": 0.0000025,
    "surface_energy": 0.490,
    "interface_thickness": 1,
    "barrier_height": 6000000,
    "transfer_coefficient": 0.5,
}

req = request.Request(
    "https://phasetree.ai/api/v1/products/phase-field/battery-interface-submit",
    data=str(dumps(params)).encode(),
)

with request.urlopen(req) as res:
    output = res.read().decode()

print(output)
