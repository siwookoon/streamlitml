# _*_ coding: utf-8 _*_

import streamlit as st
import utils
import pandas as pd                 # 데이터 가공
import matplotlib.pyplot as plt     # static 시각화
import seaborn as sns               # static 시각화
import plotly.express as px         # dynamic 시각화

def run_eda_app():
    # print('Hello World')
    st.title('Hello World')

    # 코드 작성
    with st.expander('데이터셋 정보'):
        st.markdown(utils.attrib_info)

    # 데이터셋 불러오기
    iris_df = pd.read_csv('data/iris.csv')
    st.write(iris_df.head())

    # 사이드바 만들기
    submenu_lists = ['기술통계량', '그래프']
    submenu = st.sidebar.selectbox('EDA 메뉴', submenu_lists)

    if submenu == '기술통계량':
        st.subheader('데이터 통계량을 배우자')
        st.dataframe(iris_df)

        with st.expander('Data Types'):
            result = pd.DataFrame(iris_df.dtypes).transpose()
            result.index = ['구분']
            st.dataframe(result)

        with st.expander('기술 통계량'):
            result = pd.DataFrame(iris_df.describe()).transpose()
            st.dataframe(result)

        with st.expander('타겟분포'):
            st.dataframe(iris_df['species'].value_counts())

    elif submenu == '그래프':
        st.subheader('시각화를 그리자')

        with st.expander('산점도'):
            # ploty 그래프
            fig1 = px.scatter(iris_df, x = 'sepal_width', y = 'sepal_length', color = 'species',
            size = 'petal_width', hover_data=['petal_length'], title = '산점도')

            st.plotly_chart(fig1)

        # 새로운 layout
        col1, col2 = st.columns(2)
        with col1:
            with st.expander('박스플롯 with seaborn'):
                
                # seaborn 그래프
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax=ax)
                st.pyplot(fig)

        with col2:
            with st.expander('히스토그램 with Matplotlib'):
                # Color Picker
                color = st.color_picker('색상 선택')
                # matplotlib 그래프
                fig, ax = plt.subplots()
                ax.hist(iris_df['sepal_length'], color = color)
                st.pyplot(fig)

        tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])
        with tab1:
            one = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
            submenu = st.selectbox('종 선택', one)
            st.dataframe(iris_df[iris_df['species']== submenu])
            # plotly 시각화 코드를 작성한다. color 파라미터는 제외
            fig1 = px.scatter(iris_df[iris_df['species']== submenu], x = 'sepal_width', y = 'sepal_length',
            size = 'petal_width', hover_data=['petal_length'], title = '산점도')

            st.plotly_chart(fig1)

        
        with tab2:
            pass

    else:
        pass