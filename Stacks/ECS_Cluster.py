# import os
from aws_cdk import (
    # Duration,
    Stack, aws_ec2 as _ec2,
    aws_iam as _iam,
    aws_ecr as _ecr,
    aws_ecs as _ecs,
    aws_autoscaling as _autoscaling
    # aws_sqs as sqs,)
)
# from aws_cdk.aws_s3_assets import Asset
from constructs import Construct


class ECS(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # Create the ECR Repository
        ecr_repository = _ecr.Repository(self,
                                         "ecs-devops-project-repository",
                                         repository_name="ecs-devops-project-repository"
                                         )

        # initialize your vpc
        vpc = _ec2.Vpc.from_lookup(self,
                                   "importVPC",
                                   vpc_id="vpc-0efbae3722b5b51c9")

        # Create the ECS Cluster
        cluster = _ecs.Cluster(self,
                               "ecs-devops-project-cluster",
                               cluster_name="ecs-devops-project-cluster",
                               vpc=vpc)

        auto_scaling_group = _autoscaling.AutoScalingGroup(self, "ASG",
                                                           vpc=vpc,
                                                           instance_type=_ec2.InstanceType("t2.micro"),
                                                           machine_image=_ecs.EcsOptimizedImage.amazon_linux2(),
                                                           min_capacity=1,
                                                           max_capacity=5
                                                           )

        capacity_provider = _ecs.AsgCapacityProvider(self, "AsgCapacityProvider",
                                                     auto_scaling_group=auto_scaling_group
                                                    )
        cluster.add_asg_capacity_provider(capacity_provider)

        execution_role = _iam.Role(self,
                                   "ecs-devops-project-execution-role",
                                   assumed_by=_iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                                   role_name="ecs-devops-project-execution-role")
        execution_role.add_to_policy(_iam.PolicyStatement(
            effect=_iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ]
        ))
        execution_role.add_managed_policy( _iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonRDSFullAccess"
            )
        )

        task_definition = _ecs.FargateTaskDefinition(self,
                                                     "ecs-devops-project-task-definition",
                                                     execution_role=execution_role,
                                                     family="ecs-devops-project-task-definition")
        container = task_definition.add_container(
            "ecs-devops-project",
            image=_ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
        )

        # Create the ECS Service
        service = _ecs.FargateService(self,
                                      "ecs-devops-project-service",
                                      cluster=cluster,
                                      task_definition=task_definition,
                                      service_name="ecs-devops-project-service")