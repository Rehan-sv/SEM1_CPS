x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y) #doesnt remove the value only change that index number
print(x)