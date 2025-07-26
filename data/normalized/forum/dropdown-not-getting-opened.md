# DropDown not getting opened

## Question

**kha** asked on 06 Nov 2019

Hello, i used telerik ui for blazor in a sample project and i used drop downs now i made another project im configured my blazor app but i cant use components with pop up parts( drop down , time picker , ...) and i also checked here but unfortunately it could'nt fix my problem i checked all the files it same as my last project but now i can't used these types of components im using .NET version 3.1.100-preview1-014459 with telerik trial version 2.3.0 this is my _Host.cshmtl <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title>Management</title> <base href="~/" /> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link rel="stylesheet" href="[https://unpkg.com/@@progress/kendo-theme-default@@latest/dist/all.css"](https://unpkg.com/@@progress/kendo-theme-default@@latest/dist/all.css") /> <link href="css/site.css" rel="stylesheet" /> </head> <body> <app> @(await Html.RenderComponentAsync<App>(RenderMode.Static)) </app> <script src="_content/telerik.ui.for.blazor.trial/js/telerik-blazor.js"></script> <script src="_framework/blazor.server.js"></script> </body> </html> and this is my MainLayout.razor @inherits LayoutComponentBase <TelerikRootComponent> <div class="sidebar"> <NavMenu /> </div> <div class="main"> <div class="top-row px-4"> <a href="[https://docs.microsoft.com/aspnet/"](https://docs.microsoft.com/aspnet/") target="_blank">About</a> </div> <div class="content px-4"> @Body </div> </div> </TelerikRootComponent> i also added services.AddTelerikBlazor(); to my Startup.cs and i added these @using Telerik.Blazor @using Telerik.Blazor.Components in my _imports.razor

## Answer

**Marin Bratanov** answered on 07 Nov 2019

Hello, You need .NET Core 3.1 Preview 2 at the moment, with 2.3.0 of Telerik UI for Blazor: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need.) Does installing it help? Do you get any errors (including JS errors such as the ones described here )? Regards, Marin Bratanov

### Response

**khashayar** answered on 07 Nov 2019

i've updated my .NET Core version to 3.1.100-preview2-014569 and all is in my console is VM39:72 Angular state inspector shortcuts: VM39:73 $scope/$context: Element debug info VM39:74 $getDetectChanges()/$tick()/$apply(): Trigger change detection cycle VM39:75 i get no error but dropdowns don't work

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hi Khashayar, These messages indicate that this is an Angular app, not a Blazor app. You must create a Blazor app. Please try following our instructions here and/or creating a project through our VS extensions (see here ). If those don't work for you, please open a support ticket and send me the problematic project so I can investigate and avoid further guessing. Regards, Marin Bratanov

### Response

**khashayar** answered on 07 Nov 2019

i can assure you im using blazor you i can even give you my anydesk code and see it yourself

### Response

**khashayar** answered on 07 Nov 2019

that is so odd for me to see angular error in blazor app

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hello, Please make sure that you have the TelerikRootComponent at the root of your layout: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.) You can see how the project should be set up when you create one from our VS Extensions. If those two ideas don't help you, please open a support ticket and send me a runnable sample project that showcases the Telerik DropDownList issue. Regards, Marin Bratanov

### Response

**khashayar** answered on 07 Nov 2019

but this doesn't concern me now all i want is to open datepicker in my blazor app and i can say it's blazor because i installed a blazor server side in visual studio and added ui for blazor to my project and used ui for blazor grid in project and it work's completely fine

### Response

**khashayar** answered on 07 Nov 2019

my friend i have this component and i already sent you the file to see that i have it please see my first post i added all the configs

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hello Khashayar, I made a sample that works for me so you can run it and compare against it. You can find it attached at the end of this post. If comparing (e.g., with a tool similar to WinMerge) does not help you fix the problem you are facing, I will need you to open a support ticket and send me the problematic project so I can investigate. Just guessing is not going to get us closer to solving this. Regards, Marin Bratanov

### Response

**khashayar** answered on 07 Nov 2019

i used your code and it's working fine my problem was in _Host.cshtml this is my code <app> @(await Html.RenderComponentAsync<App>(RenderMode.Static))</app> which had to be <app><component type="typeof(App)" render-mode="ServerPrerendered" /></app> but what is the differnece between these two ?

### Response

**Marin Bratanov** answered on 07 Nov 2019

Here's a table from MSDN that explains the differences: [https://docs.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-3.0#stateful-reconnection-after-prerendering.](https://docs.microsoft.com/en-us/aspnet/core/blazor/hosting-models?view=aspnetcore-3.0#stateful-reconnection-after-prerendering.) The static mode is plain HTML, not actual components you can interact with. The tag helper is the new way of rendering Razor components since .NET Core 3.1 Preview 2, it superseded the html helper. Regards, Marin Bratanov
