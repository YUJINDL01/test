import streamlit as st #  import 해서 시작 
# local URL
# 서버 중단 : CTRL + C

st.title("춘식이와 분홍 악어")
st.header("매이저와 마이너")
st.subheader("수치로 비교해보는 인기도!")

# # 파일 실행시킬 떄 가상환경이 존재하는 경로에서 찾음 
# # 1. 실행하려는 명령어 쓸 떄 추가 경로까지 작성 
# # 2. 아니면 파일을 해당 경로에 맞게 이동
#     # cd = ChangeDirectory 폴더명

my_favor = st.text_input("당신이 더 좋아하는 캐릭터는?")    
st.write(my_favor)

if st.button(f"{my_favor} 보러가기"): # true or false 의 상태로 남게 됨
     st.success(f"{my_favor} 기다리는 중 ❤️❤️❤️", icon="💕")
