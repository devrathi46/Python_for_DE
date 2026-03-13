def reverse_string(s:str)->str:
    s=list(s) 
    i=0
    j=len(s)-1
    while i<j:
       s[i],s[j]=s[j],s[i]
       i=i+1
       j=j-1
    return "".join(s)



def main():
   string=input("enter a string: ")
   result=reverse_string(string)
   print("Reversed String:",result)

if __name__=="__main__":
   main()   