import sqlite3,os

path = os.path.dirname(__file__)

# 직원테이블
def create_table():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    cur.execute('''
    create table employee(
    empid integer primary key autoincrement,
    name text,
    gender text,
    tel text,
    age integer)
    ''')
    conn.commit()
    conn.close()

# 이름,시간,주간야간테이블
def create_table2():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    cur.execute('''
    create table jobtime(
    jobtimeid integer primary key,
    name text,
    time integer,
    shift text,
    work text,
    empid integer,
    date timestamp default current_timestamp,
    foreign key (empid) references employee(empid) on delete cascade  
    )
    ''') # on delete cascade 를 넣어 employee테이블데이터가삭제되면 같은empid를가진 jobtime데이터도삭제된다.
    conn.commit()
    conn.close()

# 직무,시급테이블
def create_table3():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    cur.execute('''
    create table wage(
    wageid integer primary key,
    work text,
    shift text,
    wage integer)
    ''')
    conn.commit()
    conn.close()

# 직원등록
def insert_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'insert into employee(name,gender,tel,age) values(?,?,?,?)'
    name = input('이름 ')
    gender = input('성별 ')
    tel = input('전화번호 ')
    age = input('나이 ')
    cur.execute(sql,(name,gender,tel,age))
    conn.commit()
    conn.close()

# 알바시간입력
def insert_jobtime():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    name_emp()
    sql = 'insert into jobtime(name,time,shift,work) values(?,?,?,?)'
    name = input('이름 ')
    time = input('시간 ')
    shift = input('day or night ')
    work = input('kitchen or counter or serving ')
    cur.execute(sql,(name,time,shift,work))
    conn.commit()
    conn.close()

# 직무, 주간/야간, 시급입력
def insert_wage():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'insert into wage(work,shift,wage) values(?,?,?)'
    work = input('kitchen or counter or serving ')
    shift = input('day or night ')
    wage = input('시급 ')
    cur.execute(sql,(work,shift,wage))
    conn.commit()
    conn.close()

# 직원정보
def all_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'select * from employee'
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.close()

# 직원이름테이블
def name_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'select name from employee'
    cur.execute(sql)
    result = cur.fetchall()
    print(result)
    conn.close()

# 직원정보조회
def part_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'select * from employee where name = ?'
    name = input('검색할 직원이름 ')
    cur.execute(sql, (name,))
    result = cur.fetchone()
    if result:
        print(result)
    else:
        print("해당하는 직원이 존재하지 않습니다.")
    conn.close()

# 입력한근무시간을 리스트로 출력
def all_jobtime():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    sql = 'select * from jobtime'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()

# 직원정보수정
def update_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    all_emp()
    name = input('수정할 직원 ')
    check = 1
    while check:
        col = input('수정할 정보(gender,tel,age)')
        if col in ('gender','tel','age'):
            check = 0
    value = input(f'{col}수정할 내용 입력 ')
    sql = f'update employee set {col} = ? where name = ?'
    cur.execute(sql,(value,name))
    conn.commit()
    conn.close()

# 직원정보삭제 employee데이터를 삭제하면 같은empid를가진 jobtime데이터도 삭제된다.
def delete_emp():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    name_emp()
    name = input('삭제할 직원 ')
    sql = 'delete from employee where name = ?'
    cur.execute(sql,[name])
    conn.commit()
    conn.close()

# 이름검색해서 총근무시간출력
def sum_time():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    name_emp()
    sql = 'select sum(time) from jobtime where name = ?'
    name = input('검색할 직원이름 ')
    cur.execute(sql, (name,))
    result = cur.fetchone()
    if result:
        print('총 근무시간 ',result)
    else:
        print("해당하는 직원이 존재하지 않습니다.")
    conn.close()

# 주휴수당계산 innerjoi where group by를 사용해서 테이블3개의 데이터를 한테이블에 출력
def cal():
    conn = sqlite3.connect(path + '/empinfo.db')
    cur = conn.cursor()
    name = input('이름입력')
    cur.execute(f"select count(*) from employee where name = '{name}'")
    count = cur.fetchone()[0]
    if count == 0:
        print(f"입력한 이름 '{name}'에 해당하는 데이터가 없습니다.")
        return
    
    sql = f'''select employee.name,
                case when sum(jobtime.time) 
                then (sum(jobtime.time)*wage.wage) end as total_pay,
                case when sum(jobtime.time) >= 15 
                then (sum(jobtime.time)/5.0*wage.wage) end as holiday_pay
                from employee
                inner join jobtime on employee.empid = jobtime.empid
                inner join wage on jobtime.shift = wage.shift and jobtime.work = wage.work
                where employee.name = '{name}'
                group by employee.name;
        '''
    cur.execute(sql)
    result = cur.fetchone()
    if result[1] is None:
        print_receipt(name,result[2],result[1])
    else:
        print_receipt(name,result[1],result[2])
    conn.close()
# select case then 을 사용하여 급여를 total_pay컬럼에 일한시간*급여를 계산해 넣어주고, 
# 일한시간이 15시간 이상이면 주휴수당을 주는데 총일한시간/5 * 급여를 곱하여 계산해준다.

# 급여명세서 
from datetime import datetime
def print_receipt(name, total_pay, holiday_pay):
    print("===========================================")
    print("                급여명세서")
    print("===========================================")
    print(f"직원명: {name}")
    print(f"급여일자: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("===========================================")
    print("항목              금액")
    print("-------------------------------------------")
    print(f"총 급여           {total_pay}원")
    if holiday_pay is None:
        holiday_pay = 0
        print(f"주휴수당          {int(holiday_pay)}원")
    elif holiday_pay is not None:
        print(f"주휴수당          {int(holiday_pay)}원")
    print("-------------------------------------------")
    total = (total_pay) + int(holiday_pay)
    print(f"총 합계           {total}원")
    print("===========================================")
'''
현재 서빙,캐셔는 최저시급, 주방은 최저시급의 1.2배를 지급하고 있습니다.
그리고 야간근무는 주간근무의 1.5배의 시급을 지급합니다.
주휴수당은 주 15시간 이상 근무 시 근무시간/5*시급을 지급합니다.
'''
