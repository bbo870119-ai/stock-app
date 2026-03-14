import streamlit as st
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

st.title("행님의 주가 예측 시스템")

ticker = st.text_input("종목 코드를 입력하세요 (예: 005930)", "005930")

if st.button("분석 시작"):
    df = fdr.DataReader(ticker, "2026-01-01")
    st.write(f"### {ticker} 종목 데이터")
    st.line_chart(df['Close']) # 그래프를 아주 쉽게 그려줍니다
    st.dataframe(df.tail())    # 최근 데이터 표 보기


    