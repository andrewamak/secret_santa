import random
import os

participants = []
gift_givers = []
recipients = []

#adding people to the secret santa list using input
print('List participants (press ENTER twice to stop): ')
while True:
    add_people = input("")
    add_people = add_people.strip()
    add_people = add_people.title()

    if add_people == "":
        break
    else:
        participants.append(add_people)
random.shuffle(participants)

#using shuffled participants to generate two parallel lists:
    # gift_givers and their corresponding recipients

count = 0
for i in range(len(participants)-1):
    gift_givers.append(str(participants[count + 1]))
    recipients.append(str(participants[count]))
    count += 1

gift_givers.append(str(participants[0]))
recipients.append(str(participants[-1]))
os.system('clear')

while True:
    try:
    #the random integer portion is necessary to avoid patterns
        pick = random.randint(0, (len(gift_givers) - 1))
        print(gift_givers[pick] + ' is giving a gift to... ')
        pause = input('')
        print(recipients[pick])
        pause = input('Press enter to continue')
        gift_givers.pop(pick)
        recipients.pop(pick)
    #clear the output every cycle in order to maintain gift giver privacy
        os.system('clear')
    except:
        break



print('Done!')