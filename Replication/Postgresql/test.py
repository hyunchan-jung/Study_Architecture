import time

import psycopg2


def get_connection(node_name: str):
    nodes = {
        'node-01': '192.168.57.101',
        'node-02': '192.168.57.102',
        'node-03': '192.168.57.103',
    }
    connection = psycopg2.connect(
        host=nodes[node_name],
        port='5432',
        database='postgres',
        user='postgres',
        password='postgres',
    )
    return connection


def create_table():
    conn = get_connection('node-01')
    cur = conn.cursor()

    sql = '''
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    '''
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()


def create_dummy_data():
    conn = get_connection('node-01')
    cur = conn.cursor()

    sql = '''
        INSERT INTO users (name)
        VALUES ('user-01'), ('user-02'), ('user-03')
    '''
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()


def get_data_from_postgres():
    for node in ['node-01', 'node-02', 'node-03']:
        conn = get_connection(node)
        cur = conn.cursor()

        sql = '''
            SELECT * FROM users
        '''
        cur.execute(sql)
        rows = cur.fetchall()

        cur.close()
        conn.close()

        print(node, rows)


def get_data_from_pgpool():
    conn = psycopg2.connect(
        host='192.168.57.101',
        port='15432',
        database='postgres',
        user='postgres',
        password='postgres',
    )
    cur = conn.cursor()

    sql = '''
        SELECT * FROM users
    '''
    cur.execute(sql)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    print(rows)


if __name__ == '__main__':
    create_table()
    create_dummy_data()

    time.sleep(5)
    get_data_from_postgres()
    get_data_from_pgpool()
