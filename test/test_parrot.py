from Parrot_refactoring_Kata.parrot import AfricanParrot, EuropeanParrot, NorwegianBlueParrot


def test_speed_of_european_parrot():
    parrot = EuropeanParrot(0, False, 0)
    assert parrot.speed() == 12.0


def test_cry_of_european_parrot():
    parrot = EuropeanParrot( 0, 0, False)
    assert parrot.cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut():
    parrot = AfricanParrot(1, 0,False)
    assert parrot.speed() == 3.0


def test_cry_of_african_parrot():
    parrot = AfricanParrot(1, 0, False)
    assert parrot.cry() == "Sqaark!"


def test_speed_of_african_parrot_with_two_coconuts():
    parrot = AfricanParrot(2, 0, False)
    assert parrot.speed() == 0.0


def test_speed_of_african_parrot_with_no_coconuts():
    parrot = AfricanParrot(0, 0, False)
    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    parrot = NorwegianBlueParrot(0, 1.5, True)
    assert parrot.speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed():
    parrot = NorwegianBlueParrot(0, 1.5, False)
    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    parrot = NorwegianBlueParrot(0, 4, False)
    assert parrot.speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage():
    parrot = NorwegianBlueParrot(0, 4, False)
    assert parrot.cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage():
    parrot = NorwegianBlueParrot(0, 0, False)
    assert parrot.cry() == "..."