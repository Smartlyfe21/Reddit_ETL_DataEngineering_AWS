from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(ti):
    """
    Airflow pipeline function to upload a file to S3.

    Parameters:
    - ti: TaskInstance (Airflow context)
    """
    # Pull file path from XCom
    file_path = ti.xcom_pull(task_id='reddit_extraction', key='return_value')

    if not file_path:
        raise ValueError("No file path returned from reddit_extraction task.")

    # Connect to S3
    s3 = connect_to_s3()

    # Ensure bucket exists
    create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)

    # Upload the file
    s3_file_name = file_path.split('/')[-1]
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, s3_file_name)
