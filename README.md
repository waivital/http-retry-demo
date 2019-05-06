# Http Prematurely Closed Retry Test

To demonstrate the http retry behavior when prematurely closed

- [简体中文](README_CN.md)

## Run it

```bash
# clone this repo
git clone https://github.com/waivital/http-prematurely-closed-retry.git

cd ./http-prematurely-closed-retry

# start all containers
docker-compose -p http-prematurely-closed-retry up
```

the server will default listen on port `8080`

open http://localhost:8080 in the browser (test on Chrome and Firefox) and hit the `send request` button, wait until the request complete

in the `./sharedfile` will be two records with same requid from different host
```
[Tue May  7 03:05:59 2019] Hello there -- hostname:258f4c03429b requid:5802516b94b4f
[Tue May  7 03:06:01 2019] Hello there -- hostname:81074f0d03d1 requid:5802516b94b4f
```

## References

- [Beware of HTTP Request Automatic Retries](https://blogs.oracle.com/ravello/beware-http-requests-automatic-retries)
- [HTTP/1.1 - 8.2.4 Client Behavior if Server Prematurely Closes Connection](https://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html)
