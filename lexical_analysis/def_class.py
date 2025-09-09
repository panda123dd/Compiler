from abc import ABC,abstractmethod
from enum import Enum,auto

class TokenType(Enum):
    Plus=auto()
    Minus=auto()
    Star=auto()
    Slash=auto()

    Ge=auto()
    Gt=auto()
    Eq=auto()
    Le=auto()
    Lt=auto()

    Semicolon=auto()
    LeftParen=auto()
    RightParen=auto()

    Assigment=auto()

    If=auto()
    Else=auto()

    Int=auto()

    Identifier=auto()

    IntLiteral=auto()
    StringLiteral=auto()

class DFastate(Enum):
    Initial=auto()
    
    If=auto()
    Id_if1=auto()
    Id_if2=auto()
    Else=auto()
    Id_else1=auto()
    Id_else2=auto()
    Id_else3=auto()
    Id_else4=auto()
    Int=auto()
    Id_int1=auto()
    Id_int2=auto()
    Id_int3=auto()
    Id=auto()
    Gt=auto()
    Ge=auto()
    
    Assigment=auto()
    Plus=auto()
    Minus=auto()
    Star=auto()
    Slash=auto()

    Semicon=auto()
    LeftParen=auto()
    RightParen=auto()

    IntLiteral=auto()

class Token(ABC):
    @abstractmethod
    def get_type(self)->TokenType:
        pass

    @abstractmethod
    def get_text(self)->str:
        pass

class SimpleToken(Token):
    def __init__(self):
        self._type=None
        self._text=""
    
    def get_type(self):
        return self._type
    
    def get_text(self):
        return self._text

    def get_text_len(self):
        return len(self._text)
    
    def text_add(self,ch:str):
        self._text+=ch
    
    def set_type(self,token_type):
        self._type=token_type

class TokenReader(ABC):
    @abstractmethod
    def read()->SimpleToken:
        pass
    
    @abstractmethod
    def peek()->SimpleToken:
        pass
    
    @abstractmethod
    def unread()->SimpleToken:
        pass
    
    @abstractmethod
    def get_position():
        pass

    @abstractmethod
    def set_position(position:int):
        pass

class SimpleTokenReader(TokenReader):
    def __init__(self,simple_tokens:list[SimpleToken]):
        self.simple_tokens=simple_tokens
        self.pos=0

    def read(self):
        if self.pos<len(self.simple_tokens):
            token=self.simple_tokens[self.pos]
            self.pos+=1
            return token
        return None
    
    def peek(self):
        if self.pos<len(self.simple_tokens):
            return self.simple_tokens[self.pos]
        return None

    def unread(self):
        if self.pos>0:
            self.pos-=1

    def get_position(self):
        return self.pos
    
    def set_position(self,position:int):
        if 0<=position and position<len(self.simple_tokens):
            self.pos=position
        
    


