from fastapi import Depends, HTTPException, status

from client import GatewayClient
from services.auth.oauth2 import reuseable_oauth


async def require_user(token: str = Depends(reuseable_oauth)):
    gateway_client = GatewayClient()
    response = await gateway_client.validate_access_token(access_token=token)
    if response.status_code == 200:
        return response.success_payload
    else:
        raise HTTPException(status_code=response.status_code, detail=response.error_payload)
