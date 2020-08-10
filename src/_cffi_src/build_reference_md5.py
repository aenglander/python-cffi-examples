from glob import glob
from os import path, sep

import cffi

CFFI_SRC_DIR = path.join(path.realpath(path.dirname(__file__)), "rfc1321")

ffi = cffi.FFI()

# Expose the functions as you would in a C header to Python
ffi.cdef("""
typedef unsigned long int UINT4;

typedef struct {
  UINT4 state[4];                                   /* state (ABCD) */
  UINT4 count[2];        /* number of bits, modulo 2^64 (lsb first) */
  unsigned char buffer[64];                         /* input buffer */
} MD5_CTX;

void MD5Init(MD5_CTX *);
void MD5Update(MD5_CTX *, unsigned char *, unsigned int);
void MD5Final(unsigned char [16], MD5_CTX *);
""")

# Define the bindings between C and Python
ffi.set_source(
    "_md5_cffi",
    # Headers to include
    r"""
    #include "global.h"
    #include "md5.h"
    """,
    # Sources will be copied
    sources=[path.join(CFFI_SRC_DIR, "md5.c")],
    include_dirs=[CFFI_SRC_DIR],
    extra_compil_args=["-m32"]
)

