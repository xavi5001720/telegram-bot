
import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession


# === Configuración por variables de entorno ===
API_ID = int(os.environ["API_ID"]) # my.telegram.org
API_HASH = os.environ["API_HASH"] # my.telegram.org
SESSION = os.getenv("SESSION") # StringSession (recomendado en Railway)
SESSION_NAME = os.getenv("SESSION_NAME", "tesla_alert_bot") # fallback a sesión en archivo (menos fiable)
YOUR_CHAT_ID = int(os.environ["YOUR_CHAT_ID"]) # ID numérico de tu chat privado


# Palabras clave (se pueden sobreescribir con KEYWORDS, separadas por "|")
DEFAULT_KEYWORDS = [
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
'Aquí tienes dos opciones, responde con el número correspondiente:'
]
KEYWORDS = [kw.strip().lower() for kw in os.getenv("KEYWORDS", "|".join(DEFAULT_KEYWORDS)).split("|") if kw.strip()]


# Crear cliente: usa StringSession si existe, si no usa archivo de sesión
client = TelegramClient(StringSession(SESSION) if SESSION else SESSION_NAME, API_ID, API_HASH)


@client.on(events.NewMessage)
async def handler(event):
text = event.raw_text or ""
sender = await event.get_sender()
asyncio.run(main())
