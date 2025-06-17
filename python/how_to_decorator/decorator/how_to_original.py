def my_decorator(func):
    def wrapper():
        print("処理の前")
        func()
        print("処理の後")

    return wrapper


@my_decorator
def say_hello():
    print("こんにちは")


if __name__ == '__main__':
    say_hello()
