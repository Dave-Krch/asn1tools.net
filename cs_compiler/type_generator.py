"""
Methods for generating class properties
"""

def capitalized_first(s):
    return s[0].upper() + s[1:]

class type_generator:

    def __init__(self, file):
        self.file = file

    def write_int(self, compiled_type, variable_name, optional):
        self.file.write("        public long" + optional + " " + capitalized_first(variable_name) + " { get; set; }\n")

    def write_bool(self, compiled_type, variable_name, optional):
        self.file.write("        public bool" + optional + " " + capitalized_first(variable_name) + " { get; set; }\n")

    def write_bit_string(self, compiled_type, variable_name, optional):
        self.file.write("        public BitArray" + optional + " " + capitalized_first(variable_name) + " { get; set; }\n")

    def write_octet_string(self, compiled_type, variable_name, optional):
        self.file.write("        public byte[]" + optional + " " + capitalized_first(variable_name) + " { get; set; }\n")

    def write_custom_type(self, compiled_type, variable_name, optional):
        self.file.write("        public " + compiled_type.type_name + optional + " " + capitalized_first(variable_name) + " { get; set; }\n")

    def write(self, compiled_type, variable_name = ""):

        type_method_mapping = {
            "INTEGER": self.write_int,
            "BOOLEAN": self.write_bool,
            "BIT STRING": self.write_bit_string,
            "OCTET STRING": self.write_octet_string,
        }

        type_name = compiled_type.type_name
        
        #variable_name is set to 'val' only when generating custom type, because variable can not be named as the class
        if(variable_name == ""):
            variable_name = compiled_type.name

        #creates nullable c# property if variable is optional
        optional = "";
        if(compiled_type.optional):
            optional = "?"

        if type_name in type_method_mapping:
            type_method_mapping[type_name](compiled_type, variable_name, optional)
        else:
            self.write_custom_type(compiled_type, variable_name, optional)
