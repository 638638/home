import pandas as pd 
from pyreadstat import pyreadstat
#绘图设置
plt.rcparams["font.sans-ser"]=["simHei"] #设置字体

#读取spss格式数据
def 读取spss数据(文件所在位置):
  result,metadata = pyreadstat.read_sav(文件所在位置名词,
  apply_value_formats=Ture,formats_as_ordered_category=Ture)
  return result,metadata
 
 国家认同原始数据,meta= mytools.读取spss数据(R'identity.sav')
df, metadata = pyreadstat.read_sav(r'identity.sav')
apply_value_formats=False,
formats_as_ordered_category=Ture
return result,metadata

def 有序变量描述统计函数(表名,变量名):
  result = 表名[变量名].value_counts(sort=False)
  描述统计表=pd.DataFrame(result)
  描述统计表['比例']= 描述统计表['count']/ 描述统计表['count'].sum()
  描述统计表['累计比例']= 描述统计表['比例'] .cumsum() 
  return 描述统计表

def  数据变值描述统计(数据表,变量名):
  result = 数据表[变量名].describe()
  中位数 = result['median']
  平均值 = result['mean']
  标准差 = result['std']
  return 数据表[变量名].describe()

import pandas as pd
from scipy import stats

import pandas as pd
from scipy import stats

def 单变量参数估计(file_path, confidence_level): 
 file_path = R"movie_data_cleaned.csv"
df_movies = pd.read_csv(file_path)
# 计算均值和标准误差
mean = df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 0.95
# 设定自由度
自由度 = len(df_movies['average']) - 1
# 计算置信区间
confidence_interval = stats.t.interval(confidence_level, 自由度, loc=mean, scale=std_error)
# 输出结果
print(F"均值：{mean: .2f}")
print(F"均值在置信水平{confidence_level}下的置信区间为：", confidence_interval)


#绘图设置
plt.rcParams["font.sans-serif"] = ["SimHei"] # 设置字体

def 计算单变量均值的置信区间(数据表路径及文件名,变量名,置信水平=0.95):
""" 计算指定数据表中数值变量的均值及在指定置信水平下的置信区间 """

# 打开数据文件
file_path = 数据表路径及文件名
df = pd.read_csv(file_path)
# 计算均值和标准误差
mean-df_movies['average'].mean()
std_error = stats.sem(df_movies['average'])
# 设定置信水平
confidence_level = 置信水平
#  设定自由度
自由度=len(df_movies['average'])-1
# 计算置信区间
confidence_interval=stats.t.interval(
    confidence_level, 自由度, loc=mean, scale=std_error)
# 输出结果
print(F"均值：(mean: .2f)")
 
def 制定交叉表(数据表,自变量,因变量):
   return pd.crosstab(数据表[自变量], 数据表[因变量], nor)