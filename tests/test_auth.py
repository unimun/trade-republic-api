import hashlib
from pathlib import Path

from ecdsa import NIST256p

from trade_republic_api.auth import Auth


def test_signing_key(mocker):
    mocker.patch("pathlib.Path.open", mocker.mock_open(read_data=""))
    from_pem = mocker.patch("ecdsa.SigningKey.from_pem", side_effect=ValueError)
    generate = mocker.patch("ecdsa.SigningKey.generate")
    mkdir = mocker.patch("pathlib.Path.mkdir")
    auth = Auth(Path("tests/.cache/"))
    assert auth.signing_key
    from_pem.assert_called_once_with("", hashfunc=hashlib.sha512)
    generate.assert_called_once_with(curve=NIST256p, hashfunc=hashlib.sha512)
    generate().to_pem.assert_called_once()
    mkdir.assert_called_once_with(parents=True, exist_ok=True)
