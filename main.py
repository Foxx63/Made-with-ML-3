import os
import openai
import sys

sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


openai.api_key  = os.environ['OPENAI_API_KEY']



from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("text.pdf")
pages = loader.load()
page = pages[0]
print(page.page_content)

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter

text_splitter_1 = CharacterTextSplitter( separator= "", chunk_size = 150, chunk_overlap = 10 , length_function = len )

docs = text_splitter_1.split_documents(pages)


print(len(docs))
print(len(pages))


from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings

sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"



