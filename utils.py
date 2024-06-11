from langchain.llms import HuggingFaceEndpoint
from langchain import PromptTemplate,  LLMChain

def get_sql(text , creativity,  api_key):

    llm = HuggingFaceEndpoint(repo_id = 'mistralai/Mistral-7B-Instruct-v0.2' , temperature = creativity , huggingfacehub_api_token = api_key)


    
    template = PromptTemplate(  
        input_variables = ["text"],
        template = """
Create a SQL query snippet using the below text:
```{text}```
Just SQL query:
"""                         
)

    llm_chain = LLMChain(llm  = llm , prompt = template)

    respone = llm_chain.invoke(text)
    return respone