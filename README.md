# threadx-platform
threadx ,just learn it!

scons脚本源自rt-thread ，https://github.com/RT-Thread/rt-thread
1 采用scons方式编译threadx代码，支持生成keil 工程
2 git clone下来代码，需要更新一下threadx子模块
3 示例工程在 bsp\Nuvoton\NUC029 中。
4 想要玩转 scons方式 有rt-thread的env环境使用基础的 很快就能上手。
	进入工程目录，设置环境变量
		export TX_ROOT	= E:\tx-workspace
		export TX_CC 	= keil
		
		然后 scons一下，就可以编译了
		
		scons --target=mdk5 -s,直接生成 keil工程 免去自己添加文件。省时省力，欧耶。
		
5 比较懒，不想多说，拜拜		