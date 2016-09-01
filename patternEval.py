__author__ = 'stevenchun'
'''
1. Given n sorted lists, each with variable size, write a function to return a single, sorted list.

notes: So we've got n sorted lists. They can start at any point, end at any point. How do we take advantage
of the fact that each individual list is sorted? Okay so a collection of the first element of each list will be the collection of
least (on average) elements that we can get given what we know. As long as we keep that collection sorted, popping from it will return
the minimum value to be added to the final list
a heap is one way to efficiently keep the min element at the root
a priority queue is another option, but python apparently has a nice heapq library so let's do that
'''
import heapq

def merge(list_of_lists):
    heap = []
    result =[]
    while len(list_of_lists) > 0:
        r = range(len(list_of_lists)) #keep the range that the for loop is using mutable
        for i in r:
            lowest=list_of_lists[i].pop(0) #return and remove first element
            heapq.heappush(heap, lowest) #add to heap, maintains heap

            if len(list_of_lists[i]) == 0: #ensure we don't have any empty lists lying around
                    del list_of_lists[i]
                    r.pop(len(r)-1) #mutate the iterable that the for loop is going over to account for the deleted list

    while len(heap) > 0:
        result.append(heapq.heappop(heap))

    return result
'''
#test cases
lol=[[1], [1, 2], [1, 2, 3], [5, 6, 7, 8]]
lol2 = [[50], [1, 2], [1, 7, 20], [19, 20, 21, 88], [1]]
lol3 = []
lol4 = [[-2, 10], [-3,4]]
print merge(lol4)
'''
#concluding notes: I believe this is O(a*n*log(n)) where n is the length of list_of_lists and a is the length
# of the longest sorted list.



'''
Given a list of positive integers and another integer, write a function that determines if the list contains two numbers that add up to the integer parameter, and if so, returns those numbers. For example, if
my_list = [9, 1, 7, 10, 4, 3, 2, 5]

find_pair(my_list, 15) should return [10, 5] and
find_pair(my_list, 18) should return []

Assume the list is unsorted.

notes: okay so because lookup seems important here and duplicates not so much, my first instinct is a dictionary. I like those.

'''

def find_pair(my_list, k):
    dict = {}
    for num in my_list:
        if dict.has_key(num):
            dict[num] += 1
        else:
            dict[num] = 1 #the 1 refers to instances of that number, so we can determine if combos like 5,5 are available

        if dict.has_key(k-num):
            if (k-num) == num and dict[num]>1:  #if this is a 5+5=10 type scenario and there are more than one instance
                return [k-num, num]
            elif (k-num) != num:
                return [num, k-num]

    return []

my_list = [4, 7, 10, 4, 2, 5, 5]

print find_pair(my_list, 8)


#concluding notes: I believe this to be O(n)







