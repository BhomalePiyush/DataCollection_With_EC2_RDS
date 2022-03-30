from aws_cdk import (
    # Duration,
    Stack,
    aws_s3_deployment as _s3Deploy,
    aws_s3 as _s3
    # aws_sqs as sqs,
)

from constructs import Construct


class LoaderS3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _bucket = _s3.Bucket(self,
                             'project-S3Bucket',
                             access_control=_s3.BucketAccessControl.PUBLIC_READ_WRITE,
                             bucket_name="piyushbhomalefirstclibucket",
                             public_read_access=True)

        _s3Deploy.BucketDeployment(self,
                                   'bucket-datadeployment',
                                   sources=[_s3Deploy.Source.data(object_key="Initiator.py",
                                                                  data="Scraper/Initiator.py"),
                                            _s3Deploy.Source.data(object_key='itemlist.txt',
                                                                  data='Scraper/itemlist.txt'),
                                            _s3Deploy.Source.data(object_key='requirements.txt',
                                                                  data='Scraper/requirements.txt')],
                                   destination_bucket=_bucket,
                                   )






