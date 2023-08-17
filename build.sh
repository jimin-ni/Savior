#!/bin/bash

# libpq-dev 설치
sudo apt-get update
sudo apt-get install -y libpq-dev

# 필요한 빌드 명령들 추가
pip install -r requirements.txt
python manage.py collectstatic --noinput

chmod +x build.sh