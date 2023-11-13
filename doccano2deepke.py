import json
import random


# 把doccano导出的jsonl 数据转换成 deepke的json数据
def doccano_data2deepke_data(data):
    output = []
    for d in data:
        e = {"sentence":d['text'],"entities":[]}

        for en in d['entities']:
            
            e["entities"].append({"word":d['text'][int(en["start_offset"]):int(en['end_offset'])],"label":en["label"]})

        output.append(e)

    return output

# deepke 给的转换代码
def json2txt(fp_json, fp_txt):
  """
    Standard NER. 
    .json -> .txt
  """
  
  with open(fp_json, encoding='utf-8') as f1:
    lines = json.load(f1)
    symbol = []
    for line in lines:
      sentence = line.get('sentence')
      labels = ['O'] * len(sentence)
      entities = line.get('entities')

      for entity in entities:
        word = entity.get('word')
        label = entity.get('label')

        idx = sentence.find(word)
        if sentence[idx : idx + len(word)] == word:
          
          labels[idx] = 'B-' + label
          for i in range(idx + 1 , idx + len(word)):
            labels[i] = 'I-' + label
          
      symbol.append(labels)
    
    with open(fp_txt, 'w', encoding='utf-8') as f2:
      for idx in range(len(lines)):
        for i in range(len(lines[idx].get('sentence'))):
          
          f2.write(lines[idx].get('sentence')[i] + ' ' + symbol[idx][i] + '\n')
        if idx != len(lines) - 1:
          f2.write('\n')

def ner_doccano2deepke(jsonl_path : str, ratio = [0.8,0.1,0.1]):
    """
    jsonl_path : doccano jsonl文件的路径
    ratio : 训练集、 验证集、测试集 比例
    """
    train_ratio = ratio[0]
    valid_ratio = ratio[1]
    test_ratio = ratio[2]

    # 读取 jsonl的数据
    doccano_data = []
    with open(jsonl_path, 'r') as file:
        for line in file:
            doccano_data.append(json.loads(line))

    file.close()

    # 划分数据集

    # 随机化数据
    random.shuffle(doccano_data)

    # 计算各个集合的样本数量
    train_size = int(len(doccano_data) * train_ratio)
    valid_size = int(len(doccano_data) * valid_ratio)

    # 切分数据集
    train_data = doccano_data[:train_size]
    valid_data = doccano_data[train_size:train_size + valid_size]
    test_data = doccano_data[train_size + valid_size:]

    # 打印划分后的样本数量
    print("训练集样本数量：", len(train_data))
    print("验证集样本数量：", len(valid_data))
    print("测试集样本数量：", len(test_data))

    # 转换，把数据集写进json文件夹中
    json_train_data = doccano_data2deepke_data(train_data)
    json_valid_data = doccano_data2deepke_data(valid_data)
    json_test_data = doccano_data2deepke_data(test_data)


    with open('json/train.json', 'w',encoding='utf-8') as json_file:
        json.dump(json_train_data , json_file,ensure_ascii=False)

    with open('json/valid.json', 'w',encoding='utf-8') as json_file:
        json.dump(json_valid_data , json_file,ensure_ascii=False)

    with open('json/test.json', 'w',encoding='utf-8') as json_file:
        json.dump(json_test_data , json_file,ensure_ascii=False)


    # 写入文件，把数据集写进txt文件夹中
    json2txt("json/train.json", "txt/train.txt")
    json2txt("json/valid.json", "txt/valid.txt")
    json2txt("json/test.json", "txt/test.txt")