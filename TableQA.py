# -*- coding: utf-8 -*-

import nltk
nltk.download('omw-1.4')

def text2sql(schema, question):
  # importing libraries
  from tableqa.agent import Agent
  import pandas as pd
  import psycopg2
  import pandas.io.sql as psql
  import warnings
  warnings.filterwarnings("ignore")

  conn = psycopg2.connect(
      host="13.77.150.203",
      port = "5432",
      database="analytics",
      user="vecap_user",
      password="vecap2021@")
  df = psql.read_sql_query("select * from development.student", conn)

  agent = Agent(df)
  response = agent.query_db("show me the names is a religion of islam and female")

  # initiating vecap database connection
  conn = psycopg2.connect(
    host="13.77.150.203",
    port = "5432",
    database="auth_mgt",
    user="vecap_user",
    password="vecap2021@")
  
  # Loading the Schema as table
  df = psql.read_sql_query(f"select * from {schema}.person", conn)

  # loading schema file 
  import json
  file=open('db_schema_file.json')
  schema_file=json.load(file)
 
  # question preprocessing 
  def prep(text):
    from nltk import word_tokenize
    from nltk.corpus import stopwords
    # word tokenization
    stop_words = set(stopwords.words('english'))
    token = word_tokenize(text)
    # Removing stopwords
    def remove_stopwords(token):
      filtered =[]
      for word in token:
        if word not in stop_words:
          filtered.append(word)
      return filtered
    return ' '.join(remove_stopwords(token)).lower()
  
  # Using the TableQA tool
  agent = Agent(df.astype(str)) #, schema_file)
  # response1 = agent.query_db(prep(f"{question}"))
  m = prep(f"{question}")
  response = agent.get_query(m)
  return response #, response1




