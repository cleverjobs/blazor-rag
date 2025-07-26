# Error with Blazor Server .NET 8 and Telerik.UI.for.Blazor 4.4

## Question

**Jon** asked on 13 Dec 2023

Hi all, I've been trying to get new Blazor projects off the ground with Telerik 4.4, and had some luck with WASM but unfortunately Blazor Server I cannot get to work. I have kept my projects simple, following the guidance set out in the Getting Started articles but every time run into the same error in the web client. Error: Microsoft.JSInterop.JSException: Maximum call stack size exceeded RangeError: Maximum call stack size exceeded at e.deepExtend ([https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075205)](https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075205)) at e.deepExtend ([https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075502)](https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075502)) at e.deepExtend ([https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075440)](https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075440)) at e.deepExtend ( [https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075440](https://localhost:7144/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:50:1075440) ) .... (repeats) at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue](Int64 targetInstanceId, String identifier, Object[] args) at Telerik.Blazor.Components.TelerikMediaQuery.InitMediaQueryWidget() at Telerik.Blazor.Components.TelerikMediaQuery.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) This stops any Telerik components from working, and leaves me a bit stuck! Anyone seen similar? Or know of a workaround?

## Answer

**Dimo** answered on 14 Dec 2023

Hi Jonathan, .NET 8 requires Telerik UI for Blazor 5.0. I highly recommend using 5.0.1 that includes another .NET 8-related fix. Regards, Dimo Progress Telerik

### Response

**Chris** commented on 01 Feb 2024

Hi, I am having the same issue. I updated the Telerik Blazor UI to 5.0.1 but it did not solve the issue. Here are my current packages. <ItemGroup> <PackageReference Include="Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore" Version="8.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Identity.EntityFrameworkCore" Version="8.0.1" /> <PackageReference Include="Microsoft.AspNetCore.Identity.UI" Version="8.0.1" /> <PackageReference Include="Microsoft.CodeAnalysis" Version="4.8.0" /> <PackageReference Include="Microsoft.EntityFrameworkCore.SqlServer" Version="8.0.1" /> <PackageReference Include="Microsoft.EntityFrameworkCore.Tools" Version="8.0.1"> <PrivateAssets>all</PrivateAssets> <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets> </PackageReference> <PackageReference Include="Newtonsoft.Json" Version="13.0.3" /> <PackageReference Include="Telerik.DataSource" Version="3.0.0" /> <PackageReference Include="Telerik.Documents.Core" Version="2023.3.1106" /> <PackageReference Include="Telerik.Documents.SpreadsheetStreaming" Version="2023.3.1106" /> <PackageReference Include="Telerik.Recurrence" Version="0.2.1" /> <PackageReference Include="Telerik.UI.for.AspNet.Core" Version="2023.2.718" /> <PackageReference Include="Telerik.UI.for.Blazor" Version="5.0.1" /> <PackageReference Include="Telerik.Zip" Version="2023.3.1106" /> </ItemGroup>

### Response

**Dimo** commented on 02 Feb 2024

@Chris - please clear the browser cache. If the issue persists, open a private ticket and send us a project for inspection.
