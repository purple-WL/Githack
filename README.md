# Githack
.git信息泄露漏洞检测

不会去解析sha1值，直接下载文件

工作流程：
解析.git/index文件➡️爬取解析的结果➡️保存本地

使用方法很简单：
python Githack1.py http://xxx.com

效果：

<img width="839" alt="image" src="https://user-images.githubusercontent.com/63894044/189291569-aee7e2b0-11d6-45d4-9f90-74aece4e0668.png">


<img width="262" alt="image" src="https://user-images.githubusercontent.com/63894044/189290974-b5178a3b-8325-415c-b158-9c4809723655.png">


