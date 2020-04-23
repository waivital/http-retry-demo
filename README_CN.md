# HTTP 重连演示

复线当 http 过早关闭后，浏览器会自动重试当前请求

- [English](README.md)

## 介绍

根据 [rfc2616 section 8.2.4](https://tools.ietf.org/html/rfc2616#section-8.2.4) 中所描述的

> If an HTTP/1.1 client sends a request which includes a request body, but which does not include an Expect request-header field with the "100-continue" expectation, and if the client is not directly connected to an HTTP/1.1 origin server, and if the client sees the connection close before receiving any status from the server, the client SHOULD retry the request.

如果我们的服务运行在一个代理或者负载均衡的后面，当服务因为错误或者相应时间过长，在没发出任何消息前 http 链接被关闭后，就会导致浏览器重新发起这次请求，这样重复的请求，就有可能导致业务被重复执行一遍。

## 运行

```bash
# clone this repo
git clone https://github.com/waivital/http-retry-demo.git

cd ./http-retry-demo

# start all containers
docker-compose -p http-retry-demo up
```

启动完毕后服务器会默认监听在 `8080` 端口

在浏览器打开链接 http://localhost:8080，然后点击 `send request` 按钮，等待请求结束

在文件 `./sharedfile` 中就可以看到两条记录，来自不同的 host，有一样的 requid

```
[Tue May  7 03:05:59 2019] Hello there -- hostname:258f4c03429b requid:5802516b94b4f
[Tue May  7 03:06:01 2019] Hello there -- hostname:81074f0d03d1 requid:5802516b94b4f
```

## References

- [Beware of HTTP Request Automatic Retries](https://blogs.oracle.com/ravello/beware-http-requests-automatic-retries)
- [HTTP/1.1 - 8.2.4 Client Behavior if Server Prematurely Closes Connection](https://tools.ietf.org/html/rfc2616#section-8.2.4)
