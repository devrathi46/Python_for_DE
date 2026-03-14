def check_palindrome(s:str)->bool:
    s=list(s)
    i=0
    j=len(s)-1

    while(i<j):
        if s[i]==s[j]:
            i=i+1
            j=j-1
        else:
            return False
        
    return True    



def main():
    s=input("Enter the string: ")
    print(check_palindrome(s))


if __name__=="__main__":
    main()