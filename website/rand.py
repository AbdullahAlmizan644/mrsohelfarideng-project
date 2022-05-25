from random import randint


def random_generate():
    LIST=[1,2,3,4,5,6,7,8,9]
    token=randint(1,9)


    while True:
        if token in LIST:
            print(token)
            token=randint(1,9)
            print("new")
            continue

        else:
            break

    return token
        

print(random_generate())