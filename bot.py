import discord
from discord.ext import commands, tasks
import random
import asyncio

# This is the authentication token generated in Discord Developers.
TOKEN = 'MTExNDgzNDY4Njk0NzExNTExOQ.Gg_WKP.mdx9XQWndDgLK4kOwRpOjsIeGqAPiCPSSASsfw'

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Here the bot commands are defined.
bot = commands.Bot(command_prefix='!', intents=intents)

# Here the random curiosities are defined.
curiosities = [
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
  'Para mantenerse despierto en las mañanas son más efectivas las manzanas que la cafeína.',
  'Sabias que el Vaticano posee la cantidad de dinero suficiente para acabar con la pobreza mundial dos veces, !Alabado sea nuestro senor SATOCHI NAKAMOTO!',
  'Sabias que los caballitos de mar elijen una pareja durante toda su vida… cuando esta muere permanecen solos por un tiempo y mueren también! Y eso es muy romantico pero en las inversiones es un pesimo consejo! Nunca te cases con ninguna moneda!',
  'Sabias que los humanos y los delfines son las únicas especies que practican sexo por placer. Las demas especies lo hacen por necesidad. Chiste: Un dia xonnek el youtuber le enseño a littleAlex06 como aser un noob FIN DELFIN',
  'Sabias que las semillas de la manzana contienen cianuro, comerte 40 o 50 podrían matarte. Aveces lo mas pequeno es lo mas peligroso! Stay Safu :)',
  'Sabias que si le quitas los bigotes a un gato, éste no puede caminar bien y por lo tanto pierde el equilibrio y se cae… Tanto en el mundo animal como en el financiero cada dato cuenta! No dejes pasar nada desapercibido! Controlalo todo, Stay Safu ;)',
  'Sabias que un koala puede vivir toda su vida sin tomar agua. Si un animal puede dejar de hacer algo tan importante para la existencia durante toda su vida, poque tu no puedes parar de invertir en Shitcoins?',
  'Thomas Alva Edison, el inventor de la bombilla eléctrica, le temía a la oscuridad (El Karma existe!)',
  'Sabias que los escorpiones, son los únicos animales q se suicidan, lo hacen una vez q no pueden escapar de una situación de peligro… muy rara ves lo mata otro animal. Siempre son ellos los q terminan con su vida…',
  'Sabias que los ojos de un hámster pueden caerse si lo cuelgan con la cabeza para abajo (No quiero saber como descubrieron eso)',
  'Si divides el número de abejas hembras por el de machos de cualquier panal del mundo siempre obtendrás el mismo número, PI. 3,14159265… Las Matematicas son perfectas y por esa razon siempre debes tener un plan de gestion de riesgo',
  'Si estornudas tu corazón se detiene un 1milisegundo si aguantas en estornudo se te podría romper una costilla desgarrar la carótida o sufrir daños cerebrales. Y si por casualidad te aguantas un pedo podrias literalmente acabar con tuvida. (Mejor dejalos salir, no te reprimas ;)',
  'Sabias que los peces chicos no se aburren en las peceras porque su memoria solo dura dos minutos y es como si volvieran a nacer. No te pareceria increible poder ahora mismo olvidarte de que perdiste gran parte de tu dinero en un proyecto scam por no investigar? Stay Safe',
  'Sabias que una persona morirá más rápido por no dormir que por no comer, el hombre solo puede aguantar 10 días sin sueño, y puede estar varias semanas sin comer. Chiste: ¡Que una vez, un jamón serranos estaba enamorado de una mortadela y decidió darle una serenata con unas salchichas rancheras. FIN!',
  'Sabias que si metes una Coca Light en un recipiente con agua, flota.Si lo haces con una de Coca-Cola normal, se hunde. (La copia nunca superara al original, !Bitcoin es insuperable!)',
  'Sabias que el león, el animal de mayor actividad sexual del mundo, puede copular con la misma hembra cien veces al día. Ni los conejos llegan a ese punto :!',
  'Sabias que las primeras palmeras crecieron en el polo norte. Aveces en los peores lugares nacen las mejores joyas.',
  'Sabias que cuando un niño termina la educación primaria ha visto en su corta vida 8.000 asesinatos y 10.000 actos de violencia en la televisión. !Los ninos saben cosas :!',
  'Sabias que los chimpances, orangutanes, delfines, elefantes y… el ser humano, son las únicas especies capaces de reconocerse a sí misma en un espejo.',
  'Morir de risa es posible!: Alex Mitchell, un albañil de 50 años de edad de King’s Lynn, Inglaterra, literalmente se murió de risa mientras miraba un episodio de la serie The Goodies. Después de veinticinco minutos de risa continuada, Mitchell finalmente se derrumbo en el sofá y murió.',
  'Miguel de Cervantes Saavedra y William Shakespeare son considerados los más grandes exponentes de la literatura hispana e inglesa respectivamente; ambos murieron el 23 de abril de 1616… Ser o no Ser, ese es el dilema! Invertir o no invertir, esa es la cuestion!',
  'Desde que nacemos nuestros ojos siempre son del mismo tamaño. Hay cosas que nunca cambian y nunca lo haran. Como el rey de los activos digitales !Bitcoin!',
  'Sabias que el músculo más potente del cuerpo humano es la lengua. Solo piensatelo! La estas moviendo todo el dia y no sientes nada!',
  'Sabias que una gota de petróleo es capaz de convertir 25 litros de agua en no potable y una persona si se lo propone podria dominar el mundo!',
  'Sabias que en Bangladesh, los niños de 15 años pueden ser encarcelados por hacer trampa en sus exámenes finales, una cultura que deberia replicarse!',
  'Dato curioso: Cada mes que comienza en Domingo tiene un Viernes 13 y cada mes q comienza en Jueves tiene un Martes 13. Y porque razon esto es relevantes? Ni idea, solo se que es popular!',
  'Sabias que en 1982 se sacó a la venta un juego en Estados Unidos llamado Polybius. Meses depués se retiró a causa de las demandas de los jugadores. Los jugadores denunciaban que el juego provocaba ataques epilépticos, psicosis, pesadillas, tendencia al suicidio y en tu casa se producían sucesos paranormales. Nunca se provó que el juego existiera ya que los que en esas épocas jugaron a Polybius no lo recuerdan o lo recuerdan vagamente. Hoy es muy fácil encontrar el juego por Internet, y se pueden contemplar mensajes subliminales en él. Lo jugarias?',
  'Sabias que en la antigua Inglaterra la gente no podía tener sexo sin contarcon el consentimiento del Rey (a menos que se tratara de un miembro de la familia real). Cuando la gente quería tener un hijo debían solicitar un permiso al monarca, quien les entregaba una placa que debían colgar afuera de su puerta mientras tenían relaciones. La placa decía “Fornication Under Consent of the King” (F.U.C.K.). Ese es el origen de tan famosa palabrita.” FUCK you!',
  'Hipopomonstrosesquipedalifobia miedo a las palabras largas',
  'Sabias que la imagen más reconocida a nivel mundial, es la imagen del CHÉ GUEVARA, con su sombrerito con estrella, mirando hacia el horizonte. Ese es el orgullo de muchos y la maldicion de otros!',
  'Sabias que sólo existen tres animales con lengua azul: el perro Chow Chow, el lagarto lengua-azul y el oso negro. Y solo existe un activo capaz de sobrebir a los ultimos tiempos. !Si! Se llama Bitcoin!',
  'Sabias que un metro cuadrado de césped produce suficiente oxigeno para una persona por todo el año',
  'Sabias que la nariz tiene el mismo largo que la frente?',
  'Dato curioso el yoyo primero se uso como arma en Asia para luego volverse el juego mas popular del planeta. Eso no te recuerda a algo?...... !En efecto! La tecnologia NFT y Blockchain en sus comienzos fue utilizada para actos de maldad, pero poco a poco se convertira en la tecnologia que domine del manana!              (',
  'Sabias que: “Bitcoin” solo aparece dos veces en su Libro blanco: en su título y en el dominio web, pero ninguna en todo el cuerpo del documento.',
  '¿Quién es Satoshi Nakamoto? Hal Finney, un desarrollador de videojuegos para Atari y uno de los pioneros iniciales de Bitcoin, fue sospechoso junto al empresario Craig Wright, que ha llegado a decir de sí mismo que cuenta con las pruebas pertinentes para demostrar que él es el creador del Bitcoin. Sin embargo, ninguno de los dos casos ha sido comprobado.',
  'Sabias que OneCoin es la mayor estafa en criptomonedas y una de las más grandes de la historia, un esquema Ponzi que estafó entre 4.000 y 19.4 mil millones de dólares. Su creadora, Ruja Ignatova, lleva años desaparecida.',
  'Sabias que el rapero Akon decidió construir una nueva ciudad en su Senegal natal, firmada con su seudónimo. En enero de 2020, anunció a través de las redes sociales que Akon City había finalizado un acuerdo según el cual la ciudad se convertiría en una metrópolis de criptomonedas. Según el rapero, las criptomonedas tienen la oportunidad de garantizar un futuro mejor para la gente de Senegal e incluso para toda África. Existen más proyectos relacionados con las criptomonedas en África y su desarrollo.',
  'Orígenes: antes que el bitcoin, hubo otros intentos de monedas digitales como Digicash, que aseguraba transacciones electrónicas anónimas, Flooz, o Beenz, que protagonizó una de las más sonadas quiebras tecnológicas. “The Economist” predijo la creación de una moneda de uso internacional a la que llamó Phoenix, indicando muchos aspectos que cumplirían posteriormente, además de otros intentos anteriores como el b-money y el bit gold.',
  'Se cree que unos 1.000 usuarios controlan el 40% del total de bitcoins. Se les conoce como ballenas, y tienen tanto poder que sus decisiones pueden hacer oscilar el precio de la criptomoneda bruscamente. Dentro de estas ballenas hay algunas personas relevantes, como su propio creador, el cual se estima que posee cerca de 1 millón de bitcoins, o los gemelos Winklevoss, que intervinieron en el proceso de creación de Facebook. Otros poseedores resultan más sorprendentes, como el FBI, que tiene casi 150.000 bitcoins derivados de las incautaciones del conocido como “ebay de las drogas”, la plataforma Silk Road, así como el gobierno de Bulgaria, que posee más de 210.000 bitcoins confiscados a diversos hackers.',
  'Existen juegos para smartphones en los que se consiguen criptomonedas, como puede ser el famoso CryptoKitties con Ethereum, o los desarrollados por Phoneum, una criptomoneda que opera solamente en dispositivos móviles a través de apps – una de minado y tres de juegos. Actualmente existen muchos juegos diferentes de recompensa de criptomonedas, siendo los más conocidos los del tipo “tragaperras”.',
  'Un estudio sobre inversores retirados entre 199 y 2009 demostró que aquellos que contrataron un broker ganaron un 1,5% menos que los que manejaron su propio dinero. “Las tasas solo sumaban la mitad de la diferencia”, informó el periodista Jason Zweig, de The Wall Street Journal. ',
]

# Este es el canal al que se enviaran las curiosidades
channel_id = 1106851485142229003

# Esta es la funcion para poner una nueva curiosidad
async def post_new_curiosity():
  try:
    # Elige el canal al que enviaras la curiosidad
    channel = bot.get_channel(channel_id)
    # Elige una curiosidad random
    random_curiosity = random.choice(curiosities)
    # Envia la curiosidad al canal
    await channel.send(random_curiosity)
  except Exception as e:
    print(e)


# Crea un evento con el bot para ponerlo a correr
@bot.event
async def on_ready():
  # Enpieza a postear la curiosidad cada minuto
  @tasks.loop(minutes=1)
  async def post_curiosities():
    # Get a random curiosity.
    random_curiosity = random.choice(curiosities)

    # Get the channel where the curiosity will be posted.
    channel = bot.get_channel(channel_id)

    # Envia la curiosidad a el canal.
    await channel.send(random_curiosity)
    #Confirma que se estan publicando las curiosidades.
    print('Publicando curiosidad...')

  # Que comience la fiesta.
  post_curiosities.start()

# Pon el bot a correr
bot.run(TOKEN)
