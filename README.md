
# dStatus


dStatus is web application to monitor CPU resource on local and remote machine.

dStatus contain dServer and dClient.


### dServer

dServer is provide web interface to monitor CPU resource.

It's run client application to connect dClient and receive data. 


### dClient

dClient is collect informaation and send it to dServer.


### How to run dServer


```
python dServer/app.py
```


### How to run dClient


```
python dClient/dClient.py
```
