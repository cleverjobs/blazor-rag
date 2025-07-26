# Mix Telerik UI ASP.NET Core and UI for Blazor

## Question

**c0w** asked on 18 Jan 2021

We have an application (razorpages) that is currently using Telerik UI ASP.NET Core. We would successively like to upgrade it to be running Blazor Server-side. Razorpages and Blazor is no problem mixing, but is it possible to both run Telerik UI ASP.NET Core and UI for Blazor within the same app but use different namespace imports within the pages? I have failed installing both packages from nuget due to different versions in dependency-packages.

## Answer

**Marin Bratanov** answered on 18 Jan 2021

Hi, The following sample projects show how you can integrate Blazor components in another ASP.NET COre app (razor pages or mvc): [https://github.com/telerik/blazor-ui/tree/master/common/razor-components](https://github.com/telerik/blazor-ui/tree/master/common/razor-components) The namespace imports are tied to the code written in our packages and are not something you can change. I would suggest you try to migrate entire pages at a time so that you can have all the content on one page either a jQuery app, or a Blazor app. This might make the migration easier, and also let you handle popup elements positioning better (see the notes about the root container in the readme of the repo, and the Wrong Popup Position section of the docs). It's also important that you reference only one Kendo theme - a SASS one (Default, Bootstrap, Material are the built-in options). Regards, Marin Bratanov
