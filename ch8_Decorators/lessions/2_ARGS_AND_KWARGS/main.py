def args_logger(*args, **kwargs):
    for i in args:
        print(f" * {i}")

    sorted_kwargs = kwargs.items()
    
    for i in sorted(sorted_kwargs):
        print(f" * {i[0]}: {i[1]}")


# Don't edit below this line


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    test(1, 2, date_str="01/01/2023")
    test(message="Hello World", to_delete="l")
    test(1, 2, 3, 4, 5)
    test("hi", True, name="Lane", age=28)


main()
