def say():
    greeting = 'Hello Goodbye'

    def display():
        print(greeting)

    return display


f = say()
f()