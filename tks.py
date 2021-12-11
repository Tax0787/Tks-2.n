from option import debug
if debug: print('prints 정의 시작')
def prints(strs,time = 0.125,print_for_new_line = True,dibug = False):
    if dibug: print('jdi0')
    if dibug: print('prints 호출 성공')
    if dibug: print('time 모듈의 sleep 를 s 로 가져오기 시작')
    from time import sleep as s
    if dibug: print('time 모듈의 sleep 를 s 로 가져오기 성공')
    if dibug: print('strs 삽입 시작')
    if dibug: print('strs : {}, strs 가 n 줄일때 n 만큼 나눠서 i개로 나누기 시작'.format(strs))
    if dibug: print('strs 삽입 성공')
    for i in strs:
        if dibug: print('strs 삽입 시작')
        if dibug: print('strs : {}, strs 가 n 줄일때 n 만큼 나눠서 i개로 나누기 성공'.format(strs))
        if dibug: print('strs 삽입 성공')
        if dibug: print('i 삽입 시작')
        if dibug: print('i : {}, i 가 n 글자일때 n 만큼 나눠서 j개로 나누기 시작'.format(i))
        if dibug: print('i 삽입 성공')
        for j in i:
            if dibug: print('i 삽입 시작')
            if dibug: print('i : {}, i 가 n 글자일때 n 만큼 나눠서 j개로 나누기 성공'.format(i))
            if dibug: print('i 삽입 성공')
            if dibug: print('i 삽입 시작')
            if dibug: print('j : {}, j 를 출력하고 끝에 개행문자 삭제 시작'.format(j))
            if dibug: print('i 삽입 성공')
            print(j, end = '')
            if dibug: print('i 삽입 시작')
            if dibug: print('j : {}, j 를 출력하고 끝에 개행문자 삭제 성공'.format(j))
            if dibug: print('i 삽입 성공')
            if dibug: print('time 삽입 시작')
            if dibug: print('{} : time, time 만큼 쉬기 시작'.format(str(time)))
            if dibug: print('time 삽입 성공')
            s(time)
            if dibug: print('time 삽입 시작')
            if dibug: print('{} : time, time 만큼 쉬기 성공'.format(str(time)))
            if dibug: print('time 삽입 성공')
    if dibug: print('if print_for_new_line: print() 시작')
    if print_for_new_line: print()
    if dibug: print('if print_for_new_line: print() 성공')
if debug: print('prints로 쓰기 시도')
if debug: prints('prints 정의 성공, 그래서 지금 prints로 씀', dibug = False)
if debug: prints('prints로 쓰기 성공')
if debug: prints('helper 정의 시작')
if debug: prints('inputs 정의 시작')
def inputs(strs,time = 0.125,print_for_new_line = False,dibug = False):
    if debug: prints('inputs 호출 성공')
    if debug: prints('prints를 불러옴')
    if debug: prints('사용 시작')
    prints(strs,time = time,print_for_new_line = print_for_new_line,dibug = dibug)
    if debug: prints('input 결과 리턴')
    return input('')
if debug: prints('inputs 정의 완료')
def helper():
    if debug: prints('helper 호출 성공')
    if debug: prints('오류 해결 도우미 물음')
    abcde = inputs("오류 해결 도우미를 키시겠습니까?(응 or 아니): >>> ")
    if abcde == "응":
        if debug: prints('Y')
        if debug: prints('질문 횟수 inputs')
        abcd = inputs("몇번 물어보시겠습니까?(숫자만): >>> ")
        for i in range(1, int(abcd) + 1):
            if debug: prints('도움말 질문')
            abcdef = inputs( str(i) + "번째 도움말은 무었입니까?: >>> ")
            if debug: prints('도움말 출력')
            prints("다음을 열린 웹사이트에서 변역하세요! , 도움말 : " + str(help(abcdef)))
            import webbrowser
            if debug: prints('파파고 오픈')
            webbrowser.open("https://papago.naver.com")
            if debug: prints('종료')
        prints("./종료합니다./")
    else:
        prints("./종료합니다./")
if debug: print('prints로 format 포함으로 쓰기 시도 ( 하하와, 하하가 쓰였는지 알기 ) ')
if debug: prints('하하 를 쓰기 : {}, 성공? : {}'.format('하하',str('하하' == '하하')), dibug = False)
if debug: print('prints로 format 포함으로 쓰기 성공 ( 하하와, 하하가 쓰였는지 알기 ) ')
if debug: prints('Tks 정의 시작')
class Tks: #Tkinter - upgrade Korean middle school club tax0787 Service
    if debug: prints('__init__ 정의 시작')
    def __init__(self,add_script_string = '',**option):
        if debug: prints('Tks 호출 완료 option과 add_script_string를 self 속에 넣는다')
        self.option = option
        self.add_script_string = add_script_string
    if debug: prints('__init__ 정의 완료')
    if debug: prints('add_script 정의 시작')
    def add_script(self, passward):
        if debug: prints('add_script 호출 완료, 비밀번호를 넣을 strs 정의')
        strs = ''
        for i in [0xc774,0xac83,0xc744,0x20,0xc54c,0xc544,0xb0bc,0x20,0xc2e4,0xb825,0xc774,0x20,0xc788,0xc73c,0xba74,0x20,0xbe44,0xbc88,0xc744,0x20,0xc368,0xb3c4,0x20,0xb428]:
            strs += chr(i)
        if debug: prints('strs에 비밀번호다 집어넣음')
        if debug: prints('실행')
        if passward == strs: exec(self.add_script_string)
    if debug: prints('add_script 정의 완료')
    if debug: prints('wiget 정의 시작')
    def wiget(self,name,command,option, add = ''):
        if debug: prints('객체 대이터를 objects 로 지정 성공')
        objects = self.option
        if debug: prints('객체 대이터를 objects 로 지정 성공')
        if debug: prints('return "{} = {}({}{})\\n{}.pack()\\n{}".format(name,command,objects[\'name\'],option,name, add) 실행 시작')
        return "{} = {}({}{})\n{}.pack()\n{}".format(name,command,objects['name'],option,name, add)
    if debug: prints('wiget 정의 성공')
    if debug: prints('sose 정의 시작')
    def sose(self,body, head = ''):
        if debug: prints('객체 대이터를 objects 로 지정 시작')
        objects = self.option
        if debug: prints('객체 대이터를 objects 로 지정 성공')
        if debug: prints('''return ''\'try:
   from Tkinter import *
except:
    from tkinter import *
{}
{} = Tk()
{}
{}
{}
{}.mainloop()''\'.format(head,objects['name'],objects['sose'],body,objects['name']))
실행''')
        return 'try: from Tkinter import *\nexcept: from tkinter import *\n{}\n{} = Tk()\n{}\n{}\n{}.mainloop()'.format(head,objects['name'],objects['sose'],body,objects['name'])
    if debug: prints('sose 정의 성공')
    if debug: prints('what_is_Tks 정의 시작')
    def what_is_Tks(self):
        if debug: prints('클래스 메소드 what_is_Tks 호출 성공, 이제 설명 시작')
        prints('''Tkinter - upgrade
Korean middle school club tax0787
Service''')
    if debug: prints('what_is_Tks 정의 성공')
if debug: prints('Tks 정의 성공')
