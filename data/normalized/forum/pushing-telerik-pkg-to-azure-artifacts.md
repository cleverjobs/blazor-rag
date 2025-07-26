# Pushing Telerik pkg to Azure Artifacts

## Question

**Chr** asked on 30 Aug 2023

Sorry if this is not the right forum...I'm trying to push the UI for Blazor nuget package to Azure Artifacts for the build pipeline. I can't use a service to connect directly to Nuget.Telerik. I already have the package added to my project and its working fine. I installed it from the .msi I'm following this article: [https://www.telerik.com/blogs/azure-devops-and-telerik-nuget-packages](https://www.telerik.com/blogs/azure-devops-and-telerik-nuget-packages) and I downloaded nuget.exe v.6.7.0. When I run the command specified: C:\Users\ <my profile> \source\repos>nuget.exe push -Source "Telerik" -ApiKey az "C:\Users\ <my profile> \Documents\TelerikPackages\Telerik.UI.for.Blazor.4.4.0.nupkg" and I get an error "ERROR: This version of nuget.exe does not support updating packages to package source 'Telerik'." I 'Googled' this error and got nothing! <ugh> Any suggestions really be appreciated!

## Answer

**Chris** answered on 30 Aug 2023

Never mind. I hadn't run nuget.exe restore. It works fine now.
