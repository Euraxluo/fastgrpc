from fastapi import FastAPI
import uvicorn

from fastgrpc import FastgRPC
from typing import Optional

http = FastAPI(debug=True)

# def http_server(*args, **kwargs):
#     kwargs['http'] = {
#         'app': http,
#         'host': 'localhost',
#         'port': 8088
#     }
#     http_server = Process(target=uvicorn.run, kwargs=kwargs['http'])
#     http_server.start()

app = FastgRPC()

import example_pb2, example_pb2_grpc, test_pb2, test_pb2_grpc


@app.api(
    example_pb2_grpc.ExampleServicer.getGithubUrl,
    example_pb2.request,
    example_pb2.userGithub,
)
def getGithubUrl(name: str, github: str) -> str:
    return name + '@' + github


import requests


@app.api(
    example_pb2_grpc.ExampleServicer.getMessage,
    example_pb2.request,
    example_pb2.userGithubMessage,
)
def getMessage(name: str, github: str) -> str:
    url = name + '@' + github
    data = requests.get('http://'+url).text
    return data


@app.api(
    test_pb2_grpc.TestServicer.TestApi,
    test_pb2.testreq,
    test_pb2.testresp
)
def TestApi(user: str, role: int) -> str:
    print(user,role)
    return user + str(role)


@app.api(
    test_pb2_grpc.TestServicer.TestApi,
    test_pb2.testreq,
    test_pb2.testresp
)
def JsonApi(user: str, role: int) -> str:
    print(user,role)
    return "User:"+user + ";Role:"+str(role)


if __name__ == '__main__':
    app()
