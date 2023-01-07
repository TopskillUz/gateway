import uvicorn
from fastapi import FastAPI, status, Response
import schemas

from client import GatewayClient
from grpc_generated_files import auth_pb2, auth_pb2_grpc

app = FastAPI()


@app.post("/register", status_code=status.HTTP_201_CREATED)
def register(payload: schemas.RegisterSchema, response: Response):
    gateway_client = GatewayClient()

    resp = gateway_client.register(
        username=payload.username,
        password=payload.password,
        email=payload.email)
    response.status_code = resp.status_code
    print(response)
    if not resp.error:
        user = resp.success_payload
        return schemas.RegisterResponseSchema(id=user.id, username=user.username, email=user.email)
    else:
        return {'error': resp.error_payload}
    # auth_client = AuthClient()
    #
    # resp = auth_client.check_username(payload.username)
    # print(29, resp.value)
    # if not bool(resp.value):
    #     # user = auth_pb2.User(id=1, username=payload.username, password=payload.password, email=payload.email)
    #     # response = auth_pb2.RegisterUserResponse(
    #     #     success_payload=user,
    #     #     error=False,
    #     #     status_code=200,
    #     # )
    #     return {'status': 'ok'}


if __name__ == '__main__':
    uvicorn.run("__main__:app", host='0.0.0.0', port=8080, reload=True, workers=1)
