from __future__ import annotations
from typing import Optional
from enum import Enum,auto
class AstNodeType(Enum):
    Program=auto()

    IntDeclaration=auto()
    ExpressionStmt=auto()
    AssignmentStmt=auto()

    Primary=auto()
    Multiplicative=auto()
    Additive=auto()

    Identifier=auto()
    Intliteral=auto()

class AstNode():
    def get_parent(self)->Optional[AstNode]:
        pass
    def get_children(self)->Optional[list[AstNode]]:
        pass
    def get_text(self):
        pass
    def get_type(self):
        pass

class SimpleAstNode(AstNode):
    def __init__(self,node_type:AstNodeType,text:str):
        self.node_type=node_type
        self.text=text
        self.parent=None
        self._childen:list[SimpleAstNode]=[]

    def get_parent(self):
        return self.parent
    
    def get_children(self):
        return tuple(self._childen)

    def get_type(self):
        return self.node_type
    
    def get_text(self):
        return self.text
        
    def add_child(self,child:SimpleAstNode):
        self._childen.append(child)
        child.parent=self

    
        
