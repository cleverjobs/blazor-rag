# FileNotFoundException "Telerik.Blazor.resources" iOS Blazor Hybrid DropDownList

## Question

**Cal** asked on 28 Jun 2023

Hi -- I've added Teleirk.UI.for.Blazor to a brand new .NET MAUI Blazor Hybrid application. In my MauiProgram.cs I add `builder.Services.AddTelerikBlazor();` and I've just edited the generated page to include a DropDownListControl. Whole page code here: [https://gist.github.com/CMorooney/320976b711ea45052f20eca96f02d67c](https://gist.github.com/CMorooney/320976b711ea45052f20eca96f02d67c) adding a Breakpoint in VS for any/all System.Exception throws will expose a FileNotFoundException happening for a resource named `Telerik.Blazor.resources" this doesn't happen if you replace the DropDownList with a telerik text box but it currently does cause the BalzorWebView to crash in our production/testflight ios releases. please help. edit: further details Xcode 14.3.1 .net7.0-ios Telerik.UI.for.Blazor 4.3.0

## Answer

**Nadezhda Tacheva** answered on 03 Jul 2023

Hi Calvin, A possible reason for this issue is the configuration of the linker that all release builds are using by default. For example, if its "Link All" setting is enabled, the linker can use the whole set of its optimizations to make the application as small as possible. Throughout the process, it can strip out assemblies, methods, properties, fields, events that it mistakenly treated as unused but the app actually needs them. You can find some more details on the matter here: [https://learn.microsoft.com/en-us/dotnet/maui/ios/linking?tabs=vs#linker-behavior.](https://learn.microsoft.com/en-us/dotnet/maui/ios/linking?tabs=vs#linker-behavior.) As a first step, I would recommend configuring the linker to link SDK assemblies only. You can do that in the csproj file: <PropertyGroup Condition="'$(Configuration)|$(TargetFramework)|$(Platform)'=='Release|net7.0-ios|AnyCPU'"> <MtouchLink> SdkOnly </MtouchLink> </PropertyGroup> I hope this will help you resolve the issue. Please let us know if any other questions appear. Regards, Nadezhda Tacheva
