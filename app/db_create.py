from app import db, ctx

db.create_all()

ctx.pop()
