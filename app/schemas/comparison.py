from typing import List
from pydantic import BaseModel

from app.schemas.product import ProductDTO

class ComparisonProductDTO(BaseModel):
    id: int
    comparison_id: int
    product: ProductDTO

    class Config:
        from_attributes = True


class ComparisonBase(BaseModel):
    title: str
    description: str
    user_id: str
    date_created: str
    product_type_id: int
    products: List[int]

    class Config:
        from_attributes = True


class ComparisonDTO(ComparisonBase):
    id: int
    products: List[ComparisonProductDTO]

    class Config:
        from_attributes = True
