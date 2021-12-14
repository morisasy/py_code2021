from sqlalchemy import create_engine, text

# Make the engine

engine = create_engine("sqlite + pysqlite:///vball.db", future=True, echo=True)

# Use a context manager

with engine.connect() as conn:
	result = conn.execute(text("SELECT 'hello world"))
	print(result.all())


