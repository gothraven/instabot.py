#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from instabot_py import InstaBot

bot = InstaBot(
    login=os.environ.get('INSTA_USER', ''),
    password=os.environ.get('INSTA_PASSWORD', ''),
    start_at_h=8,
    start_at_m=0,
    end_at_h=23,
    end_at_m=0,
    like_per_day=800,
    comments_per_day=200,
    tag_list=[
        'l:212999109', #Los Angeles
        'l:6889842', #Paris
        'l:219370504', #Algers
        'l:213326726', #Warsaw
        'l:213385402', #London
        'change', 'lavieestbelle', 'doglover', 'tweegram', 'nature', 'cool', 'cat', 'cutie', 'onedirection', 'black',
        'igparis', 'igersparis', 'fuckology', 'red', 'music', 'inspiration', 'dogsofinstagram', 'bestoftheday',
        'white', 'goodmorning', 'instagramhub', 'school', 'green', 'nofilter', 'iphonesia', 'petsagram',
        'celibataire', 'doglovers', 'girl', 'pretty', 'travel', 'halloween', 'bored', 'adorable', 'precious',
        'motivationalquotes', 'equipedefrance', 'clouds', 'puppies', 'ilovedog', 'hair', 'summer', 'blue',
        'awesome', 'petstagram', 'night', 'versagram', 'dogoftheday', 'quotestoliveby', 'picpets', 'instagramers',
        'party', 'animals', 'yum', 'dogs', 'igers', 'iphoneonly', 'positivevibes', 'lyon', 'amazing', 'photo',
        'cute', 'love', 'puppy', 'parisienne', 'pet', 'parisien', 'food', 'bleublancrouge', 'sweet', 'lifequotes',
        'comment', 'girls', 'repost', 'fuckologyquotes', 'animal', 'parisjetaime', 'family', 'naturephotography',
        'morningmotivation', 'goodvibes', 'quote', 'igdaily', 'ilovemydog', 'morningvibes', 'quoteoftheday',
        'lol', 'word', 'friends', 'bestfriend', 'beautiful', 'igaddict', 'instadaily', 'pets', 'indiea',
        'instamood', 'sun', 'swag', 'life', 'mornings', 'instagood', 'allezlesbleus', 'throwbackthursday',
        'sunrise', 'me', 'parismonamour', 'poetry', 'funny', 'instagramdogs', 'harrystyles', 'baby', 'happy',
        'igfrance', 'all_shots', 'fashion', 'ilovedogs', 'ig', 'follow', 'bordeaux', 'smile', 'tagblender',
        'creativity', 'allezlesbleues', 'lifestyle', 'sunset', 'photooftheday', 'followback', 'photography',
        'pink', 'inspirationalquotes', 'instahub', 'jj', 'picstitch', 'like', 'dog', 'comments', 'followme',
        'doggy', 'instalove', 'eyes', 'motivation', 'impatience', 'hot', 'picoftheday', 'tail', 'tea', 'my',
        'yummy', 'fucklove', 'fitfrenchies', 'tbt', 'instago', 'naturel', 'quotes', 'morning', 'beach', 'art',
        'jj_forum', 'paris', 'sky', 'pup', 'dogstagram', 'fun', 'bhfyp',
    ],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=10,
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
