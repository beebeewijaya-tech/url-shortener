import boto3

from utils.settings import Settings


class DigitalOceanSpaceService:
    session = boto3.session.Session()
    client = None
    bucket_name = None

    def __init__(self, config: Settings):
        self.bucket_name = config.spaces_bucket_name
        self.client = self.session.client('s3',
                                          endpoint_url=config.spaces_bucket_url,
                                          region_name=config.spaces_region,
                                          aws_access_key_id=config.spaces_access,
                                          aws_secret_access_key=config.spaces_secret)

    def upload(self, file, filename):
        return self.client.put_object(Bucket=self.bucket_name,
                                      Key=filename,
                                      Body=file,  # The object's contents.
                                      ACL='public-read',
                                      )
