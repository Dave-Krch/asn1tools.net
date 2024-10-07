import asn1tools
import os

def generate_class(compiled_type, output_path):
    
    file_name = compiled_type.name + ".cs"
    path = os.path.join(output_path, file_name)

    file = open(path, "x")