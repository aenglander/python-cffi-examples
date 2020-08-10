from binascii import hexlify, unhexlify

import pytest
from sha3 import sha3_224, sha3_256, sha3_384, sha3_512


@pytest.mark.parametrize("msg,expected", [
    (b"", b"6b4e03423667dbb73b6e15454f0eb1abd4597f9a1b078e3f5b5a6bc7"),
    (b"Ice Ice baby", b"089efdbdac051ad57df72d3924ddf9418b4936c79348c3521355a350"),
    (b"Check out the hook while my DJ revolves it", b"a58c9046689cccac7a5c08fd51aee77417e61c4400b9f61bc5f1e6af"),
])
def test_sha3_224(msg, expected):
    actual = sha3_224(msg)
    assert hexlify(actual) == expected


@pytest.mark.parametrize("msg,expected", [
    (b"", b"a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"),
    (b"Ice Ice baby", b"7f9cd3418933d2272e265c35f6b719b0e845e7f58daa015b6a8b3fc550491f3f"),
    (b"Check out the hook while my DJ revolves it", b"8b6866e50d3dee54cc2f6ef72242dda36f7d9dd2beb7084cff7b7996fb6a1600"),
])
def test_sha3_256(msg, expected):
    actual = sha3_256(msg)
    assert hexlify(actual) == expected


@pytest.mark.parametrize("msg,expected", [
    (b"", b"0c63a75b845e4f7d01107d852e4c2485c51a50aaaa94fc61995e71bbee983a2ac3713831264adb47fb6bd1e058d5f004"),
    (b"Ice Ice baby", b"87a664231bf3650943ccb2a03b3913ba3301aa4e2825ab28bc35020da8c5f4b84b1ff09b2eef211f1ae82a67ad424eaa"),
    (b"Check out the hook while my DJ revolves it", b"a2668b559fc890794efd773d15adae669409207b7ec2cc76ce9ab194398eabde6b41060eb2be653eaaba3a29198f1e66"),
])
def test_sha3_384(msg, expected):
    actual = sha3_384(msg)
    assert hexlify(actual) == expected


@pytest.mark.parametrize("msg,expected", [
    (b"", b"a69f73cca23a9ac5c8b567dc185a756e97c982164fe25859e0d1dcc1475c80a615b2123af1f5f94c11e3e9402c3ac558f500199d95b6d3e301758586281dcd26"),
    (b"Ice Ice baby", b"26fc4354dbada866deb5a97d79b3e36325492548622a4b9a09e1bb76d0ff5ed2ec82c31459df4f4a6b3f8e7b851cc7ccfadb3c96f15f502fd7d967dcdc5df557"),
    (b"Check out the hook while my DJ revolves it", b"26591c1b8aa9059947f53bc7f3d99325bd02e40615f9c5ea4b578bde395751d4c3b77a93bb47e042007f23d2fc32b878b041ae5305d7ade0d1c1f4928e26b2c2"),
])
def test_sha3_512(msg, expected):
    actual = sha3_512(msg)
    assert hexlify(actual) == expected
