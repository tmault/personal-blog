---
layout: post
title: My Favourite Obsidian Plugins
date: "2023-07-22 13:47:06"
tags:
  - Personal Development
  - Learning
  - Technology
categories:
  - Personal Development
  - Learning
  - Technology
excerpt: "The article showcases my four key Obsidian plugins: Readwise for syncing highlights, Tasks for tracking to-dos across notes, Omnisearch for enhanced search results, and Calendar for improved note navigation, enhancing my knowledge management workflow."
featured_image: /assets/images/2023/07/CleanShot-2023-07-22-at-16.16.48-2@2x.png
published: True
---
## Introduction

[Obsidian](obsidian.md) is my current note-taking platform of choice. It has all the features I like; link & graph based ways of connecting between notes, markdown formatting, simple transparent pricing, a privacy centric design, and you can pick where you files are stored (e.g. OneDrive, Dropbox, iCloud, or just locally). The files are stored as markdown text files, so it's super easy to export your files if you ever need them.

Plug-ins are a key part of the Obsidian architecture. There are lots of features built in, but a vibrant community of plug-ins add extra features and have laid the framework for people to build Obsidian into the tool that fits their ideal workflow. Extending Obsidian with new plug-ins is a fun part of the overall experience of fitting Obsidian into your personal knowledge management workflow.

##  **My history with Obsidian**

I came across Obsidian whilst studying Tiago Forte's Build a Second Brain course last year. Before that I was using Roam Research to store my notes, but in general I found Roam to be inconvenient due to not having an offline mode & a mobile app at the time that was pretty slow & clunky. I also didn't like how my data felt tied up in the roam ecosystem & did not feel easily accessible or exportable.

Since switching to Obsidian, there are a key few things I like:

  1. My data is mine & easily exportable if I decide to stop using Obsidian 
  2. I can choose where my obsidian markdown text files are stored
  3. I can have work related information in a work specific vault, that lives inside the cloud services work approves (OneDrive)
  4. Plug-ins allow me to tailor my Obsidian experience to the features that I like



That fourth item - plug-ins, is what I want to share a bit about today. In this article I am going to write about the four plug-ins that I use in 2023:

  1. Readwise Official integration - for syncing highlights from articles and Kindle
  2. Tasks - for showing all of my open tasks across all notes in 1 convenient place
  3. Omnisearch - because the default search experience in Obsidian is not as intuitive out of the box as you may expect 
  4. Calendar - which gives you an easy widget view of daily-notes



So - let's take a look at the plug-ins!

# My Favourite Obsidian Plug-ins in 2023

## Readwise Official Integration 

