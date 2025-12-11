from main import solve


def test_main():
    assert solve([
"svr: aaa bbb",
"aaa: fft",
"fft: ccc",
"bbb: tty",
"tty: ccc",
"ccc: ddd eee",
"ddd: hub",
"hub: fff",
"eee: dac",
"dac: fff",
"fff: ggg hhh",
"ggg: out",
"hhh: out",
    ]) == 2
