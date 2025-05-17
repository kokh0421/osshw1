import streamlit as st

st.title("오픈소스소프트웨어")

st.subheader("1. 광운대학교는 어느 구에 위치해 있을까요?")
firstanswer = st.radio(
    "객관식 보기:",
    ("노원구", "성동구", "서초구", "동대문구")
)

st.subheader("2. 소가 단체로 노래를 하면?")
secondanswer = st.text_input("답변을 입력하세요:")

if st.button("제출하기"):
    firstright = firstanswer == "노원구"
    secondright = secondanswer.strip().lower() == "집단소송"
    
    if firstright:
        st.success("1번 정답입니다!")
    else:
        st.error("1번 오답입니다. 정답은 노원구 입니다.")
    
    if secondright:
        st.success("2번 정답입니다!")
    else:
        st.error("2번 오답입니다. 정답은 집단소송 입니다.")
