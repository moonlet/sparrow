#!/user/bin/env python
# -*- encoding:utf-8 -*-
import sparrowlet

fd_manager = sparrowlet.FdManager()


class Svr(sparrowlet.TcpServer):

    def on_receive(self, fd):
        fd_manager.send(fd, "hello world!")

    def on_send(self, fd):
        fd_manager.remove(fd)


if __name__ == '__main__':
    port = 8888
    timeout = 10
    tasklet_num = 10
    svr = Svr(port, timeout, tasklet_num)
    # 可以带参数0来自适应开启多进程, 也可以指定进程数
    svr.run(0)
