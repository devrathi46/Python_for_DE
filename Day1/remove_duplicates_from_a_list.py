def remove_duplicates(nums:list[int])->list:
    st=set()
    result=[]

    for i in range(len(nums)):
        if nums[i] not in st:
            st.add(nums[i])
            result.append(nums[i])
        
    return result 


def main():
    nums=[1,1,1,2,2,3,5,6,7,8,8,8,8,9,0]
    print(remove_duplicates(nums))


if __name__=="__main__":
    main()   