
def largest(nums:list[int])->int:
    largest=nums[0]
    for i in range(0,len(nums)):
        if nums[i]>largest:
            largest=nums[i]


    return largest




def main():
    v=[1,5,3,9,2]
    print(largest(v))

if __name__=="__main__":
    main()    