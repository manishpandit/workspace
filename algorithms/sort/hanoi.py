def hanoi(n, a, b, c):
    if n == 1:
        print("move disk 1 from", a, "to", b)
        return
    hanoi(n - 1, a, c, b)
    print("move disk", n, "from", a, "to", b)
    hanoi(n - 1, c, b, a)

hanoi(20, 'a', 'b', 'c')
