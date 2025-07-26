# Incorrect First Day of Week

## Question

**Gra** asked on 28 Oct 2020

The Datepicker is using Sunday as the first day of week, my Windows 10 machine is set up to use UK dates/times and Monday is selected as first day of week. I am using Client (webasm) version of Blazor. Do I need to change the culture in the code?

## Answer

**Graham** answered on 28 Oct 2020

I found the solution - its a Chrome issue for NON US English users. Cause: Google Chrome tends to be installed with U.S. English settings by default in English-speaking countries. This defaults the date stamps seen to the format of MM/DD/YYYY which is not the standard for countries outside the U.S. Resolution: To change the option to a standard DD/MM/YYYY. (Optionally update your language settings to non-U.S) Go to Chrome Options (3 vertical pips in the top right hand corner) Choose Settings. Choose Show Advanced Options. Under Language, click on Language and input settings... Click Add and find your location specific language e.g. English (United Kingdom) and add it to the existing list. Click and hold English (United Kingdom) and drag it to the top of the existing list. Restart chrome.

### Response

**Marin Bratanov** answered on 28 Oct 2020

Hi Graham, The first day of the week in our calendar comes from the current thread culture of the blazor app, not from the browser settings (more on that in the docs ). Thus, the blazor app must ensure it has the desired globalization settings: [https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-3.1.](https://docs.microsoft.com/en-us/aspnet/core/blazor/globalization-localization?view=aspnetcore-3.1.) So, you should implement that in the app and you can find a basic sample here (see the Program.cs file in the client project). I am also attaching to this post a small example I made for you that defaults to en-GB so that Monday is the first day of the week. Note that this sample only implements this default setting, not the actual culture storage and retrieval (hence the simplistic try-catch). Regards, Marin Bratanov
