from main import solve


def test_main():
    assert solve([
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]) == 6

def test_main_1000():
    assert solve([
        "R1000"
    ]) == 10