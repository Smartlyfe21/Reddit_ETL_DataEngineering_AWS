import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME

def connect_to_s3():
    """
    Connect to AWS S3 using s3fs with credentials from constants.py
    Returns the S3FileSystem object.
    """
    try:
        s3 = s3fs.S3FileSystem(
            anon=False,
            key=AWS_ACCESS_KEY_ID,
            secret=AWS_SECRET_ACCESS_KEY
        )
        print("Connected to S3 successfully!")
        return s3
    except Exception as e:
        print(f"Error connecting to S3: {e}")
        raise

def create_bucket_if_not_exist(s3: s3fs.S3FileSystem, bucket_name: str):
    """
    Create an S3 bucket if it does not exist.
    """
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f"Bucket '{bucket_name}' created.")
        else:
            print(f"Bucket '{bucket_name}' already exists.")
    except Exception as e:
        print(f"Error creating bucket '{bucket_name}': {e}")
        raise

def upload_to_s3(s3: s3fs.S3FileSystem, local_file_path: str, bucket_name: str, s3_file_name: str):
    """
    Upload a local file to S3 bucket.
    """
    try:
        s3_path = f"{bucket_name}/{s3_file_name}"
        s3.put(local_file_path, s3_path)
        print(f"Uploaded '{local_file_path}' to '{s3_path}'")
    except Exception as e:
        print(f"Error uploading file '{local_file_path}' to S3: {e}")
        raise
