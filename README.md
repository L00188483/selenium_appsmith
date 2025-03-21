
##### setup
```bash
$ git clone ...
$ cd selenium_appsmith/
$ python -m venv venv
$ chmod +x docker_restart.sh
```


##### run the Selenium container
```bash
$ ./docker_restart.sh

# check container is up
$ docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                                                                                          NAMES
0ff6d6b233ad   selenium/standalone-chrome:latest   "/opt/bin/entry_poin…"   22 minutes ago   Up 21 minutes   0.0.0.0:4444->4444/tcp, [::]:4444->4444/tcp, 5900/tcp, 0.0.0.0:7900->7900/tcp, [::]:7900->7900/tcp, 9000/tcp   selenium_chrome
```


##### run the test script
```bash
$ source venv/bin/activate
$ python selenium_appsmith/main.py
```


##### view the remote browser
* go to: http://localhost:7900/?autoconnect=1&resize=scale&password=secret
