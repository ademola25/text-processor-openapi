import logging
from functools import wraps


# Configure logging to write to a file, appending log messages
logging.basicConfig(
    filename='error.log',
    filemode='a', 
    level=logging.ERROR, 
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S' 
)

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An unexpected error occurred in {func.__name__}: {e}")
            return {"response":"Something Went wrong please try again later", "status": 400}
    return wrapper
