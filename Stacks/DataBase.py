from aws_cdk import (
    # Duration,
    Stack, aws_rds as _rds,
    aws_ec2 as _ec2,
    # aws_iam as _iam
    # aws_sqs as sqs,
)
import aws_cdk as cdk
from constructs import Construct


class Database(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # initialize your vpc
        vpc = _ec2.Vpc.from_lookup(self,
                                   "importVPC",
                                   vpc_id="vpc-0efbae3722b5b51c9")
        # Instance type
        type_of_instance = _ec2.InstanceType.of(_ec2.InstanceClass.BURSTABLE2,
                                                _ec2.InstanceSize.MICRO)
        # Creating Database Engine
        engine = _rds.DatabaseInstanceEngine.mysql(version=_rds.MysqlEngineVersion.VER_8_0_21)
        # password creation
        password = cdk.SecretValue.plain_text("vitafinalproject")
        # Database creation
        _rds.DatabaseInstance(self,
                              "mydatabase",
                              vpc=vpc,
                              engine=engine,
                              allocated_storage=20,                # this is minimun allocated
                              max_allocated_storage=21,            # Minimum Allocated
                              database_name="ProjectDatabase",     # Database Name
                              instance_identifier="projectdatabase",
                              publicly_accessible=True,
                              deletion_protection=False,
                              vpc_subnets=_ec2.SubnetSelection(
                                subnet_type=_ec2.SubnetType.PUBLIC
                                                            ),
                              instance_type=type_of_instance,
                              credentials=_rds.Credentials.from_password(username="vitaproject",
                                                                         password=password),
                              security_groups=[_ec2.SecurityGroup.from_security_group_id(self, "SG",
                                                                                         "sg-0f9bc6f84321e64e4",
                                                                                         mutable=False
                                                                                         )]
                              )

