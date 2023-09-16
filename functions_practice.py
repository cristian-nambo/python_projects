def hello():
    print("Greetings User")
    
def pack( char, int, both):
    return[char, int, both]

def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(list)):
            if i  ==0:
                print(f"First I eat {list[0]}")
            else:
                print(f"Next I eat {list[i]}")

hello()
result = pack("char", "int", "both")
print(result)
eat_lunch(["burrito", "salad", "candy", "my diet pills"])

 