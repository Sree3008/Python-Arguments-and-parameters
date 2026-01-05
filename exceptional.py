# exceptional handling
try:
    n=int(input())
    print(n//0)
except zerodivisionerror:
    print("Error")
finally:
    print("Process completed")