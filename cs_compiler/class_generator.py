import os

import type_generator

"""
Methods for generating classes enums and named types
"""

class ClassGenerator:
    def __init__(self, namespace, output_path) -> None:
        self.namespace = namespace
        self.output_path = output_path

    def generate_class(self, file, compiled_type):
        
        #file_name = compiled_type.name + ".cs"
        #path = os.path.join(self.output_path, file_name)

        #file = open(path, "x")

        file.write("namespace " + self.namespace + " {\n" + "    " + "public class " + compiled_type.name + " {\n")

        generator = type_generator.type_generator(file);

        for member in compiled_type.type.root_members:

            print(member.name)   
            
            generator.write(member)
            

        file.write("    " + "}\n}\n")

    def generate_enum(self, file, compiled_type):
        file.write("namespace " + self.namespace + " {\n" + "    " + "enum " + compiled_type.name + " {\n")

        for member in compiled_type.type.root_index_to_data:
            file.write("        " + compiled_type.type.root_index_to_data[member] + ",\n")

        file.write("    " + "}\n}\n")

    def generate_custom_type(self, file, compiled_type):
        file.write("namespace " + self.namespace + " {\n" + "    " + "custom type " + compiled_type.name + " {\n")



        file.write("    " + "}\n}\n")

    def generate_structure(self, compiled_type):
        file_name = compiled_type.name + ".cs"
        path = os.path.join(self.output_path, file_name)

        file = open(path, "x")

        type_method_mapping = {
            "SEQUENCE": self.generate_class,
            "ENUMERATED": self.generate_enum,
        }

        type_name = compiled_type.type.type_name

        if type_name in type_method_mapping:
            type_method_mapping[type_name](file, compiled_type)
        else:
            self.generate_custom_type(file, compiled_type)

        #self.generate_class(file, compiled_type)




