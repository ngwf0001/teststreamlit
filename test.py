import time
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

st.title('this is a test')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

fig = df.plot(kind='bar', x='first column', y='second column').get_figure()
st.pyplot(fig)

fig = sns.pairplot(data=df)
st.pyplot(fig)



st.line_chart(df)

map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
    columns=['lat', 'lon'])
st.map(map_data)

if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
        columns=['lat', 'lon'])
    st.map(map_data)



option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option

left_column, right_column = st.columns(2)
left_column.write("這是左邊欄位。")
right_column.write("這是右邊欄位。")