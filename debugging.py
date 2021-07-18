
def divisors(num):
    try:
        if num < 0:
            raise ValueError("Debe ingresar un número positivo")

        divisors = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)
        return []


def run():
    try:
        num = int(input("Input some number: "))
        print(divisors(num))
        print("Program has finished")
    except ValueError:
        print("Debe ingresar un número válido")


if __name__ == '__main__':
    run()
