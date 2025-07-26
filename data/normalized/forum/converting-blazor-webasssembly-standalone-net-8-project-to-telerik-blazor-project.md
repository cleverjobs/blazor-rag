# Converting Blazor WebAsssembly Standalone .NET 8 project to Telerik Blazor project

## Question

**Hei** asked on 18 Dec 2023

I have recently downloaded the latest Telerik.UI for blazor 5.0.1 commercial and I tried converting a dotnet 8 project to a telerik project using the context menu. Is there a plan to have support for the new .NET 8 project templates? The option to also create a new blazor project from the Visual Studio 2022 project templates is gone. I cannot create a blazor project. I saw the "Discover the Magic of .NET 8 and Beyond!" webinar and it seemed support for .NET 8 was ready

## Answer

**Momchil** answered on 20 Dec 2023

Hello Hernie, The Convert wizard doesn't support converting .NET 8 projects yet so I have logged a public feedback item on your behalf so you could follow the state of the issue. In the meantime you could follow the steps described in this article to manually add Telerik UI for Blazor components to.NET 8 Blazor Web App project. About the missing new Telerik Blazor project templates, please note that the Visual Studio extensions should be installed by the same user who launches the Visual Studio in order for the Visual Studio templates to be visible. If the project templates are installed by the same user but are still not showing please try reinstalling the Telerik UI for Blazor Visual Studio extension by following these steps: In the Visual Studio menu select Extensions -> Manage Extensions In the Installed section find Progress Telerik UI for Blazor Extension Click the Uninstall button on the entry Close all Visual Studio instances and follow the VSIX installer wizard which will uninstall the extension Start Visual Studio and select Extensions -> Manage Extensions again In the Online section search for Progress Telerik UI for Blazor Extension in the search box in the top right corner of the dialog In the results click the Download button of the Progress Telerik UI for Blazor Extension entry Close all Visual Studio instances and follow the VSIX installer wizard which will install the extension again Please try these steps and let us know if further assistance is needed. Regards, Momchil Progress Telerik
