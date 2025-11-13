from simple_lexer import Lexer
from def_class import SimpleTokenReader,TokenType
from ast_node import AstNodeType,SimpleAstNode
import copy
class Parse():
    def __init__(self,script):
        self.lexer=Lexer()
        self.tokens=self.lexer.tokenize(script)
        
    def parse(self):
        root_node=self.prog(self.tokens)
        return root_node

    def prog(self,tokens:SimpleTokenReader):
        node=SimpleAstNode(AstNodeType.Program,"pwc")
        while tokens.peek()!=None:
            child=self.int_declare(tokens)
            if child==None:
                child=self.expression_statement(tokens)
            if child==None:
                child=self.assignment_statement(tokens)
            if child!=None:
                node.add_child(child)
            else:
                print("Unknown Statement!")
                break
        return node

    def int_declare(self,tokens:SimpleTokenReader):
        token=tokens.peek()
        node=None
        if token!=None and token.get_type()==TokenType.Int:
            token=tokens.read()
            if tokens.peek().get_type()==TokenType.Identifier:
                token=tokens.read()
                node=SimpleAstNode(AstNodeType.IntDeclaration,token.get_text())
                token=tokens.peek()
                if token!=None and token.get_type()==TokenType.Assigment:
                    tokens.read()
                    child=self.additive(tokens)
                    if child==None:
                        raise Exception("Invalid variable initialization!")
                    else:
                        node.add_child(child)
            else:
                raise Exception("Varialble name expected")
        if node!=None:
            token=tokens.peek()
            if token!=None and token.get_type()==TokenType.Semicolon:
                tokens.read()
            else:
                raise Exception("invalid statement, expecting semicolon")
        return node

    def assignment_statement(self,tokens:SimpleTokenReader):
        node=None
        token=tokens.peek()
        if token!=None and token.get_type()==TokenType.Identifier:
           token=tokens.read()
           node=SimpleAstNode(AstNodeType.AssignmentStmt,token.get_text()) 
           token=tokens.peek()
           if token!=None and token.get_type()==TokenType.Assigment:
               tokens.read()
               child=self.additive(tokens)
               if child==None:
                   raise Exception("Expression statement required")
               else:
                   node.add_child(child)
                   token=tokens.peek()
                   if token!=None and token.get_type()==TokenType.Semicolon:
                        tokens.read()
                   else:
                        raise Exception("Invalid statement, semicolon required.")  
           else:
               tokens.unread()
        return node
    
    def expression_statement(self,tokens:SimpleTokenReader):
        pos=tokens.get_position()
        node=self.additive(tokens)
        if node!=None:
            token=tokens.peek()
            if token!=None and token.get_type()==TokenType.Semicolon:
                tokens.read()
            else:
                tokens.set_position(pos)
                node=None
        return node

    def additive(self,tokens:SimpleTokenReader):
        child1=self.multiplicate(tokens)
        node=child1
        if child1!=None:
            while True:
                token=tokens.peek()
                if token!=None and (token.get_type()==TokenType.Plus or token.get_type()==TokenType.Minus):
                    tokens.read()
                    child2=self.multiplicate(tokens)
                    if child2!=None:
                        node=SimpleAstNode(AstNodeType.Additive,token.get_text())
                        node.add_child(child1)
                        node.add_child(child2)
                        child1=node
                    else:
                        raise Exception("Invalid additive expression, expecting right part.")
                else:
                    break
        return node


    def multiplicate(self,tokens:SimpleTokenReader):
        child1=self.primary(tokens)
        node=child1
        if child1!=None:
            while True:
                token=tokens.peek()
                if token!=None and (token.get_type()==TokenType.Star or token.get_type()==TokenType.Slash):
                    child2=self.primary(tokens)
                    if child2!=None:
                        node=SimpleAstNode(AstNodeType.Multiplicative,token.get_text())
                        node.add_child(child1)
                        node.add_child(child2)
                        child1=node
                    else:
                        raise Exception("Invalid multiplicate expression, repecting right part.")
                else:
                    break
        return node

    def primary(self,tokens:SimpleTokenReader):
        token=tokens.peek()
        node=None
        if token!=None:
            token=tokens.read()
            if token.get_type()==TokenType.IntLiteral:
                node=SimpleAstNode(AstNodeType.Intliteral,token.get_text())
            elif token.get_type()==TokenType.Identifier:
                node=SimpleAstNode(AstNodeType.Identifier,token.get_text())
            elif token.get_type()==TokenType.LeftParen:
                node=self.additive(tokens)
                if node!=None:
                    token=tokens.peek() 
                    if token!=None and token==TokenType.RightParen:
                        tokens.read()
                    else:
                        raise Exception("Expecting right parenthesis.")
                else:
                    raise Exception("Expecting an additive expression inside parenthesis.")
        return node

    def dump_ast(self,node:SimpleAstNode,indent:str):
        if node.get_type()==AstNodeType.Program:
            print("---------------------parse------------------")
        print(indent,node.get_type()," ",node.get_text())
        for child in node.get_children():
            self.dump_ast(child,indent+"\t")
    
    def dump_tokens(self):
        print("---------------------tokens------------------")
        temp=copy.deepcopy(self.tokens)
        token=temp.read()
        while token!=None:
            print(token.get_type()," ",token.get_text())
            token=temp.read()
