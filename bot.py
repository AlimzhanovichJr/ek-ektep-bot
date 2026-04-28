"""
🌿 ЭКОМЕКТЕП БОТ
================
Установка:  pip install aiogram
Запуск:     python bot.py
"""

import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ─────────────────────────────────────────────
#  🔑 ТОКЕН (Railway берет из переменной окружения)
# ─────────────────────────────────────────────
TOKEN = os.getenv("TOKEN", "ВСТАВЬ_ТОКЕН_СЮДА")

# ─────────────────────────────────────────────
#  📝 ТЕКСТ ДЛЯ КАЖДОГО РАЗДЕЛА
#  ↓↓↓ МУНда өз мәтіндеріңді жаз ↓↓↓
# ─────────────────────────────────────────────

INFO = {
    "mektep": (
        "🏫 <b>Мектеп үлескісі</b>\n\n"
        "Мұнда мектеп үлескісі туралы ақпаратты жаз.\n\n"
        "Мысалы:\n"
        "• Ауданы: ... шаршы метр\n"
        "• Орналасқан жері: ...\n"
        "• Негізгі мақсаты: ..."
    ),
    "kogal": (
        "🌿 <b>Көгалдандыру</b>\n\n"
        "Мұнда көгалдандыру жобасы туралы ақпаратты жаз.\n\n"
        "Мысалы:\n"
        "• Отырғызылған ағаш саны: ...\n"
        "• Гүл түрлері: ...\n"
        "• Жоба мақсаты: ..."
    ),
    "oranzh": (
        "🌱 <b>Оранжерея</b>\n\n"
        "Мұнда оранжерея туралы ақпаратты жаз.\n\n"
        "Мысалы:\n"
        "• Өсімдіктер саны: ...\n"
        "• Өсімдік түрлері: ...\n"
        "• Күтім жасау тәртібі: ..."
    ),
    "bak": (
        "📰 <b>БАҚ-та жарияланған мақалалар</b>\n\n"
        "Мұнда жарияланған мақалалар туралы ақпаратты жаз.\n\n"
        "Мысалы:\n"
        "• «Egemen Qazaqstan» — ...\n"
        "• «Atameken Business» — ...\n"
        "• Жергілікті газет — ..."
    ),
    "jetis": (
        "🏆 <b>Жетістіктер</b>\n\n"
        "Мұнда жетістіктер туралы ақпаратты жаз.\n\n"
        "Мысалы:\n"
        "• 2024 ж. — Облыстық байқаудың жеңімпазы\n"
        "• 2023 ж. — Республикалық грант иегері\n"
        "• 2023 ж. — «Үздік экомектеп» атағы"
    ),
}

# ─────────────────────────────────────────────
#  Клавиатуры
# ─────────────────────────────────────────────

def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🏫 Мектеп үлескісі",              callback_data="mektep")],
        [InlineKeyboardButton(text="🌿 Көгалдандыру",                  callback_data="kogal")],
        [InlineKeyboardButton(text="🌱 Оранжерея",                     callback_data="oranzh")],
        [InlineKeyboardButton(text="📰 БАҚ-та жарияланған мақалалар", callback_data="bak")],
        [InlineKeyboardButton(text="🏆 Жетістіктер",                   callback_data="jetis")],
    ])

def back_btn() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅️ Негізгі менюге оралу", callback_data="menu")]
    ])

# ─────────────────────────────────────────────
#  Бот
# ─────────────────────────────────────────────

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

WELCOME = (
    "♻️ <b>ЭКОМЕКТЕП БОТ</b>\n\n"
    "🌿 Сәлем! Мені таңдаулы бөлімді басу арқылы танысуға болады.\n\n"
    "📋 <b>НЕГІЗГІ МЕНЮ</b>"
)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(text=WELCOME, reply_markup=main_menu())

@dp.callback_query(lambda c: c.data in INFO)
async def show_section(callback: types.CallbackQuery):
    await callback.message.edit_text(
        text=INFO[callback.data],
        reply_markup=back_btn()
    )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "menu")
async def go_back(callback: types.CallbackQuery):
    await callback.message.edit_text(text=WELCOME, reply_markup=main_menu())
    await callback.answer()

# ─────────────────────────────────────────────
#  Запуск
# ─────────────────────────────────────────────

async def main():
    print("✅ ЭКОМЕКТЕП БОТ іске қосылды!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
