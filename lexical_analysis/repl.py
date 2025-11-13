from simple_parser import Parse
def repl():
    while True:
        try:
            command=input(">> ")
            if command.strip().lower()=="exit":
                print("bye")
                break
            p=Parse(command)
            p.dump_tokens()
            root_node=p.parse()
            p.dump_ast(root_node,"")
        except Exception as e:
            print("Exception: ",e)
if __name__=="__main__":
    repl()