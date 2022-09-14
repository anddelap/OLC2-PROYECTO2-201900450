from Enum.typeExpression import typeExpression

Dominant = [
                #STRING                #INTEGER                #FLOAT                 #BOOL                   #CHAR              #STRING POINTER            #USIZE
    # STRING        
    [           typeExpression.STRING, None,                  None,                   None,                   None,             typeExpression.STRING,      None],
    #INTERGER
    [           None,                  typeExpression.INTEGER, None,                  None,                   None,              None,                      typeExpression.USIZE],
    #FLOAT
    [           None,                  None,                   typeExpression.FLOAT,  None,                   None,              None,                      None],
    #BOOL
    [           None,                  None,                   None,                  None,                   None,              None,                      None],
    #CHAR
    [           None,                  None,                   None,                  None,                   None,              None,                      None],
    #STRING POINTER
    [           typeExpression.STRING, None,                   None,                  None,                   None,              typeExpression.PSTRING,    None],
    #USIZE
    [           None,                  typeExpression.USIZE,   None,                  None,                   None,              None,                      typeExpression.USIZE],
]