import streamlit as st

st.title('This is a title')
st.title('_Streamlit_ is :blue[cool] :sunglasses:')

# st.header(boby, anchor=None, *,help=None)
st.header("이것은 헤더입니다")
st.header("_이텔릭체 헤더_:red[빨강색]그리고 선글라스 이모지:sunglasses:")

url = "https//docs.streamlit.io/library/api.reference/text/st.header"

#anchor가 있는경우
st.header("이것은헤더입니다",
        anchor=url,
        help="anchor 존재")

#anchor가 none인 경우
st.header("이것은 헤더입니다", anchor=None)

# st.subheader(body, anchor=None, *, help=None)
st.subheader("이것은 서브헤더입니다", help="서브헤더에 대한 설명")
