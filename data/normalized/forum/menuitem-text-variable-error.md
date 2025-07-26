# menuitem text variable error

## Question

**Alb** asked on 10 Oct 2019

When setting menu items text with a variable the application fails with error. var x="XXX"; MenuItems.Add(new MenuItem() { Text=x, Path="/test" }); error: blazor.server.js:15 [2019-10-10T12:54:11.068Z] Error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikMenu`1.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.ComponentBase.<.ctor>b__6_0(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()

## Answer

**Alberto** answered on 10 Oct 2019

You can ignore this. the problem was other thing and already fixed and everything work.
