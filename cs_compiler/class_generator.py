import os

import type_generator

"""
Methods for generating classes enums and named types
"""

class ClassGenerator:
    def __init__(self, namespace, output_path) -> None:
        self.namespace = namespace
        self.output_path = output_path

    def generate_class(self, compiled_type):

        file_name = compiled_type.name + ".cs"
        path = os.path.join(self.output_path,"sequence", file_name)
        file = open(path, "x")

        file.write("namespace " + self.namespace + ".sequence" + " {\n" + "    " + "public class " + compiled_type.name + " {\n")

        generator = type_generator.type_generator(file);

        for member in compiled_type.type.root_members:

            print(member.name)   
            
            generator.write(member)
            

        file.write("    " + "}\n}\n")


    def generate_enum(self, compiled_type):

        file_name = compiled_type.name + ".cs"
        path = os.path.join(self.output_path, "enumerated", file_name)
        file = open(path, "x")

        file.write("namespace " + self.namespace + ".enumerated" + " {\n" + "    " + "enum " + compiled_type.name + " {\n")

        # '-' from asn specification must be replaced with '_' beacues of c# syntax
        for member in compiled_type.type.root_index_to_data:
            file.write("        " + compiled_type.type.root_index_to_data[member].replace('-', '_') + ",\n")

        file.write("    " + "}\n}\n")

    def generate_custom_type(self, compiled_type):

        file_name = compiled_type.name + ".cs"
        path = os.path.join(self.output_path, file_name)

        file = open(path, "x")

        file.write("namespace " + self.namespace + " {\n" + "    " + "custom type " + compiled_type.name + " {\n")



        file.write("    " + "}\n}\n")

    def generate_bit_string(self, compiled_type):

        file_name = compiled_type.name + ".cs"
        path = os.path.join(self.output_path,"bit_string", file_name)
        file = open(path, "x")


        file.write(   "using System.Collections;\n\n"
                    + "namespace " + self.namespace + ".bit_string" + " {\n"
                    + "    " + "public class " + compiled_type.name + " {\n"
                    + "        BitArray Data { get; set; }\n"
                    + "        Dictionary<int, string> named_bits = new Dictionary<int, string>();\n"
                    + "        " + compiled_type.name + "()" + " {\n")
        
        
        if compiled_type.type.named_bits:
            for named_bit in compiled_type.type.named_bits:
                file.write("            this.named_bits.Add(" + str(named_bit[1]) + ", \"" + named_bit[0] + "\");\n")
        
        file.write("        }\n    " + "}\n}\n")

    def generate_structure(self, compiled_type):
        
        type_method_mapping = {
            "SEQUENCE": self.generate_class,
            "ENUMERATED": self.generate_enum,
            "BIT STRING": self.generate_bit_string,
        }

        type_name = compiled_type.type.type_name

        if type_name in type_method_mapping:
            type_method_mapping[type_name](compiled_type)
        else:
            self.generate_custom_type(compiled_type)

        #self.generate_class(file, compiled_type)




