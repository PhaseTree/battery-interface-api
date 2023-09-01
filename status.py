from json import dumps
from urllib import request

params = {
    "username": "my-username",
    "password": "my-password",
    "limit": 3,  # (Optional) Show status of the last 3 jobs
    "job_name": "my-job-name",  # (Optional)
    "job_id": "my-job-id",  # (Optional)
}

req = request.Request(
    "https://phasetree.ai/api/v1/products/phase-field/battery-interface-status",
    data=str(dumps(params)).encode(),
)

with request.urlopen(req) as res:
    output = res.read().decode()

print(output)
