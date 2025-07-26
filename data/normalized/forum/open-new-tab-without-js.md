# Open new Tab without JS

## Question

**Pet** asked on 02 May 2022

Hello, is it possible open new tab in browser without Javascript? without await JS.InvokeVoidAsync("open", $"www.telerik.com", "_blank"); If YES so HOW? Peter

## Answer

**Svetoslav Dimitrov** answered on 05 May 2022

Hello Peter, Using JSInterop is the only programmatic way to open a web page in a new tab in Blazor. You can see this discussion in the public GitHub repository of ASP .NET Core where Steve Sanderson, the creator of Blazor, answered that JS Interop is the only way. Regards, Svetoslav Dimitrov

### Response

**Peter** commented on 06 May 2022

Hello Svetoslav, You're right, but discussion was in 2019. Do you know whether will it possible in future and when?

### Response

**Marin Bratanov** commented on 07 May 2022

Hi Peter, I would recommend you address your query to Microsoft, as we are not the people developing the Blazor framework and choosing what JS wrappers to provide in it. In the meantime, I'd suggest you create the needed JS method in your app, and the needed C# helper method to call it with, so that you can do this only in C# after the initial creation. If you are using links to navigate you can already set their target attribute as desired too, so no need for any coding there.
