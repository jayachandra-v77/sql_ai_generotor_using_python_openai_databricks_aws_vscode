from flask import Flask, request, render_template
from sql_generator import generate_sql
from databricks_connection import run_query

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form["question"]

    sql_query = generate_sql(question)

    result = run_query(sql_query)

    return render_template(
        "index.html",
        question=question,
        sql_query=sql_query,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)