from whatsapp import WhatsApp

whatsapp = WhatsApp(
    30,
    login_qr_screenshot="./screenshot.png",
    session_name="session",
    headless=False
)
print(whatsapp.send_message("Bot Log", "This is a Bot test! :victory"))
whatsapp.quit()
