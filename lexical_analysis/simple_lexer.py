from def_class import SimpleToken,SimpleTokenReader,TokenType,DFastate
import pdb
class Lexer():
    def __init__(self):
        self.token=SimpleToken()
        self.token_list=[]

    def _is_alpha(self,ch:str)->bool:
        if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
            return True
        return False
    
    def _is_digit(self,ch:str)->bool:
        if ch>='0' and ch<='9':
            return True
        return False
    
    def _is_blank(self,ch:str)->bool:
        if ch=="\n" or ch=="\t" or ch==" ":
            return True
        return False
    
    def init_token(self,ch:str)->DFastate:
        if self.token.get_text_len()>0:
            self.token_list.append(self.token)
            self.token=SimpleToken()

        new_state=DFastate.Initial
        if self._is_alpha(ch):
            if ch=="i":
                new_state=DFastate.Id_int1
            else:
                new_state=DFastate.Id
            self.token.set_type(TokenType.Identifier)
            self.token.text_add(ch)
        elif self._is_digit(ch):
            new_state=DFastate.IntLiteral
            self.token.set_type(TokenType.IntLiteral)
            self.token.text_add(ch)
        elif ch==">":
            new_state=DFastate.Gt
            self.token.set_type(TokenType.Gt)
            self.token.text_add(ch)
        elif ch=="=":
            new_state=DFastate.Assigment
            self.token.set_type(TokenType.Assigment)
            self.token.text_add(ch)
        elif ch=="+":
            new_state=DFastate.Plus
            # pdb.set_trace()
            self.token.set_type(TokenType.Plus)
            self.token.text_add(ch)
        elif ch=="-":
            new_state=DFastate.Minus
            self.token.set_type(TokenType.Minus)
            self.token.text_add(ch)
        elif ch=="*":
            new_state=DFastate.Star
            self.token.set_type(TokenType.Star)
            self.token.text_add(ch)
        elif ch=="/":
            new_state=DFastate.Slash
            self.token.set_type(TokenType.Slash)
            self.token.text_add(ch)
        elif ch==";":
            new_state=DFastate.Semicon
            self.token.set_type(TokenType.Semicolon)
            self.token.text_add(ch)
        elif ch=="(":
            new_state=DFastate.LeftParen
            self.token.set_type(TokenType.LeftParen)
            self.token.text_add(ch)
        elif ch==")":
            new_state=DFastate.RightParen
            self.token.set_type(TokenType.RightParen)
            self.token.text_add(ch)
        else:
            new_state=DFastate.Initial
        return new_state

    def tokenize(self,code:str):
        state=DFastate.Initial
        for ch in code:
            if state==DFastate.Initial:
                state=self.init_token(ch)
            elif state==DFastate.Id:
                if self._is_alpha(ch) or self._is_digit(ch):
                    self.token.text_add(ch)
                else:
                    state=self.init_token(ch)
            elif state==DFastate.Assigment:
                if ch=="=":
                    self.token.text_add(ch)
                    self.token.set_type(TokenType.Ge)
                    state=DFastate.Ge
                else:
                    self.init_token(ch)
            elif state==DFastate.Ge or state==DFastate.Assigment or state==DFastate.Plus \
            or state==DFastate.Minus or state==DFastate.Star or state==DFastate.Slash or state==DFastate.Semicon \
            or state==DFastate.LeftParen or state==DFastate.RightParen:
                state=self.init_token(ch)
            elif state==DFastate.Id_int1:
                if ch=="n":
                    self.token.text_add(ch)
                    state=DFastate.Id_int2
                elif self._is_digit(ch) or self._is_alpha(ch):
                    state=DFastate.Id
                    self.token.text_add(ch)
                else:
                    state=self.init_token(ch)
            elif state==DFastate.Id_int2:
                if ch=="t":
                    self.token.text_add(ch)
                    state=DFastate.Id_int3
                elif self._is_digit(ch) or self._is_alpha(ch):
                    state=DFastate.Id
                    self.token.text_add(ch)
                else:
                    state=self.init_token(ch)
            elif state==DFastate.Id_int3:
                if self._is_blank(ch):
                    self.token._type=TokenType.Int
                    state=self.init_token(ch)
                else:
                    state=DFastate.Id
                    self.token.text_add(ch)
            elif state==DFastate.IntLiteral:
                if self._is_digit(ch):
                    self.token.text_add(ch)
                else:
                    state=self.init_token(ch)
        ch=""
        if self.token.get_text_len()>0:
            state=self.init_token(ch)
        return SimpleTokenReader(self.token_list)
        
def dump(simple_token_reader:SimpleTokenReader):
    token=simple_token_reader.read() 
    while token!=None:
        print(token.get_text(),token.get_type())
        token=simple_token_reader.read()

                    

if __name__ == "__main__":
    lexer=Lexer()
    token_reader=lexer.tokenize("int a+b=3 ")
    dump(token_reader)