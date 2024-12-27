import streamlit as st

st.title("사용자 정보")
st.subheader("모든 정보는 확인용으로만 사용됩니다.")

col1, col2 = st.columns(2)


with col1:

    # 공정하게 할 것을 동의 
    justice = st.checkbox("공정하게 투표에 임할 것 입니다."
                        )
    nickname = st.text_input("사용할 닉네임을 입력하세요")
    age = st.number_input("나이를 입력하세요", min_value=8, max_value=80)

    # 둘 중 더 선호하는 캐릭터는 
    options = ["없음","춘식이", "분홍악어"]
    selected = st.radio("둘 중 선호하는 캐릭터는?", options)

    if selected == "춘식이":
        st.success(f"{selected}를 좋아해줘서 고마워. 냐옹", icon="😻")
        
    elif selected == "분홍악어":
        st.success(f"{selected}를 좋아해줘서 고맙다! 크아악", icon="💢")

    # 그 이유는?
    reasons = ["귀여움", "예쁨", "잘생김", "못생김","화남", "매이저", "마이너"]
    choice = st.selectbox("가장 큰 이유 선택", reasons)
    selected_many = st.multiselect("해당 캐릭터를 좋아하는데 해당되는 이유를 모두 선택해주세요.", reasons)
    # 좋아하는 다른 캐릭터들
    checked = st.checkbox("개인정보 제공 동의")


with col2:

    if st.button("정보 입력 완료!"):
        st.write(f"닉네임: {nickname}")
        st.write(f"나이: {age}")
        st.write(f"선호하는 캐릭터: {selected}")
        st.write(f"가장 큰 이유: {choice}")
        st.write(f"모든 이유: {', '.join(selected_many)}")
        st.write(f"개인 정보 제공 동의: {"동의" if checked else "미동의"}")
        st.button("이대로 제출하시겠습니까?")