import discord
from discord.ext import commands, tasks
import random
import asyncio

# Este es el token de autenticación generado en Discord Developers.
TOKEN = 'MTExMTMxNjg0MjAxMTcwOTQ0MA.Gnlwgq.4OY4VTdHFuymF3NG80lqrDxtDyKE1WvqBGlstE'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Aquí se definen los comandos del bot.
bot = commands.Bot(command_prefix='!', intents=intents)

# Aquí se definen las curiosidades aleatorias.
curiosidades = [
    'Los nudillos de los chimpancés se vuelven blancos cuando estos se asustan.',
    'Los cangrejos pueden regenerar patas perdidas, pero en el proceso también pueden regenerar un ojo en la pata.',
    'El Premio Nobel de química de 1991 fue otorgado a una mujer que desarrolló técnicas para el estudio de moléculas congeladas en el tiempo.',
    'Los manatíes tienen flatulencias que les permiten moverse hacia adelante.'
]

#Aquí se define el canal donde se publicará la curiosidad
canal_id = 1106851485142229003

# Mensaje que se publicará
async def publicar_nueva_curiosidad():
    canal = bot.get_channel(canal_id)
    random_curiosidad = random.choice(curiosidades)
    await canal.send(random_curiosidad)

# Este es el evento que se ejecuta cuando el bot se enciende.
@bot.event
async def on_ready():
    print(f'{bot.user.name} está conectado al Discord!')
    # Inicia el ciclo de la tarea programada
    tarea_publicar = tarea_publicar_curiosidad.start()

# Tarea programada para publicar la curiosidad cada 1 minuto.
@tasks.loop(minutes=1)
async def tarea_publicar_curiosidad():
    await publicar_nueva_curiosidad()

# Manejador de errores para detener la tarea de publicación en caso de errores
@tarea_publicar_curiosidad.before_loop
async def antes_publicar_curiosidad():
    await bot.wait_until_ready()
    print('Publicando curiosidad...')
    
# El bot se conecta a Discord y espera a recibir comandos.
bot.run(TOKEN)
