import psycopg2

db_config = {
    'dbname': 'bytegenie',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432'
}

def execute_sql_query(sql_query):
    if("unrelated" in sql_query.lower()):
        data = {
            "columns": [],
            "rows": [],
            "message": "Unrelated Question. Please ask something related to events/companies or people attending them!"
        }
        return data
    
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute(sql_query)
    columns = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return { "columns": columns, "rows": rows, "message": "" }
