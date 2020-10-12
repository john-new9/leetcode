Git Bash 进行代码管理

**第一件事设置用户**。

给你的电脑设置一个用户，等你上传的时候，告诉远程仓库是谁上传的而已。

```
git config --global user.name "Your Name"
git config --global user.email "email@example.com"
```

远程仓库托管代码：本地+远程仓库

## 1. 新建远程仓库

打开github右上角，点击new repository

![img](https://img-blog.csdnimg.cn/20200425221100741.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70)

## 2. 建立连接

### 2.1 配置SSH

[配置SSH](https://blog.csdn.net/qq_36667170/article/details/79094257)

## 2.2 SSH连接

根据SSH连接的地址，可以进行下载与连接

![img](https://img-blog.csdnimg.cn/20200425223427978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM2NjY3MTcw,size_16,color_FFFFFF,t_70)

在本地仓库打开git bash。
`$ git remote add + 名字 + 连接地址`

连接地址就是你刚才复制的那块。

`$ git remote -v`

下图所示，已经建立好了连接，名称为origin。 fetch与push 成对存在。

![image-20200828001717125](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200828001717125.png)

## 2.3 文件上传

### 2.3.1 添加文件到暂存区

**git add** 将**修改的文件**添加暂存区，也就是将要提交的文件的信息添加到索引库中。
什么是修改的文件，你新建、更改、删除文件都是修改。
git add有好多种。

- `$ git add +文件名.文件类型` ，将某个文件加到缓存区
- `$ git add +文件名.文件类型 ... 文件名.文件类型` ，将n个文件添加到缓存区
- `$ git add xx文件夹/*.html`，将xx文件夹下的所有的html文件添加到缓存区。
- `$ git add *hhh` ，将以hhh结尾的文件的所有修改添加到暂存区
- `$ git add Hello*` ，将所有以Hello开头的文件的修改添加到暂存区
- `git add -u` ，提交被修改(modified)和被删除(deleted)文件，不包括新文件(new)
- `git add .`，提交新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件
- …
- **`git add -A`**，提交**所有变化**。git add前几条都可以记不住，这个必须记住！！！

**git commit**命令将索引的当前内容与描述更改的用户和日志消息一起存储在新的提交中。

`$ git commit -m "修改注释"`

### 2.3.2 推进远程仓库

向一个空的新仓库中推文件：`$ git push -u 仓库名称 分支`

- 仓库名称：刚才添加连接的时候仓库名称：origin
- 分支：主分支：master。以后合作项目的时候，成员之间建了不同的分支，就可以往自己的分支上推。

![img](https://img-blog.csdnimg.cn/2020042523273249.png)



## 2.4 使用visual studio code进行远程管理

以下操作建立在前面已经将本地仓库与远程仓库连接成功的基础上。

- 查看是否有仓库连接，是否可以进行源代码管理

### ![image-20200828002749890](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200828002749890.png)

- 提交更改

![image-20200828002929295](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200828002929295.png)

- 增加commit
- push到远程仓库

![image-20200828003039066](C:\Users\BU\AppData\Roaming\Typora\typora-user-images\image-20200828003039066.png)

## 2.4 文件克隆

如果仓库是自己的，可以使用SSH连接；如果他人仓库：切换到HTTPS，再复制地址。
`$ git clone 加上你刚才的地址`

