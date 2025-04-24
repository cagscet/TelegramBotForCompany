from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Merhaba! Ben XZ firmasının bir Telegram botuyum 🤖\n /yardim komutu ile diğer komutları görebilirsiniz")

async def yardim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Komutlar:\n/start - Botu başlat\n/yardim - Komut yardımı al\n/hakkinda - XZ hakkında bilgi\n/hizmetler - verdiğimiz hizmetler\n/time - şu anki tarih ve saat")

async def hakkinda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("XZ bir teknoloji firmasıdır ve istanbulda faaliyet göstermektedir")

async def hizmetler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Web site hizmetleri, IT danışmanlığı, sosyal medya yönetimi ve veri analizi ve yönetimi alanlarında hizmet vermekteyiz.\n/website -Web site hizmetleri\n/IT - IT danışmanlık hizmeti\n/sosyal - sosyal medya yönetimi\n/veri - veri analizi ve yönetimi")

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Firma, müşterilerine profesyonel web sitesi tasarımı, mevcut web sitelerinin düzenlenmesi ve iyileştirilmesi gibi hizmetler sunmaktadır.\nDaha fazla bilgi için - /iletisim ")

async def IT(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("IT danışmanlığı hizmetiyle işletmelerin teknoloji altyapılarını güçlendirmeyi amaçlamaktadır. Mevcut sistemlerin analizini yaparak, verimliliği artıracak özelleştirilmiş çözümler sunar.\nDaha fazla bilgi için - /iletisim")

async def sosyal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("sosyal medya yönetimi hizmeti ile markaların dijital varlıklarını güçlendirmektedir. İçerik stratejisi oluşturur.\nDaha fazla bilgi için - /iletisim")

async def veri(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("veri analizi hizmetleriyle işletmelerin verilerini daha anlamlı hale getirir ve karar destek süreçlerine katkı sağlar. Büyük veri setlerini analiz ederek, işletmelerin performansını değerlendirmelerine ve stratejik kararlar almalarına yardımcı olur.\nDaha fazla bilgi için - /iletisim")

async def iletisim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("\n +90 0590 0131 52851 \n +90 0890 55131 5851 \n xziletisim@mail.com \n xzdestek@mail.com")

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    formatted_time = now.strftime("%d.%m.%Y %H:%M:%S")
    await update.message.reply_text(f"Şu anki tarih ve saat: {formatted_time}")


app = ApplicationBuilder().token("YourAPI_KEY").build() #API BAGLANTISI

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("yardim", yardim))
app.add_handler(CommandHandler("hakkinda", hakkinda))
app.add_handler(CommandHandler("hizmetler", hizmetler))
app.add_handler(CommandHandler("website", website))
app.add_handler(CommandHandler("IT", IT))
app.add_handler(CommandHandler("sosyal", sosyal))
app.add_handler(CommandHandler("veri", veri))
app.add_handler(CommandHandler("iletisim", iletisim))
app.add_handler(CommandHandler("time", time))

app.run_polling()
