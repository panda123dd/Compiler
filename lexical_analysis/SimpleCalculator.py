from simple_lexer import Lexer,SimpleTokenReader,TokenType
from ast_node import AstNode,SimpleAstNode,AstNodeType
import copy
class SimpleCalculator():
    def evaluate(self,script:str):
        tree=self.parse(script)
        dump_ast(tree,"")
        print("-"*80)
        self.calculator(tree,"")

    def parse(self,script:str):
        lex=Lexer()
        tokens=lex.tokenize(script)
        root_node=self.prog(tokens)
        return root_node
    
    def calculator(self,node:SimpleAstNode,indent:str):
        result=0
        print(indent,node.get_type()," ",node.get_text())
        if node.get_type()==AstNodeType.Program:
            for child in node.get_children():
                result=self.calculator(child,indent+"\t")
        elif node.get_type()==AstNodeType.Additive:
            childl=node.get_children()[0]
            res1=self.calculator(childl,indent+"\t")
            childr=node.get_children()[1]
            res2=self.calculator(childr,indent+"\t")
            if node.get_text()=="+":
                result=res1+res2
            else:
                result=res1-res2
        elif node.get_type()==AstNodeType.Multiplicative:
            childl=node.get_children()[0]
            res1=self.calculator(childl,indent+"\t")
            childr=node.get_children()[1]
            res2=self.calculator(childr,indent+"\t")
            if node.get_text()=="*":
                result=childl*childr
            else:
                result=childl/childr
        elif node.get_type()==AstNodeType.Intliteral:
            result=int(node.get_text())
        print(indent,"Result:",result)
        return result

    def prog(self,tokens:SimpleTokenReader)->SimpleAstNode:
        node=SimpleAstNode(AstNodeType.Program,"Calculator")
        child=self.additive(tokens)
        node.add_child(child)
        return node
    
    def int_declare(self,tokens:SimpleTokenReader):
        node=None
        token=tokens.peek()
        if token!=None and token.get_type()==TokenType.Int:
            token=tokens.read()
            if tokens.peek().get_type()==TokenType.Identifier:
                token=tokens.read()
                node=SimpleAstNode(AstNodeType.IntDeclaration,token.get_text())
                token=tokens.peek()
                if token!=None and token.get_type()==TokenType.Assigment:
                    tokens.read()
                    child=self.additive(tokens)
                    if child!=None:
                        node.add_child(child)
            if node!=None:
                token=tokens.peek()
                if token!=None and token.get_type()==TokenType.Semicolon:
                    tokens.read()
        return node
            
    def additive(self,tokens:SimpleTokenReader):
        childl=self.multiplicate(tokens)
        node=childl
        token=tokens.peek()
        if childl!=None and token!=None:
            if token.get_type()==TokenType.Plus or token.get_type()==TokenType.Minus:
                token=tokens.read()
                childr=self.additive(tokens)
                if childr!=None:
                    node=SimpleAstNode(AstNodeType.Additive,token.get_text())
                    node.add_child(childl)
                    node.add_child(childr)
        return node
    
    def multiplicate(self,tokens:SimpleTokenReader):
        childl=self.primary(tokens)
        node=childl
        token=tokens.peek()
        if childl!=None and token!=None:
            if token.get_type()==TokenType.Star or token.get_type()==TokenType.Slash:
                token=tokens.read()
                childr=self.multiplicate(tokens)
                if childr!=None:
                    node=SimpleAstNode(AstNodeType.Multiplicative,token.get_text())
                    node.add_child(childl)
                    node.add_child(childr)
        return node
    
    def primary(self,tokens:SimpleTokenReader):
        node=None
        token=tokens.peek()
        if token!=None:
            if token.get_type()==TokenType.IntLiteral:
                token=tokens.read()
                node=SimpleAstNode(AstNodeType.Intliteral,token.get_text())
            elif token.get_type()==TokenType.Identifier:
                token=tokens.read()
                node=SimpleAstNode(AstNodeType.Identifier,token.get_text())
            elif token.get_type()==TokenType.LeftParen:
                tokens.read()
                node=self.additive(tokens)
                if node!=None:
                    token=tokens.peek()
                    if token!=None and token.get_type()==TokenType.RightParen:
                        tokens.read()
        return node

def dump_ast(node:SimpleAstNode,indent:str):
    print(indent,str(node.get_type()),node.get_text())

    for child in node.get_children():
        dump_ast(child,indent+"\t")

def dump(sr:SimpleTokenReader):
    token=sr.read()
    print(type(token))
    while token!=None:
        print(token.get_text(),"  ",token.get_type())
        token=sr.read()

sc=SimpleCalculator()
sc.evaluate("7+8+9")


    
