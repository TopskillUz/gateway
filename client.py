import os

import grpc

from grpc_generated_files import auth_pb2, auth_pb2_grpc


class GatewayClient:
    service = os.environ.get('AUTH_SVC_ADDRESS', 'localhost:9999')

    def __init__(self, service=service):
        self.service = service
        self.channel = grpc.insecure_channel(service)
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    async def register(self, email: str, password: str, phone: str, last_name: str, first_name: str, middle_name: str):
        print("GatewayClient send request")
        register_request = auth_pb2.RegisterUserRequest(password=password, email=email, phone=phone,
                                                        last_name=last_name, first_name=first_name,
                                                        middle_name=middle_name)
        response = self.stub.register(request=register_request)
        return response

    async def login(self, email: str, password: str):
        print("GatewayClient send request")
        request = auth_pb2.LoginRequest(password=password, email=email)
        return self.stub.login(request=request)

    async def get_refresh_token(self, refresh_token: str):
        print("GatewayClient send request")
        request = auth_pb2.RefreshTokenRequest(refresh_token=refresh_token)
        return self.stub.refresh_token(request=request)

    async def validate_access_token(self, access_token: str):
        print("GatewayClient send request")
        request = auth_pb2.ValidateTokenRequest(access_token=access_token)
        return self.stub.validate_access_token(request=request)