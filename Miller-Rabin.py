import random

# Miller-Rabin Algorithim
def test(n):

    k, q = (0, n-1)

    # If (n-1) is positve we divde by two to make q odd and keep k > 0
    while q % 2 == 0:
        k += 1
        q //= 2

    if n-1 == (2**k)*q:

        # Making sure 1 < a < n-1 so randomly generate a number between 2 and n-2 respectivly
        a = random.randint(2, n - 2)

        if pow(a, q, n) == 1:
            return "Inconclusive"

        # k is the amount of iterrations, the bigger k is then more acurate the result will be
        for j in range(k):
            if pow(a, pow(2, j) * q, n) == n - 1:
                return "Inconclusive"
            
        return "Composite"


n = input("Please Input A Number To Test\n");
print("\n", n, "is", test(int(n)))