import os

import grpc

from grpc_generated_files import auth_pb2, auth_pb2_grpc


class GatewayClient:
    service = os.environ.get('AUTH_SVC_ADDRESS', 'localhost:9999')

    def __init__(self, service=service):
        self.service = service

        self.channel = grpc.insecure_channel(service)
        self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)

    def register(self, username, password, email):
        print("GatewayClient send request")
        register_request = auth_pb2.RegisterUserRequest(username=username, password=password, email=email)
        response = self.stub.register(request=register_request)
        return response

# class AuthClient:
#     service = os.environ.get('USER_SVC_ADDRESS', 'localhost:9998')
#
#     def __init__(self, service=service):
#         print(28, service)
#         self.service = service
#         self.channel = grpc.insecure_channel(service)
#         self.stub = auth_pb2_grpc.AuthServiceStub(self.channel)
#
#     def check_username(self, username):
#         print("AuthClient send request")
#         request = auth_pb2.CheckUsernameRequest(username=username)
#         return self.stub.check_username(request=request)
