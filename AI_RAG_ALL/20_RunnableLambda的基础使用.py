from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.runnables import RunnableLambda

str_parser = StrOutputParser()
my_func = RunnableLambda(lambda ai_msg: {"name":ai_msg.content})

model = ChatTongyi(model = "qwen3-max")

first_prompt = PromptTemplate.from_template(
    "我的邻居姓{lastname},刚生了{gender},帮我起名，只要名字，不需要其他额外的"
)

second_prompt = PromptTemplate.from_template(
    "名字是{name}，帮我解释其含义"
)

chain = first_prompt | model | my_func | second_prompt | model | str_parser

# resp = chain.invoke({"lastname":"张", "gender":"女儿"})

for chunk in chain.stream({"lastname":"张", "gender":"女儿"}):
    print(chunk , end="", flush=True)











