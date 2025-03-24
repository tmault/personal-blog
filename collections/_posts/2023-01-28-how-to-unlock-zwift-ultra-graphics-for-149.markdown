---
layout: post
title: How to unlock Zwift Ultra Graphics for £149
date: "2023-01-28 12:01:27"
tags:
  - Technology
  - Health
  - Cycling
categories:
  - Technology
  - Health
  - Cycling
excerpt: How to build a PC for less than £150 that is capable of playing Zwift on Ultra settings at about 45 to 50 frames per second.
featured_image: /assets/images/2023/01/5ff1ee1dd4857638c558798f_IMG_3851.jpeg
published: True
---
It doesn't sound plausible. £149 for a PC capable of playing [Zwift](https://www.zwift.com/invite/7KAtZUrbYf) at 4K with the Ultra graphics profile. You can upgrade a used office PC to outperform a brand new MacBook Air on Zwift, for 14% of the cost. Yes - a £150 used office PC runs Zwift better than a £1000 brand-new MacBook Air.

I used to run Zwift via my laptop. For a long time now this has meant a MacBooks, and I have always chosen lightweight and thin models that do not have dedicated graphics cards. Generally Macs with integrated graphics run Zwift on Medium settings at around 30 to 40 frames per second. If you have a MacBook with a dedicated graphics card, you will likely see better performance than this.

I discovered the easy process of upgrading a used office PC into a Zwift powerhouse on a Facebook group. They call their PCs frankensteins - machines cobbled together for a low cost from a combination of old used office PCs and a few choice upgrades that enable brilliant performance for Zwift. If you are thinking of undertaking a project like this, I very much recommend checking out the Zwift PC Master Race Facebook Group, Dave over there has created an immensely valuable resource with guides to creating a PC capable of playing Zwift well. The community is fantastically helpful and quick to respond to questions.

## Zwift looks fine on Basic / Medium settings... why should I bother upgrading to Ultra?

Why bother upgrading from whatever you are running Zwift on at the moment?

The shadows, the sunlight beaming onto the Watopian pavement, the details in the distance (was that mountain there before?!), the activity happening all around you as you ride. There are so many intricate little details that I just aren't in the game when you are below Ultra settings. There are dinosaurs, bears falling out of trees, brilliant details on little huts in the Alp. Upgrading to Ultra graphics adds a whole level of immersion to the Zwift universe.

You're going to be spending hours on your turbo trainer getting training rides in, so upgrading your experience for a relatively trivial sum (compared to what you have already spent on a Wahoo Kickr Core seems... sensible... right? That's what I told myself as I paid for a five year old computer on eBay one cold winter morning...

## The Base Unit

I chose to target the Lenovo E73 Small Form Factor (SFF) tower as the base for my design.

If I was going to do this again, I would probably spend another £100 or so and build a PC with standard, non-proprietary, motherboard and PSU, so that I could choose my PC case and use a more capable graphics card with an external power requirement. That said, if you're building a PC just for Zwift there's no real gain to spending more than about £400 on components. With Zwift there aren't currently any benefits of going above a graphics card like the NVIDIA 1650 super. Zwift just isn't optimised to take advantage of the power of the latest graphics cards like the 3060, 3070, or completely overkill 3090. Save your money and spend it on your real bike!

I set up alerts on eBay for \"Lenovo e73\" and a local seller of refurbished office PCs had several E73s available for collection, and the stunningly low price of £40 per unit. I ordered one, which came with:

  * Intel i3 4130 processor (3.4 GHz clock speed, fixed / no turbo boost)
  * 4GB DDR3 RAM
  * 500GB Hard Drive
  * 180 Watt Power Supply Unit



The e73 tends to be listed for anywhere between £40 and £70 - from what I can tell, so it's worth waiting for a seller to list one towards the lower end of this spectrum.

## GPU Installation

The main thing that takes a used office PC from end of its life, to a hard new life as a Zwifting powerhouse is added a graphics card. The Facebook group has a specific and very useful guide to identifying what graphics cards will meet your needs.

