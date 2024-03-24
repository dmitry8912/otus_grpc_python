import asyncio
import logging

import grpc
import service_pb2
import service_pb2_grpc


async def request_iter():
    for _ in range(5):
        yield service_pb2.HelloRequest(name="Test stream request")


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = service_pb2_grpc.GreeterStub(channel)
        response = stub.SayHelloBothStream(request_iter())
        async for i in response:
            print("Greeter client received: " + i.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
