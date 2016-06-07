# -*- coding: utf8 -*-
# 상위 클래스 이름이 너무 길어져서 from import as 적용
from CashCardClass import SimpleCashCard as CashCard


# ex09CashCardClass 모듈의 simpleCashCard 클래스를
# 상속 받아 safeCashCard 클래스를 정의한다.
# simpleCashCard 는 safeCashCard 의 상위 클래스
# safeCashCard 는 simpleCashCard 의 하위 클래스
class SafeCashCard(CashCard)
    # SimpleCashCard의 다른 기능은 그대로 사용하고
    #      {__init__(), deposit(), check_balance()}
    #   withdraw() 메소드만 다시 정의한다
    def withdraw(self, amount_won):
        """
        SafeCashCard withdraw method
        Check balance before withdraw
        """
        print("SafeCashCard withdraw()") # 함수 호출 표식
        # 잔고가 충분하면
        if self.check_balance() >= amount_won:
            # 출금한다
            # 상위 클래스의 withdraw 메소드 호출
            # http://stackoverflow.com/questions/805066/
            CashCard.withdraw(self, amount_won)
        # 그렇지 않으면
        else:
            # 오류를 표시한다
            print("** 오류 발생 **")
            print("잔고가 부족합니다")
            print("인출되지 않았습니다")
#SafeCashCard 클래스 정의 끝


# 아래의 내용은 이 파일이 import 될 때는 실행되지 않음
if "__main__" == __name__:
    # Cash Card Usef 모듈의 msg-int 함수를 사용할 수 있게 함
    from CashCard_user import chk_bal

    # myCard 객체를 생선하다
    # SimpleCashCard 클래스에 정한 대로 만든다
    # SimpleCashCard __init__() 메소드가 호출된다
    myCard = CashCard()
    # mySafeCard 객체를 생성한다
    # safeCashCard 정한 대로 만든다
    # safeCahCard __init__() 메소드를 호출하려고 했지만
    # safeCahCard 클래스 안에는 정의되지 않았기 때문에
    # 상위클래스인 simpleCashCard __init__() 메소드가 호출된다
    mySafeCard = SafeCashCard()

    # 여러장의 카드를 생성할 수 있는지 확인하기 위해 객체를 하나 더 생성한다
    mySistersSafeCard = SafeCashCard()

    # 카드에 각각 만원씩 입금
    # SimpleCashCard 클래스이 deposit() 메소드가 호출된다
    myCard.deposit(10000)
    # safeCashCard deposit() 메소드를 호출하려고 하지만
    # safeCashCard 클래스 안에는 정의되지 않았기 때문에
    # 상위클래스인 SimpleCashCard의 deposit() 메소드가 호출된다.
    mySafeCard.deposit(10000)
    mySistersSafeCard.deposit(200000)

    chk_bal("myCard 입금 후 잔고 확인", myCard)
    chk_bal("mySafeCard 입금 후 잔고 확인", mySafeCard)
    chk_bal("mySistersSafeCard 입금 후 잔고 확인", mySistersSafeCard)
    # safeCashCard check_balacne() 메소드를 호출하려고 하지만
    # safeCashCard 클래스 안에는 정의되지 않았기 때문에
    # 상위클래스인 simpleCashCard 의 check_balance() 메소드가 호출된다

    # 십만원 출금
    # simpleCashCard 클래스의 withdraw() 메소드가 호출된다
    myCard.withdraw(100000)
    # safeCashCard 클래스의 withdraw() 메소드가 호출된다다
    mySafeCard.withdraw(100000)
    mySistersSafeCard.withdraw(100000)

    chk_bal("myCard 출금 후 잔고 확인", myCard)
    chk_bal("mySafeCard 출금 후 잔고 확인", mySafeCard)
    chk_bal("mySistersSafeCard 출금 후 잔고 확인", mySistersSafeCard)
    # safeCashCard check_balance() 메소드를 호출하려고 하지만
    # safeCashCard 클래스 안에는 정의되지 않았기 때문에
    # 상위 클래스인 simpleCashCard 의 check_balance() 메소드가 호출된다