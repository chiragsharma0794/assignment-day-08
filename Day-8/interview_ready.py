from typing import List, Tuple


def explain_break_continue() -> str:
    return (
        "break stops the loop completely. continue skips the current iteration and moves to the next.\n"
        "Example.\n"
        "for x in [1,2,3,4]:\n"
        "    if x == 3:\n"
        "        continue\n"
        "    print(x)\n"
        "prints 1 2 4.\n"
        "If we replace continue with break then it prints 1 2 and stops."
    )


def explain_loop_else() -> str:
    return (
        "The else clause in for and while runs only if the loop finishes normally.\n"
        "It does not run if the loop exits using break.\n"
        "Practical use case is search.\n"
        "You scan items, if found you break, else means not found."
    )


def search_with_loop_else(items: List[int], needle: int) -> bool:
    for x in items:
        if x == needle:
            return True
    else:
        return False


def find_pairs_n2(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    pairs = []
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs


def find_pairs_on(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    seen = set()
    out = []
    used_pairs = set()

    for x in numbers:
        need = target - x
        if need in seen:
            a, b = (need, x) if need <= x else (x, need)
            if (a, b) not in used_pairs:
                out.append((a, b))
                used_pairs.add((a, b))
        seen.add(x)
    return out


def explain_find_pairs_optimization() -> str:
    return (
        "O(n^2) checks all pairs using two loops. That is about n times n comparisons.\n"
        "O(n) uses a set called seen. For each element x we check if target minus x is already in seen.\n"
        "Set lookup is average O(1), so total is about one pass through the list."
    )


def is_prime_fixed(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def explain_prime_bugs() -> str:
    return (
        "Issues in the original code.\n"
        "Performance issue. Looping i from 2 to n minus 1 is too slow for large n.\n"
        "Logic improvement. You only need to test divisors up to sqrt(n).\n"
        "Extra optimization. Skip even numbers after checking divisibility by 2."
    )


def main() -> None:
    print("Q1 break vs continue")
    print(explain_break_continue())
    print()

    print("Q1 loop else")
    print(explain_loop_else())
    print("search_with_loop_else([1,2,3], 5) gives", search_with_loop_else([1, 2, 3], 5))
    print()

    nums = [1, 2, 3, 4, 5]
    target = 6
    print("Q2 find_pairs O(n^2)", find_pairs_n2(nums, target))
    print("Q2 find_pairs O(n)", find_pairs_on(nums, target))
    print(explain_find_pairs_optimization())
    print()

    print("Q3 prime fix")
    print(explain_prime_bugs())
    for t in [0, 1, 2, 3, 4, 17, 18, 19, 25]:
        print(t, is_prime_fixed(t))


if __name__ == "__main__":
    main()