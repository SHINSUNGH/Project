import empfunc as em
import sys,os


# worker=[{'name': '김화영', 'gender': 'F', 'tel': '010-4909-5658', 'age': '27','work':'cashier'},
#            {'name': '신성혁', 'gender': 'M', 'tel': '010-1234-5678', 'age': '25','work':'kitchen'},
#            {'name': '김상철', 'gender': 'M', 'tel': '010-1234-5678', 'age': '28','work':'serving'},
#            {'name': '유승완', 'gender': 'M', 'tel': '010-1234-5678', 'age': '30','work':'kitchen'}]

# 직원번호,이름,성별,번호,나이,직무,주간or야간 테이블
# em.create_table()
# 이름,시간,날짜테이블
# em.create_table2()
# 직무,시급 테이블
# em.create_table3()

while True:
    menu=input(
'''
╔════════════════════════════════════╗
   ■ 메뉴판            Q.메뉴판 종료 
╠════╦═══════════════════════════════╣
   1 ║  직원 정보 입력              
   2 ║  직원 정보( 수정, 조회, 삭제)     
   3 ║  근무시간 입력             
   4 ║  근무시간 리스트 조회        
   5 ║  급여계산 및 주휴수당 조회        
   6 ║  급여 명세서 조회           
   7 ║  급여 지급 기준            
   8 ║  급여 정보 입력                     
╚════╩═══════════════════════════════╝
'''
)
    if menu=='1':
        os.system('cls')
        em.insert_emp()
    elif menu=='2':
        while True:
            menu2_display ='''
 ========================
 1. 직원 정보 수정       |
 2. 직원 정보 조회       |
 3. 직원 정보 삭제       |
 ========================
'''
            print('조회하실 메뉴를 선택하세요:')
            menu2_display=input(menu2_display)
            if menu=='1':
                os.system('cls') 
                em.insert_wage()
            elif menu=='2':
                os.system('cls')
                em.update_emp()
            elif menu=='3':
                os.system('cls')
                em.delete_emp()
    elif menu=='3':
        os.system('cls')
        em.insert_jobtime()

    elif menu=='4':
        os.system('cls')
        em.all_jobtime()
        
    elif menu=='5':
        os.system('cls')
        em.name_emp()
        em.cal()

    elif menu=='6':
        os.system('cls')
        em.print_receipt()

    elif menu=='7':
        os.system('cls')
        print(
'''
현재 서빙,캐셔는 최저시급, 주방은 최저시급의 1.2배를 지급하고 있습니다.
그리고 야간근무는 주간근무의 1.5배의 시급을 지급합니다.
주휴수당은 주 15시간 이상 근무 시 급여의 1.2배를 지급합니다.
''')    

    elif menu=='8':
        os.system('cls')
        em.insert_wage()

    elif menu=='Q':
        os.system('cls')
        print('프로그램 종료!')
        sys.exit()