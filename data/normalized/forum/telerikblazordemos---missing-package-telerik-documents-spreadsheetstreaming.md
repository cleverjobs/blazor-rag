# TelerikBlazorDemos - missing package Telerik.Documents.SpreadsheetStreaming

## Question

**Wal** asked on 14 May 2020

I am not able to compile demo application TelerikBlazorDemos.csproj. The license is trial. I have configured all package sources including local and server Telerik. The error during build is below: Unable to find package Telerik.Documents.SpreadsheetStreaming. No packages exist with this id in source(s): AppData folder, DevExpress, Esri, [https://dotnet.myget.org/F/aspnetcore-dev/api/v3/index.json,](https://dotnet.myget.org/F/aspnetcore-dev/api/v3/index.json,) [https://dotnet.myget.org/F/blazor-dev/api/v3/index.json,](https://dotnet.myget.org/F/blazor-dev/api/v3/index.json,) Local Telerik, Microsoft Visual Studio Offline Packages, nuget.org, nuget.telerik.com TelerikBlazorDemos C:\Program Files (x86)\Progress\Telerik UI for Blazor 2.13.0\demos\TelerikBlazorDemos\TelerikBlazorDemos.csproj

## Answer

**Marin Bratanov** answered on 14 May 2020

Hello Waldek, Thank you for reaching out. It looks like our demos reference an older version of the Telerik Document Processing Libraries - 2020.1.109 - which you probably don't have access to through our online feed. I am attaching here the .csproj file updated to the new versions that you should be able to restore. Could you give it a try and let me know if it works for you? I am also attaching here the older .nupkg files that you can set up in a local feed and they should let you run things with the original project file, in case the updated csproj file does not work out. Regards, Marin Bratanov

### Response

**Waldek** answered on 14 May 2020

Hello Marin. Thank you for your response. I have tried both: 1) Replace TelerikBlazorDemos.csproj with yours. In this case the error was the same and screen was the same as attached to previous post. 2) Then I reinstalled Trial version of Telerik including Demo and added folder with dpl.Trial.2020.1.109 packages received from you. The error is the same ( Telerik.Documents.SpreadsheetStreaming ). The screen is attached.

### Response

**Marin Bratanov** answered on 14 May 2020

Hello Waldek, The NuGet tooling should be able to restore the newer version, and if it can't find it at all, my best guess is that there is an issue with the nuget feed setup on the machine. I'd suggest you try the following: Clean the solution Close Visual Studiuo Delete the bin and obj folders Clean the local nuget caches (usually executing in the shell "dotnet nuget locals all --clear" should do the trick - copy it without the quotation marks) Restart the PC Open the solution again Right click the project and select "Restore NuGet Packages" If this does not work, try: Creating a local feed with all the Telerik packages (both from the "dpl" folder and from the "packages" folder that you can find in your UI for Blazor installation) Right click on the solution and select "Manage NuGet Packages" Select the new package source from the dropdown on the top right hand side Check what packages you see - there should be the Telerik UI for Blazor, as well as the rest of the files, including the SpreadSheetStreaming Right click the solution and select "Restore NuGet packages" Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 14 May 2020

A quick follow up, Waldek, yesterday there was a short-lived issue where the Telerik UI for Blazor package trial version was seeking the SpreadSheetStreaming without the trial version - this is something that we have fixed, and performing the steps from my previous post will clear your local nuget cache and will let you download the fixed package from our online feed. Regards, Marin Bratanov

### Response

**Gary** answered on 14 May 2020

I am having the same problem. Unable to find package Telerik.Documents.SpreadsheetStreaming.Trial. No packages exist with this id in source(s): Microsoft Visual Studio Offline Packages, nuget.org, Telerik Blazor 2.13.0Telerik1C:\Users\gary\source\Telerik1\Telerik1.csproj1ResolvePackageAssets

### Response

**Marin Bratanov** answered on 14 May 2020

Hello Gary, Could you try clearing the local nuget packages, the bind and obj folders and restarting VS? There was an issue with the trial version of the Telerik.UI.for.Blazor package that had a wrong reference to the Telerik.Documents.SpreadsheetStreaming package, and we fixed that last night. It is possible that your machine has cached the old, broken package. If you are using a local nuget feed for the Telerik packages, make sure that it also includes the packages from the "dpl" folder in the installation - that's where the Telerik.Documents.* packages are. The "packages" folder contains only the three main packages for the UI elements. Does this help? Regards, Marin Bratanov

### Response

**Gary** answered on 14 May 2020

Where should the DPL folder reside? I don't see the folder at all. I am looking in the C:\Users\gary\.nuget\packages area and see three Telerik sub-folders. telerik.datasource.trial telerik.recurrence.trial telerik.ui.for.blazor.trial

### Response

**Marin Bratanov** answered on 14 May 2020

Hello Gary, It's in your Telerik UI for Blazor installation. By default, that's in the following folder for the 2.13.0 version C:\Program Files (x86)\Progress\Telerik UI for Blazor 2.13.0\ I'm attaching a screenshot below that illustrates this. Regards, Marin Bratanov

### Response

**Gary** answered on 14 May 2020

That worked! Thanks for the help!

### Response

**Waldek** answered on 14 May 2020

Hello Marin, The first section was enough to fix: Delete bin, obj and clean the local nuget caches It works with 2020.2.504 versions of packages! Thank you for your help.

### Response

**Rob** answered on 15 May 2020

Marin, Developers on my team are experiencing this same issue with the commercial version when upgrading to 2.13.0. Due to us enabling "Treat warnings as errors" on our solution, the NuGet restore fails with a NU1603 error ([https://developercommunity.visualstudio.com/content/problem/94646/nuget-package-dependency-restoration.html).](https://developercommunity.visualstudio.com/content/problem/94646/nuget-package-dependency-restoration.html).) Can you confirm that the commercial version also references an old version of the SpreadsheetStreaming NuGet, and will there be a new version (2.13.1) resolving this? Thanks, Rob

### Response

**Marin Bratanov** answered on 15 May 2020

Gary, Waldek - I'm glad to hear that you have things working! @Rob - A "silent" or "automatic" (or however else it might be called) package update that references a newer version is always a warning. If the IDE is set to treat warnings as errors, then a lot of other warnings like the "this async method does not contain await operators" will also prevent you from building the project. The only solution for that is to disable that switch in VS. On whether the commercial version references 2020.1.109 - yes, it does, and a 2.14.0 release is coming for the WebAssembly GA release next week that should have this updated. Regards, Marin Bratanov
