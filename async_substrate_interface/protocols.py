from typing import Protocol


__all__: list[str] = [
    'Keypair'
]


# For reference only
# class KeypairType:
#     """
#     Type of cryptography, used in `Keypair` instance to encrypt and sign data
# 
#     * ED25519 = 0
#     * SR25519 = 1
#     * ECDSA = 2
# 
#     """
#     ED25519 = 0
#     SR25519 = 1
#     ECDSA = 2


class Keypair(Protocol):

    @property
    def crypto_type(self) -> int:
        ...

    @property
    def public_key(self) -> bytes | None:
        ...

    @property
    def ss58_address(self) -> str:
        ...

    @property
    def ss58_format(self) -> int:
        ...

    def sign(self, data: bytes | str) -> bytes:
        ...