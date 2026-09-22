n=10
k=5
jar=n
c=1

while c==1:
    num= int(input("Enter no.of candies: "))
    if num>jar:
        print("Invalid input")
        
    else:
        jar=jar-num
        print("No.of candies sold:", num)
        print("No.of candies available:", jar)

        if jar<=k:
            jar=n
            print("Jar refilled")
            print("No.of candies available:", jar)

    c=int(input("Continue (1/0): "))
