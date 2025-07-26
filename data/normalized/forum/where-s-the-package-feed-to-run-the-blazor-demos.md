# Where's the package feed to run the Blazor demos?

## Question

**Ton** asked on 05 Jul 2024

I loaded the demos Blaxor app and I am getting all kinds of errors because the Telerik packages do not exist. They don't exist on Nuget.org (the Trial versions) and the app has no reference to any Telerik feed server. I expected that a package feed server to be defined. I want to load the project and run and expect it to run and not spend over an hour trying to fix stuff! The packages exist in my more than one folder and I don't understand why they are not centralized in one folder. The Microsoft packages reference 8.0.0 instead of the latest. Azure.Identity is referencing 1.11 and for some reason Visual Studio is refusing to load it. It's showing a moderate vulnerability so I upgraded to 1.12. It makes feel the demos haven't been upgraded in months. Now I am getting these errors and it's not clear why. (insert image in this text editor doesn't support inserting an image from my computer. Forcing me to enter a tag. Can't find demos tag, Not friendly UX)

## Answer

**Dimo** answered on 08 Jul 2024

Hello Tony, Welcome to Telerik UI for Blazor! Here are a few comments and tips to get you back on track. Please configure the Telerik NuGet feed on your environment first. This is a required step in all our Getting Started tutorials and it's better, compared to using a separate NuGet.Config file in each app on your machine. Our Demos app explicitly references Azure.Identity 1.11.4 in the . csproj file. This version has no vulnerabilities. We don't aim to reference the latest (minor) .NET version in our apps, because this is more likely to break builds on machines that haven't upgraded yet. Using an older (minor) .NET version and upgrading to a newer one is easier, compared to downgrading after the compilation fails. The errors on the screenshot do not point to a specific or known problem in the app. Other customers haven't reported it. In this case, I would delete the bin and obj folders and try again. If the errors do result from some change in the app, then it may be easier to download the product ZIP and run the Demos app from scratch. Let me know if you need further assistance. Regards, Dimo Progress Telerik

### Response

**Tony** commented on 11 Jul 2024

The demos can have a nuget source to some local folder so the demos can run without me looking for a solution. Another vendor does that and their demos work right away without me figured things out. How am I supposed to know there's a getting started tutorial? No.. your demos reference Azure.Identity 1.11.0 and the demos project refuses to compile because it's treating the warning as error. Over 4000 errors. This is ridiculous. The Telerik packages look like they are referenced fine. I don't see warning icons. I really don't have time yo fix these errors. Your demos need to work right away without errors. This gives me a bad impression of an unpolished product. Your uninstaller didn't remove all the folders. I had to manually delete them.

### Response

**Dimo** commented on 11 Jul 2024

>> How am I supposed to know there's a getting started tutorial? Our Getting Started tutorials (also called First Steps guides) are linked from: The home page of the Telerik UI for Blazor documentation. The Telerik UI for Blazor resources page on telerik.com, which is accessible from the main Docs & Support page. If you expect these tutorials to be available somewhere else, let us know and we will consider it.===With regard to the Azure.Identity NuGet package, perhaps my previous response was misleading: Our latest version 6.0.2 was released on June 4, 2024. Azure.Identity 1.11.4 was released on June 10, 2024. We updated the source code of our demo site immediately afterwards, but that's not reflected in the released installer. We do not use Azure.Identity in our product (the Telerik.UI.for.Blazor NuGet package) so there should be no need to release a patch when a third-party vulnerability is fixed. If you believe otherwise, I am ready to get your point of view.===The mentioned 4,000 errors must have one cause, but the screenshot doesn't reveal it. I would bet on the missing NuGet package and source.

### Response

**Private** commented on 30 Jul 2024

The issue for building the demos is persisting for me in VS 2022 - I believe that I have resolved all items as outlined above concerning the packages, but am still receiving errors as indicated...

### Response

**Dimo** commented on 30 Jul 2024

@Greg - error like these that don't make sense usually go away when you: Delete the bin and obj folders in the app, Restart Visual Studio Rebuild If the problem persists, then are you using Visual Studio 2022 Preview with .NET 8 support?

### Response

**Private** commented on 30 Jul 2024

Actually a closer look at this reveals the problem to be two versions of App.razor, one in the root and then in the Pages folder - removing the root version then enables the build to complete and run fine...

### Response

**Dimo** commented on 30 Jul 2024

@Greg - hm, you are right. It seems like only the trial demos suffer from this issue. Thanks for pointing this out! I awarded you some Telerik points.
