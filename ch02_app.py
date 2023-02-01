# _*_ coding: utf-8 _*_
import streamlit as st
import pandas as pd

def main():
    data = pd.read_csv('data/iris.csv')
    # print(data)
    st.title('데이터 확인')
    st.dataframe(data.style.highlight_max(axis=0))

    # table() 활용
    st.title('table() 함수 활용')
    st.table(data.head())

    # 샘플코드 보여주기
    mycode = """
    def hello():
        print("Hello World!!")
    end
    """

    st.code(mycode, language='Python')
    
if __name__ == "__main__":
    main()