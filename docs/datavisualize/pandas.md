# Pandas

## 导入Excel

```
pd.read_excel(io,sheet_name,header)
```

常用参数说明:

* io:表示,xs或 xsx文件路径或类文件对象
* sheet_name: 表示工作表，取值如下表所示
* header默认值为0，取第一工行的值为列名，数据为除列名以外的数据，如果数据不包含列名，则设置header=None

| 值 | 说明 |
| --- | --- |
| sheet_name=0 | 第一个Sheet页中的数据作为DataFrame对象 |
| sheet_name=1 | 第二个Sheet页中的数据作为DataFrame对象 |
| sheet_name='Sheet1' | 名称为'Sheet1'的Sheet页中的数据作为DataFrame对象 |
| sheet_name =[0, 1, 'Sheet3'] | 第一个、第二个和名称为Sheet3的Sheet页中的数据作为DataFrame对象 |
| sheet_name=None | 读取所有工作表 |

```
import pandas as pd

pd.set_option('display.unicode.east_asian_width', True) # 自适应合适的宽度
df = pd.read_excel('./data/daily_work_report_q3.xlsx', sheet_name='Sheet1', usecols=[1])  # 导入一列数据
print(df)
df = pd.read_excel('./data/daily_work_report_q3.xlsx', sheet_name='Sheet1', usecols=['姓名', '总成绩'])  # 导入多列数据
print(df)
df = pd.read_excel('./data/daily_work_report_q3.xlsx', 0, 3) # 导入第一个Sheet，将第4行作为列名
```

## 导入CSV文件

```
pd.read_csv(filepath_or_buffer, sep=',', header, encoding=None)
```

常用参数说明

* filepath_or_buffer：字符串、文件路径，也可以是URL链接
* sep:字符串、分隔符
* header：指定作为列名的行，默认值为0，即取第一行的值为列名。数据为除列名以外的数据，若数据不包含列表，则设置header=None
* encoding：宇符串，默认值为None，文件的编码格式

## 导入txt文件

```
pd.read_csv(filepath_or_buffer,sep='\t', header,encoding=None)
```

## 导入HTML网页

只能导入网页中含有table标签的数据

```
pd.read_html(io, match='.+', flavor,header,encoding)
```

参数说明：

* io:字符串、文件路径，可以是URL链接，网址不接受https
* match:正则表达式
* flavor:解释器默认为'lxml'
* header:指定列栐題所在的行
* encoding: 文件的編砢格式

示例代码：

```
# 导入HTML
import pandas as pd
url = 'http://www.espn.com/nba/salaries/_/year/2023/seasontype/4'
df = pd.DataFrame()  # 创建一个空的DataFrame对象
# DataFrame添加数据
df = df.append(pd.read_html(url, header=0))
print(df)
# 保存成csv文件
df.to_csv('nbasalary.csv', index=False)  # index=False设置不保存默认的索引
```

## 数据抽取

DataFrame対象的loc属性与iloc属性

* loc属性  
    以列名(columns)和行名(index)作力参数.  当只有一个参数时，默认是行名，即抽取整行数据，包括所有列。  
* iloc属性  
    以行和列位置索引（即：0,1,2,...） 作参数，0表示第一行，1表示第2行，以此类推。当只有一个参数时，默认是行索引，即抽取整行数据，包括所有列。  

示例代码：

```
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
data = [[46, 29, 29], [50, 100, 78], [63, 87, 93]]
index = ['章三', '李四', '王五']
columns = ['数学', '语文', '外语']
df = pd.DataFrame(data=data, index=index, columns=columns)
print(df)
print('--------------------------------')
# 提取行数据
print(df.loc['章三'])  # 使用行索引名称
print(df.loc[['章三', '王五']])
print('--------------------------------')
print(df.iloc[[0, 2]])
print('--------------------------------')
print(df.loc['章三':'王五'])  # 使用切片，从章三到王五，包含王五

print(df.iloc[0:2])  # 使用行索引序号的时候包含开头不包含结尾，不包含王五
print('--------------------------------')
# iloc[start:end:step]
print(df.iloc[1::])  # 从1开始到最后一个，步长为1
print(df.iloc[::2])  # 从0开始到最后一个，步长为2

```

