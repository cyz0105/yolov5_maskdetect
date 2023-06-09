# 《基于计算机视觉的口罩佩戴巡检小车设计与实现》

数据集在[我的repositories里](https://github.com/cyz0105/mask_dataset.git)

## 部署教程

### 一、树莓派刷入官方系统
[树莓派刷机教程](https://blog.csdn.net/xiaozhoukong/article/details/112726366 '树莓派刷机教程') 
### 二、链接 ssh，准备环境

1. 开启树莓派 ssh 功能
   在 SD 卡中烧录好 Raspbian 系统之后，在内存卡的根目录创建一个名为 ssh 的空文件夹

2. 创建虚拟环境

```shell
python3 -m venv /home/pi/yolovenv
```

2. 启动虚拟环境

```shell
source bin/activate
```

3. 克隆代码

```shell
git clone https://github.com/cyz0105/yolov5_maskdetect.git
```

4. 安装必要的依赖

```shell
pip3 install -r requirements.txt
```

### 三、启动代码

```shell
python3 detect.py
```
