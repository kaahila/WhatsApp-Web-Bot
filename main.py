from whatsapp import WhatsApp

whatsapp = WhatsApp(
    30,
    login_qr_screenshot="./screenshot.png",
    session_name="session",
    headless=True,
    log_chat="Bot Log"
)
try:
    print(whatsapp.send_message("Bot Test", "This is a Bot test!"))
finally:
    whatsapp.quit()
