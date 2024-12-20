import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("sub", CMD))
async def sub(_, message):
    await message.reply_text("**🕸️ <a href=https://subdl.com><b>موقع تحميل الترجمة</b></a>\n\n🖥 <a href=https://telegra.ph/برامج-عرض-الترجمة-04-24><b>برامج المشاهدة [اندرويد ايفون كمبيوتر]</b></a>\n\n➕<a href=https://adjacent-sheila-kathryn-abdallam01-bd7953ed.koyeb.app/watch/109070/subdl.mp4?hash=AgADzB><b>شرح اضافة الترجمة</b></a>\n\n<a href=t.me/subtitles_downloader_bot><b>💬 بوت تحميل الترجمة</b></a>\n\n<a href=t.me/subtitle_translate_bot><b>👾 بوت يترجم لأي لغة مفيد عند عدم وجود ترجمة عربي <u>ارسل ملف الترجمة الإنجليزي</u></b></a>**")

@Client.on_message(filters.command("help", CMD))
async def help(_, message):
    await message.reply_text("**<b>📌 𝗔𝗿𝗮𝗯𝗶𝗰\n• اضغط /Series لطريقة البحث عن <u>مسلسل</u> 📃\n• اضغط /Movie لطريقة البحث عن <u>فيلم</u> 📃\n\n📌 𝗘𝗻𝗴𝗹𝗶𝘀𝗵\n• 𝖧𝗂𝗍 /eSeries 𝖥𝗈𝗋 𝖲𝖾𝗋𝗂𝖾𝗌 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n• 𝖧𝗂𝗍 /eMovie 𝖥𝗈𝗋 𝖬𝗈𝗏𝗂𝖾 𝖲𝖾𝖺𝗋𝖼𝗁 𝖱𝗎𝗅𝖾𝗌 📃\n\n   ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n• اضغط /Sub  لشرح اضافة وتحميل الترجمة 🎯</b>**")

@Client.on_message(filters.command("eseries", CMD))
async def eseries(_, message):
    await message.reply_text("**⚠️❗️ 𝗦𝗲𝗿𝗶𝗲𝘀 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n🗣 𝖲𝖾𝗋𝗂𝖾𝗌 𝖭𝖺𝗆𝖾,𝖲𝖾𝖺𝗌𝗈𝗇 (𝖶𝗁𝗂𝖼𝗁 𝖲𝖾𝖺𝗌𝗈𝗇 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍) 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞: \n\n• Game Of Thrones S03 720𝗉✅\n• Dark S02E03✅ \n• Breaking Bad S01E05 1080p✅ \n• Prison Break 1080p x265✅ \n• Witcher S02E01 x264✅\n\n🥱 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 𝖬𝖾𝗇𝗍𝗂𝗈𝗇 𝖠𝗌 𝖲01 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 1, 𝖲02 𝖥𝗈𝗋 𝖲𝖾𝖺𝗌𝗈𝗇 2 𝖾𝗍𝖼 [𝖲03,𝖲04 ,𝖲06,𝖲10,𝖲17] 𝖦𝗈𝖾𝗌 𝖫𝗂𝗄𝖾 𝖳𝗁𝖺𝗍\n\n🔎 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 𝖬𝖾𝗇𝗍𝗂𝗈𝗇 𝖠𝗌 𝖤01 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 1, 𝖤02 𝖥𝗈𝗋 𝖤𝗉𝗂𝗌𝗈𝖽𝖾 2 𝖾𝗍𝖼 [𝖤03,𝖤07,𝖤17,𝖤21] 𝖦𝗈'𝗌 𝖫𝗂𝗄𝖾 𝖳𝗁𝖺𝗍 \n\n❌ [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗦𝗲𝗮𝘀𝗼𝗻/𝗘𝗽𝗶𝘀𝗼𝗱𝗲/𝗦𝗲𝗿𝗶𝗲𝘀 , . : - 𝗲𝘁𝗰] ❌**")

