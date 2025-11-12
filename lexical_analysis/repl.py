def repl():
    while True:
        try:
            command=input(">> ")
            if command.strip().lower()=="exit":
                print("bye")
                break
            print("hhh",command)
        except Exception as e:
            print("Exception: ",e)
if __name__=="__main__":
    repl()