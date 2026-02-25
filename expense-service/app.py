from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas
from dependencies import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expenses")
def add_expense(exp: schemas.ExpenseCreate,
                user: str = Depends(get_current_user),
                db: Session = Depends(get_db)):
    new_exp = models.Expense(email=user, title=exp.title, amount=exp.amount)
    db.add(new_exp)
    db.commit()
    return {"msg": "Expense added"}

@app.get("/expenses")
def list_expenses(user: str = Depends(get_current_user),
                  db: Session = Depends(get_db)):
    data = db.query(models.Expense).filter(models.Expense.email == user).all()
    return data