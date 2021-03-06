## K8s Commands and Aliases

````
kubectl create -f db/secret.yml
kubectl create -f db/PersistentVolumeClaim.yml
kubectl create -f db/PersistentVolume.yml
kubectl create -f db/mysql_service.yml
kubectl create -f db/mysql_deployment.yml
kubectl create -f app/flask_service.yml
kubectl create -f app/flaskapp_deployment.yml

alias kkgd='kubectl get deployments'
alias kkgp='kubectl get pods'
alias kkgj='kubectl get jobs'
alias kkgs='kubectl get service'
alias kkds='kubectl delete service'
alias kkgl='kubectl logs'
alias kkglf='kubectl logs -f'
alias kkgpvc='kubectl get pvc'
alias kkgpv='kubectl get pv'
alias kkdd='kubectl delete deployments'
alias kkdp='kubectl delete pods'
alias kkdj='kubectl delete jobs'
alias kkdpv='kubectl delete pv'
alias kkdpvc='kubectl delete pvc'
alias kkgpn='kubectl get pods -o wide --sort-by="{.spec.nodeName}"'
alias kkdcp='kubectl describe pod'
alias kkdcs='kubectl describe service'
alias kkdcpvc='kubectl describe pvc'
alias kkdcpv='kubectl describe pv'
alias kkgn='kubectl get nodes'
alias kka='kubectl apply -f'
alias kkdf='kubectl delete -f'
alias kkcc='kubectl config current-context'
alias kkx='kubectl exec -it'
alias kkuc='kubectl config use-context'
````
