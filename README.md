Hello Flask
====

* Install and launch a server

```bash
$ virtualenv ./env
$ source ./env/bin/activate
$ pip install flask
$ pip install flask_restful
$ ./api.py
```

* Upload files

```bash
$ curl -XPOST -F "files=@example_data/file1k" -F "files=@example_data/date.txt" localhost:5000/local
{
    "uploaded": [
        {
            "path": "file1k", 
            "size": 1024
        }, 
        {
            "path": "date.txt", 
            "size": 29
        }
    ]
}
```

* Download a file

```bash
$ curl -XGET localhost:5000/local/date.txt
Tue Aug 30 15:08:29 JST 2016
```

* Get metadata

```bash
$ curl localhost:5000/local/date.txt?meta=yes
{
    "path": "date.txt", 
    "size": 29
}
```
