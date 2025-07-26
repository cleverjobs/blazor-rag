# Microsoft.JSInterop.JSException: Cannot read property 'querySelector' of null

## Question

**Mic** asked on 15 Jun 2020

Hey all, I am facing a problem that just sometimes occurs and can't find the root of the issue. First I thought I messed something up but I get a feeling it might not be my fault at the end? I added the StackTrace as attachment maybe someone has an idea whats going on? I updated my Telerik.UI.for.Blazor to 2.14.1 still same behavior, randomly this error occurs.

### Response

**Jagannath** commented on 06 Apr 2022

Hi , we are getting below error ,We are using Blazor UI 2.26, Could you please help in this Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'querySelector') TypeError: Cannot read properties of null (reading 'querySelector') at e.value ([https://localhost:44387/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:51:18299)](https://localhost:44387/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:51:18299)) at Object.u ([https://localhost:44387/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:15575)](https://localhost:44387/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:15575)) at [https://localhost:44387/_framework/blazor.server.js:8:35886](https://localhost:44387/_framework/blazor.server.js:8:35886) at new Promise (<anonymous>) at e.beginInvokeJSFromDotNet ([https://localhost:44387/_framework/blazor.server.js:8:35854)](https://localhost:44387/_framework/blazor.server.js:8:35854)) at [https://localhost:44387/_framework/blazor.server.js:1:20247](https://localhost:44387/_framework/blazor.server.js:1:20247) at Array.forEach (<anonymous>) at e.invokeClientMethod ([https://localhost:44387/_framework/blazor.server.js:1:20217)](https://localhost:44387/_framework/blazor.server.js:1:20217)) at e.processIncomingData ([https://localhost:44387/_framework/blazor.server.js:1:18028)](https://localhost:44387/_framework/blazor.server.js:1:18028)) at e.connection.onreceive ([https://localhost:44387/_framework/blazor.server.js:1:11113)](https://localhost:44387/_framework/blazor.server.js:1:11113)) at Microsoft.JSInterop.JSRuntime.InvokeWithDefaultCancellation[T](String identifier, Object[] args) at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.TelerikWindow.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

## Answer

**Marin Bratanov** answered on 15 Jun 2020

Hi Michael, Could you try removing the defer attribute form our JS Interop script? It is possible that it causes the browser to parse it too late and thus can cause issues. Another thing that can be causing this is switching to another component while the window is initializing - the JS Interop call would be sent, but Blazor alters the DOM so that Window elements are no longer there and so they throw. If this is the case, this would boil down to the lack of a proper UnMount event in Blazor, you can read more about this here. I've also raised a question with the dev team to review this error as there might be ways to add some defensive check for this particular case, but I cannot promise this just yet. If you can consistently reproduce the error, that would help the investigation and fix immensely. Regards, Marin Bratanov

### Response

**Michael** answered on 16 Jun 2020

Hey Marin, first thanks for the reply and suggestions. Yesterday sadly removing the defer attribute did not change anything. However I was trying to reproduce the error this morning again and write down the steps I did... and the error did not occur again. I will try again and again over the day and give you an update. A few things I noticed yesterday: 1. It seems to never happen in the debugger, just when it is hosted on the IIS (I am using Server-Side Blazor by the way) 2. For my colleague it normally directly occurs when he presses the search button, which will fetch a bunch of data from the DataBase (through the C# Server-Side part) and updates the TelerikGrid. At the same time with the button click I set an TelerikWindow to visible as "Loading" indicator. I needed to spam click the search button and at some point the error occurred. I get a feeling that this might have something to do with a bad/slow network connection since our VPN was somekind of slow yesterday and I know my colleague often has problem with latency.

### Response

**Marin Bratanov** answered on 16 Jun 2020

Hi Michael, From the start, this looks like a timing issue - the window is trying to open, but its DOM element was removed by Blazor which tends to happen with multiple clicks and large latency - the SignalR packets are asynchronous and arrive in different order. We did log a task to add a few defensive checks that might help, though I can't promise a timeframe. I imagine that something like this might be happening: the browser sends the click that shows the window to the server the server returns the instruction to show the window (contains the js interop call) and the DOM of the window (that the js interop accesses) those two packets arrive in the wrong order and the function executes before the DOM is available The same could happen if you bash the button repeatedly Ensuring a low-latency connection to the server is likely to resolve this, or using the WebAssembly flavor which is more suitable for cases when low-latency can't be guaranteed. If your user base is expected to have similar latency issues, I would advise that you re-consider which Blazor flavor you will be using, as the server-side mode can cause you more such issues that don't have solutions when large latency is at play. Regards, Marin Bratanov

### Response

**Michael** answered on 16 Jun 2020

Thanks Marin, your investigations seems to fit with my assumptions, we will see if this is a 'real' problem or just in our test-lab. In the worst case we have to switch to WebAssembly and adjust our project. Again thanks and best regards, Michael

### Response

**Michael** answered on 16 Jun 2020

Short update since I wanted to understand a little bit more before I throw away my project. It seems my problem is more related to the TelerikWindow I used as "Loading indicator" I guess I messed something up with switching between @bind-Visible and StateHasChanged() and/or NavigationManager.NavigateTo(). After commenting out the TelerikWindows the problem was not reproducible.

### Response

**Marin Bratanov** answered on 17 Jun 2020

Hello Michael, This is, most likely, some timing issue with the Window component, as indicated by the stack trace. So, removing it will remove this particular issue. Since it is likely that it stems from SignalR latency, however, you may encounter more similar issues and out-of-sync data unless the connection gets faster or you move to a WebAssembly scenario. If a .NavigateTo() call is in place - it is likely that it causes the problem - it disposes the current DOM, while an old SignalR packet arrives later to try to use it. Perhaps adding an await Task.Delay(20) before the navigate call will avoid this error, even though it is still possible that the latency might be borderline high for a server-side Blazor scenario. Regards, Marin Bratanov

### Response

**Michael** answered on 17 Jun 2020

Hey Marin, at this point I am not really sure anymore if it is a latency issue, I switched from the TelerikWindow as Loading indicator to Eds SpinKit ([https://github.com/EdCharbeneau/BlazorPro.Spinkit/)](https://github.com/EdCharbeneau/BlazorPro.Spinkit/)) sadly it is in my scenario (fetching data for the TelerikGrid) a little bit ugly because I have to replace the complete Grid but it works. I did not change anything in my code behind but the error does not occur anymore after the replacement. The navigate scenario was pretty rare to cause the issue. Mostly it was just the search button to get the Data for my TelerikGrid and it seemed mostly to happen when the call comes back extremely fast...I tried with the delay but it seemed the delay made the error occur even more often. While figuring out what the root of all this might be i came along this: [https://github.com/dotnet/aspnetcore/issues/16032](https://github.com/dotnet/aspnetcore/issues/16032) and the error after he added the 'StateHasChanged()' sounds pretty similar... however I guess I stick just with avoid the TelerikWindow as Loading Indicator for now.

### Response

**Marin Bratanov** answered on 17 Jun 2020

Hello Michael, A key difference is what each component needs to do. The Window is a much more complicated component that does more things, and needs a little bit of JS Interop, and its main purpose is not a simple loading sign. The SpinKit package seems to use only a little bit of HTML and CSS, and so is more suitable to the task at the moment, and that's why it does not suffer from such latency issues. That said, we have a Telerik-themed on on our roadmap and you can Follow its progress here: [https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly.](https://feedback.telerik.com/blazor/1408055-busy-indicator-which-is-mvvm-friendly.) I've added your Vote to it to raise its priority. Regards, Marin Bratanov
