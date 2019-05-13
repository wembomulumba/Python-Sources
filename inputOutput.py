print("Type integers, each followed by Enter; or just Enter to finish")

total = 0
count = 0
while True:
    line = input("integer: ")
    if line:
        try:
            number = int(line)
        except Exception as err:
            print(err)
            continue
        except EOFError as err:
            print(err)
            continue    
        total += number
        count += 1
    else:
        break
if count:
    print("count =", count, "total =", total, "mean =", total / count)

