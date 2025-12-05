from main import solve


def test_main():
    assert solve([
"3-5",
"10-14",
"16-20",
"12-18",
"",
"1",
"5",
"8",
"11",
"17",
"32",
    ]) == 3
