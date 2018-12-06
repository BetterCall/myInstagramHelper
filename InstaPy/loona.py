"""
This template is written by @Mehran

What does this quickstart script aim to do?
- My quickstart is just for follow/unfollow users.

NOTES:
- It uses schedulers to trigger activities in chosen hours and also, sends me
  messages through Telegram API.
"""

# -*- coding: UTF-8 -*-
import time
from datetime import datetime
import schedule
import traceback
import requests
import random

from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = sys.argv[1]
insta_password = sys.argv[2]

# restriction data
dont_likes = ['#sex','#nude','#naked','#gun','#pussy']
ignore_list = ['sex','nude','naked','gun','pussy']


# FRIENDS data : Dont comment and unfollow
friends = ['zackaryrayann', 'rachel_971', 'tvcastingplus', 'loufitlove', 'yuzuki_fitness', 'liltonemorris', 'elsa_frenchgirl']
ignore_users = ['zackaryrayann', 'rachel_971', 'tvcastingplus', 'loufitlove', 'yuzuki_fitness', 'liltonemorris', 'elsa_frenchgirl']

# TARGET data : similar accounts and influencers
targets = [ 'jeremykohlanta','chakeup','barbaraopsomer','theogordy','lecoindelodie','jehovinh','gloomysarah','carolinemia_', 'sleepingbeautyytb',
'evamchd','beyourselfytb','ytbmanond','oceanefrc','iamgalla', 'corentinhuard', 'rsimacourbe', 'romaincosta_', 'valhery', 'bastoswithlove',
'diegoelglaoui', 'stefan_tisseyre', 'nicolassimoes', 'edgardlelegant','tristandefeuilletvang', 'lestudiodanielle', 'jimchapman',
'atrapenard', 'aline_dessine','badies.beauties', 'world__baddies', 'baddie.frr','badieseurope', 'postbadfrenchiies', 'baddiies.fr',
'meganvlt', 'julie_eden', 'marina_de_s', 'gaelle_vp', 'thebabooshka','camillejoun', 'laurievlltfit', 'chloe_tranchant', 'sarah.coulomb',
'coralie_slvt', 'mayliemartini','lea_spk', 'sabrinaboot_off', 'floorine_mtr','beauteactive', 'cameliiab', 'kaaayme','officiel_nass',
 'porrovecchiocoralie', 'nicolebernardes', 'romanegrandin', 'cecileshannon', 'sam_nounette','emmaprestifilippo', 'elsa_frenchgirl',
 'chloe_fit_', 'roxanebust', 'lucilejoseph_', 'capucine_cine','victoiremua', 'aline_dessine', 'mamzellesooz',
 'audmarshmaloo', 'marieandmood', 'mathilde_mu','jodielapetitefrenchie', 'ludivineoff', 'lilylovesfashion',
 'estherjunelife', 'paulinetrrs', 'lisagermaneau','meganvlt', 'julie_eden', 'marina_de_s', 'gaelle_vp', 'thebabooshka' ]

# COMMENT data
comments = ['comment1', 'comment2', 'comment3']


def get_session():
    session = InstaPy(username=insta_username,
                      password=insta_password,
                      headless_browser=False,
                      nogui=True,
                      multi_logs=False)

    session.set_quota_supervisor(
      enabled=True,
      sleep_after=["likes", "follows"],
      sleepyhead=True,
      stochastic_flow=True,
      notify_me=True,
      peak_likes=(100, 1000),
      peak_comments=(21, 250),
      peak_follows=(200, None) )

    session.set_dont_include( friends )
    session.set_dont_like( dont_likes )
    session.set_ignore_if_contains(ignore_list)
    session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=False)
    session.set_relationship_bounds( enabled=True,
                                   potency_ratio=None,
                                   delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=900,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=2 )

    session.set_skip_users( skip_no_profile_pic=True )

    session.set_user_interact( amount=5, randomize=True, percentage=80, media='Photo' )
    session.set_do_like( enabled=True, percentage=100 )
    session.set_do_comment(enabled=False, percentage=1)
    #session.set_comments([comments], media='Photo')
    session.set_do_follow(enabled=False, percentage=5, times=1)


    return session


def interact():
    # get a session!
    session = get_session()

    number = random.randint(5, 9)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)


    # Interact with the chosen targets...
    session.interact_user_followers(random_targets, amount=random.randint(30,60), randomize=True)


def follow():
    # Send notification to my Telegram
    requests.get(
        "https://api.telegram.org/******&text='InstaPy Follower Started @ {}'"
        .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        counter = 0

        while counter < 5:
            counter += 1

            try:
                # settings
                session.set_relationship_bounds(enabled=True, potency_ratio=1.21)

                # activity
                session.follow_by_tags(['tehran','تهران'], amount=5)
                session.follow_user_followers(['donya', 'arat.gym'], amount=5, randomize=False)
                session.follow_by_tags(['کادو','سالن','فروشگاه','زنانه','فشن','میکاپ','پوست','زیبا'], amount=10)
                session.follow_by_tags(['لاغری','خرید_آنلاین','کافی_شاپ','گل'], amount=5)
                session.unfollow_users(amount=25, allFollowing=True, style="LIFO", unfollow_after=3*60*60, sleep_delay=450)

            except Exception:
                print(traceback.format_exc())

    # Send notification to my Telegram
    requests.get("https://api.telegram.org/******&text='InstaPy Follower Stopped @ {}'"
                    .format(datetime.now().strftime("%H:%M:%S")))



def unfollow():
    requests.get("https://api.telegram.org/******/sendMessage?chat_id=*****&text='InstaPy Unfollower Started @ {}'"
                    .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=600, allFollowing=True, style="RANDOM", sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    requests.get("https://api.telegram.org/******/sendMessage?chat_id=*****&text='InstaPy Unfollower Stopped @ {}'"
                    .format(datetime.now().strftime("%H:%M:%S")))



def xunfollow():
    requests.get("https://api.telegram.org/******/sendMessage?chat_id=*****&text='InstaPy Unfollower WEDNESDAY Started @ {}'"
                    .format(datetime.now().strftime("%H:%M:%S")))

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=1000, allFollowing=True, style="RANDOM", unfollow_after=3*60*60, sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    requests.get("https://api.telegram.org/******/sendMessage?chat_id=*****&text='InstaPy Unfollower WEDNESDAY Stopped @ {}'"
                    .format(datetime.now().strftime("%H:%M:%S")))


# schedulers
schedule.every().day.at("7:30").do(interact)
schedule.every().day.at("13:30").do(interact)
schedule.every().day.at("17:33").do(interact)

#schedule.every().day.at("00:05").do(unfollow)

#schedule.every().wednesday.at("03:00").do(xunfollow)


while True:
    schedule.run_pending()
    time.sleep(1)
