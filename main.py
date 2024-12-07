import os

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
import models
from database import engine, get_db

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI CRUD Service"}


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "server": os.getenv("SERVER_NAME", "unknown"),
        "timestamp": datetime.utcnow().isoformat()
    }

@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = models.ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.ItemModel).offset(skip).limit(limit).all()
    return items


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.ItemModel).filter(models.ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.ItemModel).filter(models.ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.ItemModel).filter(models.ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted successfully"}