Thanks to a hint from the Zwift PCMR FaceBook Group I picked up a Gigabyte 1050 TI OC Low Profile graphics card for £109 from Laptops Direct. Given the current GPU shortages and general crazy prices floating around at the moment, I was quite pleased with this purchase. This model is perfect for the Small Form Factor PC case as it does not need a 6pin PSU power connection - the card can just pick up the power through the PCIe slot on the motherboard.

GPU Installation was very simple. As I chose a low profile graphics card there was no need to attach a power cable to the graphics card, it is just a case of slotting the graphics card into the PCIe x16 slot and screwing it into the backplate so it stays put.

The 1050 TI card is capable of running Zwift Ultra at 1440p at around 60 frames per second (outside of large groups), and around 45 to 50 frames per second at 4K.

## PSU Worries

The Lenovo E73 user manual states that the PCIe x16 slot is limited to providing 40 watts of power.

I initially thought this was going to be a problem, as the 1050 TI OC LP requires 75 watts of power via the PCIe slot.

In practice, I have found that the slot is not limited to 40 watts - it seems instead to be guidance provided by the manufacturer to prevent PSU overload. A comfortable margin of safety. Running a 1050 in this computer works - but it's outside the boundaries defined by the manufacturer so you choose to do so at your own risk!

## Adding 8GB of RAM

Zwift will limit the quality of textures in the game if you have less than 8GB of RAM. The Lenovo e73 uses DDR3 RAM. You can pick up a 4GB DDR3 stick of RAM for about £7 to £10 online. I ordered mine from a store called CEX, which buys and sells used hardware. Slotting in an extra stick of ram is a 30 second job and by far the simplest part of the upgrade.

## Popping in a SSD

Solid State Drives (SSDs) run much faster than the mechanical Hard Disks that most used office PCs will come with from the factory. Upgrading the PC to include a SSD is worthwhile. It will make the system very quick to boot and snappier in general. There's no need to spend much here - £20 or so on a 120GB SSD from Amazon is plenty for an installation of Zwift and Windows 10.

To install the SSD I removed the Disc Drive from the Lenovo. This freed up a SATA power and data cable, which I connected the SSD into. I then zip-tied the SSD onto one of the disc drive mounting plates. You could probably use double-sided 3m tape or similar to achieve a cleaner look, but it's inside the case so doesn't really matter.

The benefit of leaving the Hard Disk installed and adding an SSD alongside it is that I now had an extra 500Gb of storage left unused on the original HDD.

## Maxed Out Wi-Fi and Bluetooth Chip

I was planning to connect my Frankenstein PC to my Turbo Trainer via Bluetooth and internet via Wi-Fi. To ensure a solid and stable connection, I wanted a card with an Intel AX 3000 chip, which was capable of Bluetooth 5.0 and Wi-Fi 6.

I went for the Cudy WE3000 card, which was about £30 on Amazon. This device requires a USB power connection from the motherboard. I don't think the e73 has any spare internal USB headers, so I added a USB Header 1 to 2 splitter to the motherboard with cost £7 from iHaospace on Amazon. With the machine open, I disconnected the front USB header from the motherboard, plugged the splitter into the motherboard, then hooked up the power for the Cudy card and the front USB header. It worked perfectly!

In hindsight this was probably overkill, a £10 USB Wi-Fi and Bluetooth adapter probably would have done the trick.

## The Result

Ok so £149 is stretching downwards slightly - the total cost ended up edging towards £200 as I spent an extra £7 for another stick of RAM, if you don't have an SSD lying around, that's another £20, and a tenner or so for a USB Wi-Fi / Bluetooth chip.

This setup blows my MacBook M1 out of the water for running Zwift. Surprisingly it seems to be fairly capable of running many other games too. I have used it to try out a few games on Steam, like Euro Truck Simulator (surprisingly engrossing) and Forza Horizon (which plays surprisingly well at 1080p on medium settings). If you wanted a general productivity machine, I am blown away by how quick this PC performs daily routine tasks.

Upgrading to Ultra graphics has added another level of immersion and enjoyment to riding inside on my turbo trainer. Assembling the PC was a fun afternoon project, which will now be used for many hours of Zwifting. Ride on!
