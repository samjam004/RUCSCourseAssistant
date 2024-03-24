from flask import Flask, request, render_template
import os 
import sys

import constants 
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_function', methods=['POST'])
def run_function():
    # Get data from HTML form
    job_title = request.form['job_title']

    os.environ["OPENAI_API_KEY"] = constants.APIKEY

    query = f"give me 5 courses that would be useful to become a {job_title}" 
    + "but be sure to not include any quotation marks or professors in your answer" 
    + "but make sure to include the course name and id and number them appropriately"


    loader = TextLoader('data.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    result = index.query(query)
    res1, res2, res3, res4, res5 = process_res(result) 
    return res1, res2, res3 ,res4, res5

def process_res(string):
    result = string
    arr = ["", "", "","",""]
    count = 0
    for index, char in enumerate(result):
        if char == '.' and index != 1:
            count += 1
        arr[count] += (char)
    
    return arr
if __name__ == '__main__':
    app.run(debug=True)
