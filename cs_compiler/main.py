import asn1tools
import os

import generators
import class_generator

"""
Generates c# source files for every type from asn1 specification
"""
def compile_files(filenames, namespace, codec='uper'):
    specification = asn1tools.compile_files(filenames, codec)

    current_dir = os.getcwd()

    path = os.path.join(current_dir, namespace)

    try:
        os.mkdir(path)
    except OSError as err:
        print(err)

    for type in specification.types.values():
        class_generator.generate_class(type, path)

compile_files('/home/krchdavi/asn1tools.net/examples/v2x/test.asn', 'test')