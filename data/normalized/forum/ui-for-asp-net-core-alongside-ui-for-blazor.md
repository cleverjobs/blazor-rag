# UI for ASP.NET Core alongside UI for Blazor

## Question

**Giu** asked on 27 Aug 2019

Dear Progress Team We are using UI for ASP.NET Core and we want to migrate to UI for Blazor. However our project is already big and we can not migrate everything at once. Is it possible to have UI for ASP.NET Core and UI for Blazor in the same c# project? Something like that: <myapp>/admin/ <-- legacy screens working with Core <myapp>/newfeature/ <-- Blazor if this is possible would you mind to setup up a very basic project that shows how this can be done? that would be awesome. Best Giuseppe

## Answer

**Marin Bratanov** answered on 28 Aug 2019

Hello Giuseppe, The following KB article shows some information on the subject and a sample: [https://docs.telerik.com/blazor-ui/knowledge-base/blazor-in-asp-net.](https://docs.telerik.com/blazor-ui/knowledge-base/blazor-in-asp-net.) The idea is that certain views/pages can use Razor Components in them, so you can start developing the Blazor sections. I must warn that with the next versions of Blazor, passing component Parameters as an anonymous object will go away ( [https://github.com/aspnet/AspNetCore/issues/11876](https://github.com/aspnet/AspNetCore/issues/11876) ), which will impact such an approach significantly, and at this point I do not know what the future of such an integration will be. I have not yet seen separate apps (MVC and Blazor) running under the same application, though, probably because the app types are quite different. So, perhaps you may be able to get a client-side Blazor app running somewhere under an MVC app, but I am not sure if/how this can be done. Regards, Marin Bratanov
