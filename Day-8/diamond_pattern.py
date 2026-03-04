def diamond_ai_output(n: int) -> None:
    # This simulates typical AI output that follows the rules.
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()

    for i in range(n - 1, 0, -1):
        for _ in range(n - i):
            print(" ", end="")
        for _ in range(2 * i - 1):
            print("*", end="")
        print()


def diamond_improved(n: int) -> None:
    if n <= 0:
        print("")
        return

    row = 1
    while row <= n:
        spaces = n - row
        stars = 2 * row - 1

        s = 0
        while s < spaces:
            print(" ", end="")
            s += 1

        k = 0
        while k < stars:
            print("*", end="")
            k += 1

        print()
        row += 1

    row = n - 1
    while row >= 1:
        spaces = n - row
        stars = 2 * row - 1

        s = 0
        while s < spaces:
            print(" ", end="")
            s += 1

        k = 0
        while k < stars:
            print("*", end="")
            k += 1

        print()
        row -= 1


def main() -> None:
    raw = input("Enter rows for upper half: ").strip()
    try:
        n = int(raw)
    except ValueError:
        print("Please enter an integer.")
        return

    print()
    print("AI style output")
    diamond_ai_output(n)

    print()
    print("Improved output")
    diamond_improved(n)

    print()
    print("Time complexity")
    print("Total printed characters are proportional to n^2, so complexity is O(n^2).")


if __name__ == "__main__":
    main()