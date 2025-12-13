def is_even(number: int) -> bool:
    return number % 2 == 0


num = 7
result = is_even(num)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
