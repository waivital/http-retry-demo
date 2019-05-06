# Http Prematurely Closed Retry Test

重现当 http 过早关闭后，浏览器会自动重试当前请求

- [English](README.md)

## 运行

```bash
# clone this repo
git clone https://github.com/waivital/http-prematurely-closed-retry.git

cd ./http-prematurely-closed-retry

# start all containers
docker-compose -p http-prematurely-closed-retry up
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
- [HTTP/1.1 - 8.2.4 Client Behavior if Server Prematurely Closes Connection](https://www.w3.org/Protocols/rfc2616/rfc2616-sec8.html)
