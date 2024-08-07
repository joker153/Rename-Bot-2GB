import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "3261311")
    API_HASH  = os.environ.get("API_HASH", "41377ec3060b15a5105dbe1e8af95c99")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6426072097:AAFpvNEzW65qVT6XwTxzafDLJKFk-Xtbun0") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","rx100")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://amal:amal@cluster0.piduja2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/ad48ac09b1e6f30d2dae4.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot.

➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.

➻ You Can Also Convert Video To File And File To Video.

➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
"""

    ABOUT_TXT = """
<b>• {file_name}
╭──────────────────╮
•📌 ꜰɪʟᴍ ɢʀᴏᴜᴘ :<a href="https://t.me/+fx9w8TbvlU5hMzZl">ᴊᴏɪɴ ɴᴏᴡ</a>
•🎬 ꜰɪʟᴍ ᴜᴘᴅᴀᴛᴇꜱ :<a href="https://t.me/+J1ZAODvANTY3NjU1">ᴊᴏɪɴ ɴᴏᴡ</a>
•🔮 ꜰɪʟᴍ ᴜᴘᴅᴀᴛᴇꜱ :<a href="https://t.me/CineflixXLinks">ᴊᴏɪɴ ɴᴏᴡ</a>
╰──────────────────╯

• ᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href="https://t.me/CineflixXLinks">ᴄɪɴᴇꜰʟɪx</a></b>"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/MadflixOfficials>Developer</a>
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `madflixofficial@axl`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>-map 0 -c:s copy -c:a copy -c:v copy -metadata title="Encoded By :- @Madflix_Bots" -metadata author="@JishuDeveloper" -metadata:s:s title="Subtitled By :- @Madflix_Bots" -metadata:s:a title="By :- @Madflix_Bots" -metadata:s:v title="Encoded By :- @Madflix_Bots"</code>

💬 For Any Help Contact @CallAdminRobot
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @JishuBotz
# Developer @JishuDeveloper
