from _xkcp_sha3_cffi import ffi, lib


def sha3_224(msg: bytes) -> bytes:
    return __sha3(lib.FIPS202_SHA3_224, msg, 224 // 8)


def sha3_256(msg: bytes) -> bytes:
    return __sha3(lib.FIPS202_SHA3_256, msg, 256 // 8)


def sha3_384(msg: bytes) -> bytes:
    return __sha3(lib.FIPS202_SHA3_384, msg, 384 // 8)


def sha3_512(msg: bytes) -> bytes:
    return __sha3(lib.FIPS202_SHA3_512, msg, 512 // 8)


def __sha3(sha3_func: callable, msg: bytes, outlen) -> bytes:
    out = ffi.new("unsigned char[]", outlen)
    sha3_func(msg, len(msg), out)
    return ffi.buffer(out)[:]
