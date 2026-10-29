color=[]
n=int(input("enter the totatl number of colors:"))
print("enter colors:")
for i in range(n):
    ch=input()
    color.append(ch)
print(f"first color is: {color[0]} \n lastcolor is:{color[-1]}")     
