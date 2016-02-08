#!/usr/bin/env python

print("hello")


def repeat(s, exclaim):
    result = s + s + s;
    if exclaim:
        result += '!!!'

    return result

def test() :
    liczba = input("Podaj liczbę: ")
    print(liczba)
print(repeat("aa", True))
test()
