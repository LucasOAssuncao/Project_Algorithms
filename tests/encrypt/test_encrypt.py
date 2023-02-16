import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 4)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("coca", "oi")
    assert encrypt_message("coca", 100) == "acoc"

    assert encrypt_message("coca", 3) == "coc_a"
    assert encrypt_message("coca", 2) == "ac_oc"
