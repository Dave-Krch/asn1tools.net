import asn1tools
import pprint

spec_uper = asn1tools.compile_files(['/home/krchdavi/asn1tools.net/examples/v2x/test.asn'], 'uper')

def int_to_cs(int_):
    if(int_.minimum != None):
        print(f"    [Range({int_.minimum}, {int_.maximum})]")
    print(f"    int {int_.name};")

def int_to_class(int_):
    print(f"public class {int_.name}\n{{")
    int_to_cs(int_)
    print("}")
    
def seq_to_class(seq):
    print(f"public class {seq.name}\n{{")

    for member in seq.root_members:
            if (member.type_name=='INTEGER'):
                int_to_cs(member)
            else:
                print(f"    public {member.type_name} {member.name};")

    print("}")

for type in spec_uper._types:
    print("------------------------------------------")
    print(f"{type}: {spec_uper._types[type].type.type_name}\n")
    if (spec_uper._types[type].type.type_name=='SEQUENCE'):
        seq = spec_uper._types[type].type
        seq_to_class(seq)

    if (spec_uper._types[type].type.type_name=='INTEGER'):
        int_to_class(spec_uper._types[type].type)

"""
hex_data_uper = [
    "02 02 9b 26 0a a3 93 e6 00 5a 6f 0d a4 ae 7b fb 35 a2 38 23 0a 6a 3d 42 90 58 1a 90 a3 f6 7e 02 e6 92 8b 37 fe e9 fe a6 10 3f df 93 d9 80",
    "02 02 9b 26 0a a3 99 c2 40 5a 6f 0e 9f 2e 7b fc 9e 62 38 23 0a 5e 3d 42 90 58 1b 00 a3 fe 7e 02 e6 92 87 33 fb 21 ff 32 10 3f df 94 19 80 10 55 fd 6a 7f 10 58 ce 00 0c 6f d1 cb ef 74 c6 70 00 d9 7e 8a 1f 7d 46 33 80 06 db f4 40 fb f6 b2 00 00 36 df a2 37 e0 11 90 00 01 ba fd 14 bf 04 0c 80 00 0d b7 e8 25 f7 f9 64 00 00 6c bf 42 4f c0 33 20 00 03 6d fa 52 7e 16 99 32 00 1b af d3 63 f0 f8 c8 00 00 d8",
    "02 02 9b 26 0a a3 9a 8a 00 5a 6f 0e c2 8e 7b fc d1 e2 38 23 0a 5c 3d 42 90 58 1b 00 a4 00 7e 02 e6 92 87 33 fb 01 ff 4a 10 3f ff 94 19 80",
    "02 02 9b 26 0a a3 9c da 00 5a 6f 0f 27 ee 7b fd 64 82 38 22 ca 58 3d 4f 10 58 1a f0 a4 04 7e 02 e6 92 87 37 fe ea 00 9a 10 40 1f 94 19 80",

]

byte_data_uper = []

hex_data_encoded_back = []

for hexstr in hex_data_uper:
    byte_data_uper.append(bytes.fromhex(hexstr))

for bytestr in byte_data_uper:
    decoded = spec_uper.decode('CAM', bytestr)
    pprint.pprint(decoded)
    print("\n     ------------------------------------------------------------------------     \n")


    byte_data_back = spec_uper.encode('CAM', decoded) 
    hex_data_encoded_back.append(byte_data_back.hex())

for hex_back in hex_data_encoded_back:
    print(hex_back)

for i in range(len(byte_data_uper)):
    if(byte_data_uper[i].hex() == hex_data_encoded_back[i]):
        print("Same")
"""
