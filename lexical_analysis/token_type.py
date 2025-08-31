from enum import Enum,auto

class token_type(Enum):
    plus=auto()
    minus=auto()
    star=auto()
    slash=auto()

    ge=auto()
    gt=auto()
    eq=auto()
    le=auto()
    lt=auto()

    semicolon=auto()
    left_paren=auto()
    right_paren=auto()

    assigment=auto()

    ife=auto()
    elsee=auto()

    int=auto()

    identifier=auto()

    int_literal=auto()
    string_literal=auto()
    


