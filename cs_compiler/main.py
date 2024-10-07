import asn1tools
import os

import class_generator

"""
Generates c# source files for every type from asn1 specification
"""
def compile_files(filenames, namespace, output_path, codec='uper'):
    specification = asn1tools.compile_files(filenames, codec)

    current_dir = os.getcwd()

    path = os.path.join(current_dir, output_path)

    try:
        os.mkdir(path)
    except OSError as err:
        print(err)

    for type in specification.types.values():
        if(type.type.type_name == 'SEQUENCE'):
            class_generator.generate_class(type, namespace, path)

compile_files('/home/krchdavi/asn1tools.net/examples/v2x/TS102894-2v131-CDD.asn', 'test_namespace', 'test_dir')