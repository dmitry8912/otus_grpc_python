import asyncio
import logging

import grpc
import service_pb2
import service_pb2_grpc


async def run() -> None:
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = service_pb2_grpc.GreeterStub(channel)
        response = await stub.SayHello(service_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run())
