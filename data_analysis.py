def find_max(datalist):
    maxval=datalist[0]
    for item in datalist:
        if item>maxval:
            maxval=item
        else:
            maxval=maxval
    print(maxval)
def remove_duplicates(datalist):
    print(set(datalist))
def fibonacci_sequence(n):
  a=0
  b=1
  for i in range(0,n):
    print(a)
    a,b=b,a+b
def kth_smallest_numnber(numbers,k):
    sorted_numbers=sorted(numbers)
    print(sorted_numbers[k-1])
