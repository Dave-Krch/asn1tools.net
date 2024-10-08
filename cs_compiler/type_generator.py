"""
Methods for generating class properties

all - are replaced with _ in class/property names to work in c# syntax
"""

def capitalized_first(s):
    return s[0].upper() + s[1:]

def write_element_attribute(compiled_type) -> str:

    default = "false"
    if(compiled_type.default is not None):
        default = "true"

    out = "        [ASN1Element(Name=\"" + compiled_type.name + "\", IsOptional=" + str(compiled_type.optional).lower() + ", HasDefaultValue = " + default + ")]\n"
    return out

class type_generator:

    def __init__(self, file):
        self.file = file

    def write_int(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1Integer]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public long" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_bool(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1Boolean]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public bool" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_bit_string(self, compiled_type, variable_name, optional, default): 
        self.file.write(    "        [ASN1BitString]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public BitArray" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_octet_string(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1OctetString]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public byte[]" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_utf8_string(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1UTF8String]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public string" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_IA5String_string(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1IA5String]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public string" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")
        
    def write_numeric_string(self, compiled_type, variable_name, optional, default):
        self.file.write(    "        [ASN1NumericString]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public string" + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }" + default + "\n")

    def write_custom_type(self, compiled_type, variable_name, optional):
        self.file.write(    "        [ASN1NamedType]\n"
                        +   write_element_attribute(compiled_type)
                        +   "        public " + compiled_type.type_name.replace('-', '_') + optional + " " + capitalized_first(variable_name).replace('-', '_') + " { get; set; }\n")

    def write(self, compiled_type, variable_name = ""):

        type_method_mapping = {
            "INTEGER": self.write_int,
            "BOOLEAN": self.write_bool,
            "BIT STRING": self.write_bit_string,
            "OCTET STRING": self.write_octet_string,
            "IA5String": self.write_IA5String_string,
            "UTF8String": self.write_utf8_string,
            "NumericString": self.write_numeric_string,
        }

        type_name = compiled_type.type_name
        
        #variable_name is set to 'val' only when generating named type, because variable can not be named as the class
        if(variable_name == ""):
            variable_name = compiled_type.name

        #creates nullable c# property if variable is optional
        optional = "";
        if(compiled_type.optional):
            optional = "?"

        #default value for type
        default = ""
        if(compiled_type.default is not None):
            default = " = " + str(compiled_type.default).lower() + ";"

        if type_name in type_method_mapping:
            type_method_mapping[type_name](compiled_type, variable_name, optional, default)
        else:
            self.write_custom_type(compiled_type, variable_name, optional)
