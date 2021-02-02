import timeit
import copy


def solve_pt1(vstup):
    food = []
    with open(vstup, "r") as file:
        for line in file:
            line = line.strip().split("(")
            ingredients = line[0][:-1].split(" ")
            allergens = line[1][9:-1].replace(",", "").split(" ")
            food.append([ingredients, allergens])

    A = {}
    for idx, jedlo in enumerate(food):
        for allergen in jedlo[1]:
            if A.get(allergen) is None:
                A[allergen] = [idx]
            else:
                A[allergen].append(idx)

    A2 = []
    food_copy = [copy.deepcopy(food)]
    Alist = list(A.keys())
    a_id = 0
    while a_id < len(Alist):
        allergen = Alist[a_id]
        food_ids = A[Alist[a_id]]
        # for allergen, food_ids in A.items():
        j_id = 0
        while j_id < len(food_copy[-1]):
            jedlo = food_copy[-1][j_id]
            # for jedlo in food_copy[-1]:
            ok = 0
            i = 0
            while len(jedlo[0]) != 0:
                if j_id == 0 and i == 0:
                    if len(food_copy) == 0:
                        food_copy.append(copy.deepcopy(food))
                    else:
                        food_copy.append(copy.deepcopy(food_copy[-1]))
                if i == len(jedlo[0]):
                    # food_copy.pop()
                    wrong = 1
                    break
                ingredient = jedlo[0][i]
                # contains = []
                wrong = 0
                # test = food_copy[idx][0][ingredient_id]
                for cntr, idx in enumerate(food_ids):
                    # for ingredient in food_copy[idx][0][ingredient_id:]:
                    if ingredient in food_copy[-1][idx][0]:
                        pass
                        # contains.append(idx)
                        # food_copy[-1][idx][0].remove(ingredient)
                    elif cntr == 0:
                        jedlo[0].remove(ingredient)
                        wrong = 1
                        i -= 1
                        break
                    else:
                        # food_copy.pop()
                        wrong = 1
                        break
                if wrong > 0:
                    i += 1
                    continue
                for cislo, jedlo2 in enumerate(food_copy[-1]):
                    # if cislo in contains:
                    #    contains.remove(cislo)
                    #    continue
                    if ingredient in jedlo2[0]:
                        jedlo2[0].remove(ingredient)
                A2.append(ingredient)
                ok = 1
                break
            if ok:
                break
            if j_id == len(food_copy[-1]) - 1:
                food_copy.pop()
                A2.pop()
                a_id -= 2
                break
            else:
                j_id += 1
        a_id += 1

    return 0


vstup = "day21/vstup.txt"

start = timeit.default_timer()
result1 = solve_pt1(vstup)
print(result1)
print(f"Cas vykonavania pt1:{timeit.default_timer() - start} sec")

"""
start = timeit.default_timer()
result2 = solve_pt2(vstup)
print(result2)
print(f"Cas vykonavania pt2:{timeit.default_timer() - start} sec")
"""
