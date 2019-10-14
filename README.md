# flaskapp_kubernetes

============================================

kubectl create -f db/secret.yml

kubectl create -f db/PersistentVolumeClaim.yml

kubectl create -f db/PersistentVolume.yml

kubectl create -f db/mysql_service.yml

kubectl create -f db/mysql_deployment.yml

kubectl create -f app/flask_service.yml

kubectl create -f app/flaskapp_deployment.yml

===============================================
