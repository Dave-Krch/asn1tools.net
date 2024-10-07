"""
Methods for generating class properties
"""
class type_generator:

    def __init__(self, file):
        self.file = file

    def write_int(self, compiled_type):
        self.file.write("        public long " + compiled_type.name.capitalize() + " { get; set; }\n")

    def write_bool(self, compiled_type):
        self.file.write("        public bool " + compiled_type.name.capitalize() + " { get; set; }\n")

    def write_bit_string(self, compiled_type):
        self.file.write("        public BitArray " + compiled_type.name.capitalize() + " { get; set; }\n")

    def write_octet_string(self, compiled_type):
        self.file.write("        public byte[] " + compiled_type.name.capitalize() + " { get; set; }\n")

    def write_custom_type(self, compiled_type):
        self.file.write("        public " + compiled_type.type_name + " " + compiled_type.name.capitalize() + " { get; set; }\n")

    def write(self, compiled_type):
        type_method_mapping = {
            "INTEGER": self.write_int,
            "BOOLEAN": self.write_bool,
            "BIT STRING": self.write_bit_string,
            "OCTET STRING": self.write_octet_string,
        }

        type_name = compiled_type.type_name

        if type_name in type_method_mapping:
            type_method_mapping[type_name](compiled_type)
        else:
            self.write_custom_type(compiled_type)
