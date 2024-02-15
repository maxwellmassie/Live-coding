tinggi = int(input("Masukka tinggi segitiga : "))

for i in range(tinggi):
    for j in range(tinggi - i - 1):
        print(" ", end="")

    for j in range(2 * i + 1):
        print("*", end="")
    print()