# dataWhaleWithBruce
daydayUp with dataWhale

# windows下的git操作方法
1. 注册github帐号，下载github_windows，具体如何配置请自行百度，教程很多。
   并新建仓库(repositories),命名为dataWhaleWithBruce,保存；
2. 在本地文件夹下，鼠标右键，点击git bash,则会出现终端界面；
3. 输入“ mkdir dataWhaleWithBruce”,即“创建了 dataWhaleWithBruce 的文件夹”；
4. 输入“ cd dataW” 再按“Tab”键（即可补全），这样便进入了文件夹；
5. 输入“ git init”,则完成了初始化；
6. 输入“ git add ./”,则完成了本地的添加；
7. 输入“ git commit -m "这是用户自己添加的备注信息，可更改"        ”；
8. 输入“ git pull https://github.com/guanzizai1006/dataWhaleWithBruce.git”，  （后面这段代码，是可以在第一步->新建仓库 的界面，clone or download 那里进行复制粘贴的哦~）
9. 输入“ git push -u origin master”,这样，网页端就可以看到你在自己电脑新建的文件啦~
10.下一次，如何操作呢？
11.在你本地的文件夹“dataWhaleWithBruce”下，写一个代码文件，名字为bruce.py;
12.输入“git add bruce.py”或者输入“git add ./”  ;
13.输入“git commit -m "这是bruce.py的编程笔记哦，嘤嘤嘤"   ”；
14.输入“git pull https://github.com/guanzizai1006/dataWhaleWithBruce.git ”,则完成了本次所写的bruce.py代码的上传任务了。

# ubuntu下的git操作方法
1. 基本配置暂且不表;
2. 本地新建文件夹后“git init”,
   然后“git add ./”,
   然后“git commit -m "备注文件" ”
   然后“git pull https://github.com/guanzizai1006/dataWhaleWithBruce.git ”
   然后“git remote add origin https://github.com/guanzizai1006/dataWhaleWithBruce.git”
   然后“git push -u origin master”
3. 本地新建文件，然后“git add ./”并且“git commit -m "123456" ”并且“ git push -u origin master ”，搞定。
4. git status可以查看当前状态。


# 从云端下载最新版本到本地，然后合并本地项目的方法
1. 输入“ git fetch origin master:temp ”, 表示从远程的origin仓库的master分支下载到本地上所新建的temp分支；
2. 输入“ git diff temp ” 查看temp分支与本地的当前分支的区别
   (可以用git status命令查看当前分支，“git checkout 分支名称”，来切换分支)
3. 输入“ git merge temp ” 则temp分支与本地当前分支可合并，此时本地代码就完成了更新；也可以git branch -d temp 删除此分支；
4. 本地再新建内容后，依旧git add 文件名然后git commit -m "备注"后完成本地的添加；最后 git push -u origin master，完成本地代码的上传工作。


# 往云端添加整个文件夹
1. 注意哦，git此般操作，是对单个文件的大小有限制的，即小于100M，否则会报错；
2. 若直接同步空的文件夹，是没反应的；所以 需要在文件层级里面添加至少一个文件；
3. 输入“ git add 文件夹”
4. 输入“ git commit -m "内容" ”
5. 输入“ git push -u origin master ”，即可把文件夹下所属的文件一并提交~


