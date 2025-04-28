def Infix2Postfix(Infix):
    # Độ ưu tiên các toán tử
    precedence = {
        '~': 4,
        '&': 3,
        '|': 2,
        '>': 1,
        '=': 0
    }
    
    output = []   # Kết quả 
    stack = []    # Stack để chứa toán tử

    for token in Infix:
        # Nếu là toán hạng (A-Z) thêm vào output
        if token.isalpha(): 
            output.append(token)

        # Nếu là '(' thêm vào stack
        elif token == '(':
            stack.append(token)

        # Nếu là ')' thì sẽ xét theo 2 bước B1: Nếu toán tử ngoài cùng trong stack là '(' thì xóa '(', 
                                            # B2: Nếu toán tử ngoài cùng của stack không phải là '(', thì lấy toán tử đó qua output và quay lại B1
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 

        # Nếu là toán tử thực hiện theo 4 bước

        # + B1 : Nếu stack rỗng -> Thêm vào stack
        # + B2 : Nếu toán tử ngoài cùng stack là '(' -> Thêm vào stack
        # + B3 : Nếu toán tử đang xét > toán tử ngoài cùng -> Thêm toán tử đang xét vào stack 
        # + B4 : Nếu toán tử đang xét <= toán tử ngoài cùng -> Thêm toán tử ngoài cùng vào output và quay lại B1
        else: 
            while (stack and stack[-1] != '(' and precedence.get(token, -1) <= precedence.get(stack[-1], -1)):
                output.append(stack.pop())
            stack.append(token)

    # Đưa hết các toán tử còn lại ra output
    while stack:
        output.append(stack.pop())

    return ''.join(output)


expr1 = "R|(P&Q)" # Đúng
expr2 = "~P|(Q&R)>R" # SAI 
expr3 = "P|(R&Q)" # Đúng
expr4 = "(P>Q)&(Q>R)" # Đúng
expr5 = "(P|~Q)>~P=(P|(~Q))>~P" #SAI


# https://www.calcont.in/Conversion/infix_to_postfix


print(Infix2Postfix(expr1))
print(Infix2Postfix(expr2))
print(Infix2Postfix(expr3))
print(Infix2Postfix(expr4))
print(Infix2Postfix(expr5))