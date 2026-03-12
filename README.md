# SQL AI Generator

This project generates **SQL queries from natural language using Python and OpenAI**. It helps users convert plain English questions into SQL queries automatically.

## Technologies Used

* Python
* OpenAI API
* Databricks
* AWS
* VS Code

## Features

* Convert natural language into SQL queries
* Uses OpenAI LLM for query generation
* Can run queries in Databricks environment
* Simple Python-based implementation

## Setup

1. Clone the repository
   git clone https://github.com/your-username/sql_ai_generator.git

2. Install dependencies
   pip install -r requirements.txt

3. Add your OpenAI API Key as an environment variable.

## Run the Project

python main.py

## Example

Input:
Show total sales by region

Output SQL:
SELECT region, SUM(sales)
FROM sales
GROUP BY region;

## Author

Jay
