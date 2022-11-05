import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('../test.db')
    cur = conn.cursor()


def create():
    global cur
    cur = cur.execute('CREATE TABLE TESTTABLE(id text,pw text)')


def register():
    global cur
    id = input('ID: ')
    pw = input('PW: ')
    cur = cur.execute(f"INSERT INTO TESTTABLE(id, pw) VALUES ('{id}', '{pw}');")
    conn.commit()


def exist(id: str, pw: str) -> bool:
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur = cur.execute(f"SELECT * FROM TESTTABLE WHERE id='{id}' AND pw='{pw}'")
    rows = cur.fetchall()
    print(rows)
    return bool(len(rows))


if __name__ == '__main__':
    input_value = input('what to do: ')
    if input_value == 'create':
        create()
    elif input_value == 'register':
        register()
    else:
        print('nothing to do')
