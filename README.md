# INSTALL

## 1. SYSTEMD

```bash
# copy file
$ cp gohouseweb.service /etc/systemd/system/

# run service
$ sudo systemctl status|start|stop gohouseweb
```

## 2. UPSTART

```bash
# copy file
$ cp gohouseweb.conf /etc/init/

# run service
$ sudo initctl status|start|stop gohouseweb
```