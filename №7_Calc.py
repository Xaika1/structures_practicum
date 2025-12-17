class Calculator:
    
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}
    
    def is_operator(self, token):
        return token in self.precedence
    
    def infix_to_rpn(self, expression):
        output = []
        stack = []
        
        tokens = self.tokenize(expression)
        
        for token in tokens:
            if token.replace('.', '').isdigit():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            elif self.is_operator(token):
                while (stack and stack[-1] != '(' and
                       (self.precedence[stack[-1]] > self.precedence[token] or
                        (self.precedence[stack[-1]] == self.precedence[token] and 
                         self.associativity[token] == 'L'))):
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return output
    
    def tokenize(self, expression):
        tokens = []
        current_number = ''
        
        for char in expression.replace(' ', ''):
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
                tokens.append(char)
        
        if current_number:
            tokens.append(current_number)
        
        return tokens
    
    def calculate_rpn(self, rpn):
        stack = []
        
        for token in rpn:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ValueError("Деление на ноль")
                    result = a / b
                elif token == '^':
                    result = a ** b
                
                stack.append(result)
        
        return stack[0]
    
    def evaluate(self, expression):
        rpn = self.infix_to_rpn(expression)
        result = self.calculate_rpn(rpn)
        return rpn, result


def test_calculator():
    """Тестирование калькулятора"""
    
    print("ТЕСТИРОВАНИЕ КАЛЬКУЛЯТОРА")

    calc = Calculator()
    
    test_expressions = [
        ("3 + 4 * 2", "3 4 2 * +", 11.0),
        ("(3 + 4) * 2", "3 4 + 2 *", 14.0),
        ("10 / 2 - 3", "10 2 / 3 -", 2.0),
        ("2 ^ 3 + 1", "2 3 ^ 1 +", 9.0),
        ("5 + 3 * (7 - 2)", "5 3 7 2 - * +", 20.0),
        ("12.5 + 3.5 * 2", "12.5 3.5 2 * +", 19.5),
        ("2 * (3 + 4) / 2", "2 3 4 + * 2 /", 7.0)
    ]
    
    print("\nТестовые выражения:")
    
    all_passed = True
    
    for expr, expected_rpn, expected_result in test_expressions:
        try:
            rpn, result = calc.evaluate(expr)
            rpn_str = ' '.join(rpn)
            
            print(f"\nВыражение: {expr}")
            print(f"Ожидаемая ОПН: {expected_rpn}")
            print(f"Полученная ОПН: {rpn_str}")
            print(f"Ожидаемый результат: {expected_result}")
            print(f"Полученный результат: {result}")
            
            if rpn_str == expected_rpn and abs(result - expected_result) < 0.0001:
                print("ТЕСТ ПРОЙДЕН")
            else:
                print("ТЕСТ НЕ ПРОЙДЕН")
                all_passed = False
                
        except Exception as e:
            print(f"\nВыражение: {expr}")
            print(f"Ошибка: {e}")
            print("ТЕСТ НЕ ПРОЙДЕН")
            all_passed = False
    
    # Тест с ошибками
    print("\n\nТесты с ошибками:")
    
    error_expressions = [
        "10 / 0",
        "3 + * 4",
        "(3 + 4",
        "3 + 4)"
    ]
    
    for expr in error_expressions:
        try:
            rpn, result = calc.evaluate(expr)
            print(f"\nВыражение: {expr}")
            print(f"Результат: {result}")
            print("✗ Ожидалась ошибка, но её не было")
            all_passed = False
        except Exception as e:
            print(f"\nВыражение: {expr}")
            print(f"Ожидаемая ошибка: {type(e).__name__}: {e}")
            print("Ошибка обработана корректно")
    
    if all_passed:
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ!")

if __name__ == "__main__":
    test_calculator()