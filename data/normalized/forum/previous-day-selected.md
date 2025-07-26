# Previous day selected

## Question

**Ric** asked on 21 Jun 2019

When selecting a date in the picker, it binds 1 day less to the picker.

## Answer

**Marin Bratanov** answered on 24 Jun 2019

Hello Rick, This seems to work fine for me. I'm attaching below the page I tested with, and a short video of the behavior I get. Am I missing something? Can you confirm you are on 1.2.0 and .NET Core Preview 6? Regards, Marin Bratanov

### Response

**Rick** answered on 24 Jun 2019

Hi Marin, I am using preview 6 and am using 1.2. This happened after the upgrade to 1.2, it was fine in 1.1. It is also broke in the demo. [https://demos.telerik.com/blazor-ui/datepicker/index](https://demos.telerik.com/blazor-ui/datepicker/index)

### Response

**Marin Bratanov** answered on 24 Jun 2019

Hi Rick, The demo seems to work fine for me too. I'm attaching a short video of what I see, so you can confirm if there is a step I am missing. Can you also record a short video that shows how to reproduce this behavior? Considering that I also saw a couple of other rather strange reports from you today, I'd suggest you try repairing the VS 2019 Preview and .NET Core 3 installations that you have, and to also try with the browser in incognito mode to disable extensions. We have not had other such reports and our tests don't reproduce such behavior, which leads me to believe that there may be something quite particular in the current environment that causes these problems. Regards, Marin Bratanov

### Response

**Rick** answered on 24 Jun 2019

Hi Marin, I guess I actually haven't verified yet if the date in code is correct, I was going off of the displayed date. I can't attach a video, your forum doesn't allow a video upload, maybe have to be a admin to upload one. Thank you, Rick. Please see attached screen. Displayed date of the 30th, and the text under it says the 31st.

### Response

**Rick** answered on 24 Jun 2019

The 31st is the data I clicked on and in FireFox, Chrome and Edge, the correct day flashes for a quick moment then puts a day less in the display.

### Response

**Marin Bratanov** answered on 24 Jun 2019

Hello Rick, You could upload it on some cloud storage, or open a private ticket and attach a file there. That said, the only case where such a thing can happen, to the best of my knowledge, is if the keyboard is used to navigate up/down the dates and the input has not been blurred yet. Such behavior is expected at the moment. Another guess I can hazard, is that something goes wrong with the connection to the server - for example, a proxy, firewall, antivirus or other networking issue is tampering with it (for example, blocking some requests). Could you give this a try through a local installation and/or on a client-side app? Can you also try accessing our demo from a site that is not in your current workplace (e.g., from home) to see if it works there? I am attaching another video of the demo in the three browsers so you can see if this is what you are doing, to also see if it is a problem that I am missing yet. Regards, Marin Bratanov

### Response

**Rick** answered on 12 Aug 2019

Hi Martin, I am using the latest version and was hoping this would be working, still isn't. I am fixing to just use a JavaScript picker, would rather not. This is happening in any browser and happens on my work and on my home network. [https://rnrgsystems-my.sharepoint.com/:v:/g/personal/rjd_nrgsystems_com/Ec-ZIR1oHzZIpOpeYmq3yWABgqKOrWcqZ7lPYUxbiUeQiQ?e=gdYqbp](https://rnrgsystems-my.sharepoint.com/:v:/g/personal/rjd_nrgsystems_com/Ec-ZIR1oHzZIpOpeYmq3yWABgqKOrWcqZ7lPYUxbiUeQiQ?e=gdYqbp)

### Response

**Marin Bratanov** answered on 13 Aug 2019

Hello Rick, What time zone are you in? Does this happen only at certain times of day? I am asking this in case it happens only when the server and you are in different days - that would limit the occurrence to certain hours only. Could you also try running our demos locally (they are available in your installation) and see if this happens then too? We have not been able to reproduce such behavior and that makes investigating it very difficult. What I can say is that there is chance we will minimize tampering with the values of the inputs on the server in the coming month or two, so that may reduce the issue if it is related to the server getting confused (e.g., because of time zones or specific cultures being set on the client and data coming in in an unexpected format). Regards, Marin Bratanov

### Response

**Rick** answered on 13 Aug 2019

Hi Marin, yes it happens locally on my dev box in my own code. Could it be anything with the fact the time is 12 am? It doesn't matter what day I select but time is always 12 am.

### Response

**Rick** answered on 13 Aug 2019

I world think it should always be 12am though so probably not the issue.

### Response

**Rick** answered on 13 Aug 2019

I am on Eastern and happens throughout the day.

### Response

**Marin Bratanov** answered on 13 Aug 2019

Hi Rick, The default time for a new date object is 00:00:00, so this shouldn't be the issue. The date picker only fills in the date segments of the object because it does not provide facility for inputting time. You can easily test initializing the date field by also providing a time portion, helps (even though selecting a date will wipe the time portion). Something like: <TelerikDatePicker Min="@Min" Max="@Max" @bind-Value="@selectedDate"></TelerikDatePicker> <div class="pt-4">The selected date is: @selectedDate</div> @code { public DateTime Max=new DateTime(2050, 12, 31); public DateTime Min=new DateTime(1950, 1, 1); private DateTime? selectedDate { get; set; }=DateTime.Now; } Does running this snippet in a client-side Blazor app make a difference on your end? I am asking this to see if some browser input may be the issue, or if the SignalR connection may be causing this - a purely client blazor app does not transmit data to a server backend and everything happens inside the browser through wasm. In the upcoming Preview 8 there will be improvements on binding dates to standard inputs, so you would be able to, for the time being, try using a regular date input: [https://github.com/aspnet/Blazor/issues/869.](https://github.com/aspnet/Blazor/issues/869.) Regards, Marin Bratanov

### Response

**Rick** answered on 13 Aug 2019

I'll throw a client side app together and try. I haven't actually built one of those yet. I am pretty sure this use to work, I think maybe pre version 1 it worked, maybe pre 1.2.

### Response

**Marin Bratanov** answered on 14 Aug 2019

Hello Rick, I will be looking forward to your findings. If you could also try this with a different computer and/or a different time zone, that may also bring some information. Regarding our older versions - things in the framework have changed more than the date input/picker and at this point I can't say what could possibly be causing such a strange problem on your end, especially considering we haven't had other such reports. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 15 Aug 2019

Hi again Rick, This was received as a bug report in our

### Response

**Rick** answered on 15 Aug 2019

Issue has been resolved in version 1.5. Updated my project and tested, works perfectly. From the Release Notes: DatePicker FIXED Format is ignored DatePicker changes format string (placeholder) on focus

### Response

**Marin Bratanov** answered on 16 Aug 2019

That's great news, Rick, thank you for letting us know. Regards, Marin Bratanov
