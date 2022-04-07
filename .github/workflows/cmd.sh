#!/bin/bash
sudo apt-get -yq update
sudo apt update
sudo apt install -y python3-venv
sudo pip3 install --upgrade pip
sudo pip3 install --upgrade virtualenv
python3 -V
export PYTHONPATH=/usr/local/bin/python3
sudo DEBIAN_FRONTEND=noninteractive apt install -y nodejs
sudo DEBIAN_FRONTEND=noninteractive apt install -y npm
sudo npm install -g aws-cdk
python3 -m venv .venv
source .venv/bin/activate
sudo pip3 install aws-cdk.cdk
sudo pip3 install awscli
aws configure set aws_access_key_id ${{secrets.AWS_ACCESS_KEY_ID_P}}
aws configure set aws_secret_access_key ${{secrets.AWS_SECRET_ACCESS_KEY_P}}
aws configure set region ${{secrets.AWS_DEFAULT_REGION}}
sudo pip3 install -r requirements.txt
cdk ls
cdk synth
cdk deploy ecsstack --require-approval=never
