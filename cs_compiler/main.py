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
        os.mkdir(os.path.join(path, "sequence"))
        os.mkdir(os.path.join(path, "sequenceOf"))
        os.mkdir(os.path.join(path, "choice"))
        os.mkdir(os.path.join(path, "enumerated"))
        os.mkdir(os.path.join(path, "bit_string"))
    except OSError as err:
        print(err)

    generator = class_generator.ClassGenerator(namespace, output_path)

    for type in specification.types.values():
        generator.generate_structure(type)

#compile_files(['/home/krchdavi/asn1tools.net/examples/v2x/test.asn'], 'test_namespace', 'test_dir')
compile_files(['/home/krchdavi/asn1tools.net/examples/v2x/TS102894-2v131-CDD.asn', '/home/krchdavi/asn1tools.net/examples/v2x/EN302637-2v141-CAM.asn'], 'test_namespace', 'test_dir')