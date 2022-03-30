#!/bin/bash
cd /home/ec2-user
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
pip install virtualenv
virtualenv scrap
source scrap/bin/activate
pip install -r requirements.txt
aws s3 cp s3://piyushbhomalefirstclibucket/itemlist.txt itemlist.txt
aws s3 cp s3://piyushbhomalefirstclibucket/Initiator.py Initiator.py
aws s3 cp s3://piyushbhomalefirstclibucket/Program.py Program.py
python3 Initiator.py