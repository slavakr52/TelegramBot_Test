import random

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_help = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_contact = KeyboardButton('Кто я?', request_contact=True)
btn_location = KeyboardButton('Где я?', request_location=True)

kb_menu.add(btn_help)
kb_help.add(btn_start, btn_contact, btn_location)
