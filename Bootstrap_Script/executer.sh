#!/bin/bash
cd /home/ec2-user
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
pip install virtualenv
virtualenv scrap
source scrap/bin/activate
aws s3 cp s3://piyushbhomalefirstclibucket/requirements.txt requirements.txt
pip install -r requirements.txt
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
aws s3 cp s3://piyushbhomalefirstclibucket/itemlist.txt itemlist.txt
aws s3 cp s3://piyushbhomalefirstclibucket/Initiator.py Initiator.py
python Initiator.py