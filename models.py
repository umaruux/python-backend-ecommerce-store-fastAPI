from sqlalchemy import Float, String  # Imports database column types.
from sqlalchemy.orm import Mapped, mapped_column  # Imports SQLAlchemy's typed column tools.

from database import Base  # Imports the shared base class for our models.


class Product(Base):  # Defines a Product model that SQLAlchemy maps to a database table.
    __tablename__ = "products"  # Sets the table's name in the database.

    id: Mapped[int] = mapped_column(primary_key=True)  # Defines an integer ID column and makes it the primary key.
    name: Mapped[str] = mapped_column(String(100), nullable=False)  # Defines a required text column, up to 100 characters.
    price: Mapped[float] = mapped_column(Float, nullable=False)  # Defines a required floating-point price column.