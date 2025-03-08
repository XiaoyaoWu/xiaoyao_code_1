一、创建仓库：
    1.打开对应文件夹
    2.运行：git init #创建仓库（初始化仓库）
二、跟踪：
    #默认是未被跟踪状态
    1.跟踪文件或者目录：git add （文件名/目录名）
    2.取消跟踪：git rm（文件名/目录名）
    3.保留但不被跟踪：git rm --cached（文件名/目录名）
    4.查看状态：git status
    5.查看修改内容：git diff
    6.设置缓存状态：git add （文件名/目录名）
    7.取消缓存状态：get reset HEAD （文件名/目录名）
    8.提交缓存：git commit -m "提交信息"   // git commit
    9.查看提交记录：git log
    10.取消此次提交：git reset HEAD~ --soft
三、状态：
    1.查看修改内容：git diff
    2.查看修改内容：git show HEAD // git show HEAD~2 // git show // git show commitID
    3.查看提交记录：git log  // git log --all  // git log --graph
    4.美化输出：git log --pretty
    5.每次提交信息变成一行：git log --pretty=oneline
    6.自定义格式：git log --pretty=format:"%h-%an,%ar:%s"
        //%h ：简化哈希值  %an ：提交者  %ar ：提交时间（距今）  %s ：提交信息  %ad：提交时间
    7.图形化呈现：git log --graph
四、远程仓库：
    1.添加远程仓库：git remote add origin 仓库地址
    2.查看远程仓库：git remote
    3.修改远程仓库名字：git remote rename 原仓库名字 新仓库名字
    4.推送到远程仓库：git push origin master
    4.推送到远程仓库：git push origin master -f
    5.推送到远程仓库：git push origin master --force
    6.推送到远程仓库：git push origin master --force-with-lease
    *1.master 为分支名字 2.origin 仓库名字
五、分支：
    1.创建分支：git branch 分支名
    2.切换分支：git checkout 分支名
    3.创建并切换分支：git checkout -b 分支名
    4.删除分支：git branch -d 分支名
    5.查看分支：git branch  // git branch --list
    6.合并分支：git merge 分支名  //需要先切换到要合并的分支
    7.创建远程分支：git push origin 分支名
    8.删除远程分支：gitpush origin :分支名
六、贮藏：
    1.贮藏当前修改内容 ： git stash  // git stash push
    2.恢复贮藏内容：git stash apply
    3.查看修改文件：cat 文件名
    4.查看贮藏记录：git stash list
    5.恢复贮藏内容：git stash apply stash@{编号}
    6.恢复贮藏内容：git checkout -- （文件名） //恢复成没有修改的状态，慎用，所有修改无法找回
    7.恢复最后一次存储：git stash pop  //恢复之后会直接删除
    8.删除其他贮藏：git stash drop stash@{编号}
    *目录不干净，无法恢复
七、重置：
    1.撤销提交：git reset hard~ --soft
    2.撤销暂存：git reset --hard //恢复成没有修改的状态，慎用，所有修改无法找回
    3.变基：git rebase （分支名） //先到分支名，再变基
    4.分支变基：git rebase -i HEAD~3 选择前三次提交的分支进行编辑（修改）
    *hard~ 加~表示上次提交，不加表示当前 ~后面加数字表示倒数第几次
    *soft：只撤销提交，还是暂存的状态，不加表示没有暂存状态
备注：
    仓库文件状态：
        未跟踪：
        未修改：
        已修改：
        暂存：
        git add （文件名）变为暂存状态
        git commit 提交并变为未修改但已跟踪状态
        git rm (文件名) 变为未跟踪状态
        修改文件，变为已修改文件
        git add （文件名） 变为暂存文件
        git commit 提交并变为新的版本

