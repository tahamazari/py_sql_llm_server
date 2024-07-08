from flask import Flask, request, jsonify
from flask_cors import CORS
from db import execute_sql_query
from llm import convert_to_sql

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    natural_language_query = data.get('query')

    # Generate the SQL query using LLM
    sql_query = convert_to_sql(natural_language_query)

    # Execute the SQL query
    results = execute_sql_query(sql_query)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
