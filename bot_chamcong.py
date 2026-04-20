import asyncio
import schedule
import time
from telegram import Bot

# ============================================================
# CẤU HÌNH BOT
# ============================================================
TOKEN   = "8698625194:AAFhMOFuX0e2EgLbjIKSIQ0XYxubZCaI_w8"
CHAT_ID = "-1001513893466"  # Nhóm: HQPLAY - Thưởng Bước Chân

# ============================================================
# NỘI DUNG TIN NHẮN CHẤM CÔNG
# ============================================================
MSG_SANG = (
    "🎉 8h25 – HỆ THỐNG ĐIỂM DANH ĐANG GỌI TÊN BẠN!\n\n"
    "Nếu bạn đang đọc tin này mà chưa chấm công...\n"
    "👉 thì đây chính là \"dấu hiệu vũ trụ\" 🪄\n\n"
    "Nhanh tay chấm công nào!\n"
    "Không là hệ thống ghi nhận: \"đi làm bằng tâm linh\" đó nha 😄"
)

MSG_CHIEU = (
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
    print(f"[OK] Đã gửi lúc {time.strftime('%H:%M:%S')}: {text[:40]}...")

def send(text: str):
    asyncio.run(_send(text))

# ============================================================
# LỊCH GỬI TIN NHẮN (Thứ 2 - Thứ 6)
# ============================================================
schedule.every().monday.at("08:25").do(send, MSG_SANG)
schedule.every().tuesday.at("08:25").do(send, MSG_SANG)
schedule.every().wednesday.at("08:25").do(send, MSG_SANG)
schedule.every().thursday.at("08:25").do(send, MSG_SANG)
schedule.every().friday.at("08:25").do(send, MSG_SANG)

schedule.every().monday.at("18:00").do(send, MSG_CHIEU)
schedule.every().tuesday.at("18:00").do(send, MSG_CHIEU)
schedule.every().wednesday.at("18:00").do(send, MSG_CHIEU)
schedule.every().thursday.at("18:00").do(send, MSG_CHIEU)
schedule.every().friday.at("18:00").do(send, MSG_CHIEU)

# ============================================================
# CHẠY BOT
# ============================================================
if __name__ == "__main__":
    print("🤖 Bot chấm công đang chạy...")
    print("   📅 Lịch: Thứ 2 - Thứ 6")
    print("   ⏰ Sáng: 08:25 | Chiều: 18:00")
    print("   Nhấn Ctrl+C để dừng.\n")
    while True:
        schedule.run_pending()
        time.sleep(30)
