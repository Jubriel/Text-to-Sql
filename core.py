from TableQA import text2sql

schema = input("Enter the name of the schema: ")
question = input('Enter the question for the database: ')

print(text2sql(schema, question))