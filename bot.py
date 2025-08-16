from telethon import TelegramClient, events
import asyncio
import os

# --- Configuración desde variables de entorno ---
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = 'tesla_alert_bot'
your_chat_id = int(os.getenv("YOUR_CHAT_ID"))

# --- Palabras clave ---
keywords = [
    'comprar tesla',
    'quiero comprar un tesla',
    'me quiero comprar un tesla',
    'estoy pensando en comprar un tesla',
    'vale la pena un tesla',
    'recomendáis el tesla',
    'recomendais el tesla',
    'cambiar mi coche por un tesla',
    'quiero referido para tesla',
    'comprar coche eléctrico',
    'comprar coche electrico',
    'estoy entre tesla y',
    'me interesa el model ',
    'alguna opinión del tesla',
    'cuánto cuesta un tesla',
    'cuanto cuesta un tesla',
    'estoy mirando el tesla',
    'oferta tesla',
    'dónde comprar un tesla',
    'donde comprar un tesla',
    'configurador tesla',
    'precio tesla model',
    'model s vale la pena',
    'quién tiene un tesla',
    'quien tiene un tesla',
    'estoy mirando coches eléctricos',
    'estoy mirando coches electricos',
    'alguien ha comprado un tesla',
    'me entregarian el tesla',
    'voy a reservar un tesla',
    'cita en tesla',
    'quiero hacer el pedido del tesla',
    'necesito referido',
    'necesito descuento tesla',
    'referido',
    'quiero un coche electrico',
    'necesito un código de descuento',
    'mandarme un referido',
    'quiero un tesla',
    'interesado en comprar',
    'quiero comprar',
    'necesito comprar',
    'estoy interesado',
    'probar un tesla',
    'cuánto cuesta un tesla',
    'quiero reservar un tesla',
    'que opinais del tesla',
    'cuanto cuesta un tesla',
    'si buscas una tarifa económica para cargar tu coche, te recomiendo esta oferta',
    'te recomiendo visitar los modelos de inventario tesla con descuento.', 
]

# Convertir todas las keywords a minúsculas
keywords = [kw.lower() for kw in keywords]

# --- Crear cliente Telethon ---
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage(chats=None))
async def handler(event):
    text = event.raw_text or ""
    sender = await event.get_sender()
    chat = await event.get_chat()
    username = sender.username or sender.first_name or "Sin nombre"
    group = getattr(chat, 'title', 'Mensaje privado')

    print(f"[DEBUG] Mensaje recibido de {username} en {group}: {text}")

    # Ignorar mensajes salientes o que ya contienen la etiqueta para evitar bucles
    if "#botalert" in text or event.out:
        print("[DEBUG] Ignorado por ser mensaje saliente o contener #botalert.")
        return

    # Normalizar texto: minúsculas y quitar saltos de línea
    text_lower = text.lower().replace("\n", " ")

    # Buscar coincidencia parcial
    matched = any(kw in text_lower for kw in keywords)

    if not matched:
        print("[DEBUG] No se detectó ninguna palabra clave.")
        return

    msg = (
        f"🔔 *Posible comprador detectado:*\n"
        f"👤 Usuario: {username}\n"
        f"📍 Grupo: {group}\n"
        f"💬 Mensaje: {text}\n"
    )

    if hasattr(chat, 'username') and chat.username:
        msg += f"🔗 Enlace: https://t.me/{chat.username}/{event.message.id}"
    elif hasattr(chat, 'id') and str(chat.id).startswith('-100'):
        chat_id = str(chat.id).replace("-100", "")
        msg += f"🔗 Enlace: https://t.me/c/{chat_id}/{event.message.id}"
    else:
        msg += "🔗 Enlace: No disponible (grupo privado o chat personal)"

    msg += "\n\n#botalert"

    try:
        await client.send_message(your_chat_id, msg, parse_mode='markdown')
        print(f"[DEBUG] Mensaje de alerta enviado.")
    except Exception as e:
        print(f"[ERROR] No se pudo enviar mensaje: {e}")

async def main():
    print("✅ Bot iniciado. Escuchando mensajes...")
    await client.start()
    try:
        await client.send_message(your_chat_id, "Bot iniciado correctamente y conectado.")
        print("[DEBUG] Mensaje de inicio enviado.")
    except Exception as e:
        print(f"[ERROR] No se pudo enviar mensaje de inicio: {e}")

    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())

