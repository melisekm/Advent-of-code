import timeit
import re


def solve_pt1(vstup):
    def evaluate(rovnica):
        def solve(expresia):
            res = 0
            cisla = re.findall(r"\d+", expresia)
            symboly = re.findall(r"[*|+]", expresia)
            symbol = "+"
            while len(cisla) != 0:
                cislo = cisla.pop(0)
                if symbol == "+":
                    res += int(cislo)
                elif symbol == "*":
                    res *= int(cislo)
                if len(symboly) != 0:
                    symbol = symboly.pop(0)
            return str(res)

        stack = []
        for znak in rovnica:
            if znak == "(":
                stack.append(znak)
            elif znak == ")":
                stack[-1] += znak
                expresia = stack.pop()
                vysledok_expr = solve(expresia)
                if len(stack) == 0:
                    stack.append(vysledok_expr)
                else:
                    stack[-1] += vysledok_expr
            elif znak in ("+", "*"):
                stack[-1] += znak
            else:  # cislo
                if len(stack) == 0:
                    stack.append(znak)
                else:
                    stack[-1] += znak
        return solve(stack.pop())

    res = 0
    with open(vstup, "r") as file:
        for line in file:
            res += int(evaluate(line.strip().replace(" ", "")))
    return res


def solve_pt2(vstup):
    def evaluate(rovnica):
        def vykonaj_operacie(cisla, symboly, znak):
            while True:
                try:
                    pos = symboly.index(znak)
                except ValueError:
                    break
                symboly.pop(pos)
                cislo1 = int(cisla.pop(pos))
                cislo2 = int(cisla.pop(pos))
                if znak == "+":
                    cisla.insert(pos, str(cislo1 + cislo2))
                else:
                    cisla.insert(pos, str(cislo1 * cislo2))

        def solve(expresia):
            cisla = re.findall(r"\d+", expresia)
            symboly = re.findall(r"[*|+]", expresia)
            vykonaj_operacie(cisla, symboly, "+")
            vykonaj_operacie(cisla, symboly, "*")

            return cisla[0]

        stack = []
        for znak in rovnica:
            if znak == "(":
                stack.append(znak)
            elif znak == ")":
                stack[-1] += znak
                expresia = stack.pop()
                vysledok_expr = solve(expresia)
                if len(stack) == 0:
                    stack.append(vysledok_expr)
                else:
                    stack[-1] += vysledok_expr
            elif znak in ("+", "*"):
                stack[-1] += znak
            else:  # cislo
                if len(stack) == 0:
                    stack.append(znak)
                else:
                    stack[-1] += znak
        return solve(stack.pop())

    res = 0
    with open(vstup, "r") as file:
        for line in file:
            res += int(evaluate(line.strip().replace(" ", "")))
    return res


vstup = "day18/vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")


start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
