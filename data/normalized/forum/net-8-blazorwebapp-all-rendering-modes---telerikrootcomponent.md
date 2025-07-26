# .NET 8 BlazorWebApp (All Rendering Modes) - TelerikRootComponent

## Question

**Sco** asked on 08 Dec 2023

Is there a plan to fix this in the long term? The "work-around" listed in your documentation, Configure the Render Mode per Page found at [https://docs.telerik.com/blazor-ui/getting-started/web-app#configure-the-render-mode-per-page](https://docs.telerik.com/blazor-ui/getting-started/web-app#configure-the-render-mode-per-page) technically functions as the root component error goes away and site starts working... However, it misses the bigger issue in that it now loads the entire page including all of the layout code and components, re-executing them as well... put some components in the TelerikLayout and add break points to the OnInit functions to see what I am referring to. It will now do this for every single page in application now... So... to my initial question... what is the plan to fix/address the TelerikRootComponent in the multiple rendering mode world that is .NET 8 now? I will say it looks like the Blazor team added a new concept of using builder.Services.AddCascadingValues() to address this problem, I have used it with our internal RootComponent to fix this same concept with our internal code... thoughts? builder.Services.AddTelerikCascadingParameters(); is referenced at url below: [https://github.com/dotnet/aspnetcore/issues/50724](https://github.com/dotnet/aspnetcore/issues/50724) by SteveSandersonMS, I realize he was just throwing out an idea, the above line of code doesn't actually exist to my knowledge, at least not yet... :) Thanks in advance!

## Answer

**Dimo** answered on 11 Dec 2023

Hello Scott, You are right that the TelerikRootComponent relies on cascading values to work. This component has two main tasks: Pass global settings down the component hierarchy. For example, IconType or EnableRtl (and probably more in the future). Render all our popups. This works by transferring RenderFragments from each popup-enabled component up the component hierarchy. The new .NET 8 service ( builder.Services.AddCascadingValues() ) does not support passing of RenderFragments, because they are not JSON serializable. This brings the requirement that our TelerikRootComponent is part of an interactive component hierarchy. I understand that some of our features may impose restrictions or requirements on our customers and the Blazor app configuration. There are boundaries and framework requirements (or limitations) that apply also to us and which even we cannot overcome. So, for the time being, we have no specific plans to change the TelerikRootComponent mechanism. Even if a technical solution exists (which relies on a completely different approach), we want to be sure that enough customers need it, before we venture into an initiative that may break 100% of our customers. Regards, Dimo Progress Telerik

### Response

**Scott** commented on 11 Dec 2023

Thank you for your response.

### Response

**Charles** commented on 29 Dec 2023

Hello Dimo, Just to clarify, does this mean that the render mode per page will not work on components that requires the TelerikRootComponent? ( TelerikRootComponent - List of Components that depend on it? in UI for Blazor | Telerik Forums ). We are trying to port an older Blazor project to NET8 to utilize its ability to have different rendering modes per page, but we are currently stuck with I believe the same TelerikRootComponent error observed by Scott. We managed to make some pages run using the workaround but we had to temporarily remove the components that requires the TelerikRootComponent. I have attached a sample project with the problem that we are encountering on this thread:.NET 8 Interactive mode on individual components in UI for Blazor | Telerik Forums Any inputs are greatly appreciated. Thanks

### Response

**Svetoslav Dimitrov** commented on 29 Dec 2023

Hello Charles, I have added an answer to your question in the.NET 8 Interactive mode on individual components forum thread. Regards, Svetoslav Dimitrov
