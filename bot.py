import discord
from discord.ext import commands, tasks
import random
import asyncio

# Este es el token de autenticación generado en Discord Developers.
TOKEN = 'MTExNDgzNDY4Njk0NzExNTExOQ.Gd30rA.oYVECb2J_sB-PN7_dXpNNVBN5vLOrCDd1lTEq8'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Aquí se definen los comandos del bot.
bot = commands.Bot(command_prefix='!', intents=intents)

# Aquí se definen las curiosidades aleatorias.
curiosidades = [
    'Sabias que: Hace unos pocos anos se registró uno de los sucesos más extraños en la industria de minería de Bitcoin, el cual fue reportado por la cuenta de Twitter de Jameson Lopp. Lopp publicó los datos de un bloque totalmente vacío de bitcoins, cuya recompensa por confirmación no había sido reclamada. Es decir, un minero había trabajado gratis. Los 12,5 BTC que le correspondían al minero por sus operaciones en la red no habían sido reclamados al momento de finalizar la operación, por lo cual los mismos se perdieron irremediablemente. Un error que salió muy costoso, en vista de que 12,5 BTC representan hoy en día un total de más de 338 mil dólares. De esta manera, el bloque 501726 ha quedado grabado como el único bloque de la red sin ningún bitcoin registrado', 
  "Muchos preguntan intrigados si la Blockchain cambiara el mundo tal y como lo conocemos, y la respuesta es un rotundo SI: El Blockchain representa una innovación en el registro y distribución de información, el cual elimina la necesidad de un partido de confianza para facilitar las relaciones digitales. La Blockchain aumenta la confianza, la seguridad, la transparencia y la trazabilidad de los datos compartidos en una red empresarial, aumentando los ahorros en costos gracias a sus nuevas eficiencias. Una tecnologia que marcara el futuro",
    'En el bloque 270953 se encuentra registrada la transacción más grande de Bitcoin nunca antes hecha, la cual logró enviar un total de 194.993 bitcoins, monto que hoy en día representa casi 2 billones de dólares americanos. Sin lugar a dudas, una cantidad monstruosa de dinero. La comisión total por la transacción fue de tan sólo 0,5 BTC, un descuento irrisorio ante dicha dimensión de dinero. Asimismo, la operación se realizó en el mes de noviembre del 2013, fecha en donde el Bitcoin todavía no despegaba su popularidad y sus precios de mercado eran muy inferiores a los registrados hoy en día',
    'Los NFTs o tokens no fungibles (Non Fungible Token en inglés) son representaciones inequívocas de activos, tanto digitales como físicos, en la red blockchain. Usan la misma tecnología que las criptomonedas, pero al contrario que estas, no se pueden dividir ni intercambiar entre sí, pero sí se pueden comprar y vender.',
    'Los manatíes tienen flatulencias que les permiten moverse hacia adelante.',
  'Sabias que: Luxemburgo es la nación más rica del mundo, genera alrededor de $78.000 por persona al año (!BRUTAL!) Entonces porque nadie habla de ella?',
  ' Sabias que segun la ONU: La nación más pobre del mundo es la República Democrática del Congo: genera US$365 por persona al ano :(. Otro dato curioso: El salario minimo de Venezuela es de 8$ segun las personas que viven alli! (Conclusion: La ONU tiene informacion de dudosa procedencia ヽ ಠ_ಠ ノ ).',
  'Sabias que: El cinco por ciento de los más ricos en Estados Unidos aumentaron sus ingresos 19% desde 1988, Esta informacion es totalmente irrelevante para tu dia a dia pero nunca esta demas saber que mientras tu te quejas sobre el RugPull que te comiste como un tanque, mucha gente lo que hace es seguir adelante adquiriendo cada vez mas conocimiento (Conclusion: El conocimiento, el esfuerzo y las memecoins son la clave del exito ;).',
  'Sabias que: En 1988, 44% del mundo vivía con menos de US$1,25 diarios. Los tiempos cambian rapido :!',
  'Sabias que: En Sudáfrica la esperanza de vida es de 49 años mientras que en China la esperanza de vida es de 75 años. Porque?',
  'Sabias que: Casi 250 millones de personas han abandonado su país natal (Mas del 70% son latinos !(',
  'Dato curioso y totalmente irrelevante: Sabias que el elefante es el único mamífero que no puede saltar :?',
  'Sabias que si te dieran un dolar por cada vez que has parpadeado: ahora mismo fueras la persona mas rica de la historia! Para que te hagas una idea: quintuplicarias la fortuna de Elon Musk',
  'Sabias que: Los búhos son las únicas aves que pueden ver el color azul y tu eres la unica persona que tiene ADA en su billetera :)',
  'Sabias que: Al nacer tenemos 300 huesos, pero de adulto solo tenemos 206 (Proque?)',
  'Sabias que: Los dientes humanos son casi tan duros como piedras o la comunidad detras de Solana (Un aplauso para ellos por favor 👏).',
  'Sabias que: Un topo puede cavar un túnel de 300 pies de largo en solo una noche? Mas o menos de asi deberia ser el tamano del tunel si es que Do Hyeong Kwon quiere salir de la carcel! ヽ ಠ_ಠ ノ', 
  'Sabias que: La Tierra pesa alrededor de 6.588.000.000.000.000.000.000.000 toneladas. Para que te hagas una idea, es la misma cantidad de ceros que tiene PEPE !(',
  'Sabias que Tomas Alba Edison creador de la bombilla electrica: Le tenia tanto miedo a la oscuridad como los RugPulers a estafar (Curioso verdad 😔?)',
  'Sabias que los delfines duermen con un ojo abierto, de seguro no les gusta que les roben sus cosas 😒',
  'Sabias que: Algunas personas solo necesitan cuatro horas de sueño, esto pasa por la mutacion del gen hDEC2 que regula la duracion del sueno y lo vigila. (Y por si te lo preguntabas, tu no eres uno de ellos 🙏)',
  'Sabias que: La Fosa de las Marianas es el lugar más profundo de la corteza terrestre ubicado en el occidente del Océano Pacífico y alcanza una profundidad máxima conocida de 10.994 metros. Y por si te lo preguntas, el lugar mas profundo jamas visto en web3 se llama Shiba Inu (Muchos entran pero pocos salen con vida)', 
  'Sabias que: El planeta Tierra es el quinto planeta más grande del sistema solar superado por: 1)Júpiter (Un gigante hecho de gas que no tiene una superficie sólida, pero puede tener un núcleo interno sólido de aproximadamente el tamaño de la Tierra), 2) Saturno (Es el planeta que a lo largo del año se puede observar durante más tiempo en el firmamento y es el mas popular por sus grandes anillos), Urano (El planeta mas frio e inestable de todo el sistema solar debido a que esta compuesto de metano y amoniaco sobre un pequeno y diminuto nucleo rocoso) y Neptuno (El planeta que aparte se compartir gran popularidad con Saturno debido a sus seis anillos, es un gigante de gas que esta echo con una espesa mezcla de agua y amoniaco). Mientras que en web3 El quinto planeta del sistema Bitcoiniano es ADA superado por XRP, BNB, Tether y Ethereum (Bastante curioso 😒)',
  'Sabias que la Antartida cuenta con el 70% del agua fresca de la tierra, asi como Bitcoin con el 99% de la confianza en el mundo crypto?',
  'Sabias que: Hay cerca de 200 cuerpos congelados en el Monte Everest y mas de un miilon de cuentas que perdiron en FTX 💁?',
  'Sabias que se supone que dentro de 4 mil millones de años nuestra galaxia chocará con la galaxia Andromeda. Me pregunto si BTC existira cuando eso pase 🙏',
  '. El agua es el principal regulador de temperatura del planeta y de nuestro cuerpo, recuerda siempre hidratarte bien! Ya que dejar de tomar agua es como invertir en MemeCoins, tarde o temprano llegara tu hora! 💨', 
  'Sabias que el Vaticano tiene el segundo tesoro en oro más grande del mundo tras Estados Unidos, pfffff',
  'Sabias que los primeros despertadores eran personas. Su trabajo consistía en despertar de madrugada a los trabajadores para que llegaran a tiempo a las fábricas. (El mejor trabajo del mundo 😜)',
  'Especialistas señalan que los NFT se pueden entender como certificados digitales que garantizan la propiedad sobre gráficos, vídeos, textos o cualquier otro objeto digital.',
  '1. La primera colección de NFT es CryptoKitties. Fueron los primeros en llegar al mundo NFT. Se trata de un juego de gatitos virtuales donde los jugadores pueden comprar, vender e incluso cruzar diferentes gatitos. En este caso, cada personaje (gato) es un NFT, no es broma, mucha gente pago millones por gatitos de Internet. (Y despues se quejan de que invierta en PEPE !(',
  'Recuerda que los NFTs son inmutables pero si pueden ser robados, Stay Safe', 'Sabias que la miel es el único alimento que no se pudre, y justo es del mismo color que Bitcoin, casualidad? No lo creo!',
  'Sabias que para hacer un kilo de miel, una abeja debe recorrer 4 millones de flores',
  'Sabias que el número de pestañas del párpado superior oscila entre las 150 y 200 mientras que en el párpado inferior tenemos entre 80 y 90 pestañas (No quiero saber como descubrieron eso .-.)',
  'Sabias que en Jupiter y Saturno la lluvia está hecha de diamantes. No estaria mal pasarce por alli de vez en cuando no? ;)',
  'Sabias que lamerse el codo es tan imposible como intentar destruir Bitcoin, pero por alguna razon muchos siguen intentandolo 😢',
  'Sabias que los cocodrilos tienen la mordida mas fuerte del mundo pero no pueden sacar la lengua, perro que ladra no murde! !{',
  'Sabias que si la población de China desfilara a tu lado en fila de a uno, la hilera no acabaría nunca debido al ritmo de reproducción, los conejos le dicen 😝', 
  'La silla eléctrica fue inventada por un dentista y Bitcoin lo creo Elon Musk!',
  '¿Sabías que compartes tu fecha de cumpleaños con al menos otros 9 millones de personas en el mundo? Alegrate! Eso significa que tienes 9 millones de hermanos de diferentes madres',
  'Sabias que: Einstein en su niñez no hablaba fluidamente y sus padres pensaban que era un retrasado. Es una historia bastante parecida a la de BTC, con la diferencia de que Bitcoin **nunca** morira',
  'Hagamos un reto: Si plegas un pedazo de papel a la mitad mas de 7 veces, te regalo un consejo millonario! .......................................................................................................................................................................................................................................... Sabes que mejor te lo digo ahora! Crea un plan de Gestion de Riesgo!',
  'Una persona morirá más rápido por no dormir que por no comer, el hombre solo puede aguantar 10 días sin sueño, y puede estar varias semanas y haata un mes sin comer',
  'La tecnología blockchain está llamada a generar incontables oportunidades de inversión. La gran repercusión que tendrán estas innovaciones es solo el principio',
  'Sabias que La Blockchain representa la 5ta revolucion tecnologica mas grande hasta la fecha? 1) La revolución neolítica (10.000 a. C. aproximadamente) 2) La Revolución Industrial (1780-1840) 3) La Segunda Revolución Industrial (1870-1914), 4) La Revolución Digital (1985-2000)',
  'Si pones un huevo en medio de dos móviles encendidos lograras que se cocine en aproximadamente 62 minutos, huevo a la movilada le dicen algunos',
  'El material más resistente creado por la naturaleza es la tela de araña, y la tecnologia mas segura, clara y resistente creada por el ser humano es la Blockchain',
  'Increible pero cierto: En Alemania del siglo XVIII, la sangre menstrual de las mujeres se añadía como afrodisíaco en comidas y bebidas (Funcionara?)',
  'Sabias que: Los antiguos romanos cuando tenían que decir la verdad en un juicio, en vez de jurar sobre la Biblia como en la actualidad, lo hacían apretándose los testículos con la mano derecha. De esta antigua costumbre procede la palabra testificar.',
  'Para mantenerse despierto en las mañanas son más efectivas las manzanas que la cafeína.'
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
    tarea_publicar = tarea_publicar_curiosidad.start()

# Tarea programada para publicar la curiosidad cada 1 minuto.
@tasks.loop(minutes=1)
async def tarea_publicar_curiosidad():
    await publicar_nueva_curiosidad()

# Manejador de errores para detener la tarea de publicación en caso de errores
@tarea_publicar_curiosidad.before_loop
async def antes_publicar_curiosidad():
    await bot.wait_until_ready()
    
# El bot se conecta a Discord y espera a recibir comandos.
bot.run(TOKEN)
