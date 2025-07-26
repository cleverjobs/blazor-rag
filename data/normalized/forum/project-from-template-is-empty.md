# Project from template is empty

## Question

**Jef** asked on 20 Sep 2023

I am trying to create a new project using Telerik C# Blazor Application template in Visual Studio 2022. I am able to go through the template steps however on finish no project is created. The message bar at the bottom of visual studio says it was successful. I have Telerik UI for Blazor Extension installed and enabled.

## Answer

**Misho** answered on 21 Sep 2023

Hi Jeff, I've tried to create a new project using Telerik C# Blazor Application template in Visual Studio 2022. I was able to produce the following server hosting model templates successfully on my side with .NET 7 which is currently the latest supported version: Blank CRUD. Form, Chart Dashboard Admin All projects seem to be runnable and stretch properly on my side. I've attached a video showing the steps that I perform on my end called Capture.gif What I could suggest you is to Uninstall Progress Telerik UI for Blazor Extension. Verify the extension is not available in Visual Studio any more and install it again from Visual Studio -> Extensions -> Manage Extensions -> Search for Telerik UI for Blazor I hope this will help you to solve the problematic behavior on your side. I've attached a sample runnable project for you reference. Looking forward to your feedback. Best Regards, Misho Progress Telerik
