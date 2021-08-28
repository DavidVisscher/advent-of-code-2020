from day7 import Haversack


def test_haversack_length():
    bluesack = Haversack("blue")
    assert len(bluesack) == 0
    bluesack.add(Haversack("red"))
    assert len(bluesack) == 1
    bluesack.add(Haversack("red"))
    assert len(bluesack) == 2

def test_haversack_contents():
    bluesack = Haversack("blue")
    assert len(bluesack.counts) == 0

    bluesack.add(Haversack("red"))
    assert len(bluesack.counts) == 1
    assert bluesack.counts["red"] == 1

    bluesack.add(Haversack("red"))
    assert len(bluesack.counts) == 1
    assert bluesack.counts["red"] == 2

    bluesack.add(Haversack("yellow"))
    assert len(bluesack.counts) == 2
    assert bluesack.counts["red"] == 2
    assert bluesack.counts["yellow"] == 1
