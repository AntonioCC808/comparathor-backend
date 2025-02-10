from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON
from sqlalchemy.orm import relationship, Mapped
from app.database import Base


class ProductType(Base):
    __tablename__ = "product_types"
    id = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = Column(String)
    description: Mapped[str] = Column(String)
    metadata_schema = Column(JSON)
    products = relationship("Product", back_populates="product_type")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    product_type_id = Column(Integer, ForeignKey("product_types.id"))
    user_id = Column(String, ForeignKey("users.user_id"))
    name = Column(String)
    image_base64 = Column(String)
    brand = Column(String)
    score = Column(Float)
    user = relationship("User", back_populates="products")
    product_type = relationship("ProductType", back_populates="products")
    # One-to-Many relationship with ProductMetadata
    product_metadata = relationship(
        "ProductMetadata",
        back_populates="product",
        cascade="all, delete-orphan"
    )


class ProductMetadata(Base):
    __tablename__ = "product_metadata"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    attribute = Column(String)
    value = Column(String)
    score = Column(Float)
    product = relationship("Product", back_populates="product_metadata")
