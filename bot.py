#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login=os.environ.get('ABRICOT_INSTA_USERNAME', ''),
    password=os.environ.get('ABRICOT_INSTA_PASSWORD', ''),
    start_at_h=10,
    start_at_m=0,
    end_at_h=18,
    end_at_m=0,
    like_per_day=1000,
    comments_per_day=120,
    max_like_for_one_tag=50,
    tag_list=[
        'parisien', 'parisienne', 'paris', 'igparis', 'igersparis', 'lavieestbelle',
        'fitfrenchies', 'celibataire', 'impatience', 'parisjetaime', 'parismonamour', 'igfrance',
        'bordeaux', 'lyon', 'bleublancrouge', 'allezlesbleus', 'allezlesbleues', 'equipedefrance', 'naturel'
    ],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    follow_per_day=0, # 300
    follow_time=0, # 1 * 60 * 60
    unfollow_per_day=0, # 300
    unlike_per_day=0,
    time_till_unlike=0, # 3 * 24 * 60 * 60
    unfollow_break_min=0, # 15
    unfollow_break_max=0, # 30
    user_max_follow=0,
    # session_file=False, # Set to False to disable persistent session, or specify custom session_file (ie ='myusername.session')
    user_min_follow=0,
    log_mod=0,
    proxy='',
    # List of list of words, each of which will be used to generate comment
    comment_list=[
        ['🍑','⭐️','👌','🙏','💪','👏','😬','😍','🧡','✌️','☀️','🎉','😎','😯','😉','😘','😈','😻','🤙'],
        ['🍑','⭐️','👌','🙏','💪','👏','😬','😍','🧡','✌️','☀️','🎉','😎','😯','😉','😘','😈','😻','🤙'],
        ['🍑','⭐️','👌','🙏','💪','👏','😬','😍','🧡','✌️','☀️','🎉','😎','😯','😉','😘','😈','😻','🤙'],
    ],
    # Use unwanted_username_list to block usernames containing a string
    # Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    # 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog', 'free',
        'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop', 'store', 'sex',
        'toko', 'jual', 'online', 'murah', 'jam', 'kaos', 'case', 'baju', 'fashion',
        'corp', 'tas', 'butik', 'grosir', 'karpet', 'sosis', 'salon', 'skin', 'care',
        'cloth', 'tech', 'rental', 'kamera', 'beauty', 'express', 'kredit', 'collection',
        'impor', 'preloved', 'follow', 'follower', 'gain', '.id', '_id', 'bags',
    ],
    unfollow_whitelist=['example_user_1', 'example_user_2'],
)

bot.mainloop()
