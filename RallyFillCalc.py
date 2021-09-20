def Intro():
    send = int(input('\n What rally comp? '))

    split = [int(x) for x in str(send)]
    inf = split[0]
    rng = split[1]
    cav = split[2]

    if inf + rng + cav == 10:
        inf = inf * 2
        rng = rng * 2
        cav = cav * 2
    elif inf + rng + cav != 20:
        print(' Hey dumbass, the numbers should add up to 10 or 20. Try again')
        Intro()

    number = int(input(' How many troops are you sending? ') or '200')
    percent = int(input(' What percentage of T5? ') or '60')

    t5perc = percent / 100
    t4perc = 1 - t5perc

    infSendPercent = inf * 5
    rngSendPercent = rng * 5
    cavSendPercent = cav * 5

    infSend = (infSendPercent / 100) * number
    rngSend = (rngSendPercent / 100) * number
    cavSend = (cavSendPercent / 100) * number

    print('\n Inf T5 -', infSend * t5perc, ' Inf T4 -', infSend * t4perc, '\n Range T5 -', rngSend * t5perc,
          'Range T4 -', rngSend * t4perc, '\n Cav T5 -', cavSend * t5perc, 'Cav T4 -', cavSend * t4perc)
    Intro()


if __name__ == '__main__':
    print('\n Rally Fill Calculator')
    print(' Enter the comp asked for by the rally lead, the number of troops you are sending and the percentage of T5 (if less than 60% you\'re a bitch)')
    Intro()
