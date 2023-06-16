import discord
from discord.ext import commands, tasks
import random
import asyncio

# This is the authentication token generated in Discord Developers.
TOKEN = ''

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

# Here the bot commands are defined.
bot = commands.Bot(command_prefix='!', intents=intents)

# Here the random curiosities are defined.
curiosities = [
  'Did you know: A few years ago, one of the strangest events in the Bitcoin mining industry was recorded, which was reported by Jameson Lopp's Twitter account. Lopp published the data of a completely empty block of bitcoins, whose confirmation reward had not been claimed. That is, a miner had worked for free. The 12.5 BTC that corresponded to the miner for his operations in the network had not been claimed at the time of completion of the operation, for which reason they were irretrievably lost. A mistake that turned out to be very costly, given that 12.5 BTC today represents a total of more than 338 thousand dollars. In this way, block 501726 has been recorded as the only block in the network without any registered bitcoin.', 
  "Many intrigued ask if the Blockchain will change the world as we know it, and the answer is a resounding YES: The Blockchain represents an innovation in the registration and distribution of information, which eliminates the need for a trusted party to facilitate relationships. digital. The Blockchain increases the trust, security, transparency and traceability of data shared in a business network, increasing cost savings thanks to its new efficiencies. A technology that will mark the future",
  'In block 270953, the largest Bitcoin transaction ever made is registered, which managed to send a total of 194,993 bitcoins, an amount that today represents almost 2 billion US dollars. Undoubtedly, a monstrous amount of money. The total commission for the transaction was only 0.5 BTC, a ridiculous discount compared to such a dimension of money. Likewise, the operation was carried out in November 2013, a date when Bitcoin had not yet taken off its popularity and its market prices were much lower than those registered today.',
  'NFTs or non-fungible tokens (Non Fungible Token in English) are unequivocal representations of assets, both digital and physical, in the blockchain network. They use the same technology as cryptocurrencies, but unlike cryptocurrencies, they cannot be divided or exchanged with each other, but they can be bought and sold.',
  'Manatees have flatulence that allows them to move forward.',
  'Did you know: Luxembourg is the richest nation in the world, generating around $78,000 per person per year (BRUTAL!) So why is nobody talking about it?',
  'Did you know that according to the UN: The poorest nation in the world is the Democratic Republic of the Congo: it generates US$365 per person per year :(. Another curious fact: The minimum wage in Venezuela is $8 depending on the people who live there! ( Conclusion: The UN has information of dubious origin ヽ ಠ_ಠ ノ ).',
  'Did you know that: The five percent of the richest in the United States increased their income 19% since 1988. This information is totally irrelevant to your day-to-day life, but it never hurts to know that while you complain about the RugPull that you ate like a tank, what many people do is keep going acquiring more and more knowledge (Conclusion: Knowledge, effort and memecoins are the key to success;)',
  'Did you know: In 1988, 44% of the world lived on less than US$1.25 a day. Times change fast :!',
  'Did you know: In South Africa life expectancy is 49 years while in China life expectancy is 75 years. Because?',
  'Did you know that: Almost 250 million people have left their native country (More than 70% are Latinos!(',
  'Curious and totally irrelevant fact: Did you know that the elephant is the only mammal that cannot jump :?',
  'Did you know that if you were given a dollar for every time you blinked: right now you would be the richest person in history! To give you an idea: you would multiply Elon Musk's fortune fivefold',
  'Did you know: Owls are the only birds that can see the color blue and you are the only person who has ADA in your wallet :)',
  'Did you know that: At birth we have 300 bones, but as adults we only have 206 (Why?)',
  'Did you know: Human teeth are almost as hard as stones or the community behind Solana (A round of applause for them please 👏).',
  'Did you know: A mole can dig a tunnel 300 feet long in just one night? This is more or less the size of the tunnel should be if Do Hyeong Kwon wants to get out of jail! ヽಠ_ಠノ',
  'Did you know: The Earth weighs about 6,588,000,000,000,000,000,000,000 tons. To give you an idea, it's the same number of zeros that PEPE has!(',
  'Did you know that Tomas Alba Edison, creator of the electric light bulb: he was as afraid of the dark as the RugPulers were of cheating (Curious right 😔?)',
  'Did you know that dolphins sleep with one eye open, they surely don't like having their things stolen 😒',
  'Did you know that: Some people only need four hours of sleep, this happens due to the hDEC2 gene mutation that regulates the duration of sleep and monitors it. (And in case you were wondering, you are not one of them 🙏)',
  'Did you know that: The Mariana Trench is the deepest place in the earth's crust located in the western Pacific Ocean and reaches a maximum known depth of 10,994 meters. And in case you wonder, the deepest place ever seen on web3 is called Shiba Inu (Many go in but few come out alive)',
  'Did you know that: Planet Earth is the fifth largest planet in the solar system surpassed by: 1) Jupiter (A giant made of gas that does not have a solid surface, but can have a solid inner core about the size of Earth) 2) Saturn (It is the planet that can be observed in the sky for the longest time throughout the year and is the most popular for its large rings), Uranus (The coldest and most unstable planet in the entire solar system because is composed of methane and ammonia on a small and tiny rocky core) and Neptune (The planet that apart from sharing great popularity with Saturn due to its six rings, is a gas giant that is made with a thick mixture of water and ammonia) . While on web3 the fifth planet of the Bitcoin system is ADA surpassed by XRP, BNB, Tether and Ethereum (Pretty curious 😒)',
  'Did you know that Antarctica has 70% of the fresh water on earth, as well as Bitcoin with 99% of trust in the crypto world?',
  'Did you know: There are about 200 bodies frozen on Mount Everest and more than a million accounts lost on FTX 💁?',
  'Did you know that it is supposed that within 4 billion years our galaxy will collide with the Andromeda galaxy. I wonder if BTC will exist when that happens 🙏',
  'Water is the main temperature regulator for the planet and our body, always remember to hydrate well! Since stopping drinking water is like investing in MemeCoins, sooner or later your time will come! 💨',
  'Did you know that the Vatican has the second largest gold treasure in the world after the United States, pfffff',
  'Did you know that the first alarm clocks were people. His job was to wake up the workers at dawn so that they would arrive at the factories on time. (The best job in the world 😜)',
  'Specialists point out that NFTs can be understood as digital certificates that guarantee ownership of graphics, videos, texts or any other digital object.',
  '1. The first NFT collection is CryptoKitties. They were the first to come to the NFT world. This is a virtual kitten game where players can buy, sell, and even breed different kittens. In this case, each character (cat) is an NFT, no joke, many people paid millions for internet kittens. (And then they complain that I invested in PEPE!(',
  'Remember that NFTs are immutable but if they can be stolen, Stay Safe', 'Did you know that honey is the only food that does not rot, and it is just the same color as Bitcoin, by chance? I don't believe it!',
  'Did you know that to make a kilo of honey, a bee must visit 4 million flowers',
  'Did you know that the number of eyelashes on the upper eyelid oscillates between 150 and 200 while on the lower eyelid we have between 80 and 90 eyelashes (I don't want to know how they discovered that .-.)',
  'Did you know that on Jupiter and Saturn the rain is made of diamonds. It wouldn't be bad to go there from time to time, right? ;)',
  'Did you know that licking your elbow is as impossible as trying to destroy Bitcoin, but for some reason many keep trying 😢',
  'Did you know that crocodiles have the strongest bite in the world but they cannot stick out their tongue, a barking dog does not bite! !{',
  'Did you know that if the population of China paraded past you in a row one by one, the line would never end due to the rate of reproduction, the rabbits tell them 😝',
  'The electric chair was invented by a dentist and Bitcoin was created by Elon Musk!',
  'Did you know that you share your birthday with at least 9 million other people in the world? Get happy! That means you have 9 million siblings from different mothers',
  'Did you know that: Einstein in his childhood did not speak fluently and his parents thought he was retarded. It's a pretty similar story to BTC, except that Bitcoin will **never** die',
  'Let's do a challenge: If you fold a piece of paper in half more than 7 times, I'll give you a million dollar tip! ................................................................ ................................................................ ................................................................ ................................................................ ..................................... You know what better I tell you now! Create a Risk Management plan!',
  'A person will die faster from not sleeping than from not eating, a man can only last 10 days without sleep, and he can go several weeks and up to a month without eating',
  'Blockchain technology is destined to generate countless investment opportunities. The huge impact these innovations will have is just the beginning',
  'Did you know that Blockchain represents the 5th biggest technological revolution to date? 1) The Neolithic Revolution (approximately 10,000 BC) 2) The Industrial Revolution (1780-1840) 3) The Second Industrial Revolution (1870-1914), 4) The Digital Revolution (1985-2000)',
  "If you put an egg in the middle of two mobile phones on, you will cook it in approximately 62 minutes, some say egg to the mobilidad,"
  'The most resistant material created by nature is the spider web, and the safest, clearest and most resistant technology created by the human being is the Blockchain',
  'Unbelievable but true: In 18th century Germany, women's menstrual blood was added as an aphrodisiac to food and drink (Will it work?)',
  'Did you know: The ancient Romans, when they had to tell the truth in court, instead of swearing on the Bible as they do today, did so by squeezing their testicles with their right hand. From this ancient custom came the word "testify.',
  'To stay awake in the morning, apples are more effective than caffeine.',
  'Did you know that the Vatican has enough money to end world poverty twice, Praise be to our lord SATOCHI NAKAMOTO!',
  'Did you know that seahorses choose a partner throughout their lives... when it dies they remain alone for a while and die too! And that's very romantic but in investments it's lousy advice! Never marry any coin!',
  'Did you know that humans and dolphins are the only species that have sex for pleasure. The other species do it out of necessity. Joke: One day xonnek the youtuber taught littleAlex06 how to be a noob FIN DELFIN',
  'Did you know that apple seeds contain cyanide, eating 40 or 50 could kill you. Sometimes the smallest is the most dangerous! Stay Safu :)',
  'Did you know that if you remove a cat's whiskers, it cannot walk properly and therefore loses its balance and falls... Both in the animal world and in the financial world, every piece of information counts! Don't let anything go unnoticed! Control everything, Stay Safu ;)',
  'Did you know that a koala can live its entire life without drinking water? If an animal can stop doing something so important for its existence throughout its life, why can't you stop investing in Shitcoins?',
  'Thomas Alva Edison, the inventor of the light bulb, was afraid of the dark (Karma exists!)',
  'Did you know that scorpions are the only animals that commit suicide, they do it once they cannot escape from a dangerous situation... very rarely another animal kills them. They are always the ones who end his life…',
  'Did you know that a hamster's eyes can fall out if they hang it upside down (I don't want to know how they discovered that)',
  'If you divide the number of female bees by the number of males in any honeycomb in the world, you will always get the same number, PI. 3.14159265… Mathematics are perfect and for that reason you should always have a risk management plan',
  'If you sneeze your heart stops for 1 millisecond if you hold it in a sneeze you could break a rib, tear the carotid artery or suffer brain damage. And if you happen to hold in a fart you could literally end your life. (Better let them out, don't hold back ;)',
  'Did you know that small fish are not bored in aquariums because their memory only lasts two minutes and it is as if they were reborn. Wouldn't it be incredible to be able to forget right now that you lost a large part of your money in a scam project for not investigating? Stay Safe',
  'Did you know that a person will die faster from not sleeping than from not eating, man can only last 10 days without sleep, and he can go several weeks without eating. Joke: Once upon a time, a Serrano ham was in love with a mortadella and decided to serenade it with some ranch sausages. END!',
  'Did you know that if you put a Diet Coke in a container with water, it floats. If you do it with a normal Coca-Cola, it sinks. (The copy will never beat the original, Bitcoin is second to none!)',
  'Did you know that the lion, the most sexually active animal in the world, can copulate with the same female one hundred times a day. Not even rabbits get to that point :!',
  'Did you know that the first palm trees grew at the North Pole. Sometimes the best jewels are born in the worst places.',
  'Did you know that when a child finishes primary school he has seen 8,000 murders and 10,000 acts of violence on television in his short life? !Children know things:!',
  'Did you know that chimpanzees, orangutans, dolphins, elephants and... humans are the only species capable of recognizing themselves in a mirror.',
  'Dying of laughter is possible!: Alex Mitchell, a 50-year-old bricklayer from King's Lynn, England, literally cracked up while watching an episode of The Goodies. After twenty-five minutes of non-stop laughter, Mitchell finally collapsed on the sofa and died.',
  'Miguel de Cervantes Saavedra and William Shakespeare are considered the greatest exponents of Spanish and English literature respectively; both died on April 23, 1616... To be or not to be, that is the dilemma! To invest or not to invest, that is the question!',
  'Since we are born our eyes are always the same size. There are things that never change and never will. As the king of digital assets 'Bitcoin!',
  'Did you know that the most powerful muscle in the human body is the tongue. Just think about it! You're moving it all day and you don't feel anything!',
  'Did you know that a drop of oil is capable of making 25 liters of water undrinkable and a person could dominate the world if he wanted to!',
  'Did you know that in Bangladesh, 15-year-old boys can be jailed for cheating on their final exams, a culture that should be replicated!',
  'Fun fact: Every month that starts on a Sunday has a Friday the 13th and every month that starts on a Thursday has a Tuesday the 13th. And why is this relevant? No idea, I just know it's popular!',
  'Did you know that in 1982 a game called Polybius was released in the United States. Months later he withdrew due to demands from the players. Players denounced that the game caused epileptic seizures, psychosis, nightmares, a tendency to suicide, and paranormal events occurred in your house. It was never proven that the game existed since those who played Polybius in those times do not remember it or vaguely remember it. Today it is very easy to find the game on the Internet, and you can see subliminal messages in it. would you play it?'
  'Did you know that in ancient England people could not have sex without the consent of the King (unless it was a member of the royal family). When people wanted to have a child, they had to request permission from the monarch, who gave them a plaque that they had to hang outside his door while they had sex. The plaque read “Fornication Under Consent of the King” (F.U.C.K.). That is the origin of such a famous little word.” FUCK you!',
  'Hipopomonstrosesquipedaliphobia fear of long words',
  'Did you know that the most recognized image worldwide is the image of CHÉ GUEVARA, with his hat with a star, looking towards the horizon. That is the pride of many and the curse of others!',
  'Did you know that there are only three animals with blue tongues: the Chow Chow dog, the blue-tongued lizard and the black bear. And there is only one asset capable of overcoming recent times. !Yeah! It's called Bitcoin!',
  'Did you know that a square meter of grass produces enough oxygen for one person for the whole year',
  'Did you know that the nose has the same length as the forehead?',
  'Fun fact, the yoyo was first used as a weapon in Asia and then became the most popular game on the planet. Doesn't that remind you of something?...... Indeed! NFT and Blockchain technology in its beginnings was used for acts of evil, but little by little it will become the dominant technology of tomorrow! (',
  'Did you know: “Bitcoin” only appears twice in its White Paper: in its title and in the web domain, but never in the entire body of the document.',
  'Who is Satoshi Nakamoto? Hal Finney, a video game developer for Atari and one of the early pioneers of Bitcoin, was suspected along with businessman Craig Wright, who has even said of himself that he has the relevant evidence to prove that he is the creator of Bitcoin. . However, neither case has been proven.',
  'Did you know that OneCoin is the largest cryptocurrency scam and one of the largest in history, a Ponzi scheme that defrauded between 4,000 and 19.4 billion dollars. Its creator, Ruja Ignatova, has been missing for years.',
  'Did you know that the rapper Akon decided to build a new city in his native Senegal, signed with his pseudonym. In January 2020, he announced via social media that Akon City had finalized an agreement under which the city would become a cryptocurrency metropolis. According to the rapper, cryptocurrencies have a chance to ensure a better future for the people of Senegal and even all of Africa. There are more projects related to cryptocurrencies in Africa and its development.',
  'Origins: before bitcoin, there were other attempts at digital currencies such as Digicash, which ensured anonymous electronic transactions, Flooz, or Beenz, which led one of the most notorious technological bankruptcies. "The Economist" predicted the creation of a currency for international use which he called Phoenix, indicating many aspects that would be fulfilled later, in addition to other previous attempts such as b-money and bit gold.',
  'It is believed that about 1,000 users control 40% of all bitcoins. They are known as whales, and they have so much power that their decisions can send the price of cryptocurrency swinging wildly. Within these whales there are some relevant people, such as their own creator, who is estimated to have close to 1 million bitcoins, or the Winklevoss twins, who were involved in the process of creating Facebook. Other holders are more surprising, such as the FBI, which has almost 150,000 bitcoins derived from seizures of the so-called “drug ebay”, the Silk Road platform, as well as the Bulgarian government, which has more than 210,000 bitcoins confiscated from various hackers.',
  'There are games for smartphones in which cryptocurrencies are obtained, such as the famous CryptoKitties with Ethereum, or those developed by Phoneum, a cryptocurrency that only operates on mobile devices through apps – one for mining and three for games. Currently there are many different cryptocurrency reward games, the best known being the “slot” type.',
  'A study on retired investors between 1999 and 2009 showed that those who hired a broker earned 1.5% less than those who managed their own money. “The rates were only half the difference,” reported Jason Zweig of The Wall Street Journal. ',
]

# Este es el canal al que se enviaran las curiosidades
channel_id = 

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
