from proto.compiled import simple_pb2

p = simple_pb2.Person()

p.name = 'test'
p.id = 146
p.email = 'admin@outs.ru'

phone_number = simple_pb2.Person.PhoneNumber()
phone_number.number = '555-555-5555'
phone_number.type = 1

p.phones.append(phone_number)

print(f"Protobuf message representation:\n{p}")
print()
print(f"Protobuf raw message representation:\n{p.SerializeToString()}")
print()
p2 = simple_pb2.Person()
p2.ParseFromString(p.SerializeToString())

print(f"Protobuf message parsed:\n{p2}")
