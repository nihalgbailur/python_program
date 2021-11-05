# prime number


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    for i in range(15):
        if is_prime(i):
            print(i)


if __name__ == '__main__':
    main()

