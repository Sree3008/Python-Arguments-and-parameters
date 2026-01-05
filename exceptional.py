# exceptional handling
try:
    n=int(input())
    print(n//0)
except Exception: 
    print("Error")
finally:
    print("Process completed")