## What this does?
This repo along with https://github.com/pman06/kubernetesmanifest creates a Jenkins pipeline with GitOps to deploy code into a Kubernetes cluster. CI part is done via Jenkins and CD part via ArgoCD (GitOps).

## Jenkins installation
Jenkins is installed on EC2. Follow the instructions on https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/ . You can skip "Configure a Cloud" part for this demo. Please note some commands from this link might give errors, below are the workarounds:

1. If you get daemonize error while running the command `sudo yum install jenkins java-1.8.0-openjdk-devel -y` then , run the commands from the answer of https://stackoverflow.com/questions/68806741/how-to-fix-yum-update-of-jenkins

2. Install Docker on the EC2 after Jenkins is installed by following the instructions on https://serverfault.com/questions/836198/how-to-install-docker-on-aws-ec2-instance-with-ami-ce-ee-update

3. Run `sudo chmod 666 /var/run/docker.sock` on the EC2 after Docker is installed.

4. Install Git on the EC2 by running `sudo yum install git`

### Jenkins plugins

Install the following plugins for the demo.
- Amazon EC2 plugin (No need to set up Configure Cloud after)
- Docker plugin  
- Docker Pipeline
- GitHub Integration Plugin
- Parameterized trigger Plugin

## ArgoCD installation 

Install ArgoCD in your Kubernetes cluster following this link - https://argo-cd.readthedocs.io/en/stable/getting_started/

## How to run!
1. Fork this repository as well as the [kubernetes manifest](https://github.com/pman06/kubernetesmanifest "manifest repository") repository
2. Add Jenkins server URl webhooks to both repositories webhooks settings
3. Also add the repository to your created Jenkins pipeline projects
    - Your manifest jenkins projects should be named updatemanifest in order to receive docker image tags as paramater. 
4. Add docker hub credentials to jenkins environment variables to allow image push to dockerhub
5. Add Gitub credentials(username and personal access token) to Jenkins server environmet
6. Add kubernetesmanifest repository url to your argocd app (running in the kubernetes cluster from the tutorial above) to fetch latest updates from the repo when new version is pushed to the repository.

### Thanks and Enjoy
