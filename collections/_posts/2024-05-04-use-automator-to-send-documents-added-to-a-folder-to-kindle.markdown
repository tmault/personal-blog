---
layout: post
title: Automatically Send New Documents in a Folder to Kindle with Automator
date: "2024-05-04 07:03:46"
tags:
  - Productivity
  - Technology
categories:
  - Productivity
  - Technology
excerpt: In this blog post, I explain how I use Automator on my Mac to automate sending documents directly to my Kindle. I set up a particular folder where any files I add (like PDFs, ePub, or Mobi files) are automatically emailed to my Kindle through an Automator folder action. 
featured_image: /assets/images/2024/05/CleanShot-2024-05-04-at-09.02.47-2.png
published: True
---
Here's a simple use case for using Automator on the Mac to make your life easier. I am lazy, and if I repeat an action too many times, I try to automate it to make life easier.

I often want to send documents to my Kindle from my Mac. An example would be PDFs, ePub, or Mobi files of eBooks. I wanted to create a folder on my Mac that would automatically forward any files added to it straight to my Kindle. Here's how to set it up. Thank you to _Underdub_ , who posted about a similar process on the Apple forum in 2014 [here](https://discussions.apple.com/thread/6154643?sortBy=best).

## How to configure Automator to forward files to Kindle.

Open Automator on your Mac and create a new **Folder Action**.

![](/assets/images/2024/05/CleanShot-2024-05-04-at-09.02.47.png)

### Make a new folder

Select or create a new folder. I called mine _03.19 Send to Kindle_. That naming convention is a story for another day.

![](/assets/images/2024/05/CleanShot-2024-05-04-at-09.04.35.png)

### Configure the actions

Now set the following actions in Automator:

  1. Launch Application: **Mail**
  2. New Mail Message
    1. To: **Enter your send to kindle address**
    2. Subject: Enter something to identify the email e.g. "Document for kindle"
  3. Add Attachments to Front Message
  4. Send Outgoing Messages



Automator should look something like this:

![](/assets/images/2024/05/CleanShot-2024-05-04-at-09.09.29.png)

Press CMD + S to save the folder action. The first time you add a file to your Send to Kindle folder, you must grant Automator permission to access Mail. Your Mac will prompt you for this automatically.

Now, whenever you drag and drop a file to your specified folder, Automator will automatically launch Mail, attach it, and send it to your Kindle. Neat!
