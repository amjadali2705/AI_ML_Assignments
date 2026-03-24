from fastapi import FastAPI

app = FastAPI()

# Endpoint 1
@app.get("/")
def get_msg():
    return {
        "message": "Hello World"
    }

# Endpoint 2
@app.get("/data")
def get_data():
    return {
        "name": "Amjad",
        "empId": "25191",
        "company": "NPCI",
        "language": ["golang", "python", "java", "react"]
    }