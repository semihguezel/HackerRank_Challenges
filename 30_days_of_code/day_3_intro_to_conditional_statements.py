if __name__ == '__main__':
    N = int(input().strip())
    string = 'Weird' if 6 <= N <= 20 or N % 2 != 0 else 'Not Weird'

    print(string)
