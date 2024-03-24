#!/bin/bash

python -m grpc_tools.protoc -I. --python_out=./compiled --pyi_out=./compiled --grp
c_python_out=./compiled service.proto