# 分布式计算作业

## 作业要求：使用Diango，并仿照百度盘，编写一个具有秒传功能的云盘系统。

## 作业完成过程

## 主要问题和解决方法：
#  问题1：在git克隆仓库时，没有访问权限

解决方法:使用ssh-keygen命令生成密钥，将生成的公钥文件 id_ras.pub内容拷贝e值到服务器端ssh公钥

#  问题2：在github建立好仓库之后，本地也新增了ssh key，同时也在本地新增了远程仓库， 但是在git push的时候出现错误 The authenticity of host 'github.com (192.30.255.113)' can't be established.

解决方法：直接回车的话会出现验证失败
Host key verification failed.
fatal: Could not read from remote repository.
百度后得知原来是本地少了 know_host文件，只要在刚刚那个位置输入yes就可以了，而不是回车。

#  问题3：在转入建好的本地仓库时，因为仓库名以-开头 使用cd语句无法转入

解决方法：百度学习后得知可以用cd /.-xxxxxxxx转入，转入成功





## 作业结果展示
