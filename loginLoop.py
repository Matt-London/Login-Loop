#!/usr/bin/python3
from robobrowser import RoboBrowser
from random_word import RandomWords
import datetime
import random
import names
import time

## Change the following if needed
loginURL = "" # URL to login form
formID = "" # form ID
firstTerm = "email" # name of first term, default email
secondTerm = "pass" # name of second term, default pass
emailExt = ["aol.com", "att.net", "comcast.net", "facebook.com", "gmail.com", "gmx.com", "googlemail.com", "google.com", "hotmail.com", "hotmail.co.uk", "mac.com", "me.com", "mail.com", "msn.com", "live.com", "sbcglobal.net", "verizon.net", "yahoo.com", "yahoo.co.uk", "email.com", "fastmail.fm", "games.com", "gmx.net", "hush.com", "hushmail.com", "icloud.com", "iname.com", "inbox.com", "lavabit.com", "love.com", "outlook.com", "pobox.com", "protonmail.ch", "protonmail.com", "tutanota.de", "tutanota.com", "tutamail.com", "tuta.io", "keemail.me", "rocketmail.com", "safe-mail.net", "wow.com", "ygm.com", "ymail.com", "zoho.com", "yandex.com", "bellsouth.net", "charter.net", "cox.net", "earthlink.net", "juno.com", "btinternet.com", "virginmedia.com", "blueyonder.co.uk", "freeserve.co.uk", "live.co.uk", "ntlworld.com", "o2.co.uk", "orange.net", "sky.com", "talktalk.co.uk", "tiscali.co.uk", "virgin.net", "wanadoo.co.uk", "bt.com", "sina.com", "sina.cn", "qq.com", "naver.com", "hanmail.net", "daum.net", "nate.com", "yahoo.co.jp", "yahoo.co.kr", "yahoo.co.id", "yahoo.co.in", "yahoo.com.sg", "yahoo.com.ph", "163.com", "yeah.net", "126.com", "21cn.com", "aliyun.com", "foxmail.com", "hotmail.fr", "live.fr", "laposte.net", "yahoo.fr", "wanadoo.fr", "orange.fr", "gmx.fr", "sfr.fr", "neuf.fr", "free.fr", "gmx.de", "hotmail.de", "live.de", "online.de", "t-online.de", "web.de", "yahoo.de", "libero.it", "virgilio.it", "hotmail.it", "aol.it", "tiscali.it", "alice.it", "live.it", "yahoo.it", "email.it", "tin.it", "poste.it", "teletu.it", "mail.ru", "rambler.ru", "yandex.ru", "ya.ru", "list.ru", "hotmail.be", "live.be", "skynet.be", "voo.be", "tvcablenet.be", "telenet.be", "hotmail.com.ar", "live.com.ar", "yahoo.com.ar", "fibertel.com.ar", "speedy.com.ar", "arnet.com.ar", "yahoo.com.mx", "live.com.mx", "hotmail.es", "hotmail.com.mx", "prodigy.net.mx", "yahoo.com.br", "hotmail.com.br", "outlook.com.br", "uol.com.br", "bol.com.br", "terra.com.br", "ig.com.br", "itelefonica.com.br", "r7.com", "zipmail.com.br", "globo.com", "globomail.com", "oi.com.br"]

## Special thanks to Gaurav Jain on Quora for the RoboBrowser setup
# Setup before the loop
rw = RandomWords()
browser = RoboBrowser(parser='html.parser')
browser.open(loginURL)
form = browser.get_form(id=formID)
counter = 1
waitBetweenIter = 100 + random.randint(0, 99 + random.randint(-12, 17))

try:
    while(True):
        start = time.time()
        tempRand = random.randint(0, 2)
        email = ""
        if tempRand == 0: # gives word, num
            email = "{}{}@{}".format(rw.get_random_word(hasDictionaryDef="true"), str(random.randint(0, 12 + tempRand)), emailExt[random.randint(0, len(emailExt) - 1)])
        elif tempRand == 1: # gives name, num
            email = "{}{}@{}".format(names.get_first_name(), str(random.randint(0, 15 + tempRand)), emailExt[random.randint(0, len(emailExt) - 1)])
        elif tempRand == 2: # gives name, word or word name --- rand order
            if random.randint(0, 1) == 0: # name, word
                email = "{}{}@{}".format(names.get_first_name(), rw.get_random_word(hasDictionaryDef="true"), emailExt[random.randint(0, len(emailExt) - 1)])
            else: # word, name
                email = "{}{}@{}".format(rw.get_random_word(hasDictionaryDef="true"), names.get_first_name(), emailExt[random.randint(0, len(emailExt) - 1)])
        else:
            print("Error")
            continue
        password = ""
        tempRand = random.randint(0, 1)
        if tempRand == 0: # word, number, last name or word, last name, number
            if random.randint(0, 1) == 0: # word, num, last name
                password = "{}{}{}".format(rw.get_random_word(hasDictionaryDef="true"), str(random.randint(0, 20 + tempRand)), names.get_last_name())
            else: # word, last name, num
                password = "{}{}{}".format(rw.get_random_word(hasDictionaryDef="true"), names.get_last_name(), str(random.randint(0, 20 + tempRand)))
        elif tempRand == 1: # word, num or num, word
            if random.randint(0, 1) == 0: # word, num
                password = "{}{}".format(rw.get_random_word(hasDictionaryDef="true"), str(random.randint(0, 30 + tempRand)))
            else: # num, word
                password = "{}{}".format(str(random.randint(0, 23 + tempRand)), rw.get_random_word(hasDictionaryDef="true"))

        ## Submit it
        form[firstTerm].value = email
        form[secondTerm].value = password
        try:
            browser.submit_form(form)
        except:
            print("error in submit")
            continue
        print("{}. Email: {} Password: {}\t{} seconds".format(counter, email, password, round(time.time() - start, 2)))

        # After 100ish sends wait 10 ish minutes, after each send wait twentyish seconds
        if counter == waitBetweenIter:
            time.sleep(600 + random.randint(-23 + random.randint(-5, 5), 18 + random.randint(-4, 4)))
            waitBetweenIter = 100 + random.randint(0, 99 + random.randint(-12, 17))
        else:
            time.sleep(20 + random.randint(-4 + random.randint(1, 3), 10 + random.randint(-1, 4)))

        counter += 1


except KeyboardInterrupt:
    print("Shutting down at:\n{}".format(str(datetime.datetime.now())))
