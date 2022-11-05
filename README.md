# attack-test
학년연계 웹보안 테스트 서버

**보안 상 취약점이 존재합니다! 교육용 목적으로 설계되었으며, 절대 일반 서버로 사용하지 마세요.**

## 설치
0. python 및 pip 설치
1. 우측 위 Code -> Download zip 눌러서 코드를 다운받으세요. 또는 git이 설치되어 있다면 아래의 명령어를 입력해도 됩니다.
```shell
git clone https://github.com/RoDeLa5/attack-test
```
2. 해당 폴더에 진입하세요
```shell
cd attack-test
```
3. 가상 환경을 구축해주세요.
```shell
python -m venv .venv
```
4. 필요 모듈을 설치해주세요.
```shell
pip install -r requirements.txt
```
5. DB 테이블을 생성해주세요.
```shell
python polls/db_controller.py
create
```
6. 계정을 등록해주세요. (아이디/비밀번호 칸에 정보 입력)
```shell
python polls/db_controller.py
register
아이디
비밀번호
```
7. 서버를 실행해주세요.
```shell
python manage.py runserver
```
이제 `127.0.0.1:8000`으로 접속하여 테스트할 수 있습니다.

## SQL Injection
데이터베이스에 전송하는 명령문을 입력값을 통해 위조하는 방법입니다.

예를 들어 다음의 명령어가 있다고 합시다. (아이디, 비밀번호에 해당하는 유저를 찾는 명령어)
```sqlite-sql
select * from TESTTABLE where id='아이디' and pw='비밀번호'
```
여기에 아이디로 `asdf`, 비밀번호로 `'or 1=1 --`를 입력하면
```sqlite-sql
select * from TESTTABLE where id='asdf' and pw='' or 1=1 --'
```
가 됩니다. `OR 1=1`로 인해 비밀번호가 틀렸는데도 불구하고 유저의 정보가 성공적으로 반환되고, `--`(SQL 구문에서 주석)로 뒤쪽 명령어를 주석 처리하여 오류가 나지 않게 됩니다.

이렇게 비밀번호를 몰라도 로그인이 가능한 취약점입니다.
