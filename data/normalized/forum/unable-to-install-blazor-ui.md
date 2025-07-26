# Unable to install Blazor UI

## Question

**Nik** asked on 23 Sep 2019

Greetings! I am unable to install the Telerik Blazor UI in both new and existing projects .. Visual Studio 16.3.0 Preview 4.0 Blazor WebAssembly App, ASP.NET Core Hosted Blazor 3.0.0-preview9.19457.4 current .NET Core 3.0.100 New project: Error: Expecting an option, got instead: Files\dotnet\sdk\NuGetFallbackFolder\system.xml.xpath\4.3.0\lib\netstandard1.3\System.Xml.XPath.dll -a C:\Program TelerikExample.Client ... Error: The command "dotnet "C:\Users\Admin\.nuget\packages\microsoft.aspnetcore.blazor.mono\3.0.0- .... Existing (running with EF Core, AutoMapper, ...) project: Error after adding the Telerik.UI.for.Blazor.Trial: NU1107 Version conflict detected for Microsoft.CodeAnalysis.CSharp.Workspaces. Install/reference Microsoft.CodeAnalysis.CSharp.Workspaces 3.3.0 directly to project Weca.Server to resolve this issue. Error: MSB3073 The command "dotnet "C:\Users\Admin\.nuget\packages\microsoft.aspnetcore.blazor.mono\3.0.0-preview9.19456.1\build\netstandard1.0\../../tools/illink/illink.dll" -l none --disable-opt unreachablebodies ... What can i do? I'm unable to solve the version conflict (either the manual added version of CShap.Workspaces and the NuGet installed version doesn't work) I'm trying to check which UI framework to pick, so any help is MUCH appreciated! Niklas

## Answer

**Marin Bratanov** answered on 23 Sep 2019

