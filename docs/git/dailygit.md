git tag -d v2016062101 删除本地tag

git push origin --delete tag v2016062101 删除远程tag

git branch -r 查看所有远程分支

拉取远程分支并创建本地分支   
方法一：  
git checkout -b 本地分支名x origin/远程分支名x  
方法二：  
git fetch origin 远程分支名x:本地分支名x


## git如何删除远程tag？

分为两步:

1. 删除本地tag
```
git tag -d tag-name
```

2. 删除远程tag
```
git push origin :refs/tags/tag-name
```

# git maintenance start

git maintenance start，用于自动启动 Git 仓库的后台维护任务。这个命令会在你的系统上安排定期的 Git 维护任务，这些任务包括：

    清理：Git的垃圾收集器会清理那些不再需要的文件和对象，以减少仓库的大小；   
    压缩：Git会重新打包你的对象。这个过程会将多个小文件合并成一个大文件，从而提高Git的性能；   
    修复：如果Git仓库出现了问题，Git会检查和修复它。   

如果你想要停止后台的维护任务，你可以运行 git maintenance stop 命令。这对于代码仓库很大的场景非常有用！试一试吧。

如下待验证：

```
Git maintenance命令的基本用法
git maintenance命令提供了一种灵活的方式来优化Git仓库。通过指定不同的子命令，可以运行一个或多个维护任务。如果指定了--task选项，则按指定的顺序运行这些任务；如果没有指定，则根据maintenance.<task>.enabled配置选项来确定要运行的任务。默认情况下，只有maintenance.gc.enabled配置为true的任务会被运行‌1。

Git maintenance命令的子命令
‌gc‌：运行垃圾收集器，清理未使用的对象和松散的对象。
‌prune‌：删除远程跟踪分支和标签，这些分支和标签不再存在于远程仓库中。
‌fsck‌：检查仓库的完整性和一致性。
‌repack‌：重新打包仓库的对象，以减少磁盘空间占用并提高性能。
‌filter-branch‌：重新写历史，例如删除敏感信息或重写提交历史。
‌filter-repo‌：使用BFG Repo-Cleaner工具清理大型仓库。
启用和维护Git maintenance的步骤
‌启用维护任务‌：可以通过配置文件设置哪些维护任务在每次提交时自动运行。例如，将maintenance.gc.enabled设置为true，以便在每次提交时运行垃圾收集器。
‌手动运行维护任务‌：使用git maintenance start命令并指定要运行的子命令，例如git maintenance start gc prune fsck。
‌定期运行维护任务‌：可以通过cron作业或其他调度工具定期运行维护任务，以确保仓库保持最佳状态。
通过合理使用和维护Git maintenance命令和子命令，可以显著提升Git仓库的性能和稳定性，减少因仓库过大而导致的性能问题。
```