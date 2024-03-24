import asyncio
import logging
from typing import Iterator, Iterable, AsyncIterator, AsyncIterable

import grpc
import service_pb2
import service_pb2_grpc


class Greeter(service_pb2_grpc.GreeterServicer):
    async def SayHello(
        self,
        request: service_pb2.HelloRequest,
        context: grpc.aio.ServicerContext,
    ) -> service_pb2.HelloReply:
        print(f"SayHello received {request}")
        return service_pb2.HelloReply(message="Hello, %s!" % request.name)

    async def SayHelloBothStream(
        self,
        request_iter: AsyncIterator[service_pb2.HelloRequest],
        context: grpc.aio.ServicerContext,
    ) -> AsyncIterable[service_pb2.HelloReply]:
        async for r in request_iter:
            print(f"Stream request {r}")
            yield service_pb2.HelloReply(message="Hello, %s!" % r.name)


async def serve() -> None:
    server = grpc.aio.server()
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())