Hello Niklas, Does starting up a new project by following this article work for you: [https://docs.telerik.com/blazor-ui/getting-started/client-blazor?](https://docs.telerik.com/blazor-ui/getting-started/client-blazor?) Once you have that running you should be able to add other projects and references that you need. If it does not - I advise that you uninstall .NET Core 3 RC 1, restart the PC and install it again, the error you get seems pretty generic and there may be some issue with the framework installation. On the version conflicts - the Telerik.DataSource package depends on Microsoft.CodeAnalysis.CSharp.Workspaces and we reference the latest version. If this raises a conflict when adding it to an existing project, this means that the project relies on an old version and should get updated first. For example, it uses an older EF version. On choosing a framework - I will assume that you are referring to choosing between Server-side Blazor and Client-side Blazor. What I can say on this is that they are fundamentally different and I personally find the server-side flavor to be a stepping stone so people can try out the concepts earlier. The true innovation and the actual SPA framework is going to be the client-side flavor that runs on WebAssembly. It is, however, not ready for prime-time, the latest news I know of indicate that it may officially ship in the Spring of 2020. So, for the time being, I'd suggest making a proof of concept on the server-side blazor flavor. It will be supported officially in the upcoming .NET Core 3.0 release (that is expected to drop before the end of the week). If you are referring to third party toolsets such as ours, what I can say is that we are building native components from the ground up so we can follow the emerging best practices. We decided to not wrap jQuery widgets as this will clash with the Blazor framework. We are using the experience we have from our other web toolsets to get this off the ground as fast as possible (for example, the grid has all the core features a grid needs about 6 months after its initial release). Regards, Marin Bratanov

### Response

**Niklas** answered on 24 Sep 2019

Hey Marin, thank you very much for taking the time! [quote]Does starting up a new project by following this article work for you: [https://docs.telerik.com/blazor-ui/getting-started/client-blazor?](https://docs.telerik.com/blazor-ui/getting-started/client-blazor?) Once you have that running you should be able to add other projects and references that you need. If it does not - I advise that you uninstall .NET Core 3 RC 1, restart the PC and install it again, the error you get seems pretty generic and there may be some issue with the framework installation.[/quote] Restarting VS solved this "generic" error message. Wherever it came from ... [quote]On the version conflicts - the Telerik.DataSource package depends on Microsoft.CodeAnalysis.CSharp.Workspaces and we reference the latest version. If this raises a conflict when adding it to an existing project, this means that the project relies on an old version and should get updated first. For example, it uses an older EF version.[/quote] I updated everything (every package in every referenced project) and i still got this error. My "Server" project has this little yellow icon on the packages symbol, but it does not show where this conflicts really is. EF Core is referenced in two projects, and only one (Server) is having problems. If i want to install this ...CSharp.Workspaces to my Server project (i cant get 3.3.0 because 3.3.0 only has prereleases, 3.3.1 is the current normal release), i get another version conflict: Client project - Telerik,DataSource.Trial uses Microsoft.CodeAnalysis 3.2.0 -> VisualBasic.Workspaces 3.2.0 -> Microsofot.CodeAnalysis.Common 3.2.0, which is not version 3.3.1 (which is included in the current CSharp.Workspaces 3.3.1 release) So, the problem is not in referencing the current EF Core package, but in the referenced 3.3.0 release of the CodeAnalysis.Workspaces (in Detail, the CodeAnalysis.Common 3.3.1 which is not compatible to the DataSource.Trial referenced Common 3.2.0) Do you know how to solve this? Do i need an updated version of the DataSource.Trial? .. [quote]On choosing a framework - I will assume that you are referring to choosing between Server-side Blazor and Client-side Blazor. What I can say on this is that they are fundamentally different and I personally find the server-side flavor to be a stepping stone so people can try out the concepts earlier. The true innovation and the actual SPA framework is going to be the client-side flavor that runs on WebAssembly. It is, however, not ready for prime-time, the latest news I know of indicate that it may officially ship in the Spring of 2020. So, for the time being, I'd suggest making a proof of concept on the server-side blazor flavor. It will be supported officially in the upcoming .NET Core 3.0 release (that is expected to drop before the end of the week).[/quote] Super good to know, thanks for clearing this up! [quote]If you are referring to third party toolsets such as ours, what I can say is that we are building native components from the ground up so we can follow the emerging best practices. We decided to not wrap jQuery widgets as this will clash with the Blazor framework. We are using the experience we have from our other web toolsets to get this off the ground as fast as possible (for example, the grid has all the core features a grid needs about 6 months after its initial release).[/quote] Thank you! Sounds very good and reasonable. I like the approach of having native (!) UI components instead of wrapped jQuery/JS stuff. I think this is the way to go :) Niklas

### Response

**Marin Bratanov** answered on 24 Sep 2019

Hello Niklas, As with all things Blazor, things changed rapidly. When I wrote my response, it was true. Right now, the official release of .NET Core 3 is available and with it, new versions of those packages, so we need to update again. It is likely that we will update them for our next release that will bring compatibility with .NET Core 3. We are working on it at this very moment and so the best advice I can offer is that you wait a little for it to become available and test again (hopefully, it will be available on Wednesday). Regards, Marin Bratanov

### Response

**Niklas** answered on 24 Sep 2019

Thanks, Marin! I can wait until Wednesday. I was writing another reply a few seconds ago ... so, for the record :) .. I now have a very clear and readable message where the version conflict comes from: Weca.Server -> Microsoft.VisualStudio.Web.CodeGeneration.Design 3.0.0 -> Microsoft.VisualStudio.Web.CodeGenerators.Mvc 3.0.0 -> Microsoft.VisualStudio.Web.CodeGeneration 3.0.0 -> Microsoft.VisualStudio.Web.CodeGeneration.EntityFrameworkCore 3.0.0 -> Microsoft.VisualStudio.Web.CodeGeneration.Core 3.0.0 -> Microsoft.VisualStudio.Web.CodeGeneration.Templating 3.0.0 -> Microsoft.VisualStudio.Web.CodeGeneration.Utils 3.0.0 -> Microsoft.CodeAnalysis.CSharp.Workspaces (>=3.3.0) Weca.Server -> Weca.Client -> Telerik.DataSource.Trial 1.1.0 -> Microsoft.CodeAnalysis 3.2.0 -> Microsoft.CodeAnalysis.CSharp.Workspaces (=3.2.0). This shows, that the package "Microsoft.VisualStudio.Web.CodeGeneration.Design" is using a more up-to-date version of the CSharp.Workspaces (>=3.3.0) compared to the provided Telerik.DataSource.Trial (CSharp.Workspaces=3.2.0). Greetings! Niklas

### Response

**Marin Bratanov** answered on 24 Sep 2019

Hello Niklas, Thank you for bringing this entire thread up. We have just committed an update to 3.3.1 <PackageReference Include="Microsoft.CodeAnalysis" Version="3.3.1" /> <PackageReference Include="Microsoft.CodeAnalysis.CSharp" Version="3.3.1" /> and it will be live with our upcoming 2.1.0 release. Regards, Marin Bratanov

### Response

**Niklas** answered on 25 Sep 2019

Hello Marin, i installed the updated UI package but still - i am unable to make it work. - everything the docs require is setup - everything is up-to-date (Visual Studio 16.4.0 Preview 1.0, Blazor v3.0.0-preview9.19465.2, ...) - the project works without the Telerik packages I attached a screenshot of the browser console errors, i hope this helps. Sadly i'm still unable to test the Progress UI components ... Greetings, Niklas

### Response

**Marin Bratanov** answered on 25 Sep 2019

Hi Niklas, This console error means that the Telerik services are not registered with the framework. THat is, the following line is missing from Startup.cs in the Client Blazor project: namespace MyBlazorAppName.Client { public class Startup { public void ConfigureServices ( IServiceCollection services ) { //more code may be present here services. AddTelerikBlazor(); } //more code may be present here }
} If you had generated the project through our VS extensions, perhaps they were an older version. I had made a mistake when re-generating them a week ago for the previous release and this line was missing in the previous version for two of the templates. The latest version should have that fixed, though. Regards, Marin Bratanov

### Response

**Niklas** answered on 25 Sep 2019

Hey Marin! You are correct - i added the AddTelerikBlazor() in my Server project which was of coruse the wrong place. Adding this to the Client project services solved this issue and the project now runs without any errors. Thank you very much for fast and detailed help! Greetings, Niklas

### Response

**Marin Bratanov** answered on 26 Sep 2019

You're welcome, Niklas. Thank _you_ for pointing out that some package references got bumped again by MS, so we could ship a better release too. Regards, Marin Bratanov
