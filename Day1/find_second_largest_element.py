def second_largest(nums:list[int])->int:
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(len(nums)):
        if nums[i]>largest:
            if(i==len(nums)-1):second_largest=largest
            largest=nums[i]
        elif nums[i]<largest and nums[i]>second_largest:
            second_largest=nums[i]    

    if second_largest==float('-inf'):
        return -1
    return second_largest


def main():
    nums=[10,10,10]
    print(second_largest(nums))

if __name__=="__main__":
    main()    
