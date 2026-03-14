def find_factorial(n:int)->int:
    if n==0:
        return 1
    if n==1:
        return 1
    
    else:
        return n*find_factorial(n-1)
    


def main():
    n=int(input("Enter a number: "))
    print(find_factorial(n))


if __name__=="__main__":
    main()
