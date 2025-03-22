
##### setup
```bash
$ git clone git@github.com:L00188483/selenium_appsmith.git 
$ cd selenium_appsmith/
$ python -m venv venv
$ pip install -r requirements.txt
$ chmod +x docker_restart.sh
```


##### run the Selenium container
```bash
$ ./docker_restart.sh

# check container is up
$ docker ps
CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS          PORTS                                                                                                          NAMES
0ff6d6b233ad   selenium/standalone-chrome:latest   "/opt/bin/entry_poin…"   2 minutes ago   Up 2 minutes   0.0.0.0:4444->4444/tcp, [::]:4444->4444/tcp, 5900/tcp, 0.0.0.0:7900->7900/tcp, [::]:7900->7900/tcp, 9000/tcp   selenium_chrome
```

##### run the tests
```bash
$ source venv/bin/activate
$ pytest selenium_appsmith/
```

##### run pdb 'main' script
```bash
$ source venv/bin/activate
$ python selenium_appsmith/webpage_interface.py
```


##### view the remote browser
* go to: http://localhost:7900/?autoconnect=1&resize=scale&password=secret
