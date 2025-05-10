from openai import OpenAI

with open("api_key.txt", "r") as file:
    secret_key = eval(file.read().strip())

 
client = OpenAI(api_key=secret_key['secret'])

response = client.chat.completions.create(
    model="gpt-4",  # ou "gpt-4-turbo", "gpt-3.5-turbo"
    messages=[
        {"role": "data engineer", 
         "content": "quais são as melhores práticas para criar um banco de dados em nuvem?"}
    ]
)
 
print("Resposta do modelo:\n")

print(response)
#print(response.choices[0].message.content)

                      