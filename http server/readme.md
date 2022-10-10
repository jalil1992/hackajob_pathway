# DevOps - HTTP Server

## Requirements

Install either NGINX and set up 3 virtual hosts/server blocks that will listen to the following ports: 8081, 8082, 8083. To check the ports have been set up correctly, make sure http://localhost:port displays "Hello From %port%" (Example: the first host should print "Hello From 8081").

Use NGINX to set up a load balancer on port 8080 (this port is already in use and your task is to detect and kill the process using it; make sure you do not kill all the processes as the challenge requires you to clear port 8080 only). The load balancer should redirect requests to the following ports 8081, 8082, 8083 using the round-robin strategy.

Note: Systemd is not available. Start NGINX using "nginx" command.

## Solution

1. Install the necessary packages.
   ```
   sudo apt update
   sudo apt install nginx
   apt install net-tools
   apt install psmisc
   ```
2. Kill the process occupying 8080 port.
   After `netstat -ltnp` it turned out that a process from `ruby` occupies that port and it keeps spawning itself whenever tried to kill.
   So need to find the parent of that process and kill it.
   So used `pstree -p` and found that a process with PID 9 is monitoring the subprocesses and recreating them.
   ```
   kill -9 9
   ```
3. Prepare html files to use as `index.html`.
   ```
   mkdir /usr/data/8081
   vi /usr/data/8081/index.html
   # paste the html with proper port content
   mkdir /usr/data/8082
   vi /usr/data/8082/index.html
   # paste the html with proper port content
   mkdir /usr/data/8083
   vi /usr/data/8083/index.html
   # paste the html with proper port content
   ```
4. Remove the default conf and modify the nginx conf.

   ```
   rm /etc/nginx/sites-enabled/default
   vi /etc/nginx/conf/nginx.conf
   # paste the contents from nginx.conf file of this repo
   ```

5. Finally, check if the `conf` is ok and start nginx.
   ```
   nginx -t
   service nginx start
   ```
