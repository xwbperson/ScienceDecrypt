# - 
[科学文库（ScienceReading）](https://book.sciencereading.cn/shop/main/Login/shopFrame.do)自动化下载解密工具

使用说明：
- information.xls文件是科学文库网站所有的书籍目录（截止到2023年3月28日）
- Python脚本中使用了MySQL 8.0版本数据库，建议安装MySQL 8.0和Navicat 16 for MySQL（可视化数据库管理工具），连接到默认数据库后创建“科学文库”数据库，导入information.xls，生成一个表，重命名为information，也可以更改代码在xls文件中检索，但是效率不高
- decrypt.py来源与GitHub的另一个仓库[ScienceDecrypting](https://github.com/skq1998/ScienceDecrypting)，ScienceDecrypting.exe是打包好的解密工具，带有GUI界面，来自已经删除的GitHub项目，可以选择文件进行解密
- Download.py中的FilePath是下载的书籍要保存的路径，记得改成自己的，并注意路径中“\”要替换成“\\”或者“/”
- 本工具唯一有点儿意义的代码就是伪造IP进行书籍下载，IP可以替换为各大高校或机构的IP，可以在通过CARSI登录科学文库的界面找到支持的高校或机构，通过ping域名的方式找到IP地址填入即可
