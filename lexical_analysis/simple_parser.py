from simple_lexer import Lexer
from def_class import SimpleTokenReader,TokenType
from ast_node import AstNodeType,SimpleAstNode
class Parse():
    def __init__(self,script):
        lexer=Lexer()
        tokens=lexer.tokenize(script)
        
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
                    token.read()
                    child=self.additive(tokens)
                    if child==None:
                        raise Exception("Invalid variable initialization!")
                    else:
                        node.add_child(child)
            else:
                raise Exception("Varialble name expected")
        if node==None:
            token=tokens.peek()
            if token!=None and token.get_type()==TokenType.Semicolon:
                token.read()
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

           
                   


    def expression_statement(self,tokens:SimpleTokenReader):
        pass

    def assignment_statement(self,tokens:SimpleTokenReader):
        pass

    def additive(self,tokens:SimpleTokenReader):
        pass