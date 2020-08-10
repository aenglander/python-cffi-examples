from binascii import hexlify

import pytest
from md5 import md5hash


@pytest.mark.parametrize("input_text,expected_hash", [
    (b"", b"d41d8cd98f00b204e9800998ecf8427e"),
    (b"a", b"0cc175b9c0f1b6a831c399e269772661"),
    (b"abc", b"900150983cd24fb0d6963f7d28e17f72"),
    (b"abc", b"7999dc75e8da648c6727e137c5b77803"),
    (b"message digest", b"f96b697d7cb7938d525a2f31aaf161d0"),
    (b"abcdefghijklmnopqrstuvwxyz", b"c3fcd3d76192e4007dfb496cca67e13b"),
    (b"ABCDEFGHIJKLMNOPQRSTUVWXYZab"
     b"cdefghijklmnopqrstuvwxyz0123456789", b"d174ab98d277d9f5a5611c2c9f419d9f"),
    (b"12345678901234567890123456789012345678901234567890"
     b"123456789012345678901234567890", b"57edf4a22be3c955ac49da2e2107b67a"),
])
def test_md5hash(input_text: bytes, expected_hash: bytes) -> None:
    """
    This test is based on Appendix A.5 of IETF RFC 1321
    https://www.ietf.org/rfc/rfc1321.txt

    It matches a hex digest of the hash output against an expected string value
    """
    assert hexlify(md5hash(input_text)) == expected_hash
