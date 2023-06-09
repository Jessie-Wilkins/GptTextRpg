from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """Question: {question}

Answer: Let's think step by step and stop when I find the answer."""

prompt = PromptTemplate(template=template, input_variables=["question"])

local_path = 'model/ggml-gpt4all-j-v1.3-groovy.bin'  # replace with your desired local file path

# Callbacks support token-wise streaming
callbacks = [StreamingStdOutCallbackHandler()]
# If you want to use a custom model add the backend parameter
# Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
llm = GPT4All(model=local_path, backend='gptj', callbacks=callbacks, verbose=True)

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "You have a 1 liter pitcher and a 2 liter pitcher. How would you measure 1 liter of water?"

llm_chain.run(question)