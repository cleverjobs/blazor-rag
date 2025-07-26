# Tips to migrate from WinForms

## Question

**Mar** asked on 13 Dec 2024

I am looking into the feasibility of migrating an old WinForms application that uses the Telerik WinForms Grid control to web. The Blazor Grid Control seems to have all the functionality I need. The application uses (typed) DataSets as data sources (on a SQL database we don't want to change), but there is a substantial amount of logic coded into the screens itself which will have to be duplicated to the web pages (or extracted and placed in business components). The goal is to make it work first - make it pretty later. I want to do a Pilot where I migrate a couple of (complex) WinForm screens (of the application) into a Web version using as much of the old code as possible. One of the obvious problems is state management of the user interaction on a screen. I should also say that I do have some experience with web technology, I am quite new to Blazor (although the experiments I did so far seems to point into the direction that the basic stuff is not complicated to get to work). Any tips, hints or suggestions would be very welcome. Have you experience doing this type of thing? Let me know how you did it and what problems you had to solve. Thanks!

## Answer

**Dimo** answered on 13 Dec 2024

Hi Marc, We at Telerik haven't done WinForms-to-Blazor app migration, but I hope someone from the community can share thoughts. Regards, Dimo Progress Telerik
