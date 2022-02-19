from models.base import engine, Base
from models.user import User
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

session = Session(bind=engine, future=True)

stmt = select(User)
res = session.execute(stmt).all()
res[0][0].created_at
res = session.execute(stmt).scalars().all()
res[0].created_at

stmt = select(Base.metadata.tables["user"])
res = session.execute(stmt).all()

res[0].keys()

stmt = select(Base.metadata.tables["user"]).where(Base.metadata.tables["user"].c.username == "b")
res = session.execute(stmt).all()
res = session.execute(stmt).first()
list(res.keys())
session.commit()  # end our current transaction by committing or rolling back
with session.begin():
    res = session.execute(stmt).all()
