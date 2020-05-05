# Python编程学习环境配置

## 1、工具

工具安装中，都可以选用默认选项，一直点击下一步下一步即可。

+ pycharm下载安装：https://www.jetbrains.com/pycharm/download/#section=windows
+ python下载安装：https://www.python.org/
+ Mysql下载安装（一般使用5.7.30版本）：https://dev.mysql.com/downloads/mysql/
+ git下载安装：https://git-scm.com/download/win；如果下载很慢，可以通过阿里云镜像等下载。

## 2、步骤

主要是链接pycharm、python、git三个软件，使得写的代码可以通过github云端实现多台电脑同步。

> 步骤一：https://blog.csdn.net/MattenLi/article/details/86287474
>
> **1、首次安装使用git，先配置用户名称和邮箱：**打开Git bash，输入
>
> `git config --global user.name "姓名"`
> `git config --global user.email "邮箱地址"`
> **2、检查是否有ssh目录及对应的key：**进入C盘>当前用户>用户文件夹。在该目录下查看是否有 .ssh文件夹
>
> 若没有该目录，则手动生成密钥：打开Git Bash 输入
>
> `ssh-keygen -t rsa -C "你的邮箱地址"`
> **3.查看对应的ssh-key：**执行上述命令之后，可看到.ssh文件，里面包含两个文件
>
> 使用noteapp++等软件打开文件：id_rsa.pub
>
> 将内容全部复制：ssh-rsa  xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
>
> **4.将SSH-key配置到github中：**
> 登录进入github网址：https://github.com/login
>
> 进入个人中心--setting
>
> 进入SSH and GPG keys，点击New SSH key
>
> 将复制的ssh-rsa粘贴到Key中，Title（我填的是邮箱地址）
>
> 添加成功页面
>