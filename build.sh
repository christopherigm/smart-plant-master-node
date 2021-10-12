#! /bin/sh

docker build -t smart-plant .

docker tag smart-plant longmont.iguzman.com.mx:5000/smart-plant:1.0

docker push longmont.iguzman.com.mx:5000/smart-plant:1.0

echo "done"
