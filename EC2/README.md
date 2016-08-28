#LOGIN TO EC2 AS UBUNTU
ssh -i BuzzfeedKeyPair.pem ubuntu@52.40.23.26

#PUT FILE FROM MAC TO EC2
scp -i BuzzfeedKeyPair.pem  pullBuzzFeed.py  ubuntu@52.40.23.26:/home/ubuntu

#COPY DATA FILES FROM EC2 TO CURRENT DIRECTORY
scp -i ../BuzzfeedKeyPair.pem  ubuntu@52.40.23.26:/home/ubuntu/buzzfeeddata/*.txt .
