from fastapi import FastAPI, Request, Path, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form
import os

from responsebuilder.buildresponse import BuildResponse, ConfigReader

templates = Jinja2Templates(directory="templates")


# initialize 'fastAPI'
app = FastAPI()

config_data = ConfigReader().get_yaml_data()
br = BuildResponse(config_data=config_data)

os.environ["OPENAI_API_KEY"] = "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"


# create endpoints / route
@app.get('/')
def home():
    html_content = """
        <html>
           <body>
              <form action="/qasubmit" method="POST">
                 <h3>Enter your Query : </h3>
                 <p>
                    <textarea id="query" name="query" rows="10" cols="50">Write your query ! </textarea>
                </p>
                 
                 <p><input type='submit' value='Submit Query'/></p>
              </form>
           </body>
        </html>
    """

    return HTMLResponse(content=html_content, status_code=200)


@app.post("/qasubmit")
async def qasubmit(query: str = Form(...)):

    answer = br.get_response(question=query)

    html_content = f"""
                <html>
                   <body>
                      <form action="/qasubmit" method="POST">
                         <h3>Enter your Query : </h3>
                         <p>
                            <textarea id="query" name="query" rows="10" cols="50">Write your query ! </textarea>
                        </p>

                         <p><input type='submit' value='Submit Query'/></p>
                      </form>
                      <p>
                      Question Asked : {query}
                      </p>
                      <p>
                      Proposed Answer from OpenAI and VectorDB <br/>
                      {answer}
                      </p>
                   </body>
                </html>
            """

    # return {"Query asked was ": query}
    return HTMLResponse(content=html_content, status_code=200)

