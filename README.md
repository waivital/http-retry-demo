# HTTP Retry Demo

To reproduce the http retry behavior after connection prematurely closed

- [简体中文](README_CN.md)

## Introduction

As [rfc2616 section 8.2.4](https://tools.ietf.org/html/rfc2616#section-8.2.4) mentioned

> If an HTTP/1.1 client sends a request which includes a request body, but which does not include an Expect request-header field with the "100-continue" expectation, and if the client is not directly connected to an HTTP/1.1 origin server, and if the client sees the connection close before receiving any status from the server, the client SHOULD retry the request.

If our service runs behind a proxy or a load balancer, and a client's request is close before receiving any data from the service - due to an error or the response time is too long, it will cause the browser to resend this request, and duplicate request may be generated.

## Run it

```bash
# clone this repo
git clone https://github.com/waivital/http-retry-demo.git

cd ./http-retry-demo

# start all containers
docker-compose -p http-retry-demo up
```

The server will default listen on port `8080`

Open http://localhost:8080 in the browser (test on Chrome and Firefox) and hit the `send request` button, wait until the request complete

And in the `./sharedfile` will be two records with same requid from different host
```
[Tue May  7 03:05:59 2019] Hello there -- hostname:258f4c03429b requid:5802516b94b4f
[Tue May  7 03:06:01 2019] Hello there -- hostname:81074f0d03d1 requid:5802516b94b4f
```

## References

- [Beware of HTTP Request Automatic Retries](https://blogs.oracle.com/ravello/beware-http-requests-automatic-retries)
- [HTTP/1.1 - 8.2.4 Client Behavior if Server Prematurely Closes Connection](https://tools.ietf.org/html/rfc2616#section-8.2.4)
