
# input()과 sys.stdin.readline()의 차이

테스트할 때는 input()을 쓰고 제출할 때에만 sys.stdin.readline()을 쓰는 코드가 종종 보임.
알아보니 Jupyter를 쓰시는 분들이 주로 그렇게 사용. <br>

Jupyter에는 sys.stdin.readline이 구현되어 있지 않아서 어쩔 수 없이 제출할 때와 코드를 달리해야 하는데, 그렇다면 둘의 차이를 확실하게 알고 사용 필요.
<br>
<br>

--- 

### 내부적으로도 뭔가 차이가 있겠지만, 일단 겉으로 드러나는 매우 중요한 차이점은 바로
* sys.stdin.readline()은 매 줄의 끝에 있는 개행 문자를 포함하여 반환해준다는 것
    * 예를 들어, 입력으로 abc를 치고 엔터를 쳤다면 이를 s = input()으로 받으면 s에 "abc"가 저장되겠지만, s = sys.stdin.readline()으로 받으면 "abc\n"이 저장됨.

        * 이를 구분하지 않고 그대로 input = sys.stdin.readline으로 놓고 사용하면 여러 문제가 생기게됨.
        * 위의 "abc\n"의 경우 len(s)를 하면 3이 아닌 4가 되고, for x in s: 를 하면 x는 'a', 'b', 'c', '\n' 이렇게 네 개의 문자에 대해 돌게 됨.

        * 따라서, 제출할 때에만 input을 sys.stdin.readline으로 대체할 거라면 그냥 =으로 바로 대입하기보다는 다음과 같이 하여 끝의 개행 문자를 버리고 사용하는 것이 좋다.

<br>

---
```Python
input = lambda: sys.stdin.readline().rstrip()
```

### * Point

또 한 가지 중요한 차이점은 input은 입력의 끝 (EOF)을 만났을 때 EOFError를 raise하지만 sys.stdin.readline은 에러를 발생시키지 않고 정상적으로 빈 문자열을 반환한다는 것입니다. 따라서 로컬에서 input으로 EOF를 처리한 코드를 그대로 sys.stdin.readline으로 바꾸면 제대로 처리되지 않을 가능성이 높습니다. 요즘에는 EOF를 직접 판단해야 하는 문제가 많이 없지만 옛날 문제들 중에는 이 때문에 고생하게 되는 경우가 종종 있으니 주의


    * EOF? 
        * EOF는 파일의 끝을 의미합니다. 프로그래밍에서 파일이나 표준 입력(콘솔 입력)을 읽다가 더 이상 읽을 데이터가 없을 때 이를 EOF라고 합니다.
        
    * EOFError
        * EOFError는 Python에서 input() 함수가 더 이상 읽을 데이터가 없을 때 발생하는 예외입니다. 즉, EOF에 도달했을 때 발생합니다.


<br>
### 실제 적용

> * input() 함수와 EOF 처리
input() 함수는 사용자 입력을 기다리며, 사용자가 텍스트를 입력하고 엔터 키를 누를 때까지 대기합니다. 만약 입력의 끝(EOF)을 만나면 input() 함수는 EOFError 예외를 발생시킵니다.

```Python
try:
    user_input = input("Enter something: ")
except EOFError:
    print("EOFError: No more input!")

```
* 위 코드에서 EOF를 만나면 EOFError가 발생하고, 예외 처리 부분에서 이를 잡아냄



> * sys.stdin.readline() 함수와 EOF 처리
sys.stdin.readline() 함수는 표준 입력으로부터 한 줄을 읽습니다. EOF에 도달하면 빈 문자열을 반환합니다. 이 함수는 EOFError를 발생시키지 않습니다.

```Python
import sys

while True:
    line = sys.stdin.readline()
    if line == '':
        break
    print(f"Received input: {line.strip()}")

```
* 위 코드에서 EOF를 만나면 빈 문자열을 반환하고, 이는 while 루프를 종료시키는 조건이 된다.




### * Point 차이점 총 요약
    * input() 함수는 EOF를 만나면 EOFError를 발생시킵니다.
    * sys.stdin.readline() 함수는 EOF를 만나면 빈 문자열을 반환합니다.
    * input() 함수를 사용하는 코드에서 EOF를 처리하는 경우, sys.stdin.readline()으로 변경하면 빈 문자열을 반환하는 상황을 고려해야함.
        * input()은 EOF 시 EOFError를 발생시키고, sys.stdin.readline()은 EOF 시 빈 문자열을 반환합니다. 코드를 변환할 때는 이 차이점을 염두에 두고 처리해야 합니다. EOF를 직접 처리해야 하는 경우가 드물긴 하지만, 옛날 문제나 특정 상황에서는 이를 고려해야 한다.