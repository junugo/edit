![icon](https://github.com/junugo/Nuclear-sports-games-system/raw/master/Non-development%20file/icon.svg)

# 核能运动会操作系统
# Nuclear-sports-games-system

故名思意，是一款非常爆炸的体育运动会管理系统

更多功能正在赶来
- [ ] 数据大屏
- [ ] 答题卡存储读取
- [x] 多端支持
- [ ] 高度自定义配置

---
您可能需要 [**更新日志**](https://github.com/junugo/Nuclear-sports-games-system/blob/master/Non-development%20file/Update%20log.md) [**架构图**](https://github.com/junugo/Nuclear-sports-games-system/blob/master/Non-development%20file/%E6%A0%B8%E8%83%BD%E8%BF%90%E5%8A%A8%E4%BC%9A%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E6%80%BB%E6%9E%B6%E6%9E%84.svg) [~~中英对照表~~](https://github.com/junugo/Nuclear-sports-games-system/blob/master/Non-development%20file/Chinese-english%20enquiry%20form.md)(已并入架构图)

---
## 安装

请确保您已经安装好 **Python 3.9+** 环境，然后执行以下命令（据测试 **3.8 及以下版本不支持部分依赖库** ，另外**请不要使用 32bit-python** ，否则可能需使用预编译库）：
```bash
git clone https://github.com/junugo/Nuclear-sports-games-system.git
cd Nuclear-sports-games-system
pip install -r requirements.txt
```

## 运行
如果您是 **windows 系统** ，您可以直接使用 start.bat 运行 server.py 程序，随后您可以打开 `localhost:80` 访问网页端。

如果您是 **其它系统** ，您可以使用 python 运行 server.py 程序，并访问 `127.0.0.1:80` 打开界面


如果您开启了frp功能，可以在启动后直接打开对应frp网址访问网站

### 请注意
此程序为 **Windows 系统** 设计，如果您使用其它系统，部分附加功能 **可能运作不正常** 。（如 frp 功能）如果您需要使用这些功能，请自行更换对应代码

## 图标解释
~~这个图标是我花了多达5分钟完成的~~

图中为一位奔跑的运动员，手上拿着笔记本电脑与 EXCEL 表格，象征着本系统的数据自动化与表格处理功能。~~（实际是在登分处飞奔的我）~~