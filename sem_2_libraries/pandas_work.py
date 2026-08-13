import numpy as np
import pandas as pd
dict1={
    "name":["Nikhil","ratan","Kedar","Abhay"],
    "marks":[20,34,53,36],
    "city":["Lucknow","Madras","Goa","Delhi"]
}
df=pd.DataFrame(dict1)
print(df)
df.to_csv("friend.csv",index=False)