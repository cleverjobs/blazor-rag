# Getting started, server-side blazor setting up

## Question

**Bit** asked on 30 Oct 2019

Just updated to Telerik.UI.for.Blazor 2.2.1, but was having the problem before updating as well. I suspect its just something Im missing. This section [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) <head> . . . <script src="_content/telerik.ui.for.blazor/js/telerik-blazor.js" defer></script> <!-- For Trial licenses use <script src="_content/telerik.ui.for.blazor.trial/js/telerik-blazor.js" defer></script> --> </head> When I load my page, im getting 404 errors in the dev console for telerik-blazor.js. I am adding dependencies to an existing Blazor project I started. We have the private nuget feed setup. So that much looks right. What am I missing? This is in _Host.cshtml <app> @(await Html.RenderComponentAsync<App>(RenderMode.ServerPrerendered)) </app> This is my MainLayout.cshtml @inherits LayoutComponentBase <TelerikRootComponent> <NavMenu /> <div class="container-fluid"> @Body </div> </TelerikRootComponent>

## Answer

**BitShift** answered on 30 Oct 2019

What is this _content folder, do I need to create that first?

### Response

**BitShift** answered on 30 Oct 2019

Oh, forgot to mention that I made sure to follow along all the "setup" bits in this area, esp for static assets [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) Somethings still not right

### Response

**BitShift** answered on 30 Oct 2019

In the notes, I see this [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) Static assets are automatically included in the solution by the Nuget package, so all that's needed is then to reference the asset: Which makes me wonder what this _content folder is

### Response

**BitShift** answered on 30 Oct 2019

Well, silly me I think I skipped right past the very first thing. [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) Make sure that you have .NET Core 3.1 Preview 1 and Visual Studio 2019 Preview installed. The latest version of Telerik UI for Blazor is 2.2.1 and it supports .NET Core 3.1 Preview 1. I only have the 3.0 release of .net core installed. However, my questions still stand. - What is the "_content" folder mentioned in the example, is this created in the wwwroot folder when adding the nuget feed to the project? Or does one have to create it manually before adding the nuget feed? - I suppose its obvious, but I will ask - I guess I need to use the 3.1 preview of .net core

### Response

**BitShift** answered on 30 Oct 2019

Ive updated my framework to 3.1 and still having an issue with loading the static resource telerik-blazor.js Here is what I see in my dev console with chrome. See attached file

### Response

**Marin Bratanov** answered on 31 Oct 2019

Hi, To answer the two direct questions first: - What is the "_content" folder mentioned in the example, is this created in the wwwroot folder when adding the nuget feed to the project? Or does one have to create it manually before adding the nuget feed? - this is the folder that contains the static assets from the packages that the project references. This is where our JS Interop file resides, for example. The build process copies it from the local nuget package that is expanded into the local nuget cache into the project's target folder. - I suppose its obvious, but I will ask - I guess I need to use the 3.1 preview of .net core - yes. At the moment, .NET Core 3.1. Preview 1 is the latest and the only supported SDK. I am pasting here my answer to your ticket on the continued 404 of the static asset: This means that the build did not successfully copy the static assets from our NuGet package into the output folder of the problematic project. This is something that the framework does and we can't influence. The only suggestion I can make is to try the steps from this article: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors.) Assuming that the correct package is referenced (not the trial one) the only other hope is that cleaning the bin, obj and local cache folders may help. Of course, you can also use our CDN. Regards, Marin Bratanov

### Response

**DR** commented on 14 Mar 2022

I just 'signed up for trail' and installed UI for Blazor. I ran Visual Studio 2022, removed package, and then added from nuget telerik.ui.for.blazor.trial. Then rebuilt solution... Run from Visual Studio 2022, I get this error in Network tab of browser console _content/Telerik.UI.for.Blazor/js/telerik-blazor.js net::ERR_ABORTED 404 I don't see a _content folder. I went trough the troubleshooting steps with no joy. please advise

### Response

**Marin Bratanov** commented on 15 Mar 2022

DR, The path to static assets includes the package name, and in your case it needs to include .Trial: _content/Telerik.UI.for.Blazor.Trial /... You can find examples and more details here. The _content folder is made by the framework at build time, and it is only in the output folder of the project, it is not visible in VS.

### Response

**DR** commented on 15 Mar 2022

Thank you Marin. That makes sense. Maybe you guys should note that in the GitHub page, where you do mention "If you don't have a commercial license for UI for Blazor, start a trial and replace the package reference with Telerik.UI.for.Blazor.Trial." [https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-dashboard](https://github.com/telerik/blazor-ui/tree/master/sample-applications/blazor-dashboard) However, I still don't see the output _content folder when I run in debug mode (in VS). If I " Publish " to a local folder (e.g. \bin\Release\net6.0\publish\, I do see it in a subfolder of wwwroot, So, why don't I see it when I build/run in debug mode?

### Response

**Marin Bratanov** commented on 15 Mar 2022

I suppose that question is more suitable for the Blazor repo of Microsoft. I haven't played much with the build process and this is not something we influence - the framework does it on its own. My best guess at the moment is that it is either nested in many folders and is hard to find, or is resolved at runtime in a different way during debug mode.
