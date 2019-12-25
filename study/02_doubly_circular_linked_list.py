ppt_turn = None # 발표할 사람
pay_turn = None # 돈 낼 사람
head = None # 가장 먼저 들어온 사람
now = 0 # 오늘 날짜

class Person:
    def __init__(self, name, prev=None, next=None):
        self.name = name
        self.prev = prev
        self.next = next

# 스터디 시작
def init(person):
    global ppt_turn
    global pay_turn
    global head

    person.next = person
    person.prev = person
    head = person
    ppt_turn = person
    pay_turn = person

# 가장 마지막 순서로 가입
def join(person):
    global head

    person.prev = head.prev
    person.next = head
    head.prev.next = person
    head.prev = person

# 가장 먼저 들어온 사람 탈퇴
def leave():
    global ppt_turn
    global pay_turn
    global head

    if ppt_turn == head:
        ppt_turn = head.next
    if pay_turn == head:
        pay_turn = head.prev

    head.prev.next = head.next
    head.next.prev = head.prev
    head = head.next

# 날짜 경과
def after(day):
    global now
    global ppt_turn
    global pay_turn

    while day > 0:
        day -= 1
        now += 1
        print('now : ' + str(now).rjust(2, '0') + ' ppt_turn: ' + ppt_turn.name.rjust(6, ' ') + ' pay_turn: ' + pay_turn.name.rjust(6, ' '))
        ppt_turn = ppt_turn.next
        pay_turn = pay_turn.prev
    
    print('=' * 20)

# yangjh 가입
yangjh = Person('YANGJH')
init(yangjh)
# yangjh <-> yangjh
print('yangjh 가입')
after(3)

# kimcw 가입
kimcw = Person('KIMCW')
join(kimcw)
# yangjh <-> kimcw <-> yangjh <-> kimcw
print('kimcw 가입')
after(5)

# ohyj 가입
ohyj = Person('OHYJ')
join(ohyj)
# yangjh <-> kimcw <-> ohyj <-> yangjh <-> kimcw <-> ohyj
print('ohyj 가입')
after(7)

# iu 가입
iu = Person('IU')
join(iu)
# yangjh <-> kimcw <-> ohyj <-> iu <-> yangjh <-> kimcw <-> ohyj <-> iu
print('iu 가입')
after(10)

# yangjh 탈퇴
# kimcw <-> ohyj <-> iu <-> kimcw <-> ohyj <-> iu
print('yangjh 탈퇴')
leave()
after(10)
