import logging
from logging.config import fileConfig  # Add the missing import for fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.declarative import declarative_base
import sys
import os

# Add the app directory to the path so we can import the models dynamically
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Import the Base class from models so Alembic can access the metadata
# This will automatically detect all models defined in the app/models directory
from app.models.Employee import Base  # Import Base (where all models inherit from)

# Define the target metadata object that Alembic will use
target_metadata = Base.metadata

# Configuring the connection string from alembic.ini
config = context.config
fileConfig(config.config_file_name)  # Ensure this is correctly called

# Set up the connection and run migrations
def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