This is a simple plug-in published by [Readwise](https://readwise.io/i/tom290). Readwise is one of my favourite services - for a few dollars a month it provides an awesome inbox for all your reading (from articles saved across the web, to substack emails, to favourite tweets). It also acts as a super robust syncing service for highlights from Kindle. Readwise acts as the glue of my personal knowledge management system, automatically pulling together highlights from all my favourite sources. The Readwise Official plug-in allows you to export all of your highlights into Obsidian with no effort.

![](/assets/images/https://raw.githubusercontent.com/readwiseio/obsidian-readwise/master/screens/readwise_obsidian_export.gif)GIF produced by the Readwise team. You can see how it automatically pulls in book notes into Obsidian, and maintains all the key details, plus supplements it with metadata like the Author and Book Cover. 

I have the Readwise plug-in set to sync on start-up plus once every 60 minutes. It puts notes into my 03 - Resource folder (which you will recognise if you're a fan of the PARA folder system from Tiago Forte), and has sub-folders for Articles, Books, Tweets, and Podcast notes.

![](/assets/images/2023/07/CleanShot-2023-07-22-at-16.04.06@2x-1.png)

[Click here to install Readwise Official](obsidian://show-plugin?id=readwise-official).

## Tasks

[Tasks](obsidian://show-plugin?id=obsidian-tasks-plugin) is another critical app in my workflow. Tasks lets you query across your entire Obsidian vault, and find Tasks in any notes.

It's super easy to declare a task in Markdown:

![](/assets/images/2023/07/CleanShot-2023-07-22-at-16.07.25.gif)Declaring a task in Markdown is super easy, just type "- [ ]"

After a while of using Obsidian, I found that I was declaring tasks, but then losing them in my vault. I would have to remember where I flagged a task or action item, which just doesn't work.

That's where Tasks comes in; with some simple language you can run queries and return all open Tasks.

My query for this is:
[code]
    status.type is TODO
    path does not include 02 - Areas/Direction
    
[/code]

I have excluded any Tasks inside the directory _02 - Areas/Direction_ because these notes contain long term visions Tasks, that I don't need to see as part of my daily workflow.

I use Things 3 for primary Task management, so this part of my workflow is more about making sure I can see everything that's open in Obsidian, and decide whether to pick it up in Things. As an example, I might makes notes in a meeting and record an action item. At the end of my workday, I can have a quick scan of my Tasks page in Obsidian, and see any tasks I generated. My Tasks page in Obsidian looks like this:

## Omnisearch

The default search in Obsidian takes a bit of getting used to. If I am totally honest, I want a simple search box where I can whack some phrases in & see the content that I want. By default I found a search for a simple phrase like "time management" was finding all the documents that contain "time" and "management". In my case, there are over 5000 results across my notes.

You can see in the image below that the search for time management returns a lot of noise - 5000 plus results, and a load of places where the word 'time' appears. Great... but not quite what I was looking for...

![](/assets/images/2023/07/CleanShot-2023-07-22-at-16.20.30@2x.png)The default search experience in Obsidian returns hyper specific places where the exact word(s) you typed appear... not necessarily together 

[Omnisearch](obsidian://show-plugin?id=omnisearch) fixes that.

Here's the same query, boom - the 3rd note is actually the book I was trying to find:

![](/assets/images/2023/07/CleanShot-2023-07-22-at-16.19.38@2x.png)The Omnisearch experience is way better - I would describe this as the type of search tool you would expect Roam to have out of the box. The default search tool is super powerful, but I don't want to have to learn queries when I am lazy and used to quick searches providing meaningful relevant hits (thanks ... Google)

## Are you enjoying this article about Obsidian?

If you want to get an email whenever I share a post on a new tactic, tip, or tool, you can sign-up here. Thanks! Tom 

Subscribe

Email sent! Check your inbox to complete your signup. 

No spam. Unsubscribe anytime.

## Calendar

[Calendar](obsidian://show-plugin?id=calendar) is a super simple plug in that provides a daily view of your notes on the right hand side nav bar.

There's not too much to say - it's a simple app but it quickly becomes useful when you want to hop back to your meeting notes from last Wednesday.

![](/assets/images/2023/07/CleanShot-2023-07-22-at-16.24.09@2x.png)Highlighted areas show the Calendar plug-in

## Conclusion

So, there we have it - my favourite 4 plug-ins for Obsidian. 

I find the combo of these helps me be productive; I can capture Tasks quickly and elegantly right in my notes, and be confident I can find them later.

Readwise lets me get access to all of my notes from all of my reading; that feature alone is a game changer.

And Omnisearch lets me find content super quickly from across my personal knowledge management system. It's like having your own Google for everything you've ever highlighted or taken a note on.

And finally, Calendar acts as the glue to help you hop between recent notes and recall recent information in a time-based way.

  1. Brief summary of each plug-in discussed in the article
  2. Highlight the unique benefits of each plug-in



I love keeping an eye on the Obsidian community plug-in marketplace to see if any new tools arise. 

My suggestion would be to start simple, and extend your Obsidian Vault as you go. The Projects, Areas, Resources, Archive structure makes total sense with the folder based nature of Obsidian, and the graph & hyperlinking helps you glue everything together where you need to, and see links between ideas & concepts.

Are there any plug-ins you love for Obsidian? Let me know in the comments!
