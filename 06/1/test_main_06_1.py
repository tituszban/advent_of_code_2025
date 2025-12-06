from main import solve


def test_main():
    assert solve([
"123 328  51 64",
" 45 64  387 23",
"  6 98  215 314",
"*   +   *   +",
    ]) == 4277556
