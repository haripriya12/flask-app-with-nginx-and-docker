
HOW TO CREATE AN NGINX REVERSE PROXY, LOAD BALANCER WITH DOCKER
      
REQUIREMENTS:

Lets start by running a simple nginx container listening on our localhost's port.You should have installed 
Docker and Nginx in your machine before start this project.

    • To install Dcoker, please follow the reference below
    
    	https://docs.docker.com/install/
        https://docs.docker.com/get-started/
        https://docs.docker.com/compose/gettingstarted/

    • To install Nginx, please follow the below reference
             https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04

Step-1: if you install Docker in your machine, use below command lines that helps you to interact with the containers.

    •  docker ps ( this command gives you a list of existing docker containers ) 
    •  docker ps -a ( this command gives you a list of containers has run recently )
    •  docker stop container-name ( stop the container )
    •  docker rm container-name ( remove the container from the list )


Step-2: Start creating the Nginx Docker container


     docker run --name docker-nginx-1 -p 80:80 -d nginx
        
        
      1. Run the above command for creating the container
      2. --name specifies the name of the container
      3. -p specifies the port. In this command we are mapping port 80 in the container to the port 80 on the server
      4. -d specifies to run this docker in the background
      5. nginx is the name of the image
      6. Enter the command ( $ docker ps ) you see the docker-nginx in the container’s list
      7. $ docker stop docker-nginx-1 ( stop working the docker )
      8. $ docker rm docker-nginx-1 ( remove the container from list )


     docker run –name docker-nginx-2 -p 80 -d nginx
         
	 
	1. Run the above command for creating the another container
        2. In the second container the port was directly mapping to the default port
    
    
USE NGINX AS A REVERSY PROXY TO YOUR DOCKER CONTAINER


    For setting up the reversy proxy, you should go the container using below command.
    	• docker exec -it docker nginx 1 bin/bash
    	• cd /etc/nginx ( go to the directory structure, where all your configuration files are stored)
    Now you should have a config folder on your host, go to the directory called conf.d. 
    Inside conf.d, there is a single file called default.conf. You can delete that default file.
    	• nano yourtestfile.conf ( you can create this new file and and set server’s in this file)
    In your new file, enter the following
          
          server {
                  listen 80;
                  location / {
                     proxy_pass http://your-ip-addres/;
                   }
           }
 
    •  $ nginx -t ( You can test, if nginx has errors)
    • nginx -s reload (For start the nginx)
    • Now go to the browser and type localhost, you can see youe local server.
                           
