# networkprojectForcyber
## 一、安装环境（Windows 10）
```cmd
pip install -r requirements.txt
```
将MergeDB文件夹下的movie_total.rar文件解压到app.py的同级目录下
## 二、运行
- 创建数据库（在创建自己的数据库前请先删除我提供的数据库，你也可以跳过创建数据库这一步而使用我提前创建好的数据库）
```cmd
python app.py
```
## 三、文件说明
- static/ --------------JS以及前端渲染文件
- templates/ ------------html界面文件
- MergeDB/ --------------合并各个数据库文件
- app.py ----------------运行Flask框架的脚本
- createdb.py -----------创建数据库的脚本
- dbopt.py ------------一些操作数据库的函数
- spider.py -------------爬取电影数据的爬虫脚本
- doubanMovielinks.xlsx ------------爬取数据用的链接
- movie.db ------------前端展示用的数据库文件
- movie_total.db -----------包含爬取到的10000+条电影数据的数据库文件
- movie.sql --------------创建数据库的sql语句
- requirements.txt ----------------环境依赖
## 四、前端展示说明
**使用两种数据库的原因是部分图表和表格在展示大量数据时会显示效果不佳或出现卡顿现象**
- 折线图、饼状图统计的数据为随机100条电影数据数据库（movie.db）
- 柱状图、词云统计的数据为10000+条电影数据（movie_total.db）
- 前端数据库展示的是随机100条电影数据数据库（movie.db）
- 提交更改操作的是100条电影数据数据库（movie.db）