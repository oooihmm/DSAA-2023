import random


def infix_to_postfix(expression):
    OPERATORS = set(["+", "-", "*", "/", "(", ")", "^"])
    PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    stack = []
    output = ""

    index = 0

    for value in expression:
        if value not in OPERATORS:
            output += value
        elif value == "(":
            stack.append("(")
        elif value == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()
        else:
            while stack and stack[-1] != "(" and PRIORITY[value] <= PRIORITY[stack[-1]]:
                output += stack.pop()
            stack.append(value)
        print("단계 " + str(index) + " 스택 상태 : " + str(stack))
        index += 0

    while stack:
        output += stack.pop()

    print("포스트픽스 변환 결과 : " + output)
    return output


def create_random_infix():
    OPERATORS = ["+", "-", "*", "/", "^", "(", ")"]
    number = random.randrange(10, 15)  # 수식 내의 숫자와 연산자 개수 랜덤 선정
    expression = ""

    open = 0
    close = 0

    for i in range(number):
        if i == 0 or i % 2 == 0:
            value = str(random.randrange(1, 100))
            expression += value
        else:
            if i != (number - 1):
                operator = random.choice(OPERATORS)
                expression += operator

    is_true = check_expression(expression)
    if is_true == True:
        print("생성된 수식 : " + expression)
        return expression
    else:
        create_random_infix()


def check_expression(expression):
    stack = []

    for char in expression:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            else:
                top = stack[-1]
                if char == ")" and top == "(":
                    stack.pop()
                else:
                    return False

    if len(stack) != 0:
        return False

    return True


if __name__ == "__main__":
    expression = input("수식을 입력해주세요 : ")
    if expression == "0":
        print("수식 계산기를 종료합니다.")
    elif expression == "1000":
        print("랜덤한 인픽스 수식을 생성하고 있습니다...")
        new_expression = create_random_infix()
        infix_to_postfix(new_expression)
    else:
        infix_to_postfix(expression)
