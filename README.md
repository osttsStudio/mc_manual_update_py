# 基于python3的mc客户端手动更新v0.0.2

## 关于项目

[自动更新版本](https://github.com/osttsStudio/mc-clientup-py)

## 使用环境

python3 windows 理论上支持linux<br>

## 使用须知

非盈利开源软件 可二次修改 如果可以 请尽量在修改后的软件中署名原作者osttsStudio<br>

## 关于功能

简单粗暴的手动更新，程序会下载服务器配置文件并和本地配置文件进行比对,如果版本号不等于本地文件，会自动下载更新包并解压覆盖，然后删除本地的服务器配置文件和zip（需要下载源码修改url然后封包）

## 如何编译

#### 关于封包

pyinstaller -F mc_manual_update_py.py

pyinstaller -F -i xxx.ico mc_manual_update_py.py 封包图标

### 直接使用

因为需要修改url和部分变量 请下载源码自行封包

## 如何使用

如果有python3和相关库，可不封包直接运行py文件，修改批处理文件

## TODO

- [x] 

## 更新日志

[更新日志](./CHANGELOG.md)

