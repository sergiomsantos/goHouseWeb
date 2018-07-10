[![Build Status](https://travis-ci.org/sergiomsantos/goHouseWeb.svg?branch=master)](https://travis-ci.org/sergiomsantos/goHouseWeb)

# INSTALL

```bash
# install dependencies
$ pip install -r requirements.txt

# give it a first try:
$ python main.py
 * Running on http://localhost:4000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: <SOME_PIN>
```

## INSTALL AS A SERVICE

### 1. SYSTEMD

```bash
# copy file
$ cp gohouseweb.service /etc/systemd/system/

# run service
$ sudo systemctl status|start|stop gohouseweb
```

### 2. UPSTART

```bash
# copy file
$ cp gohouseweb.conf /etc/init/

# run service
$ sudo initctl status|start|stop gohouseweb
```

# TEST

```bash
# install development dependencies
$ pip install -r dev-requirements.txt

# run tests
$ nose2
```