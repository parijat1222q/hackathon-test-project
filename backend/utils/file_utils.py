
import os
import logging

def save_upload(file: bytes, dest_path: str) -> bool:
    try:
        with open(dest_path, "wb") as f:
            f.write(file)
        return True
    except Exception as e:
        logging.error(f"Error saving file: {e}")
        return False

def cleanup_uploads(upload_dir: str = "static/uploads", max_age_hours: int = 24) -> None:
    now = os.path.getmtime
    for filename in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, filename)
        try:
            if os.path.isfile(file_path):
                age_hours = (os.path.getmtime(file_path) - now(file_path)) / 3600
                if age_hours > max_age_hours:
                    os.remove(file_path)
                    logging.info(f"Deleted old upload: {file_path}")
        except Exception as e:
            logging.error(f"Error cleaning up file {file_path}: {e}")
