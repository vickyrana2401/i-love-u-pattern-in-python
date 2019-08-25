for i in range (6):
    for j in range (6):
        if (j//2==1) or ((i==0 or i==5) and j%1==0) :
            print(" O ",end=' ')
        else:
            print("   ",end=' ')
    for j in range (7):
        if (i==0 and j%3!=0) or (i==1 and j%3==0) or (i-j==2) or (i+j==8):
            print(" O ",end=' ')
        else:
            print("   ",end=' ')
    for j in range (4):
        if ((i%1==0 and (j==0 or j//3==1))or(i//5==1 and j%1==0)):
            print("  O  ",end=' ')
        else:
            print("     ",end=' ')
    print("\n")
