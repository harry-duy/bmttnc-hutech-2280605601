openssl req -newkey rsa:2048 -nodes -keyout server-key.key -x509 -days 365 -out server-cert.crt -config server-cert.cnf
pause