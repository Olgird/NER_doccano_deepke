# NER_doccano_deepke
Named entity extraction(命名实体抽取),通常会用到doccano平台，有时训练模型会用到deepke，这个代码功能是将doccano导出的jsonl数据直接转换成deepke中ner所用的数据



## 1. 文件说明

- example.jsonl 文件为doccano做命名实体抽取导出的jsonl文件
- doccano2deepke.py 为主要的代码文件
- doccano2deepke.ipynb 需要运行的文件，你可以直接打开运行
- 程序会导出json 文件到json文件夹
- 程序对导出txt文件（deepke ner 所需文件）到txt文件夹



## 2. notebook文件操作

### 1. 打开doccano2deepke.ipynb

![image-20231113144633767](https://github.com/Olgird/NER_doccano_deepke/blob/main/image/image-20231113144633767.png)

### 2. 填写jsonl_path 和 ratio

jsonl_path 为 导出的jsonl 文件路径

ratio 为 训练集、测试集、验证集比例

![image-20231113144912504](https://github.com/Olgird/NER_doccano_deepke/blob/main/image/image-20231113144912504.png)

### 3. 运行doccano2deepke.ipynb，查看结果

结果会在json文件夹中输出json文件

![image-20231113145008452](https://github.com/Olgird/NER_doccano_deepke/blob/main/image/image-20231113145008452.png)

在txt文件夹中输出txt文件

![image-20231113145134883](https://github.com/Olgird/NER_doccano_deepke/blob/main/image/image-20231113145134883.png)

txt文件的数据集为deepke ner中所需数据
