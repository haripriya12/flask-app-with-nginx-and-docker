
HOW TO SETUP NGINX USING MULTIPLE DOCKER CONTAINERS
      
REQUIREMENTS:

Lets start by running a simple nginx, that listening on our localhost's default port(80).You should have installed 
Docker Compose, Docker Engine and Nginx in your machine before start this project.

    • To install Dcoker, please follow the reference below
    
    	https://docs.docker.com/install/
        https://docs.docker.com/get-started/
        https://docs.docker.com/compose/gettingstarted/

    • To install Nginx, please follow the below reference
    
        https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04

Step-1: Build a simple python web application and run the app on Docker Compose. follow the reference below

    https://docs.docker.com/compose/gettingstarted/
    
    Play with some of the docker containers:
    •  docker ps ( this command gives you a list of existing docker containers ) 
    •  docker ps -a ( this command gives you a list of containers has run recently )
    •  docker stop container-name ( stop the container )
    •  docker rm container-name ( remove the container from the list )


Step-2: Host Multiple Docker Containers 
    
1. USE NGINX AS A REVERSY PROXY TO YOUR DOCKER CONTAINER


    For setting up the reversy proxy, you should go the container using below command.
    	• docker exec -it docker nginx 1 bin/bash
    	• cd /etc/nginx ( go to the directory structure, where all your configuration files are stored)
    Now you should have a config folder on your host, go to the directory called conf.d. 
    Inside conf.d, there is a single file called default.conf. You can delete that default file.
    	• nano yourtestfile.conf ( you can create this new file and and set server’s in this file)
    In your new file, see the example below
          
          server {
                  listen 80;
                  location / {
                     proxy_pass http://your-ip-addres/;
                   }
		   location / second {
		      proxy_pass http://your-ip-address/;
		   }
           }
 
    • nginx -t ( You can test, if nginx has errors)
    • nginx -s reload ( or ) sudo syatemctl restart nginx.service (For start the nginx)
    • Now go to the browser and type localhost and localhost/second, you can see the result.
    
  2. USE NGINX AS A LOAD BALANCER
     In the loadbalancer.conf file, you need to add upstream and server. see the example below
     
	     http {
		   upstream backend {
		      server localhost:5555;
		      server localhost:5556
		   }
		   server {
		      listen 80;
		      location / {
				proxy_pass http://backend;
			}
		    }
		 }
                           
