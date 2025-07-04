#Using Heapq in python to find the nth element of a list and sort the list in ascending order
import heapq

def nelement(nums,n):
    if n<len(nums):
        nth_element= heapq.nsmallest(n,nums)[-1]
        print(f"The nth element of the list is:{nth_element}")
    else:
        print("Not found")
    

def sort_list(nums):
    print(f"Original list:{nums}")
    
    heapq.heapify(nums)
    print(f"Heap:{nums}")
    
    sorted_list=[] 
    while nums:
        smallest=heapq.heappop(nums)
        sorted_list.append(smallest)
    
    
    print(f"The Sorted list is:{sorted_list}")


nums=[34,7,98,53,100,87,9,2,49,71] #replace-with-your-list
n=3 #replace-with-nth-element
nelement(nums,n)
sort_list(nums)



    