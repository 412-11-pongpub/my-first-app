import streanlit as st

#ส่วนที่ ๅ หะวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# ;red[🏋️ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่านํ้าหนัก และ ส่วนสูง
weight = st.number_input("กรอกนํ้าหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0

#ส่วนที่ 3 สร้างปุ่มกดคฎนวณ
if st.button("คำนวณค่า BMI 🎯"): 
    # แปลงส่วนสูงจาก cm เป็น เมตร แล้วคำนวณ BMI                            
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    st.write("---")
st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

#ส่วนที่4 4 แปลผลค่า bmi ตามเกณ
