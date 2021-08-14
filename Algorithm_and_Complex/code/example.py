print("~" * 60)
print("Tower of Hanoi")


def hanoi(n, src, dst, tmp):
    if n > 0:
        hanoi(n - 1, src, tmp, dst)
        print(f"Move disk {n} from {src} to {dst}")
        hanoi(n - 1, tmp, dst, src)


hanoi(4, "A", "B", "C")

print("~" * 60)
print("8 Queens Problem")

queen = [0 for _ in range(8)]
rfree = [True for _ in range(8)]
du = [True for _ in range(15)]
dd = [True for _ in range(15)]


def solve(c):
    global solutions

    if c == 8:
        solutions += 1
        print(solutions, end=": ")
        for r in range(8):
            print(queen[r] + 1, end=" " if r < 7 else "\n")
    else:
        for r in range(8):
            if rfree[r] and dd[c + r] and du[c + 7 - r]:
                queen[c] = r
                rfree[r] = dd[c + r] = du[c + 7 - r] = False
                solve(c + 1)
                rfree[r] = dd[c + r] = du[c + 7 - r] = True


solutions = 0
solve(0)

print(f"\nThere are {solutions} solutions")
