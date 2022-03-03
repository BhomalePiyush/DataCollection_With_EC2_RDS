from aws_cdk import (
    # Duration,
    Stack
    # aws_sqs as sqs,
)
import boto3
from constructs import Construct


class LoaderS3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        client = boto3.client('s3')
        clientResponse = client.create_bucket(ACL='public-read-write',
                                             Bucket='piyushbhomalefirstclibucket')
        s3 = boto3.resource('s3')
        BUCKET = "piyushbhomalefirstclibucket"

        s3.Bucket(BUCKET).Object("Initiator.py").upload_file("Scraper/Initiator.py")
        s3.Bucket(BUCKET).Object("itemlist.txt").upload_file("Scraper/itemlist.txt")
