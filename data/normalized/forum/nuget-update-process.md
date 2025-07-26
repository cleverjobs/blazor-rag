# Nuget Update Process

## Question

**Zac** asked on 13 Aug 2020

Looking at your online documentation for upgrading a project to the latest version with nuget, I must be missing something... it only shows to run the update command. When I run it (NuGet Sources Update -Name "telerik.com" -Source "[https://nuget.telerik.com/nuget"...),](https://nuget.telerik.com/nuget"...),) then I go into our projects, the nuget manager shows that 2.14.1 is latest stable. Actually it shows as the only version option. How do we get the nuget manager to offer the latest release (2.16 at this time)?

## Answer

**Eric R | Senior Technical Support Engineer** answered on 14 Aug 2020

Hi Zack, Our template ships with a solution-level NuGet.config file that references the default installation folder of the version at the time of project creation. This is to avoid breaking changes between releases and to ensure you can reference the packages even if you don't have the live feed set up. To elaborate on what is happening, the solution-level configuration is taking precedence over the update command. See the Common NuGet Configurations and Package Sources documentation for information related to this. Note the Tip in the Package Sources section. Can you confirm if the NuGet.config file looks like the following? <?xml version="1.0" encoding="utf-8"?> <configuration> <packageSources> <add key="Telerik Blazor 2.14.1 " value="C:\Program Files (x86)\Progress\Telerik UI for Blazor 2.14.1 \" /> </packageSources> </configuration> If so, there are a couple of options that I have listed below. 1. Use the Telerik NuGet Feed in Visual Studio and remove the NuGet.config file. 2. Manually update the NuGet.config file to match the specific version that is installed like below. <?xml version="1.0" encoding="utf-8"?> <configuration> <packageSources> <add key="Telerik Blazor 2.16.0 " value="C:\Program Files (x86)\Progress\Telerik UI for Blazor 2.16.0 \" /> </packageSources> </configuration> Please let me know if you need any additional information. Thank you for using the UI for Blazor Forums. Regards, Eric R | Senior Technical Support Engineer

### Response

**Zack** answered on 14 Aug 2020

I must be missing something. Sorry. I used the Progress Control Panel to "upgrade" UI for Blazor. It reports success going to 2.16. In appdata\nuget\nuget.config, it looks like the following: <? xml version="1.0" encoding="utf-8"?> <configuration> <packageSources> <add key="nuget.org" value=" [https://api.nuget.org/v3/index.json](https://api.nuget.org/v3/index.json) " protocolVersion="3" /> <add key="telerik.com" value=" [https://nuget.telerik.com/nuget](https://nuget.telerik.com/nuget) " /> </packageSources> <packageSourceCredentials> <telerik.com> <add key="Username" value="xxxxx@xxxxx.com" /> <add key="ClearTextPassword" value="xxxxxx" /> </telerik.com> </packageSourceCredentials> <packageRestore> <add key="enabled" value="True" /> <add key="automatic" value="True" /> </packageRestore> <bindingRedirects> <add key="skip" value="False" /> </bindingRedirects> <packageManagement> <add key="format" value="0" /> <add key="disabled" value="False" /> </packageManagement> </configuration> I run the update command in that folder: C:\Users\zack\AppData\Roaming\NuGet>NuGet Sources Update -Name "telerik.com" -Source " [https://nuget.telerik.com/nuget](https://nuget.telerik.com/nuget) " -UserName "xxxxxx@xxxxxxx.com" -Password "xxxxxxx" -StorePasswordInClearText Package source "telerik.com" was successfully updated. But still in VS 2019 my existing projects nuget manager has 2.14 as "latest stable" and only option.

### Response

**Eric R | Senior Technical Support Engineer** answered on 14 Aug 2020

Hi Zack, There are three locations to reference a NuGet configuration file and each location has its own scope. The locations in order of scope are the Solution Folder, the User's AppData Folder and the Computer's Program Files (x86) folder. The User configuration is referenced in the previous reply. This means that a Solution Folder configuration is taking precedence over the User configuration. I recommended confirming that the NuGet.config at the Solution level doesn't reference the 2.14.1 version. See the below screenshot for a visual reference of a Solution Level configuration. Note the location of the NuGet.config file. This will be used before the AppData and Program Files configurations. For more information see the Common NuGet Configurations documentation. Please let me know if you need any additional information. Thank you. Regards, Eric R | Senior Technical Support Engineer

### Response

**Zack** answered on 14 Aug 2020

I finally figured it out. In NuGet, the package source was set to nuget.org. I see there is both a telerik.com as well as a Telerik Blazor package source (the second being installed by the full Telerik Control Panel I assume). When I change the source to try to upgrade it was failing due to downgrades detected in other dependencies like webassembly itself. Then finally, after upgrading all dependent nuget packages, I was able to switch to the telerik.com private feed and upgrade to 2.16. Fingers crossed a bunch of stuff doesn't quit working or have dependency breaking changes :) Note: I did not have a nuget.config file in the solution folder. I think I actually was able to add it to our current solution with nuget. Probably because it was still available in the nuget.org feed since I had installed it with the private feed to a different solution.

### Response

**Eric R | Senior Technical Support Engineer** answered on 14 Aug 2020

Hi Zack, Glad to hear you figured it out! As always, thank you for using the Forums and please don't hesitate to reach out if you have any additional questions. Regards, Eric R | Senior Technical Support Engineer

### Response

**Zack** answered on 14 Aug 2020

All is well. Thank you for your quick response assistance.
