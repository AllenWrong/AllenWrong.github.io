---
title: "常用的git操作"
excerpt: "以列表的形式列出了常用的git命令，方便以后的查阅和使用"
mathjax: false
tags: "新文章在写"
---

- 配置git
  全局配置git
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "email@example.com"
  ```
  查看配置信息
  ```bash
  git config --list
  ```

- git克隆仓库
  ```bash
  git clone xxx
  ```

- 查看仓库的当前状态
  ```bash
  git status
  ```

- 追踪新文件
  ```bash
  git add newfile
  ```

- 暂存已修改的文件
  ```bash
  git add modifiedfile
  ```
  是的，git add命令既可以用于追踪新文件，又可以将暂存已经修改的文件。或者可以这么理解，git add的命令就是将文件暂存，如果文件和暂存状态的文件没有差异，那么git add就不会有任何影响。

- 查看具体修改了什么地方
  ```bash
  git diff
  ```
  这个操作只能查看当前文件和暂存文件中的差异，而不能查看暂存文件和上次提交的文件的差异。若查看暂存文件和上次提交的文件的差异，则用--staged参数或--cached参数
  ```bash
  git diff --staged
  ```

- 提交更新
  ```bash
  git commit -m "massge"
  ```
  使用-m参数可以编辑比较短的提交信息，如果提交信息比较长，则直接输入`git commit`并执行就可以缓解编辑器进行编辑提交信息。

- 一次性提交现在追踪过的文件的变动
  ```bash
  git commit -a -m "add all modified"
  ```

- 移除文件
  从文件暂存区移除并从当前工作目录中移除
  ```bash
  git rm file
  ```
  从文件暂存区移除，但不从当前工作目录中移除
  ```bash
  git rm --cached file
  ```

- 移动文件
  ```bash
  git mv src_file dest_file
  ```

- 查看提交历史
  ```bash
  git log
  ```
  查看历史的时候也要查看每次做的变动
  ```bash
  git log -p
  ```
  控制每次查看的历史的条数为3
  ```bash
  git log -3
  ```
  看出历史的统计信息，比如修改的文件数，行数
  ```bash
  git log --stat
  ```
  以一行的形式显示每次提交
  ```bash
  git log --pretty=oneline
  ```
  查看每次提交的简写信息并以图形的方式显示出来
  ```bash
  git log --pretty=format:"%h %s" --graph
  ```

- 覆盖上一次的提交
  上一次的提交除了问题，或者是忘记添加文件了，或者是提交信息写错了，但我们又不想重新提交一次，导致历史信息冗余杂乱，这时候可以使用下面这个命令来解决，它可以将本次的提交和上次的提交合并。
  ```bash
  git commit --amend
  ```

- 取消暂存的文件
  错误的将文件进行暂存后，可以使用下面的命令进行取消
  ```bash
  git reset HEAD file
  ```

- 撤销对文件的修改
  如果对当前的修改不满意，想将文件撤销成上次commit的样子。【危险命令，一旦执行，本地的修改彻底消失】
  ```bash
  git checkout -- file
  ```


**参考**
- <a href="https://github.com/datawhalechina/faster-git/tree/main">faster-git</a>