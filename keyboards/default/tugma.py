from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uz = ReplyKeyboardMarkup(

	keyboard = [
		[
			KeyboardButton(text="O'zbek tili"),
			KeyboardButton(text="Menu⬅️"),
		],
	],
	resize_keyboard=True
)

ar = ReplyKeyboardMarkup(

	keyboard = [
		[
			KeyboardButton(text="Arab tili"),
			KeyboardButton(text="Menu⬅️"),
		],
	],
	resize_keyboard=True
)


menu = ReplyKeyboardMarkup(

	keyboard = [
		[
			KeyboardButton(text="Arab tili"),
			KeyboardButton(text="O'zbek tili"),
		],
	],
	resize_keyboard=True
)


