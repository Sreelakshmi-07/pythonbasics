a = [1,2,3]
i = int(input("Enter index:"))
try:
    print(a[i])
# except:
#     print("Unexpected error occurred")
except Exception as e:
    print(e)