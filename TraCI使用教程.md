# TraCI使用教程

2019-07-01 17:27:32

 

Liuss2

 

阅读数 156

更多

分类专栏： [sumo使用教程](https://blog.csdn.net/liuss2/article/category/9049791)





版权声明：本文为博主原创文章，遵循[ CC 4.0 BY-SA ](http://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。

本文链接：<https://blog.csdn.net/Liuss2/article/details/94399285>

## **1. 什么是****TraCI**

TraCI是"Traffic Control Interface"的缩写，是sumo给出的连接到交通仿真的一个接口，使得人们可以获取仿真中的参数还有实时控制仿真。Traci使用基于TCP的客户端/服务器体系结构，将SUMO作为服务器，python脚本是客户端。

## 2. **TraCI 交通灯实例**

这个实例时sumo给出的教程，代码可以在安装的sumo文件夹下的/ docs / tutorial / traci_tls目录中找到，如果找不到也可以留下邮箱，我发给你。

（1）示例描述

有一个十字交叉路口如下图，在南北方向放上环路传感器，它的控制逻辑是当南北方向有车通过时，东西方向切换为红灯，南北方向切换为绿灯，否则，保持东西绿灯，南北红灯。

![img](https://img-blog.csdnimg.cn/20190702084303584.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0xpdXNzMg==,size_16,color_FFFFFF,t_70)

（2）代码流程

- 在脚本中导入traci

```python
import os, sys



 



 if 'SUMO_HOME' in os.environ:



 



     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')



 



     sys.path.append(tools)



 



 else:  



 



     sys.exit("please declare environment variable 'SUMO_HOME'")
```

注意：一定要将SUMO_HOME加入环境变量中

- 将python脚本与sumo接口连接

可以选择使用sumo，还是sumo-gui进行仿真

sumoBinary = checkBinary('sumo-gui') # 出现图像界面，

sumoBinary = checkBinary('sumo')

使用命令行

```python
traci.start([sumoBinary, "-c", "data/cross.sumocfg",



 



                             "--tripinfo-output", "tripinfo.xml"])
```

- 执行仿真步骤   

- ```python
  traci.simulationStep()
  ```

   

- 关闭连接

```python
traci.close（）
```