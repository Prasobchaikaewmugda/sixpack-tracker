import streamlit as st
import pandas as pd
import os
from datetime import date

# --- 1. ปฏิทินสมอง AI (ตารางเวร มี.ค. 69) ---
shift_schedule = {
    1: 'เช้า', 2: 'ดึก', 3: 'ออฟ (พัก)', 4: 'บ่าย', 5: 'บ่าย',
    6: 'บ่าย', 7: 'เช้า', 8: 'ดึก', 9: 'ออฟ (พัก)', 10: 'ออฟ (พัก)',
    11: 'บ่าย', 12: 'เช้า', 13: 'ดึกควบบ่าย', 14: 'เช้า', 15: 'ดึก',
    16: 'ดึก', 17: 'ออฟ (พัก)', 18: 'บ่าย', 19: 'เช้า', 20: 'ดึก',
    21: 'ดึก', 22: 'ดึกควบบ่าย', 23: 'เช้า', 24: 'ดึก', 25: 'ดึก',
    26: 'ออฟ (พัก)', 27: 'บ่าย', 28: 'เช้า', 29: 'ดึก', 30: 'ดึก', 31: 'ออฟ (พัก)'
}

# --- 2. ระบบเทรนเนอร์ส่วนตัว (คิดแผนตามเวร) ---
def get_trainer_advice(shift):
    if 'ออฟ' in shift:
        return "🌟 วันหยุด! จัดเต็มได้เลย นอนให้พอ ตื่นมาทำ IF เป๊ะๆ ลุยวิ่ง 30 นาที + คลิป 9 นาที และอย่าลืมแวะเรียน AI/English ด้วยนะ!"
    elif 'เช้า' in shift and 'ควบ' not in shift:
        return "☀️ เวรเช้า: พกไข่ต้มกล้วยต้มไปกินตอนพักเที่ยง เลิกงานแล้วค่อยมาลุยวิ่ง 30 นาที + คลิป 9 นาที!"
    elif 'บ่าย' in shift and 'ควบ' not in shift:
        return "🌤️ เวรบ่าย: ตื่นเช้ามาเคลียร์วิ่ง 30 นาที + คลิป 9 นาทีให้จบ! เริ่ม IF สายๆ เลิกเวรดึกจะได้นอนเลย"
    elif 'ดึก' in shift and 'ควบ' not in shift:
        return "🌙 เวรดึก: โหมดเอาตัวรอด! เน้นนอนตุนแรง ถ้าไหวจัดแค่คลิป 9 นาทีพอ (งดวิ่งหนัก) และกินกล้วยต้มคุมหิวรอบดึก"
    elif 'ควบ' in shift:
        return "🚨 โหมดพระเจ้า! (เวรดึกต่อบ่าย): ร่างกายสำคัญสุด! อนุญาตให้หลุด IF ได้ถ้ารู้สึกหวิว ห้ามออกกำลังกายหนัก เน้นงีบและกินไข่ต้มเอาแรง!"
    else:
        return "💪 พร้อมลุยเสมอ! อย่าลืมฟังสัญญาณร่างกายตัวเองนะ"
    
# --- ตั้งค่าหน้าตาเว็บ ---
st.title("🔥 Six-Pack Tracker รับสงกรานต์")
st.write("ยินดีต้อนรับ CEO ติดลม ชมสวน สู่เส้นทางปั้นหุ่น!")
st.divider()

# --- ส่วนที่ 1: รับข้อมูลจากคุณ ---
st.header("📝 บันทึกภารกิจวันนี้")
today = st.date_input("เลือกวันที่เข้าเวร/ทำภารกิจ", value=date(2026, 3, 1))

current_month = today.month
current_year = today.year
current_day = today.day

if current_month == 3 and current_year == 2026:
    today_shift = shift_schedule.get(current_day, "ไม่ทราบตาราง")
    st.info(f"📅 ตารางของคุณวันนี้: **เวร{today_shift}**")
    
    advice = get_trainer_advice(today_shift)
    st.warning(f"💡 **Trainer แนะนำ:** {advice}")
else:
    st.info("📅 (ระบบเทรนเนอร์รองรับเฉพาะการเลือกวันที่ในเดือน มีนาคม 2569 ครับ)")

st.divider()

col1, col2 = st.columns(2)
with col1:
    start_time = st.time_input("เวลาเริ่มกินมื้อแรก (Break Fast)")
with col2:
    end_time = st.time_input("เวลาหยุดกิน (Start Fasting)")

# --- 🌟 ไฮไลท์การแก้ไข: เพิ่มการภารกิจที่เสริม ---
st.header("🥚 ภารกิจเสริม")
egg = st.checkbox("กินไข่ต้มแล้ว ✅")
banana = st.checkbox("กินกล้วยน้ำว้าห่ามต้มเย็นแล้ว ✅")

# --- 🌟 ไฮไลท์การแก้ไข: เพิ่มการภารกิจที่หลัก ---
st.header("📖 ภารกิจหลัก")
learn_eng = st.checkbox("เรียนEnglish ✅")
learn_Ai = st.checkbox("เรียน AI ✅")
sleep_time = st.checkbox("นอนตรงเวลาไม่เกิน 1ชม.")

# --- 🌟 ไฮไลท์การแก้ไข: แยกภารกิจออกกำลังกาย ---
st.header("💪 ภารกิจปั้นหน้าท้อง")
run_30m = st.checkbox("🏃‍♂️ วิ่ง 30 นาที สำเร็จ! ✅")
clip_9m = st.checkbox("💦 ทำตามคลิป 9 นาที สำเร็จ! ✅")

# --- ส่วนที่ 2: ระบบความจำ (บันทึกข้อมูลลงไฟล์) ---
st.divider()
if st.button("💾 บันทึกความสำเร็จวันนี้!"):
    # --- 🌟 อัปเดตกล่องพัสดุ ให้มีช่องใส่ข้อมูลเพิ่ม ---
    new_data = pd.DataFrame({
        "วันที่": [today],
        "เริ่มกิน": [start_time],
        "หยุดกิน": [end_time],
        "ไข่ต้ม": [egg],
        "กล้วยต้ม": [banana],
        "เรียนEnglsihr": [learn_eng],
        "เรียน AI": [learn_Ai],
        "นอน" : [sleep_time],
        "วิ่ง 30 นาที": [run_30m],
        "คลิป 9 นาที": [clip_9m]
    })
    
    file_name = "sixpack_data.csv"
    if os.path.exists(file_name):
        new_data.to_csv(file_name, mode='a', header=False, index=False)
    else:
        new_data.to_csv(file_name, index=False)
        
    st.success("บันทึกข้อมูลเรียบร้อย! วินัยเหล็กสุดๆ พักผ่อนให้เต็มที่นะ!")
    st.balloons()

# --- ส่วนที่ 3: โชว์ตารางประวัติย้อนหลัง ---
st.header("📊 ตารางสรุปความถึกทน")
if os.path.exists("sixpack_data.csv"):
    history = pd.read_csv("sixpack_data.csv")
    st.dataframe(history)
    

    


