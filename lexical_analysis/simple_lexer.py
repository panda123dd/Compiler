from def_class import SimpleToken,TokenReader,TokenType
class Lexer():
    def __init__(self):
        self.token=SimpleToken()
        self.token_list=[]
        self.token_text=""

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
    
    def init_token(self,ch:str):
        if len(self.token_text)>0:
            
if __name__ == "__main__":
    a='bv'
    if a>='c' and a<="e":
        print("y")