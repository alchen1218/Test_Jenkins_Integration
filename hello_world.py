# class HelloWorld:
print('hello world outside function')

def run_hello_world(platform):
    print('Hello World')
    print('first change being made to the build')
    count = 0
    for i in range(10):
        print(count, 'I am using ', platform, "OS")
        count += 1


def first_change():
    print('first change being made to the build')
