class worker:
    def __init__(self):
        print("function created")
    def __del__(self):
        print("deleted")

def x():
    y=worker()
    return y

y=x()