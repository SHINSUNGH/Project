import empfunc as em
import sys,os

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
   ■ 직원관리         Q.메뉴판 종료  
╠════╦═══════════════════════════════╣
   1 ║  직원 정보 입력              
   2 ║  직원 정보(수정, 조회, 삭제)     
   3 ║  근무시간 입력 및 리스트 조회               
   4 ║  급여 명세서 조회           
   5 ║  급여 지급 기준               
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
 1. 직원 정보 수정       
 2. 직원 정보 조회       
 3. 직원 정보 삭제       
 Q. 이전 메뉴로 돌아가기 
 ========================
'''
            print('조회하실 메뉴를 선택하세요:')
            menu4=input(menu2_display)
            if menu4=='1':
                os.system('cls') 
                em.update_emp()
            elif menu4=='2':
                os.system('cls')
                em.part_emp()
            elif menu4=='3':
                os.system('cls')
                em.delete_emp()
            elif menu4== 'Q':
                break  
            else:
                print('잘못된 입력입니다. 다시 입력해주세요.')
    elif menu=='3':
        while True:
            menu3_display ='''
 ========================
 1. 근무시간 입력        
 2. 근무시간 리스트 조회
 Q. 이전 메뉴로 돌아가기
 ========================
'''
            print('조회하실 메뉴를 선택하세요:')
            menu5=input(menu3_display)
            if menu5=='1':
                os.system('cls') 
                em.insert_jobtime()
            elif menu5=='2':
                os.system('cls')
                em.all_jobtime()
            elif menu5 == 'Q':
                break  
            else:
                print('잘못된 입력입니다. 다시 입력해주세요.')
    elif menu=='4':
        os.system('cls')
        em.cal()

    elif menu=='5':
        os.system('cls')
        print(
'''
현재 서빙,캐셔는 최저시급, 주방은 최저시급의 1.2배를 지급하고 있습니다.
그리고 야간근무는 주간근무의 1.5배의 시급을 지급합니다.
주휴수당은 일한시간이 15시간 이상이면 총일한시간/5 * 급여를 곱하여 계산해준다.
''')    

    elif menu=='Q':
        os.system('cls')
        print('프로그램 종료!')
        sys.exit()