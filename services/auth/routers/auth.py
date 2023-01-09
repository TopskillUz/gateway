from fastapi import APIRouter, status, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm

from client import GatewayClient
from services.auth import schemas

auth_router = APIRouter()


@auth_router.post("/jwt/register", summary="Register new user API", responses={
    status.HTTP_201_CREATED: {"model": schemas.RegisterResponseSchema},
    status.HTTP_400_BAD_REQUEST: {"model": schemas.RPCErrorSchema},
})
async def register(payload: schemas.RegisterSchema, response: Response):
    gateway_client = GatewayClient()

    resp = await gateway_client.register(
        email=payload.email,
        password=payload.password,
        phone=payload.phone,
        last_name=payload.last_name,
        first_name=payload.first_name,
        middle_name=payload.middle_name
    )
    response.status_code = resp.status_code
    if not resp.error:
        user = resp.success_payload
        return schemas.RegisterResponseSchema(id=user.id, email=user.email, phone=user.phone, last_name=user.last_name,
                                              first_name=user.first_name, middle_name=user.middle_name)
    else:
        return schemas.RPCErrorSchema(error=resp.error_payload)


@auth_router.post('/jwt/login', summary="Login API", responses={
    status.HTTP_200_OK: {"model": schemas.RegisterResponseSchema},
    status.HTTP_400_BAD_REQUEST: {"model": schemas.RPCErrorSchema},
})
async def login(response: Response, payload: OAuth2PasswordRequestForm = Depends()):
    gateway_client = GatewayClient()

    resp = await gateway_client.login(
        email=payload.username,
        password=payload.password)
    response.status_code = resp.status_code
    if not resp.error:
        tokens = resp.success_payload
        return schemas.TokenSchema(
            access_token=tokens.access_token,
            refresh_token=tokens.refresh_token,
        )
    else:
        return schemas.RPCErrorSchema(error=resp.error_payload)


@auth_router.post('/jwt/refresh', summary="Refresh access token API", responses={
    status.HTTP_200_OK: {"model": schemas.RefreshTokenResponseSchema},
    status.HTTP_400_BAD_REQUEST: {"model": schemas.RPCErrorSchema},
})
async def refresh_token(response: Response, payload: schemas.RefreshTokenSchema):
    gateway_client = GatewayClient()

    resp = await gateway_client.get_refresh_token(
        refresh_token=payload.refresh_token)
    response.status_code = resp.status_code
    if not resp.error:
        access_token = resp.success_payload.access_token
        return schemas.RefreshTokenResponseSchema(
            access_token=access_token,
        )
    else:
        return schemas.RPCErrorSchema(error=resp.error_payload)
