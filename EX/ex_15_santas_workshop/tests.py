import santas


def test_child():
    new_child = santas.Child("Lauri")
    assert new_child.name == "Lauri"
