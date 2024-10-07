import os

import type_generator

"""
Methods for generating classes enums and named types
"""
def generate_class(compiled_type, namespace, output_path):
    
    file_name = compiled_type.name + ".cs"
    path = os.path.join(output_path, file_name)

    file = open(path, "x")
 
    tab = "    "

    file.write("namespace " + namespace + " {\n" + tab + "public class " + compiled_type.name + " {\n")

    generator = type_generator.type_generator(file);

    for member in compiled_type.type.root_members:

        print(member.name)   
        
        generator.write(member)
        

    file.write(tab + "}\n}\n")
