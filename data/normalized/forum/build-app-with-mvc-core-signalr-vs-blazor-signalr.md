# Build app with MVC core signalR vs. Blazor signalR

## Question

**DonDon** asked on 27 Sep 2019

I have a new project that requires real-time data updates on a grid for a team of users to collaborate within the application. It seems SignalR is a good candidate for this project. I am new to programming with SignalR. Since I am familiar with .NET 4.x framework and MVC, I initially was thinking of implementing the project as an ASP.NET Core 3.0 MVC with Telerik.UI for Asp.Net Core since it has Grid Binding to SignalR. However, with the release of Blazor, I am considering using Blazor and Telerik.UI.for.Blazor. But I don't see any samples or documentations to use with SignalR in Telerik.UI. My questions: 1. Given that my project requires SignalR for real-time data updates, should I choose the stable approach of ASP.NET Core with MVC and the more-documented Telerik.UI for asp.net Core grid ? or is it possible to use Blazor / SignalR / Telerik.UI (if such thing exists) ? What are the pros vs. cons of those 2 choices? 2. Where can I find tutorials on building: 1) ASP.NET Core 3.0 MVC / SignalR / Telerik for ASP.NET Core; 2) ASP.NET Core Blazor / SignalR / Telerik for Blazor

## Answer

**Marin Bratanov** answered on 27 Sep 2019

Hello Don, The Blazor grid can bind to observable data, so you can change it at will: [https://demos.telerik.com/blazor-ui/grid/observable-data.](https://demos.telerik.com/blazor-ui/grid/observable-data.) Server-side Blazor already runs on top of a SignalR connection to the server, so if you have a service that raises the appropriate events, you can consume them in the razor components and update data. We don't have such an example at the ready because it depends too much on the server logic. As for ASP.NET Core and SignalR - we have a demo: [https://demos.telerik.com/aspnet-core/grid/signalr.](https://demos.telerik.com/aspnet-core/grid/signalr.) Which technology stack you will choose is something that you would need to decide as the application developer, considering all the pros and cons of both, and other factors specific to your situation (such as integration with other apps, data access layers, personal preferences and future plans). Regards, Marin Bratanov

### Response

**Andy** answered on 13 Jul 2020

Hi Marin, I'm pretty familiar with SignalR and Core, but I'm just hopping into blazor. Could you please clarify what you mean by a service that raises the appropriate events? Is service a term for an API or are you referring to a class that you're calling a service that continuously runs and raises events that the razor components can wire into? I understand the concept of binding to an observable collection but not how I'd react to a different session/user/browser raising an event and update the list in my browser. In SignalR I'd react in the hub and send a message to all other clients- what is reacting to what in your scenario? Thanks so much.

### Response

**Marin Bratanov** answered on 13 Jul 2020

Hi Andy, I'm referring to a data service, similar to the WeatherForecastService that the Blazor app template registers. Of course, it should be modified accordingly. An alternative is to use a Razor Component that encapsulates the desired logic and exposes the required events and add it in components that need it so you can consume those events, and each instance can create a separate connection, if needed. The scenario you described is the same in Blazor as in other web apps: SignalR hub exists on the server client apps connect to it and push data/events to the hub client apps connect to that hub and also receive events when needed (e.g., someone else pushed data to the hub) With Blazor, you can now do all of this in C# without JS, because there are already existing NuGet packages for wiring up to the hub from your components (Blazor app). Regards, Marin Bratanov
