import random
from instapy import InstaPy
from instapy.util import smart_run


# login credentials
insta_username = 'username'
insta_password = 'password'

# restriction data
dont_likes = ['#sex','#nude','#naked','#gun','#pussy']
ignore_list = ['sex','nude','naked','gun','pussy']


# FRIENDS data : Dont comment and unfollow
friends = ['zackaryrayann', 'rachel_971', 'tvcastingplus', 'loufitlove', 'yuzuki_fitness', 'liltonemorris', 'elsa_frenchgirl']
ignore_users = ['zackaryrayann', 'rachel_971', 'tvcastingplus', 'loufitlove', 'yuzuki_fitness', 'liltonemorris', 'elsa_frenchgirl']


# TARGET data : similar accounts and influencers
targets = [ 'jeremykohlanta','chakeup','barbaraopsomer','theogordy','lecoindelodie','jehovinh','gloomysarah','carolinemia_', 'sleepingbeautyytb', 'evamchd','beyourselfytb','ytbmanond','oceanefrc']
# COMMENT data
comments = ['comment1', 'comment2', 'comment3']

# get a session!
session = InstaPy(username=insta_username,
                      password=insta_password,
                        headless_browser=False,
                          disable_image_load=True,
                            multi_logs=True)

# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
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


    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(4, 6)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    """ Interact with the chosen targets...
    """
    session.follow_user_followers(random_targets, amount=random.randint(30,60), randomize=True, sleep_delay=600, interact=True)


    # UNFOLLOW activity
    """ Unfollow nonfollowers after one day...
    """
    session.unfollow_users(amount=random.randint(75,100), InstapyFollowed=(True, "nonfollowers"), style="FIFO", unfollow_after=24*60*60, sleep_delay=600)

    """ Unfollow all users followed by InstaPy after one week to keep the following-level clean...
    """
    session.unfollow_users(amount=random.randint(75,100), InstapyFollowed=(True, "all"), style="FIFO", unfollow_after=168*60*60, sleep_delay=600)



"""
Have fun while optimizing for your purposes, Nuzzo
"""
