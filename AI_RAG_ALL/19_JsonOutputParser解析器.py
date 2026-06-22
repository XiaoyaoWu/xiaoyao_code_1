from langchain_core.output_parsers import JsonOutputParser,StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi

str_parser = StrOutputParser()
Json_parser = JsonOutputParser()

model = ChatTongyi(model = "qwen3-max")

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},帮我起名，并封装成Json格式返回给我"
    "要求key是name , 名字是你帮我起的，请严格遵守格式要求"
)

second_prompt = PromptTemplate.from_template(
    "名字是{name}，帮我解释其含义"
)

chain = first_prompt | model | Json_parser | second_prompt | model | str_parser

# resp = chain.invoke({"lastname":"张", "gender":"女儿"})

for chunk in chain.stream({"lastname":"张", "gender":"女儿"}):
    print(chunk , end="", flush=True)











