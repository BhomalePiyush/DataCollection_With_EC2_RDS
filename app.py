#!/usr/bin/env python3
import os
import aws_cdk as cdk
from Stacks.DataBase import Database
from Stacks.Data_genrator import EC2
from database.database_stack import DatabaseStack
from Stacks.DataLoader import LoaderS3
from Stacks.ECS_Cluster import ECS

dev_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))
prod_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()
database = Database(app, "databasestack", env=dev_env)
ecs_cluster = ECS(app, 'ecsstack', env=dev_env)
ecs_cluster.add_dependency(database, 'for creating ecs cluster database is required')
# loader = LoaderS3(app, "filesloader", env=dev_env)
# loader.add_dependency(database, "database should be available to deploy s3")
# genrator = EC2(app, "datagenrator", env=dev_env)
# genrator.add_dependency(loader, "database is required to put records")
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<production envornment>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# prod_database = Database(app, "Proddatabasestack", is_prod=True, env=dev_env)
# prod_ecs_cluster = ECS(app, 'ecsstack', is_prod=True, env=dev_env)
# prod_ecs_cluster.add_dependency(database, 'for creating ecs cluster database is required')
# prod_loader = LoaderS3(app, "Prodfilesloader", is_prod=True, env=prod_env)
# prod_loader.add_dependency(database, "database should be available to deploy s3")
# prod_genrator = EC2(app, "Proddatagenrator", is_prod=True, env=dev_env)
# prod_genrator.add_dependency(prod_loader, "database is required to put records")
app.synth()
