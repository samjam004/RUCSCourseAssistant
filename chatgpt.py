import os 
import sys

import constants 
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.APIKEY

query = "give me 5 courses that would be useful to become a cybersecurity specialist" 
+ "but be sure to not include any quotation marks or professors in your answer" 
+ "but make sure to include the course name and id and number them appropriately"


loader = TextLoader('data.txt')
index = VectorstoreIndexCreator().from_loaders([loader])
print(index.query(query))