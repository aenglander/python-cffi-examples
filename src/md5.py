"""
This software is a derivative work based on mddriver.c created an copyrighted
by RSA Data Security, Inc. in IETF RFC 1321.

This reference example does not wor correctly on
"""

from _md5_cffi import ffi, lib


def md5hash(string: bytes) -> bytes:
    """
    Generate an RFC 2321 MD5 hash digest from the input bytes
    :param string: Input bytes
    :return: Hash digest
    """
    context = ffi.new("MD5_CTX *")
    digest = ffi.new("unsigned char[]", 16)
    len_ = len(string)

    lib.MD5Init(context)
    lib.MD5Update(context, string, len_)
    lib.MD5Final(digest, context)

    return ffi.buffer(digest, 16)[:]
