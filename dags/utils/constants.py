import configparser

CONFIG_PATH = '/opt/airflow/config/config.conf'

config = configparser.ConfigParser()
config.optionxform = str  # preserves the case of keys
config.read(CONFIG_PATH)

# API keys
if 'api_keys' not in config:
    raise KeyError("Section 'api_keys' not found in config.conf")

try:
    CLIENT_ID = config.get('api_keys', 'CLIENT_ID').strip()
    SECRET = config.get('api_keys', 'SECRET').strip()
except configparser.NoOptionError as e:
    raise KeyError(f"Missing option in 'api_keys' section: {e}")

# AWS credentials
if 'aws' not in config:
    raise KeyError("Section 'aws' not found in config.conf")

AWS_ACCESS_KEY_ID = config.get('aws', 'aws_access_key_id').strip()
AWS_SECRET_ACCESS_KEY = config.get('aws', 'aws_secret_access_key').strip()
AWS_REGION = config.get('aws', 'aws_region').strip()
AWS_BUCKET_NAME = config.get('aws', 's3_bucket_name').strip()  # Corrected key

# File paths
if 'file_paths' not in config:
    raise KeyError("Section 'file_paths' not found in config.conf")

INPUT_PATH = config.get('file_paths', 'input_data_path').strip()  # Corrected key
OUTPUT_PATH = config.get('file_paths', 'output_data_path').strip()
LOGS_PATH = config.get('file_paths', 'logs_path').strip()
