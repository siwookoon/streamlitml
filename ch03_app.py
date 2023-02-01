# _*_ coding: utf-8 _*_
# 라이브러리 불러오기 
import streamlit as st

def main():
    
    name = 'siwoo'

    if st.button('Submit'):
        st.write(f'name: {name.upper()}')

    status = st.radio('Status', ('활성화', '비활성화'))

    if status == '활성화':
        st.success('활성화 상태')
    else:
        st.error('비활성화 상태')

    # 체크박스
    if st.checkbox('Show/Hide'):
        st.text('보여주세요!')

    with st.expander('Python'):
        st.text('Hello Python')
        st.text('고로롱')
        st.text('몰?루')
        st.text('냐항~')

if __name__ == "__main__":
    main()