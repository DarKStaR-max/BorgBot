"""QuickHeal Total Security Scan

Available Commands:

.quickheal
.sqh
.vquickheal"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 4

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "quickheal":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "sqh":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault: No Virus Found...`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "vquickheal":

        await event.edit(input_str)

        animation_chars = [
        
            "`Downloading File..`",
            "`File Downloaded....`",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 84%\n█████████████████████▒▒▒▒ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nFile Scanned... 100%\n█████████████████████████ `",
            "`Quick Heal Total Security Checkup\n\n\nSubscription: Pro User\nValid Until: 31/12/2099\n\nTask: 01 of 01 Files Scanned...\n\nReault:⚠️Virus Found⚠️\nMore Info: Torzan, Spyware, Adware\n\nPro User @DarKStaR2001 Can Fix This File For $69 Only.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
