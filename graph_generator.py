import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
df = pd.read_csv(r"./game_record_output.csv")

### 三分
df1 = df.iloc[0:, [0, 4, 5]]
df2 = df1["三分"].str.split("-", expand = True)
df1["命中"] = df2[0]
df1["出手"] = df2[1]

x = df1["日期"] # 日期
y1 = df1["命中"] # 命中
y2 = df1["出手"] # 出手
y3 = df1["%.1"] / 100 # 命中率

myfont = FontProperties(fname = r"./NotoSansTC-Black.otf")

plt.plot(x, y1, "-")
plt.plot(x, y2, "-")
# 設定標頭和字體
plt.title('三分隨著賽事進展出手數和命中數的趨勢', fontproperties=myfont, fontsize = 12)
# 設定 x 軸標頭和字體
plt.xlabel('日期', fontproperties=myfont, fontsize = 12)
# 設定 y 軸標頭和字體
plt.ylabel('數量', fontproperties=myfont, fontsize = 12)
# 設定右上角說明圖示字體
plt.legend(["命中數", "出手數"], prop = myfont, fontsize = 12)
plt.xticks(rotation=90)
plt.yticks(range(0, 50, 5))
plt.savefig('三分_命中數與出手數_by_date')
plt.clf()

plt.plot(x, y3, "-")
# 設定標頭和字體
plt.title('三分隨著賽事進展命中率的趨勢', fontproperties=myfont, fontsize = 12)
# 設定 x 軸標頭和字體
plt.xlabel('日期', fontproperties=myfont, fontsize = 12)
# 設定 y 軸標頭和字體
plt.ylabel('命中率', fontproperties=myfont, fontsize = 12)
# 設定右上角說明圖示字體
plt.legend(["命中率"], prop = myfont, fontsize = 12)
plt.xticks(rotation=90)
plt.savefig('三分_命中率_by_date')
plt.clf()

### 二分
df1 = df.iloc[0:, [0, 2, 3]]
df2 = df1["二分"].str.split("-", expand = True)
df1["命中"] = df2[0]
df1["出手"] = df2[1]

x = df1["日期"] # 日期
y1 = df1["命中"] # 命中
y2 = df1["出手"] # 出手
y3 = df1["%"] / 100 # 命中率

myfont = FontProperties(fname = r"./NotoSansTC-Black.otf")

plt.plot(x, y1, "-")
plt.plot(x, y2, "-")
# 設定標頭和字體
plt.title('二分隨著賽事進展出手數和命中數的趨勢', fontproperties=myfont, fontsize = 12)
# 設定 x 軸標頭和字體
plt.xlabel('日期', fontproperties=myfont, fontsize = 12)
# 設定 y 軸標頭和字體
plt.ylabel('數量', fontproperties=myfont, fontsize = 12)
# 設定右上角說明圖示字體
plt.legend(["命中數", "出手數"], prop = myfont, fontsize = 12)
plt.xticks(rotation=90)
plt.yticks(range(0, 45, 5))
plt.savefig('二分_命中數與出手數_by_date')
plt.clf()

plt.plot(x, y3, "-")
# 設定標頭和字體
plt.title('二分隨著賽事進展命中率的趨勢', fontproperties=myfont, fontsize = 12)
# 設定 x 軸標頭和字體
plt.xlabel('日期', fontproperties=myfont, fontsize = 12)
# 設定 y 軸標頭和字體
plt.ylabel('命中率', fontproperties=myfont, fontsize = 12)
# 設定右上角說明圖示字體
plt.legend(["命中率"], prop = myfont, fontsize = 12)
plt.xticks(rotation=90)
plt.savefig('二分_命中率_by_date')
plt.clf()
