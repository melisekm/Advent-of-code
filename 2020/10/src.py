def solve_pt1(vstup):
    def vyries(arr):
        arr.sort()
        curr = 0
        diff1 = 0
        diff3 = 0
        for cislo in arr:
            rozdiel = cislo - curr
            if rozdiel == 1:
                diff1 += 1
            elif rozdiel == 2:
                diff2 += 1
            elif rozdiel == 3:
                diff3 += 1
            curr += rozdiel
        diff3 += 1
        return diff1 * diff3

    arr = []
    with open(vstup, "r") as file:
        for line in file:
            arr.append(int(line.strip()))

    return vyries(arr)


DP = {}


def solve_pt2(vstup):
    def najdi_susedov(arr, idx):
        susedia = []
        for i in range(1, 4):
            if idx + i < len(arr) and arr[idx + i] - arr[idx] <= 3:
                susedia.append(arr[idx + i])
        return susedia

    def hladaj(j, kontent, slovnik):
        global DP
        if not kontent:
            return 1
        if j in DP:
            return DP[j]
        ans = 0
        for i in kontent:
            ans += hladaj(i, slovnik[i], slovnik)
        DP[j] = ans
        return ans

    def rob(slovnik):
        return hladaj(0, slovnik[0], slovnik)

    def vyries(arr):
        arr.append(0)
        arr.sort()
        slovnik = {}
        for idx, cislo in enumerate(arr):
            slovnik[cislo] = najdi_susedov(arr, idx)
        return rob(slovnik)

    arr = []
    with open(vstup, "r") as file:
        for line in file:
            arr.append(int(line.strip()))

    return vyries(arr)


vstup = "vstup.txt"
result1 = solve_pt1(vstup)
result2 = solve_pt2(vstup)
print(result1)
print(result2)
