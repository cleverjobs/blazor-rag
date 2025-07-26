# Sporadic error: this.element is null

## Question

**And** asked on 10 Jun 2020

Hello, I have a Blazor server app with multiple pages. Each
page has 1 to 3 Kendo grids on it. Everything works fine but if I
navigate between pages then I am getting the error this.element is null
(in browser development tools). The full error is below. It could be a
couple of hours working fine an then error occur on random pages and
Blazor message asks to reload but page's content showing fine. I do understand that it could be no answer for this, I am just asking if somebody had the same Blazor behaviour. Thanks. [2020-06-10T15:38:56.950Z] Error: Microsoft.JSInterop.JSException: this.element is null value@[http://flextest2/_content/telerik.ui.for.blazor/js/telerik-blazor.js:40:18644](http://flextest2/_content/telerik.ui.for.blazor/js/telerik-blazor.js:40:18644) u@[http://flextest2/_content/telerik.ui.for.blazor/js/telerik-blazor.js:1:10606](http://flextest2/_content/telerik.ui.for.blazor/js/telerik-blazor.js:1:10606) beginInvokeJSFromDotNet/r<@[http://flextest2/_framework/blazor.server.js:8:31421](http://flextest2/_framework/blazor.server.js:8:31421) beginInvokeJSFromDotNet@[http://flextest2/_framework/blazor.server.js:8:31390](http://flextest2/_framework/blazor.server.js:8:31390) C</e.prototype.invokeClientMethod/<@[http://flextest2/_framework/blazor.server.js:1:19202](http://flextest2/_framework/blazor.server.js:1:19202) C</e.prototype.invokeClientMethod@[http://flextest2/_framework/blazor.server.js:1:19173](http://flextest2/_framework/blazor.server.js:1:19173) C</e.prototype.processIncomingData@[http://flextest2/_framework/blazor.server.js:1:17165](http://flextest2/_framework/blazor.server.js:1:17165) e/this.connection.onreceive@[http://flextest2/_framework/blazor.server.js:1:10276](http://flextest2/_framework/blazor.server.js:1:10276) x</e.prototype.poll/</<@[http://flextest2/_framework/blazor.server.js:1:30261](http://flextest2/_framework/blazor.server.js:1:30261) s/</<@[http://flextest2/_framework/blazor.server.js:1:27386](http://flextest2/_framework/blazor.server.js:1:27386) s/<@[http://flextest2/_framework/blazor.server.js:1:27491](http://flextest2/_framework/blazor.server.js:1:27491) a@[http://flextest2/_framework/blazor.server.js:1:26261](http://flextest2/_framework/blazor.server.js:1:26261) at Microsoft.JSInterop.JSRuntime.InvokeWithDefaultCancellation[T](String identifier, Object[] args) at Telerik.Blazor.Components.TelerikWindow.OnAfterRenderAsync(Boolean firstRender) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle) blazor.server.js:15:27309 [2020-06-10T15:38:57.003Z] Information: Connection disconnected. blazor.server.js:1:5212 Error: Cannot send data if the connection is not in the 'Connected' State.

## Answer

**Andrey** answered on 10 Jun 2020

Update. If I comment out Kendo Grid then no further errors occur on this particular page.

### Response

**Andrey** answered on 10 Jun 2020

Looks like the Export to MS Excel button on a Grid creates this problem: <GridToolBar> @*<GridCommandButton Command="ExcelExport" Icon="@IconName.FileExcel">Export to Excel</GridCommandButton>*@</GridToolBar>

### Response

**Marin Bratanov** answered on 11 Jun 2020

Hi Andrey, The initial stack trace points to a Window component and its OnAfterRenderAsync method - this initializes the window if its Visible parameter is true, so it is not likely to come from the grid. The Excel export does not use a window and so it should not be related to this problem. Thus, this looks like SignalR latency issues to me - the DOM in the browser, the events it sends and what the server receive can become out of sync which can cause a variety of strange issues. Perhaps WebSockets are not enabled on the hosting server, or it is simply too far away (in terms of latency) for the server-side flavor and you may need to consider switching to the WebAssembly flavor. That said, if you can reproduce a problem with the Telerik components reliably, please open a support ticket and send us a minimal runnable reproducible so we can investigate it. Regards, Marin Bratanov

### Response

**Andrey** answered on 11 Jun 2020

Hi Marin, You are right, it is not related to Grid or Kendo UI at all. I am using: component type="typeof(App)" render-mode="Server" and DOM is not ready for some reason. The workaround I've found so far is using Delay in OnInitializedAsync(): protected override async Task OnInitializedAsync() { await Task.Delay(TimeSpan.FromSeconds(0.2)); ... } It's really poor solution (but works fine) and I am still investigating. Thanks!

### Response

**Marin Bratanov** answered on 11 Jun 2020

Hello Andrey, Since sometime in the winter, the HTML helper should not be used to render the Razor component, you should use the tag helper, something like this: <app> <component type="typeof(App)" render-mode="Server" /> </app> Regards, Marin Bratanov
