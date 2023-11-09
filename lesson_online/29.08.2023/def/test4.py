def prost(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            print('число составное')
            break
    else:
        print('простое')


prost(4)