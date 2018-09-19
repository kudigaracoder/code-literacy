#!/usr/bin/python
# -*- coding: utf-8 -*-

relation = raw_input("Someone you know (girlfriend/wife/sister):")
expression = raw_input("You felt (anger/astonishment/sad/fright):")
maxspeed = raw_input("Fastest speed you've gone (km/h):")
minspeed = raw_input("Slowest speed (km/h):")
neighborhood = raw_input("A neighborhood you've recently been in:")
road = raw_input("Road recently traveled:")
age = raw_input("How old are you?:")
friend = raw_input("Your best friend's name")

short_story = "Hmm... said Walter Mitty. He looked at his " + relation + " in the seat beside him, with shock and " + expression + \
". She seemed grossly unfamiliar, like a strange woman who had yelled at him in a crowd. You were up to " + maxspeed + \
". You know I don’t like to go more than " + minspeed + " You were up to " + maxspeed + \
". Walter Mitty drove on toward " + neighborhood + " in silence, the roaring of the " + road + " through the worst storm in " + age + \
" of Navy flying fading in the remote, intimate airways of his mind. You’re tensed up again, said your " + relation + \
". It’s one of your days. I wish you’d let Dr." + friend + " look you over."

print(short_story)