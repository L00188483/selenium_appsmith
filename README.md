
##### setup
```bash
$ git clone git@github.com:L00188483/selenium_appsmith.git 
$ cd selenium_appsmith/
$ python -m venv venv
$ pip install -r requirements.txt
```


##### run the containers
```bash
$ docker compose up

# check container is up
$ docker ps

CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                    PORTS                                                                                                          NAMES
89f70feef4f7   appsmith/appsmith-ce                "/opt/appsmith/entry…"   16 minutes ago   Up 16 minutes (healthy)   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp, 0.0.0.0:4431->443/tcp, [::]:4431->443/tcp                             appsmith
5b4451eceac7   selenium/standalone-chrome:latest   "/opt/bin/entry_poin…"   43 minutes ago   Up 16 minutes             0.0.0.0:4444->4444/tcp, [::]:4444->4444/tcp, 5900/tcp, 0.0.0.0:7900->7900/tcp, [::]:7900->7900/tcp, 9000/tcp   selenium_chrome
```

##### run the tests
```bash
$ source venv/bin/activate
$ pytest selenium_appsmith/
```

##### run 'main' pdb script
```bash
$ source venv/bin/activate
$ python selenium_appsmith/webpage_interface.py
```


##### view the remote browser
* go to: http://localhost:7900/?autoconnect=1&resize=scale&password=secret
