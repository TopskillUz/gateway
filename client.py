import os

import grpc

import auth_pb2, auth_pb2_grpc


class GatewayClient:
    auth_host = os.environ.get('AUTH_HOST', 'localhost')

    def __init__(self, host=auth_host, server_port=9999):
        self.host = host
        self.server_port = server_port

        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    def register(self, username, password, email):
        print("GatewayClient send request")
        register_request = auth_pb2.RegisterUserRequest(username=username, password=password, email=email)
        response = self.stub.register(request=register_request)
        return response
