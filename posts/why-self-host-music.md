---
title: why do I self-host my music?
date: 2026-08-30
description: a explanation of why I dont just use spotify.
tags: [homelab, selfhosted, music]
---

many ppl always ask me:

"matei, why not just use Spotify like everyone else? Why even bother maintaining a music library when you could just easily have it all in one place?"

and those are good questions, and it boils down to *preference* and *cost*

# a bit of a backstory first

I actually used to use Spotify like everyone else and **not** the free version either, the paid one and it was great honestly, I could download all my music and listen offline, no ads at all, and all of that good stuff, andddd thats until I calculated how expensive it was after a while, and as I was hearing that Spotify might increase prices soon I was very sure I didnt want to keep paying for this.

..so I researched and eventually found Navidrome which was AWESOME, most features spotify had (besides the massive library ofc) but for free! So I started researching it and such and I set it up on my PC to test it first and it worked fine I even put some songs on it and was amazed how it worked even on other devices so I decided to self-host it

# my first setup

So I was completely new to self-hosting back then so clearly *I had no idea what I was doing*, and no reading the docs is not what I do because thats lame and for smelly nerds ngl

I bought a Hetzner VPS (which was cheaper then my spotify subscription), and decided to host it there, it was ofc a small VPS one of those shared ones IIRC, so it wasnt fast or anything but it was mine sooo it was great, anyway so I went ahead and set up Navidrome on there using docker (my first time using it smh, now I use it for everything) and put some of my songs I uploaded it on the server via ```rsync``` (my beloved), at that time I didnt really have much experience using *very legal sources to get music from* so I just used yt-dlp, which made the quality really, REALLY bad, like mp3 120kbps I think, but hey it worked so its a win, I used cloudflare tunnels to expose it to the internet and it was all good, and I was thrilled to see that last.fm works by default on Navidrome (I mean i think i did have to put some api keys but besides that it was fire) at that time I discovered apps like **Tempo** and **Aonsoko** which worked great honestly (I now use other clients like Navic and Feishin but thats a story for another time)

ofc this system had its flaws such as poor music quality and the fact that the vps had only 50gb of storage but it worked just fine for me

# my current setup (aka homelab)

just 3 months after my first setup I realized I rather not pay for a VPS either, so I found a old laptop and plugged it in, turned off sleep, closed the lid and voilà we have a homelab (refer to [this](https://blog.devmatei.com/blog/my-homelab) blog post for the specs of my homelab) then I setup Navidrome again on it, moved the db over and the library and it worked just fine again, but free (as I dont pay the electricity bill lmfao), then I had a suggestion to replace my MP3s with FLACs and since I was dumb back then I didnt know what is a FLAC I just ignored that guy, after a while tho I did found out what FLACs are and I now really wanted my library to be lossless, so I basically deleted all my MP3s and started finding how to get FLACs, now i wont disclose the *api* which some might even call *hi-fi* and works great and its on github (im not slick am i) for copyright reasons but anyway, I managed to get all my old songs + most major artists in lossless quality which was great (and it was like 50gb which mind you was exactly what my VPS had in total) and it was great and I really liked the FLACs and I didnt ever think i'd need more or my library would be any bigger then that.. (slight foreshadowing)

# well it did get bigger then that

now its almost 1TB... well I'm sure my ISP hates me now but hey at least i have a lot of music right guys??

long story short I made a lil script to download songs for me from 70 major artists and after 78hrs of running it downloaded all this, now I literally have a little Spotify in my home I dont even have to add new songs cuz most of the times all the songs I need are already there which is just crazy to me

# tldr to answer the question

self-hosting is cheaper for me then paying a big corpo and I get all features I want for free which is just peak and its also very convenient which may be counter-intuitive since you have to maintain it and such but its really just fun to and I got a lot of sysadmin experience from this and now I am very comfortable with Linux and self-hosting stuff lol 

ofc do not pirate and its very bad you should def support the big corpos and its highly unethical and ilegal according to the corpos  
 