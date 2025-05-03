from functions import *

print("########################\n")
print ("Qual a data de vencimento?")
print("Formato: DIA-MES-ANO. Exemplo: 01-01-2000")
print("########################\n")

due_date = input("")

print(verify_due(due_date))