from sqlModel import create_engine, Session

engine = create_engine("sqlite:///iwansusanto.db", echo=True)

def get_db():
    with Session(engine) as session:
        yield session