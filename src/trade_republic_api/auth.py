from __future__ import annotations

import hashlib
from pathlib import Path

from ecdsa import NIST256p
from ecdsa import SigningKey


class Auth:
    def __init__(self, cache_dir: Path):
        self.keyfile = Path("key")
        self.hashfunc = hashlib.sha512
        try:
            with cache_dir.joinpath(self.keyfile).open(mode="rb") as f:
                self.signing_key = SigningKey.from_pem(f.read(), hashfunc=self.hashfunc)
        except ValueError:
            self.signing_key = SigningKey.generate(curve=NIST256p, hashfunc=hashlib.sha512)
            pem = self.signing_key.to_pem()
            cache_dir.mkdir(parents=True, exist_ok=True)
            with cache_dir.joinpath(self.keyfile).open(mode="wb") as f:
                f.write(pem)
