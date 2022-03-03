#!/usr/bin/env python3
import os
import aws_cdk as cdk
from Stacks.DataBase import Database
from Stacks.Data_genrator import EC2
from database.database_stack import DatabaseStack
from Stacks.DataLoader import LoaderS3

dev_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()
LoaderS3(app,"filesloader", env=dev_env)
database = Database(app, "databasestack", env=dev_env)
genrator = EC2(app, "datagenrator", env=dev_env)
genrator.add_dependency(database, "database is required to put records")
app.synth()
