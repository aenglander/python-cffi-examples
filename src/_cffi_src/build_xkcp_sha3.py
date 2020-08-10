from os import path, sep

import cffi

SRC_DIR = path.join(path.realpath(path.dirname(__file__)),
                    "XKCP", "Standalone", "CompactFIPS202", "C")

ffi = cffi.FFI()

# Expose the functions as you would in a C header to Python
ffi.cdef("""
void FIPS202_SHA3_224(const unsigned char *input, unsigned int inputByteLen, unsigned char *output);
void FIPS202_SHA3_256(const unsigned char *input, unsigned int inputByteLen, unsigned char *output);
void FIPS202_SHA3_384(const unsigned char *input, unsigned int inputByteLen, unsigned char *output);
void FIPS202_SHA3_512(const unsigned char *input, unsigned int inputByteLen, unsigned char *output);
""")

# Define the bindings between C and Python
ffi.set_source(
    "_xkcp_sha3_cffi",
    "",
    # Sources will be copied
    sources=[path.join(SRC_DIR, "Keccak-readable-and-compact.c")],
    include_dirs=[SRC_DIR],
)
