Airport = Room(name="San Francisco International Airport", description="Welcome to the city!\
You spot the beautiful San Francisco bay as you fly in, excited to be in \
California at last. First thing's first, how do you want to get into the city? Uber? Lyft? \
Super shuttle? BART? Walking?", dictionary = {'uber': 'nob-hill', 'lyft': 'nob-hill',
'super shuttle': 'nob-hill', 'bart': 'nob-hill', 'walking': 'you-lose-walking', 'walk': 'you-lose-walking'},
slug="SFO")
Airport.save()

You_lose_walking = Room(name="You lose :(", description="You tried to walk all the way \
from SFO to the city. Why would you do that?? As you try to walk up the 101, you stumble\
 across a hippie commune and join their ranks, never making it to the fair city. Oh well.\
  There are definitely worse fates.", dictionary = {}, slug="you-lose-walking")
You_lose_walking.save()

Nobhill = Room(name="Nob Hill", description="You start the day \
in Nob Hill and have to rent an apartment. How much do you want to pay? \
$1,000? $2,000? $3,000?", dictionary = {'$1,000': 'you-lose-housing', '$2,000': 'SOMA', '$3,000': 'SOMA', '1,000': 'you-lose-housing', '2,000': 'SOMA', '3,000': 'SOMA', '1000': 'you-lose-housing', '2000': 'SOMA', '3000': 'SOMA'}, slug="nob-hill")
Nobhill.save()

You_lose_housing = Room(name="You lose :(", description="You tried to find an apartment \
for the low, low price of $1,000, but just couldn't find anything, even when surfing \
Craigslist. Drat. The housing market is a cruel, cruel mistress. Better luck next time.",
 dictionary = {}, slug="you-lose-housing")
You_lose_housing.save()

Soma = Room(name="SOMA", description="Great! You surf PadMapper and Craigslist until you find a \
nice little apartment in Nob Hill. Now that that's settled, it's your first day at work here in SOMA, \
the heart of the San Francisco start-up world. Nobody is wearing shoes and there are\
 bean bags and ping-pong tables everywhere. You see some schwag on your desk. \
Do you put it in your bag?", dictionary = {'yes': 'chinatown', 'yep': 'chinatown', 'no': 'you-lose-schwag', 'nope': 'you-lose-schwag'}, slug="SOMA")
Soma.save()

You_lose_schwag = Room(name="You lose :(", description="You tried to be a good person and not take the schwag without asking \
but you just can't make it in this city without a proper tech wardrobe...You pack up your bags and leave. The End.",
 dictionary = {}, slug="you-lose-schwag")
You_lose_schwag.save()

Chinatown = Room(name="Chinatown", description="Newly equipped with a techie hoodie and \
Fitbit, you're really starting to fit in! Feeling pretty proud of yourself, you decide \
to go for a little walk and explore your new city. You've found yourself in Chinatown! \
It is swarming with tourists and some old man playing the Erhu. Do you want to buy a \
mini-Erhu before leaving?", dictionary = {'yes': 'north-beach', 'yep': 'north-beach', 'no': 'you-lose-cable-car', 'nope': 'you-lose-cable-car'}, slug="chinatown")
Chinatown.save()

Cable_car = Room(name="You lose :(", description="You decide not to buy a souvenir in Chinatown, \
but get this sinking feeling that you're not living the San Francisco experience. So, you try to \
get on the cable car, but don't realize it can't stop too easily when it's hurtling down the \
California St. hill...Clang clang clang goes the trolly indeed. Better luck next time.",
dictionary={}, slug="you-lose-cable-car")
Cable_car.save()


North_beach = Room(name="North Beach", description="Fresh from your exploration in Chinatown \
you turn north towards North Beach, home of the bros. Swoll men in backwards caps greet you \
at every turn. Hungry from your long journey, you decide to duck into Tony's Pizza Napoletana,\
which you read about on your Yelp app (naturally). What do you want to order - pizza, lasagna, or salad?", 
dictionary = {'pizza': 'golden-gate', 'lasagna': 'golden-gate', 'salad': 'you-lose-hungry'}, slug="north-beach")
North_beach.save()


You_lose_hungry = Room(name="You lose :(", description="*rumble rumble* What's that? Oh, right\
it's the sound of your stomach regretting your decision to order a salad. You try to continue your walk\
to the Golden Gate Bridge, but you just...can't...make it...Your legs grow weak and you faceplant just as you\
reach Cow Hollow. Looks like you'll stay in the land of yoga pants, lattes, and OMG's forever...The End.", 
dictionary = {}, slug="you-lose-hungry")
You_lose_hungry.save()

Golden_gate = Room(name="The Golden Gate Bridge", description="Excellent choice! Well-fueled from dinner \
you continue your little walk. At long last, you spot the Golden Gate Bridge! You notice how it is \
especially beautiful as the waves lap up on the shore. However, even though the timing is strange, you see Karl the \
fog rear his ugly, foggy head. Oh no! What are you going to do?? Maybe there's something in your inventory you can use...", 
dictionary = {'use erhu': 'you-lose', 'use fitbit': 'the-end', 'fitbit': 'the-end', 'hoodie': 'the-end', 'use hoodie': 'the-end', 'techie hoodie': 'the-end', 'use techie hoodie': 'the-end', 'use schwag': 'the-end', 'erhu': 'you-lose', 'schwag': 'the-end', 'play erhu': 'you-lose', 'give shwag to karl the fog': 'the-end', 'give him the schwag': 'the-end'}, slug="golden-gate")
Golden_gate.save()

The_end_winner = Room(name="The End", description="You give Karl the Fog your tech schwag, and he is appeased.\
The fog begins to subside, and you can see a beautiful view of the Golden Gate Bridge as the sun sets. \
Congratulations! You've made it in San Francisco. \
Now you can relax in your mansion in the Marina and sail ships all day. \
Awesomesauce - you won!", dictionary = {}, slug="the-end")
The_end_winner.save()

The_end_loser = Room(name="You lose :(", description="You try to use the mini-Erhu,\
but it has no effect. Guess fog monsters just don't like music. His Golden Gate-iness Karl the Fog\
decrees that you just didn't make it in the city. You pack up your bags and take the next flight out.", dictionary = {}, slug="you-lose")
The_end_loser.save()