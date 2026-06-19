#let us print charan 4 times using recursion
# Head Recursion
count = 0

def func():
    global count
    if count == 4:
        return

    print("Charan")
    count += 1
    func()

func()


#tc = o(n)
#sc = o(n)