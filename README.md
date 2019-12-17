# greenAllGithubPush
每天使GitHub上传记录变绿，下次朋友圈秀年终报告好看点    
<hr/>    

## 使用方法
很简单的哦    
* 在github将[本项目](https://github.com/lsc183754539/greenAll)fork到自己的存储库中(以阿里云9.8每月的ubuntu操作系统的ECS为例)
* 记得开放服务器的防火墙的端口
* <code>sudo apt install git</code>
* <code>git config --global user.name "写入自己的GitHub用户名"</code>
* <code>git config --global user.email "写入自己的GitHub注册邮箱"</code>
* <code>git config --global credential.helper store</code> //使下次登录时使用的GitHub账号密码永久保存，不再重复输入
* <code>git clone https://github.com/lsc183754539/greenAll.git</code>
* 在shell中执行`python3 项目路径/greenall.py`输入用户名及密码登录(如有错误请将错误提示提交Issues或fork修改归并)
* 记录clone后的项目地址，安装[Phpstudy For Linux](https://www.xp.cn/linux.html) 如Ubuntu：<code>wget -O install.sh https://download.xp.cn/install.sh && sudo bash install.sh</code>
* 安装完成后使用<code>xp</code>命令启动phpstudy面板，会提示管理地址
* 访问面板管理地址，登陆后选择`计划任务>Shell脚本>每天>python3 项目路径/greenall.py`
* 查看是否生效，有问题请提交Issues.
