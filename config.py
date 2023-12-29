import os

api_id = int(os.environ.get("API_ID", "15890589"))
api_hash = os.environ.get("API_HASH", "27fe60ebafe8a74117bfae10407925c7")
bot_token = os.environ.get("BOT_TOKEN", "6826195273:AAFjSeGQGm87MdjGxBGFBbbkCoBm3STIGtg")
# =========================================================== #

db_url = os.environ.get("DB_URL", "mongodb+srv://doadmin:9r260Iqy437zS1lA@db-mongodb-sgp1-52558-1312a8db.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-sgp1-52558")
db_name = os.environ.get("DB_NAME", "doadmin")
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "-1001665881786"))
channel_2 = int(os.environ.get("CHANNEL_2", "-1002100850265"))
channel_log = int(os.environ.get("CHANNEL_LOG", "-1002130415408"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "1948147616"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "3"))
batas_talent = int(os.environ.get("BATAS_TALENT", "20"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "30"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "200"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "200"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "200"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "200"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "200"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "200"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#PixyGirl #PixyBoy #PixyCurhat #PixySpill #PixyPap").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph//file/b1b084fdcc3254aa4c212.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph//file/3db21c15c059d6a6080d1.jpg")
pic_talent = os.environ.get("PIC_TALENT", "")
pic_bf_rent = os.environ.get("PIC_BF_RENT", "")
pic_gf_rent = os.environ.get("PIC_GF_RENT", "")
pic_sugar_daddy = os.environ.get("PIC_SUGAR_DADDY", "")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Hai {mention} Sobat Pixy Base [😉](https://telegra.ph//file/b52849db161f0e56e3461.jpg) ,\n\nKamu Tidak dapat Mengirim Menfes , Harap Join Terllebih Dahulu Untuk Mengirim Menfess di Pixy Base👍")
start_msg = os.environ.get("START_MSG", "Hai {fullname} hallo selamat datang dibot auto post Pixy Menfes base [✨](https://telegra.ph//file/b52849db161f0e56e3461.jpg) .\n\nIni adalah bot Menfes ya BG Menfes, semua pesan yang kamu kirim akan masuk ke channel secara anonim sesuai hastag:\n#PixyGirl Untuk Cewek\n#PixyBoy Untuk Cowok\n#PixyCurhat Untuk Curhat\n#PixyPap Untuk Mengirim Pap random kalian\n\nContoh:\n. {mention} Cari Mutualan Dom Depok @fulann #PixyGirl\n\nSupport: @Pixy_Update")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
Halo {mention} 

pesan mu gagal terkirim silahkan gunakan hastag:
#PixyGirl / #PixyBoy Untuk Mencari Pasangan, Teman , Partner FWB
#PixyAsk Untuk Bertanya
#PixyCurhat Untuk Berbagi Cerita / Curhat.
#PixySpill Untuk Spill Masalah / Pengalaman
#PixyPap Untuk Mengirim Pap random kalian.

""")
