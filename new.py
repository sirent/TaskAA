def main():

    s = 0
    A = []
    newmax = 0

    for p in range(0,99000):
        try:
            data = int(raw_input())
            A.append(data)
            
            temp = A[p]
            if temp >= newmax:
                newmax = temp
                p += 1
                s += 1

        except ValueError:
            break
    print s

if __name__ == '__main__':
    main()