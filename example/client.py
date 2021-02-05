import grpc
import example_pb2, example_pb2_grpc, test_pb2, test_pb2_grpc


def TesteClient():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = test_pb2_grpc.TestStub(channel)
        response = stub.TestApi(test_pb2.testreq(user='Euraxluo', role=1))
    print(response.userRole)


def ExampleClient():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = example_pb2_grpc.ExampleStub(channel)
        response1 = stub.getGithubUrl(example_pb2.request(name='Euraxluo', github='github.com'))
        response2 = stub.getMessage(example_pb2.request(name='Euraxluo', github='github.com'))
    print(response2)
    print(response1)

if __name__ == '__main__':
    ExampleClient()
    TesteClient()