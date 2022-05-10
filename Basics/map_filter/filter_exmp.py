list1=[1,2,3,4,5,6,7,8]
list1.sort(reverse=True)
print(list1)
evens=list(filter(lambda num:num%2==0,list1))
print(evens)
odd=list(filter(lambda num:num%2!=0,list1))
print(odd)
greate=list(filter(lambda num:num>5,list1))
print(greate)