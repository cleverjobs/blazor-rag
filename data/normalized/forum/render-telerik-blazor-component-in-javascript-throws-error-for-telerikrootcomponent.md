# Render Telerik Blazor component in Javascript throws error for TelerikRootComponent

## Question

**Dou** asked on 30 Nov 2021

I'm trying to make the "Render Blazor Components From Your JavaScript Code" section of the blog, Final Blazor Improvements Before .NET 6 (telerik.com), work with a Blazor application that includes Telerik components. I created a "Telerik C# Blazor Application" template, with .NET6, Hosting Model Server, Target Framework .NET 6.0, CRUD template. (Attached). There's a htmlcounter.html page that works great, I can render the Counter in javascript and it functions correctly. When I try with htmlgrid.html, I get the following error. I've tried referencing telerik-blazor.js, but can't get that to satisfy the render. How do I configure a TelerikRootComponent for this Javascript rendered page? Error: System.Exception: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration) at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragment.OnInitializedAsync() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() log @blazor.server.js:1

## Answer

**Dimo** answered on 03 Dec 2021

Hi Douglas, Please do 2 things to make this work: Add our CSS and JS file to htmlgrid.html <head> <meta charset="utf-8" /> <title> </title> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> </head> Wrap the Grid.razor content in a <TelerikRootComponent> @page "/grid"

@using TelerikBlazorApp2.Models
@using TelerikBlazorApp2.Services
@inject WeatherForecastService ForecastService <TelerikRootComponent> <div class="container-fluid"> <div class='row my-4'> <div class='col-12 col-lg-9 border-right'> <TelerikGrid /> </div> <div class='col-12 col-lg-3 mt-3 mt-lg-0'> </div> </div> </div> </TelerikRootComponent> @code { } Here is some additional information for context: Razor components, which are rendered with JavaScript, do not support cascading parameters, or at least not now. We use a cascading value to pass the TelerikRootComponent and the DialogFactory from the MainLayout to all child components. In this way, our Blazor components consume these two objects regardless of their placement. In other words, you may need to add a TelerikRootComponent in multiple places, similar to when sing Blazor components in a ASP.NET apps. Also note that the placement of the TelerikRootComponent affects popup positioning. Finally, let's keep in mind that JavaScript rendering of Blazor components is an experimental feature in alpha state. We do not claim support for it. Regards, Dimo Progress Telerik
