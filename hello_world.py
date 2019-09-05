import sys
# class HelloWorld:
print('hello world outside function')

if len(sys.argv) == 1:
    platform = 'an unspecified'
else:
    platform = str(sys.argv[1])  

def run_hello_world(platform):
    print('Hello World')
    print('first change being made to the build')
    count = 0
    for i in range(10):
        print(str(count), 'I am using', platform, "OS")
        count += 1

run_hello_world(platform)