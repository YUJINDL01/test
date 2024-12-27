import streamlit as st
import pandas as pd

# pandas # 데이터 프레임 

st.title("춘식이와 분홍 악어")
# 데이터 프레임(표 형태로 데이터가 들어간다.)을 하나 그려서 보여지게 할 것 이다.

st.write(" ")

data = pd.DataFrame({
    "캐릭터" : ["춘식이", "분홍 악어", "춘봉이", "라이언", "와니야마상", "초코비공룡"], 
    "선택횟수" : [120, 12, 30, 90, 9, 20],
    "인지도 (%)" : [95, 2, 4, 90, 5, 80],
    "선호도 (%)" : [90, 7, 80, 90, 15, 20],
    "인기도 (%)" : [55, 2, 10, 30, 1, 2]
    })

st.dataframe(data, use_container_width=True) # 수정 못 함 # 화면의 너비에 맞게 늘려줌

col1, col2, col3 = st.columns(3)

with col1:

    #edited_data = st.data_editor(data) # 데이터 수정할 수 있게 
    #st.write(edited_data)


    # chart element
    st.bar_chart(data.set_index("캐릭터")["선택횟수"] ) # 캐릭터라고 하는 걸 인덱스 . 선택 획수를 값으로 해서 그림 그림

with col2:
    
    st.line_chart(data.set_index("캐릭터")["인지도 (%)"])


with col3:

    colors = ['#E91E63', '#F44336', '#D32F2F', '#FFC107', '#FF9800', '#FFEB3B']
    
    # 설치가 안되어 있는 것 
    fig = data.plot.pie(
        y = "인기도 (%)", # 열이 될 것 
        labels = data["캐릭터"], # 그릴 떄 붙일 이름(인덱스와 유사)
        autopct = "%0.0f%%", # 그래프 비율의 형식을 어떻게 보여줄 지,이건 소수점 첫번째 자리까지
        figsize = (6, 6), # 크기, 6 * 6 사이즈즈
        color=colors,
        legend = True, # 범례 
        title = "캐릭터 별 인기도" # 제목
    ).get_figure()

    st.pyplot(fig)