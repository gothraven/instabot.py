#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login=os.environ.get('INSTA_USER', ''),
    password=os.environ.get('INSTA_PASSWORD', ''),
    start_at_h=13,
    start_at_m=46,
    end_at_h=17,
    end_at_m=45,
    like_per_day=3000,
    comments_per_day=2000,
    tag_list=['fuckology', 'fuckologyquotes', 'quotes',
            'follow', 'morningvibes', 'morning', 'goodmorning',
            'photography', 'love', 'instagood', 'morningmotivation',
            'sunrise', 'sky', 'photooftheday', 'happy', 'picoftheday',
            'goodvibes', 'naturephotography', 'like', 'sun', 'indiea',
            'lifestyle', 'mornings', 'travel', 'ig', 'tea', 'photo',
            'positivevibes', 'bhfyp', 'fucklove', 'comments', 'creativity',
            'bestoftheday', 'follow', 'fun', 'funny', 'cool', 'amazing',
            'awesome', 'friends', 'quote', 'quotes', 'comment', 'word',
            'fuckology', 'fuckologyquotes', 'fuckology', 'quotes',
            'motivation', 'follow', 'inspiration', 'instagood',
            'quoteoftheday', 'poetry', 'motivationalquotes',
            'lifequotes', 'inspirationalquotes', 'quotestoliveby'],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=51,
    follow_per_day=0, #follow_per_day = 500
    follow_time=0, #follow_time=1 * 60 * 60,
    unfollow_per_day=0, #unfollow_per_day=300
    unfollow_break_min=0, #unfollow_break_min=15 * 60,
    unfollow_break_max=0, #unfollow_break_max=30 * 60
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=[['👆', '👌', '💪'],
                  ['😎', '😍', '😉'],
                  ['🤙', '👍']],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
        'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
        'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
        'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
        'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
        'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
        'follow', 'follower', 'gain', '.id', '_id', 'bags'
    ],
    unfollow_whitelist=[])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        bot.bot_mode = 3
        while(bot.login_status == 1):
            bot.unfollow_recent_feed()
            time.sleep(5)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