@Client.on_message(filters.command("emovie", CMD))
async def emovie(_, message):
    await message.reply_text("**⚠️❗️ 𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗾𝘂𝗲𝘀𝘁 𝗙𝗼𝗿𝗺𝗮𝘁 ❗️⚠️\n\n📝 𝖬𝗈𝗏𝗂𝖾 𝖭𝖺𝗆𝖾, 𝖸𝖾𝖺𝗋,(𝖨𝖿 𝗒𝗈𝗎 𝖪𝗇𝗈𝗐) 𝖶𝗂𝗍𝗁 𝖢𝗈𝗋𝗋𝖾𝖼𝗍 𝖲𝗉𝖾𝗅𝗅𝗂𝗇𝗀 📚\n\n🗣 𝖨𝖿 𝖨𝗍 𝗂𝗌 𝖺 𝖥𝗂𝗅𝗆 𝖲𝖾𝗋𝗂𝖾𝗌. 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖮𝗇𝖾 𝖡𝗒 𝖮𝗇𝖾 𝖶𝗂𝗍𝗁 𝖯𝗋𝗈𝗉𝖾𝗋 𝖭𝖺𝗆𝖾 🧠\n\n🖇𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\n\n• The Godfather 1972✅\n• John Wick 2023✅\n• Her 2013✅\n• Harry Potter 2005\n• ✅ Harry Potter 2001✅ \n\n❌ [𝗗𝗼𝗻𝘁 𝗨𝘀𝗲 𝘄𝗼𝗿𝗱𝘀 𝗟𝗶𝗸𝗲 𝗗𝘂𝗯𝗯𝗲𝗱/𝗠𝗼𝘃𝗶𝗲𝘀/𝗦𝗲𝗻𝗱/𝗛𝗗 , . : - 𝗲𝘁𝗰] ❌**")

@Client.on_message(filters.command("movie", CMD))
async def movie(_, message):
    await message.reply_text("**<b>⚠️❗ تـنـسـيق الـبـحــث عـن فـيـلـم❗️⚠️</b>\n\n📝 اسم الفيلم , التاريخ\n<u>تــأكد من الاسم والتاريخ بالذهاب الي جوجل وانسخ الاسم الصحيح</u>\nلمعرفة اجزاء الفيلم استخدم الامر /Search بعدها اسم الفيلم\n\n🖇<b>مــثــال📚</b>:\n\n• The Godfather 1972✅\n• John Wick 2023✅\n• Her 2013✅ \n• Harry Potter 2005✅\n• Harry Potter 2001✅\n\n❌ لا تستخدم الرموز في البحث *:-.& ❌**")
    
@Client.on_message(filters.command("series", CMD))
async def series(_, message):
    await message.reply_text("**<b>⚠️❗️ تـنـسـيق الـبـحــث عـن مسلسل ❗️⚠️</b>\n\n<b><u>للبحث العادي</u></b>\n📝 اسم المسلسل والموسم (الموسم الذي تريده)\n\n<b><u>للبحث المتقدم</u></b>\n📝 اسم المسلسل ، الموسم ، الجودة (720p) ، الترميز \n\n🖇<b>مــثــال</b>: \n\n• Game Of Thrones S03 720𝗉✅\n• Dark S02E03 ✅ \n• Breaking Bad S01E05 1080p✅ \n• Prison Break S01 1080p x265✅ \n• Witcher S02E01 x264✅\n\n🎬 للموسم الأول S01 ، للموسم التاني S02 [𝖲03,𝖲04 ,𝖲06,𝖲10,𝖲17]\n\n🔎 للحلقة الاولي E01 ، للحلقة التانية E02 [𝖤03,𝖤07,𝖤17,𝖤21] \n\n❌ Season 1 , الحلقة الاولي , الموسم الأول ❌\n❌ لا تستخدم الرموز في البحث *:-.& ❌**")
    
@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
