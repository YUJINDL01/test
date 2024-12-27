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

# 히히 일부러 수정 사항 만들기!
print("히히 일부러 수정사항 만들기")
# 수정사항 
print("깃헙아 못 잡니?")
# 다시 수정 사항 만들기 
# 내가 느끼기엔 아까 이미 add, commit 된 상태여서 그런 듯 
# 그래서 내 pc 에서는 병경 사항이 없는데 pu노 하지 않아서 main 에서는 보이지 않았던 거지!
print("가설 증명")
print("실패??")
# 다른 위치를 보고 있었던 것 같음!
print("아닌가?")
