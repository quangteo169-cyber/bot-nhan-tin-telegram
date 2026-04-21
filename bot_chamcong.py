import asyncio
import schedule
import time
import requests
from telegram import Bot

# ============================================================
# CẤU HÌNH BOT
# ============================================================
TOKEN          = "8698625194:AAFhMOFuX0e2EgLbjIKSIQ0XYxubZCaI_w8"
CHAT_ID        = "-1001513893466"  # Nhóm: HQPLAY - Thưởng Bước Chân
GEMINI_API_KEY = "AIzaSyDR5SsEyWUHvYAi-ZBCBUVZL4mUGuw_oRU"
GEMINI_URL     = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# ============================================================
# TẠO LỜI NHẮC BẰNG GEMINI AI
# ============================================================
def generate_message(ca: str) -> str:
    if ca == "sang":
        prompt = (
            "Viết 1 tin nhắn nhắc nhân viên công ty chấm công VÀO CA lúc 8h25 sáng. "
            "Phong cách: vui vẻ, hài hước, dí dỏm, có emoji. "
            "Độ dài: 4-6 dòng. "
            "Không dùng tiêu đề, không dùng markdown. "
            "Mỗi ngày phải khác nhau, sáng tạo, đừng lặp lại. "
            "Viết bằng tiếng Việt."
        )
    else:
        prompt = (
            "Viết 1 tin nhắn nhắc nhân viên công ty chấm công RA CA lúc 18h00 chiều. "
            "Phong cách: vui vẻ, hài hước, dí dỏm, có emoji. "
            "Độ dài: 4-6 dòng. "
            "Không dùng tiêu đề, không dùng markdown. "
            "Mỗi ngày phải khác nhau, sáng tạo, đừng lặp lại. "
            "Viết bằng tiếng Việt."
        )

    try:
        response = requests.post(
            GEMINI_URL,
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=15
        )
        data = response.json()
        text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
        return text
    except Exception as e:
        print(f"[Gemini Error] {e}")
        # Fallback nếu API lỗi
        if ca == "sang":
            return (
                "🎉 8h25 – HỆ THỐNG ĐIỂM DANH ĐANG GỌI TÊN BẠN!\n\n"
                "Nếu bạn đang đọc tin này mà chưa chấm công...\n"
                "👉 thì đây chính là \"dấu hiệu vũ trụ\" 🪄\n\n"
                "Nhanh tay chấm công nào!\n"
                "Không là hệ thống ghi nhận: \"đi làm bằng tâm linh\" đó nha 😄"
            )
        else:
            return (
                "🔔 18h00 – MISSION HOÀN THÀNH?\n\n"
                "Trước khi off và hoà vào dòng đời 🏃\n"
                "👉 nhớ chấm công ra về nha!\n\n"
                "Chỉ mất 3 giây thôi,\n"
                "nhưng giúp bạn tránh drama \"quên chấm công\" ngày mai đó 🙂"
            )

# ============================================================
# HÀM GỬI TIN NHẮN
# ============================================================
async def _send(text: str):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=text)
    print(f"[OK] Đã gửi lúc {time.strftime('%H:%M:%S')}: {text[:50]}...")

def send_ca(ca: str):
    text = generate_message(ca)
    asyncio.run(_send(text))

# ============================================================
# LỊCH GỬI TIN NHẮN (UTC = giờ VN - 7)
# 08:25 VN = 01:25 UTC | 18:00 VN = 11:00 UTC
# ============================================================
for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    getattr(schedule.every(), day).at("01:25").do(send_ca, "sang")
    getattr(schedule.every(), day).at("11:00").do(send_ca, "chieu")

# ============================================================
# CHẠY BOT
# ============================================================
if __name__ == "__main__":
    print("🤖 Bot chấm công AI đang chạy...")
    print("   📅 Lịch: Thứ 2 - Thứ 6")
    print("   ⏰ Sáng: 08:25 | Chiều: 18:00 (giờ Việt Nam)")
    print("   🤖 Lời nhắc tự động thay đổi mỗi ngày bởi Gemini AI")
    print("   Nhấn Ctrl+C để dừng.\n")
    while True:
        schedule.run_pending()
        time.sleep(30)
