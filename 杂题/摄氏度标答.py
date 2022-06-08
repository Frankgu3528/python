x,y=[int(x) for x in input().split()]
if x>y:
    print("Invalid.")
else:
    print(f"fahr celsius")
    i=x
    while i<=y:
        print(f"{i:d}{(i-32)/9.0*5:>6.1f}")
        i+=2
