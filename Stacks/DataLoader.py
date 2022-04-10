from aws_cdk import (
    # Duration,
    Stack,
    aws_s3_deployment as _s3Deploy,
    aws_s3 as _s3,
    RemovalPolicy
    # aws_sqs as sqs,
)

from constructs import Construct


class LoaderS3(Stack):

    def __init__(self, scope: Construct, construct_id: str, is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        if is_prod:
            _bucket = _s3.Bucket(self,
                                 'project-S3Bucket',
                                 access_control=_s3.BucketAccessControl.PUBLIC_READ_WRITE,
                                 bucket_name="prod-piyushbhomalefirstclibucket",
                                 public_read_access=True,
                                 removal_policy=RemovalPolicy.RETAIN,
                                 versioned=True)

            _s3Deploy.BucketDeployment(self,
                                       'bucket-datadeployment',
                                       sources=[_s3Deploy.Source.asset(path="Scraper")
                                                ],
                                       destination_bucket=_bucket,
                                       )
        else:
            _bucket = _s3.Bucket(self,
                                 'project-S3Bucket',
                                 access_control=_s3.BucketAccessControl.PUBLIC_READ_WRITE,
                                 bucket_name="piyushbhomalefirstclibucket",
                                 public_read_access=True,
                                 removal_policy=RemovalPolicy.DESTROY)

            _s3Deploy.BucketDeployment(self,
                                       'bucket-datadeployment',
                                       sources=[_s3Deploy.Source.asset(path="Scraper")
                                                ],
                                       destination_bucket=_bucket,
                                       )







