import asn1tools

def compile_files(filenames, namespace, codec='uper'):
    specification = asn1tools.compile_files(filenames, codec)