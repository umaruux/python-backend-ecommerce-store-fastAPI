from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field
from database import Base, engine
from models import Product

Base.metadata.create_all(bind=engine)
app = FastAPI()


products = [
         {"id": 1, "name": "Water Bottle", "price": 12.99},
         {"id": 2, "name": "Notebook", "price": 4.50},
    ]

class ProductCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    price: float = Field(gt=0)


@app.get("/")
def home():
    return {"message":"Shop API is running"}


@app.get("/products")
def get_products(search:str | None = None):
   

    if search:
        matching_products = []

        for product in products:
            if search.lower() in product["name"].lower():
                matching_products.append(product)

        return matching_products


    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products", status_code=201)  # send JSON inputs to create new products
def create_product(product: ProductCreate):
    new_product = product.model_dump()
    new_product["id"] = max(
        (item["id"] for item in products),
        default=0,
    ) + 1

    products.append(new_product)
    return new_product



@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: ProductCreate):
    for product in products:
        if product["id"] == product_id:
            product["name"] = updated_product.name
            product["price"] = updated_product.price
            return product

    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail="Product not found")