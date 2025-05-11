
##### Local python-venv setup, this installs pytest
```bash
$ git clone git@github.com:L00188483/selenium_appsmith.git 
$ cd selenium_appsmith/
$ python -m venv venv
$ pip install -r requirements.txt
```


##### run the containers
```bash
$ docker compose up -d

# check container is up
$ docker ps

CONTAINER ID   IMAGE                               COMMAND                  CREATED          STATUS                    PORTS                                                                                                          NAMES
89f70feef4f7   appsmith/appsmith-ce                "/opt/appsmith/entry…"   16 minutes ago   Up 16 minutes (healthy)   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp, 0.0.0.0:4431->443/tcp, [::]:4431->443/tcp                             appsmith
5b4451eceac7   selenium/standalone-chrome:latest   "/opt/bin/entry_poin…"   43 minutes ago   Up 16 minutes             0.0.0.0:4444->4444/tcp, [::]:4444->4444/tcp, 5900/tcp, 0.0.0.0:7900->7900/tcp, [::]:7900->7900/tcp, 9000/tcp   selenium_chrome
```

##### Unzip the test data
```bash

```

##### Set up Appsmith database
* go to: http://localhost:8080/
* Register a user
* Import an application
* Share the application as a public URL, copy it to your clipboard
* Paste this unique URL path into: `selenium_appsmith/tests/conftests.py:WEBPAGE_URL_PATH`


##### Run the tests
```bash
$ source venv/bin/activate
$ pytest pytest selenium_appsmith/tests/test_with_selenium.py
```

##### Debugging: Run a browser instance and pause at a pdb breakpoint
```bash
$ source venv/bin/activate
$ python selenium_appsmith/webpage_interface.py
```


##### View the remote browser
* go to: http://localhost:7900/?autoconnect=1&resize=scale&password=secret


##### Tear down containers
```bash
$ docker compose down
```
