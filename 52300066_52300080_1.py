import itertools

def Infix2Postfix(Infix):
    # Độ tiên của các toán tử
    precedence = {
        '~': 4, # Cao nhất
        '&': 3,
        '|': 2,
        '>': 1,
        '=': 0 # Thấp nhất
    }

    output = [] # Kết quả Postfix
    stack = [] # Dùng để thao tác với các toán tử

    for token in Infix:
        # Nếu là toán hạng thì thêm vào output
        if token.isalpha():
            output.append(token)
        # Nếu là '(' hạng thì thêm vào stack
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
        # + B3 : Nếu toán tử đang xét > (độ ưu tiên cao hơn) toán tử ngoài cùng -> Thêm toán tử đang xét vào stack 
        # + B4 : Nếu toán tử đang xét <= (độ ưu tiên thấp hơn hoặc bằng) toán tử ngoài cùng -> Thêm toán tử ngoài cùng vào output và quay lại B1
        else:
            while (stack and stack[-1] != '(' and precedence.get(token, -1) <= precedence.get(stack[-1], -1)):
                output.append(stack.pop())
            stack.append(token)
    # Đưa hết các toán tử còn lại trong stack ra output
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# In ra màn hình kết quả chuyển đổi từ Infix sang Postfix
expr1 = "R|(P&Q)" 
expr2 = "~P|(Q&R)>R"  
expr3 = "P|(R&Q)" 
expr4 = "(P>Q)&(Q>R)"
expr5 = "(P|~Q)>~P=(P|(~Q))>~P"

print(f"Infix 1: {expr1} → Postfix 1: {Infix2Postfix(expr1)}\n")
print(f"Infix 2: {expr2} → Postfix 2: {Infix2Postfix(expr2)}\n")
print(f"Infix 3: {expr3} → Postfix 3: {Infix2Postfix(expr3)}\n")
print(f"Infix 4: {expr4} → Postfix 4: {Infix2Postfix(expr4)}\n")
print(f"Infix 5: {expr5} → Postfix 5: {Infix2Postfix(expr5)}\n")


# Đánh giá biểu thức hậu tố với các giá trị biến cho trước
def eval_postfix(postfix, values):
    stack = []
    for token in postfix:
        # Nếu là toán hạng thì đưa giá trị True/False vào stack
        if token.isalpha():
            stack.append(values[token])
        # Nếu là NOT thì đảo ngược giá trị
        elif token == '~':
            a = stack.pop()
            stack.append(not a)
        else: # Các toán tử nhị phân: &, |, >, =
            b = stack.pop()
            a = stack.pop()
            if token == '&':
                stack.append(a and b)
            elif token == '|':
                stack.append(a or b)
            elif token == '>':
                stack.append((not a) or b)
            elif token == '=':
                stack.append(a == b)
    return stack[0] # Trả về kết quả cuối cùng


# 
def Postfix2Truthtable(Postfix):
    # Tìm tất cả các toán tử (ký tự chữ cái), sắp xếp lại
    variables = sorted(set(filter(str.isalpha, Postfix)))

    print("Truth Table for:", Postfix)
    print(' | '.join(variables) + " | Result")
    print('-' * (len(variables) * 4 + 10))
    # Duyệt tất cả các tổ hợp True/False của các toán tử
    for values_tuple in itertools.product([False, True], repeat=len(variables)):
        values = dict(zip(variables, values_tuple))
        result = eval_postfix(Postfix, values)
        row = ' | '.join(['T' if values[var] else 'F' for var in variables])
        print(f"{row} |   {'T' if result else 'F'}")

# In kết quả bảng chân trị ra màn hình
if __name__ == "__main__":
    expr1 = "R|(P&Q)"
    expr2 = "~P|(Q&R)>R"
    expr3 = "P|(R&Q)" 
    expr4 = "(P>Q)&(Q>R)"
    expr5 = "(P|~Q)>~P=(P|(~Q))>~P"

    postfix1 = Infix2Postfix(expr1)
    postfix2 = Infix2Postfix(expr2)
    postfix3 = Infix2Postfix(expr3)
    postfix4 = Infix2Postfix(expr4)
    postfix5 = Infix2Postfix(expr5)

    print("Expression 1 (Infix):", expr1)
    print("Postfix:", postfix1)
    Postfix2Truthtable(postfix1)
    print("\n" + "-"*40 + "\n")

    print("Expression 2 (Infix):", expr2)
    print("Postfix:", postfix2)
    Postfix2Truthtable(postfix2)
    print("\n" + "-"*40 + "\n")

    print("Expression 3 (Infix):", expr3)
    print("Postfix:", postfix3)
    Postfix2Truthtable(postfix3)
    print("\n" + "-"*40 + "\n")

    print("Expression 4 (Infix):", expr4)
    print("Postfix:", postfix4)
    Postfix2Truthtable(postfix4)
    print("\n" + "-"*40 + "\n")

    print("Expression 5 (Infix):", expr5)
    print("Postfix:", postfix5)
    Postfix2Truthtable(postfix5)
    print("\n" + "-"*40 + "\n")

