"""
It was a school project for my little cousin
and we both solved it to compete :)

Sorry for Hungarian comments.
"""

from random import randint

# Alapfeladat

soldTickets = []

def random_generated_tickets():
    for i in range(8):
        soldTickets.append(randint(1, 1000))
        print('Az ' + str(i + 1) + '. órában eladott belépők száma: ' + str(soldTickets[i]))

# 1. Hány olyan óra volt, amikor több mint 800 látogatót fogadott a vidámpark?

def number_of_hours_over_800():
    overEightHundred = 0

    for i in range(0, len(soldTickets)):
        if (soldTickets[i] > 800):
            overEightHundred = overEightHundred + 1

    print(str(overEightHundred) + ' olyan óra volt, amikor több mint 800 látogatót fogadott a vidámpark.')

# 2. Nőtt-e a forgalom délután a délelőtthöz képest?

def is_traffic_higher_at_pm():
    ticketsAm = 0
    ticketsPm = 0

    for i in range(0, len(soldTickets)):
        if (i <= 3):
            ticketsAm = ticketsAm + soldTickets[i]
        else:
            ticketsPm = ticketsPm + soldTickets[i]

    if (ticketsAm < ticketsPm):
        print('A forgalom a délelőtthöz képest nőtt!')
    elif (ticketsAm > ticketsPm):
        print('A forgalom a délelőtthöz képest csökkent!')
    else:
        print('A forgalom ugyanakkora volt délelőtt és délután is.')

# 3. Igaz-e, hogy legtöbb látogató egy délutáni órában volt?

def is_visitor_number_higher_afternoon():
    highestHour = 0
    highestHourIndex = 0

    for i in range(0, len(soldTickets)):
        if (soldTickets[i] > highestHour):
            highestHour = soldTickets[i]
            highestHourIndex = i

    if (highestHourIndex <= 3):
        print('A legtöbb látogató egy délelőtti órában volt.')
    else:
        print('A legtöbb látogató egy délutáni órában volt.')

# 4. Kérd be egy óra sorszámát (a nyitástól számítva) és határozd meg, hogy a forgalom akkor meghaladta-e az azt megelőző órait? (A nyitást követő órával természetesen nem kell foglalkoznod)

def is_previous_hour_higher():
    usrHour = input('Add meg egy óra sorszámát! (1 - 8) ' )
    usrIndex = int(usrHour) - 1

    if (usrIndex == 0):
        print('Ez a nyitóóra, az előző óra nem mérhető!')
    else:
        if (soldTickets[usrIndex - 1] < soldTickets[usrIndex]):
            print('A forgalom meghaladta az előző órait!')
        elif (soldTickets[usrIndex - 1] > soldTickets[usrIndex]):
            print('A forgalom nem haladta meg az előző órait!')
        else:
            print('A forgalom pont ugyanannyi mint az előző órában!')

# 5. Volt-e 100 fő alatti vendégszám valamelyik órában?

def any_hours_below_100_visitors():
    isUnderHundred = False

    for i in range(0, len(soldTickets)):
        if (soldTickets[i] < 100):
            isUnderHundred = True

    if (isUnderHundred):
        print('Volt olyan óra amikor 100 alatti vendégszám volt.')
    else:
        print('Nem volt 100 alatti vendégszám egyik órában sem.')

# Függvények meghívása

random_generated_tickets()
number_of_hours_over_800()
is_traffic_higher_at_pm()
is_visitor_number_higher_afternoon()
is_previous_hour_higher()
any_hours_below_100_visitors()