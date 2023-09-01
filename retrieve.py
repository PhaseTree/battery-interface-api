from json import dumps
from urllib import request

params = {
    "username": "my-username",
    "password": "my-password",
    "timestep": 1,
    "type": "order",  # pot | chem | order | coordinate
    "job_name": "my-job-name",  # (Optional)
    "job_id": "my-job-id",  # (Optional)
}

req = request.Request(
    "https://phasetree.ai/api/v1/products/phase-field/battery-interface-retrieve",
    data=str(dumps(params)).encode(),
)

with request.urlopen(req) as res:
    output = res.read().decode()

print(output)
