from minio import Minio
from minio.error import S3Error
import logging
from app.dependencies import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)

class ImageHandler:
    
    @staticmethod
    def upload_file(file:str, filename:str) -> bool:
        

        try:
            minio_client = Minio(
                endpoint="play.min.io",
                access_key="ycPmXgLht8mDU0NEZ1Hw",
                secret_key="aXiBpWLM6FVSfV38nhTfSppmDtpl8S2jBr3K7luw",
                secure=True
            )


            # The destination bucket and filename on the MinIO server
            bucket_name = "mybucket-testapp"

            # Make the bucket if it doesn't exist.
            found = minio_client.bucket_exists(bucket_name)
            if not found:
                minio_client.make_bucket(bucket_name)

            # Upload the file, renaming it in the process
            minio_client.fput_object(
                bucket_name, filename, file,
            )
            return True
        except S3Error as e:
            logger.error(f"MinIO Error: {e}")
            return False
