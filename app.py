from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def helloworld():
    return {"Hello", "World"}

if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0', port=8000)
