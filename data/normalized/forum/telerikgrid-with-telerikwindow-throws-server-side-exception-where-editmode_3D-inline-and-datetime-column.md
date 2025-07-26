# TelerikGrid with TelerikWindow throws server-side exception where EditMode="inline" and DateTime column

## Question

**And** asked on 28 May 2019

I have a TelerikWindow containing a TelerikGrid, with EditMode="inline" and an "Add" TelerikGridCommandButton: <TelerikWindow> <TelerikWindowContent> <TelerikGrid Data=@ScheduledJobs EditMode="inline"> <TelerikGridToolBar> <TelerikGridCommandButton Command="Add" Icon="add"></TelerikGridCommandButton> </TelerikGridToolBar> <TelerikGridColumns> <TelerikGridColumn Field=@nameof(ScheduledJob.DateTime) Title="Date" /> </TelerikGridColumns> </TelerikGrid> </TelerikWindowContent> </TelerikWindow> At run-time when I click the "Add" button in the grid I get the following error: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazorDateInput' in 'window'. Error: Could not find 'TelerikBlazorDateInput' in 'window'. at [https://localhost:5000/_framework/blazor.server.js:8:20878](https://localhost:5000/_framework/blazor.server.js:8:20878) at Array.forEach (<anonymous>) at d ([https://localhost:5000/_framework/blazor.server.js:8:20839)](https://localhost:5000/_framework/blazor.server.js:8:20839)) at [https://localhost:5000/_framework/blazor.server.js:8:21429](https://localhost:5000/_framework/blazor.server.js:8:21429) at new Promise (<anonymous>) at e.beginInvokeJSFromDotNet ([https://localhost:5000/_framework/blazor.server.js:8:21403)](https://localhost:5000/_framework/blazor.server.js:8:21403)) at [https://localhost:5000/_framework/blazor.server.js:1:16653](https://localhost:5000/_framework/blazor.server.js:1:16653) at Array.forEach (<anonymous>) at e.invokeClientMethod ([https://localhost:5000/_framework/blazor.server.js:1:16624)](https://localhost:5000/_framework/blazor.server.js:1:16624)) at e.processIncomingData ([https://localhost:5000/_framework/blazor.server.js:1:14624)](https://localhost:5000/_framework/blazor.server.js:1:14624)) at async void Telerik.Blazor.Components.DateInput.TelerikDateInputBase.OnAfterRender() at void System.Threading.Tasks.Task.ThrowAsync(Exception exception, SynchronizationContext targetContext)+(object state)=> { } at void Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteSynchronously(TaskCompletionSource<object> completion, SendOrPostCallback d, object state) at void Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecutionContextThunk(object state) at void Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteBackground(WorkItem item) If I change the data type of the column from DateTime to string, this error goes away. Please assist?

## Answer

**Marin Bratanov** answered on 29 May 2019

Hello Andrew, The error indicates that the JS Interop file is missing. Can you confirm you have it, as shown in Step 4 in this article: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor#add-to-existing-project?](https://docs.telerik.com/blazor-ui/getting-started/server-blazor#add-to-existing-project?) I am attaching here a small sample that works as expected on my end and does not throw errors, so you can compare against it. Regards, Marin Bratanov

### Response

**Andrew** answered on 29 May 2019

Yes, that fixed it thanks. The issue here is you have to remember to change the version of .js file referenced in _Host.cshtml every time you use NuGet package manager to fetch a new version of the Telerik packag, BUT only when the version of the .js file has changed too. I understand this is a Blazor issue with static files, but it will keep tripping people up. Thanks anyway though, problem solved for now :-)

### Response

**Marin Bratanov** answered on 29 May 2019

Hi Andrew, The version of the JS file will match the version of the package. For the time being, there is no other way to do this, until Microsoft decide on how to handle assets from class libraries. Maybe then there will be a neater solution (or maybe not, we don't know what will happen yet). Once there is something new, we will update the documentation. Regards, Marin Bratanov
