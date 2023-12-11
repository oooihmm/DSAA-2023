class BracketChecker:
    def __init__(self):
        self.stack = []  # 스택을 초기화합니다.

    def check_brackets(self, expression):
        stack_status = []
        for char in expression:
            if char in "([{":
                self.stack.append(char)
            elif char in ")]}":
                if not self.is_matching_pair(char):
                    stack_status.append(f"오류: 짝이 맞지 않는 '{char}'가 있습니다.")
                    return False, stack_status
                else:
                    self.stack.pop()
            stack_status.append(f'stack 상태 : {" -> ".join(self.stack)}')

        if not self.stack:
            return True, stack_status
        else:
            stack_status.append("오류: 괄호 짝이 맞지 않습니다.")
            return False, stack_status

    def is_matching_pair(self, char):
        if not self.stack:
            return False
        top = self.stack[-1]
        if char == ")" and top == "(":
            return True
        if char == "}" and top == "{":
            return True
        if char == "]" and top == "[":
            return True
        return False
