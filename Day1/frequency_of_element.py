class solution:
    def find_frequency(self,nums:list[int])->dict:
        mpp={}
        for i in range(len(nums)):
            if nums[i] in mpp:
                mpp[nums[i]]+=1
            else:
                mpp[nums[i]]=1
        return mpp            
class App:
    def run(self):
        nums=[1,2,2,3,1,4,2]

        sol=solution()
        result=sol.find_frequency(nums)

        for key,value in result.items():
            print(key,":",value)

if __name__=="__main__":
    app=App()
    app.run()            