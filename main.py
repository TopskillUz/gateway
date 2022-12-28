import uvicorn
from fastapi import FastAPI, status, Response
import schemas

from client import GatewayClient

app = FastAPI()


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: schemas.RegisterSchema, response: Response):
    gateway_client = GatewayClient()

    resp = gateway_client.register(
        username=payload.username,
        password=payload.password,
        email=payload.email)
    response.status_code = resp.status_code

    if not resp.error:
        user = resp.success_payload
        return schemas.RegisterResponseSchema(id=user.id, username=user.username, email=user.email)
    else:
        return {'error': resp.error_payload}


if __name__ == '__main__':
    uvicorn.run("__main__:app", host='0.0.0.0', port=8000, reload=True, workers=1)
