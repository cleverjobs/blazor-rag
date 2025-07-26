# .Net8 Blazor Web Application Support

## Question

**Tif** asked on 15 Oct 2023

I'm getting the below error as I'm trying to update to .net8. I've also created a bare minimum blazor web application with the same results. I'm not finding any Telerik .net8 documentation related to Blazor UI so I'm not sure what is missing? Is not.8 not currently supported? "Unhandled exception rendering component: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration."](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration.") Code Program.cs app.UseStaticFiles(); App.razor <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="/" /> <link rel="stylesheet" href="bootstrap/bootstrap.min.css" /> <link rel="stylesheet" href="app.css" /> <link rel="stylesheet" href="BlazorWebApp.styles.css" /> <link rel="icon" type="image/png" href="favicon.png" /> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <HeadOutlet /> </head> <body> <Routes /> <script src="_framework/blazor.web.js"> </script> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> </body> </html> MainLayout.razor @inherits LayoutComponentBase <TelerikRootComponent> <div class="page"> <div class="sidebar"> <NavMenu /> </div> <main> <div class="top-row px-4"> <a href="[https://learn.microsoft.com/aspnet/core/"](https://learn.microsoft.com/aspnet/core/") target="_blank"> About </a> </div> <article class="content px-4"> @Body </article> </main> </div> <div id="blazor-error-ui"> An unhandled error has occurred. <a href="" class="reload"> Reload </a> <a class="dismiss"> 🗙 </a> </div> </TelerikRootComponent> counter @page "/counter"
@using Telerik.Blazor.Components.Editor
@attribute [RenderModeInteractiveServer] <PageTitle> Counter </PageTitle> <h1> Counter </h1> <p role="status"> Current count: @currentCount </p> <button class="btn btn-primary" @onclick="IncrementCount"> Click me </button> <TelerikEditor @bind-Value="@Value" Tools="@Tools" Height="880px"> </TelerikEditor>

## Answer

**Dennis** answered on 16 Oct 2023

see answer here [https://www.telerik.com/forums/net8-support](https://www.telerik.com/forums/net8-support)
