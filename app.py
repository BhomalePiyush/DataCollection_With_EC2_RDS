#!/usr/bin/env python3
import os
import aws_cdk as cdk
from Stacks.DataBase import Database
from Stacks.Data_genrator import EC2
from database.database_stack import DatabaseStack
from Stacks.DataLoader import LoaderS3
from Stacks.ECS_Cluster import ECS

dev_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()
loader = LoaderS3(app, "filesloader", env=dev_env)
database = Database(app, "databasestack", env=dev_env)
database.add_dependency(loader,"to run program S3 bucket should be present")
# genrator = EC2(app, "datagenrator", env=dev_env)
# genrator.add_dependency(database, "database is required to put records")
ecs_cluster = ECS(app, 'ecsstack', env=dev_env)
ecs_cluster.add_dependency(database, 'for creating ecs cluster database is required')
app.synth()
