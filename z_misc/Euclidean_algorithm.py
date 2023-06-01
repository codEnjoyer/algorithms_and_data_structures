def find_greatest_common_divisor(a: int, b: int) -> int:
    n = 0
    qn, un, vn = [], [], []
    print(f"a = {a}, b = {b}")

    while a and b:
        n += 1
        qn.append(max(a, b) // min(a, b))
        if n == 1:
            un.append(1)
            vn.append(-qn[0])
        elif n == 2:
            un.append(-qn[1])
            vn.append(1 + qn[0] * qn[1])
        if a > b:
            a %= b
        else:
            b %= a

        if n > 2 and a and b:
            un.append(un[n - 2 - 1] - un[n - 1 - 1] * qn[n - 1])
            vn.append(vn[n - 2 - 1] - vn[n - 1 - 1] * qn[n - 1])

    print(f"n = {[k for k in range(n)]}\n"
          f"Qn = {qn}\n"
          f"Un = {un}\n"
          f"Vn = {vn}")
    return a + b


def main():
    d = find_greatest_common_divisor(5517, 4608)
    print(f"НОД = {d}")


if __name__ == "__main__":
    main()
