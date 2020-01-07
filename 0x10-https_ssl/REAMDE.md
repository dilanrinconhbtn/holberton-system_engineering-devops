# HTTPS SSL

## 0. HTTPS ABC

What is HTTPS?

Why do you need HTTPS?

You want to setup HTTPS on your website, where shall you place the certificate?



## 1. World wide web

Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.


## 2. HAproxy SSL termination mandatory
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

Requirements:

HAproxy must be listening on port TCP 443
HAproxy must be accepting SSL traffic
HAproxy must serve encrypted traffic that will return the / of your web server
When querying the root of your domain name, the page returned must contain Holberton School
Share your HAproxy config as an answer file (/etc/haproxy/haproxy.cfg)
The file 2-haproxy_ssl_termination must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, SSL termination is not available before v1.5.