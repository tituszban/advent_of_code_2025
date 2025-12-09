from main import solve


def test_main():
    assert solve([
"7,1",
"11,1",
"11,7",
"9,7",
"9,5",
"2,5",
"2,3",
"7,3",
    ]) == 50
