from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from assignment-1!"}


def main():
    print("Hello from assignment-1!")


if __name__ == "__main__":
    main()
