import re
import pandas as pd

#读取本地的html文件
path=r"./cbd.html"
fp = open(path,'rb')
html = fp.read().decode('utf-8')

#对html进行解析
#([\s\S]*使用正则提取所有的字符串，？表示使用使用非贪婪模式
goodslist=re.findall(r'<span class="fooddetails-nameText_250s_">([\s\S]*?)</span>',html)
#-?\d+\.?\d*e?-?\d*？提取所有的数字，包括小数
# currentpricelist=re.findall(r'￥</span>(-?\d+\.?\d*e?-?\d*?)</div>',html)
text=re.sub('\s+'," ",html)
description=re.findall(r'<p class="fooddetails-desc_3tvBJ">([\s\S]*?)</p>',text)
# description=re.sub('\s+'," ",description)
print(description)
#将list转为datafarme
goods=pd.DataFrame(goodslist)
descriptions=pd.DataFrame(description)
#横向拼接
result=pd.concat([goods,descriptions],axis=1)
#更改dataframe列名称
result.columns=['商品名','描述信息']
#保存文件
result.to_excel(r"./result.xlsx",index=None)