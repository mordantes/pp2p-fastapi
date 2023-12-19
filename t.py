


def gen():
    for i in 'abc':
        yield i


def main():
    print('123')
    a =  gen()
    print(
        [yield from a]
    )
    # print(
    #     gen()
    # )

if __name__ == '__main__' :
    main()