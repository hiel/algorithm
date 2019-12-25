class PrefixCalcurator():
    def __init__(self):
        self.__init()
    
    def __init(self): # 초기화
        self.__infix = '' # 중위표기식
        self.__prefix = '' # 후위표기식
        self.__answer = 0 # 답
        self.__stack = []
    
    def execute(self, c): # 실행
        self.__init() # 초기화
        self.__set_infix(c) # 공백 제거
        self.__convert() # 후위표기식으로 컨버팅
        self.__calcuate() # 계산
        self.__print_status() # 결과 출력

    def test(self): # 테스트
        self.execute('6 - 1 * 3')
        self.execute('(9 - 4 / 1) * 4')
        self.execute('(2 + 5) * 3 * (2 + 1)')

    def __set_infix(self, c): # 공백 제거
        self.__infix = c.replace(' ', '')

    def __convert(self): # 후위표기식으로 컨버팅
        def __get_weight(c): # 우선순위 추출
            weight = 0
            if c in ['*', '/']:
                weight = 3
            elif c in ['+', '-']:
                weight = 2
            elif c == '(':
                weight = 1
            return weight

        for c in self.__infix:
            if c == '(': # ( 는 무조건 push
                self.__stack.append(c)

            elif c == ')': # ) 는 ( 를 만날 때 까지 계속 pop
                e = self.__stack.pop()
                while e != '(':
                    self.__prefix += e
                    e = self.__stack.pop()

            elif c in ['+', '-', '*', '/']: # 가감승제 연산자를 만나면 스택 맨 위 연산자보다 우선순위가 높을 때까지 계속 스택에서 pop
                while len(self.__stack) > 0 and __get_weight(c) <= __get_weight(self.__stack[-1]):
                    self.__prefix += self.__stack.pop()
                self.__stack.append(c) # 만난 연산자가 스택 최상위 연산자보다 우선순위가 높아지면 push
            
            else: # 피연산자는 무조건 출력
                self.__prefix += c
        
        while len(self.__stack) > 0: # 최종으로 스택에 남은 연산자 모두 출력
            self.__prefix += self.__stack.pop()
    
    def __calcuate(self): # 계산
        def __calc(num1, num2, op): # 계산 함수
            answer = None
            if op == '+':
                answer = int(num1) + int(num2)
            elif op == '-':
                answer = int(num1) - int(num2)
            elif op == '*':
                answer = int(num1) * int(num2)
            elif op == '/':
                answer = int(num1) / int(num2)
            return answer

        for c in self.__prefix:
            # 연산자를 만나면 스택에 push해놓은 피연산자 두개를 pop해 만난 연산자로 계산
            if c in ['+', '-', '*', '/']:
                num1 = self.__stack.pop()
                num2 = self.__stack.pop()
                self.__stack.append(__calc(num2, num1, c)) # 계산 후 결과값을 다시 push
            else: # 연산자를 만날 때까지 스택에 push
                self.__stack.append(c)

        self.__answer = self.__stack.pop() # 마지막으로 남은 값이 정답
    
    def __print_status(self): # 결과 출력
        print('#'*30)
        print('INFIX  : ' + self.__infix)
        print('PREFIX : ' + self.__prefix)
        print('ANSWER : ' + str(self.__answer))

calcurator = PrefixCalcurator()
calcurator.test()
