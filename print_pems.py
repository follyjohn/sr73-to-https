# -*- coding: utf-8 -*-
"""

Created on May 2022
@author: Mr ABBAS-TURKI

"""

import pem


RESOURCES_DIR = "resources/"
CA_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "ca-private-key.pem"
CA_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "ca-public-key.pem"
SERVER_PRIVATE_KEY_FILENAME = RESOURCES_DIR + "server-private-key.pem"
SERVER_CSR_FILENAME = RESOURCES_DIR + "server-csr.pem"
SERVER_PUBLIC_KEY_FILENAME = RESOURCES_DIR + "server-public-key.pem"
from cryptography import x509
from cryptography.hazmat.backends import default_backend

def print_perms(filename: str):
    certs = pem.parse_file(filename)  # using pem module
    for pem_certificates in certs:
        strcert = str(pem_certificates)
        print(strcert)
        cert_obj = x509.load_pem_x509_certificate(pem_certificates.as_bytes(), default_backend())
        print("Issuer : ", cert_obj.issuer)
        print("Subject : ", cert_obj.subject)
        print("Serial Number : ", cert_obj.serial_number)
        print("Version : ", cert_obj.version)
