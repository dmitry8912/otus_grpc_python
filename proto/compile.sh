#!/bin/bash

./protoc/bin/protoc -I . --python_out=./compiled $1
