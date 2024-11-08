from fastapi import FastAPI, Response, HTTPException, status, Depends, APIRouter
from typing import Optional, List
from sqlalchemy.orm import Session
from app.database import get_db
import app.models as models
import app.schemas as schemas
import app.utils as utils
import app.oauth2 as oauth2

router = APIRouter(prefix="/products", tags=['Products'])

@router.post("/addproducts")
def add_product(products: schemas.ProductCreate, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO products (name, price) VALUES (%s, %s) RETURNING *""", (product.name, product.price))
    # new_product = cursor.fetchall()
    # conn.commit() #Push changes to db
    print(products.model_dump()) #-->Converts input schema to the expected format mapping for the query
    print("User id: ", user_id.id)
    new_product = models.Product(user_id=user_id.id, **products.model_dump())
    db.add(new_product)
    db.commit()
    
    return {"data": new_product}

@router.get("/getproducts")
def get_products(products: schemas.ProductBase, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    # print(name)
    # cursor.execute(""" SELECT name, price FROM products WHERE name = %s """, (name,))
    # product = cursor.fetchall()
    product = db.query(models.Product).filter(models.Product.name == products.name).first()
    print(product)
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{products.name} not found")
    return product


@router.get("/", response_model=List[schemas.ProductBase])
def get_allproducts(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user), 
                    limit: int = 10, skip: int = 0):  # noqa: F811
    product = db.query(models.Product).filter(models.Product.user_id == int(user_id.id)).limit(limit).offset(skip).all()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No products found")
    return product


@router.delete("/deleteproducts", status_code=status.HTTP_204_NO_CONTENT, )
def delete_products(products: schemas.ProductBase, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    
    product_query = db.query(models.Product).filter(models.Product.name == products.name)
    
    product = product_query.first()
    
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{products.name} not found")
    
    if product.user_id != int(user_id.id):
        print(product.user_id, user_id.id)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You cant delete this post")
     
    product_query.delete(synchronize_session=False)
    db.commit()
    
    return {"data": "Deleted"}