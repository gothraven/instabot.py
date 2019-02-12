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
    start_at_h=9,
    start_at_m=0,
    end_at_h=20,
    end_at_m=0,
    like_per_day=2000,
    comments_per_day=1000,
    tag_list=[
        'fuckology', 'fuckologyquotes', 'quotes', 'follow', 'morningvibes', 'morning', 'goodmorning',
        'photography', 'love', 'instagood', 'morningmotivation', 'sunrise', 'sky', 'photooftheday', 'happy',
        'picoftheday', 'goodvibes', 'naturephotography', 'like', 'sun', 'indiea', 'lifestyle', 'mornings',
        'travel', 'ig', 'tea', 'photo', 'positivevibes', 'bhfyp', 'fucklove', 'comments', 'creativity',
        'bestoftheday', 'follow', 'fun', 'funny', 'cool', 'amazing', 'awesome', 'friends', 'quote', 'quotes',
        'comment', 'word', 'fuckology', 'fuckologyquotes', 'fuckology', 'quotes', 'motivation', 'follow',
        'inspiration', 'instagood', 'quoteoftheday', 'poetry', 'motivationalquotes', 'lifequotes', 'inspirationalquotes',
        'quotestoliveby', 'parisien', 'parisienne', 'paris', 'igparis', 'igersparis', 'lavieestbelle', 'fitfrenchies',
        'celibataire', 'impatience', 'parisjetaime', 'parismonamour', 'igfrance', 'bordeaux', 'lyon', 'bleublancrouge',
        'allezlesbleus', 'allezlesbleues', 'equipedefrance', 'naturel'
    ],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=27,
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

bot.mainloop()
