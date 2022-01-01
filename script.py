from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} 

I am Telegram Most Powerful Galaxy Bot

I can Mux Any Srt or Txt File in File or Video

Use Help Command to Know How to Use me

Made With ❤️‍🔥 POWERED BY : @Filmy_Hangama
#TFH
"""
    HELP_TEXT = """
Recommended
➠ Use Hardmux If You Have More Time

Recommended
➠ Use Softmux To add Subtitle Fastly in It

Softmux
➠ Send /softmux to add Subtitle Softly in it

HardMux
➠ Send /hardmux to add Subtitle hardly in it 

Made With ❤️‍🔥 POWERED BY : @Filmy_Hangama
#TFH
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Galaxy\n
 **👲 Developer :** [FHKL_Team](https://telegram.me/FHKL_Team)\n
 **👥 Channel :** [Filmy Hangama](https://telegram.me/Filmy_Hangama)\n
 **❄️ Credits :** Everyone in this journey\n
 **🍴 Source :** [Click here](https://github.com/LionKetty)\n
 **📝 Language :** [Python3](https://python.org)\n
 **📚 Library :** [Pyrogram v1.2.0](https://pyrogram.org)\n
 **🌟 Server :** [Heroku](https://heroku.com)\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/Filmy_Hangama'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/LegendsRequest')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
