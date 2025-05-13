# from fastapi import FastAPI
# import uvicorn
# import sys
# import os
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from fastapi.responses import JSONResponse
# from src.TEXT_SUMMARIZATION.pipeline.predict_pipeline import PredictionPipeline

# text: str = "What is Text Summarization?"

# app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")


# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return JSONResponse(content={"message": "Training successful !!"})
#     except Exception as e:
#         return JSONResponse(content={"error": f"Error Occurred! {str(e)}"}, status_code=500)


# @app.post("/predict")
# async def predict_route(text: str):
#     try:
#         obj = PredictionPipeline()
#         result = obj.predict(text)
#         return JSONResponse(content={"prediction": result})
#     except Exception as e:
#         return JSONResponse(content={"error": f"Error Occurred! {str(e)}"}, status_code=500)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)
from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.TEXT_SUMMARIZATION.pipeline.predict_pipeline import PredictionPipeline


text:str = "What is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")



@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")
    



@app.post("/predict")
async def predict_route(text):
    try:

        obj = PredictionPipeline()
        text = obj.predict(text)
        return text
    except Exception as e:
        raise e
    

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)