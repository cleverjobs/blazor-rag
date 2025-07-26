# Datagrid Exception 2.10 Bug

## Question

**Mar** asked on 15 Apr 2020

in version 2.10, while not in 2.9 if you refresh F5 a page with a datagrid you get an error: System.InvalidOperationException: The current thread is not associated with the Dispatcher. Use InvokeAsync() to switch execution to the Dispatcher when triggering rendering or component state.
at Microsoft.AspNetCore.Components.Dispatcher.AssertAccess()
at Microsoft.AspNetCore.Components.RenderTree.Renderer.AddToRenderQueue(Int32 componentId, RenderFragment renderFragment)
at Microsoft.AspNetCore.Components.ComponentBase.StateHasChanged()
at Telerik.Blazor.Components.Common.BaseComponent.StateHasChanged()
at Telerik.Blazor.Components.TelerikGridBase`1.RemoveColumn(IGridColumn column)
at Telerik.Blazor.Components.TelerikGridBase`1.Telerik.Blazor.Components.Grid.IGridContainer.RemoveColumn(IGridColumn column)
at Telerik.Blazor.Components.Grid.GridColumnBase.Dispose()
at Microsoft.AspNetCore.Components.Rendering.ComponentState.Dispose()
at Microsoft.AspNetCore.Components.RenderTree.Renderer.Dispose(Boolean disposing)
--- End of stack trace from previous location where exception was thrown ---
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.HandleException(Exception exception)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.Dispose(Boolean disposing)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.Dispose()
at Microsoft.AspNetCore.Mvc.ViewFeatures.StaticComponentRenderer.PrerenderComponentAsync(ParameterView parameters, HttpContext httpContext, Type componentType)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ComponentRenderer.PrerenderedServerComponentAsync(HttpContext context, ServerComponentInvocationSequence invocationId, Type type, ParameterView parametersCollection)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ComponentRenderer.RenderComponentAsync(ViewContext viewContext, Type componentType, RenderMode renderMode, Object parameters)
at Microsoft.AspNetCore.Mvc.TagHelpers.ComponentTagHelper.ProcessAsync(TagHelperContext context, TagHelperOutput output)
at Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner.<RunAsync>g__Awaited|0_0(Task task, TagHelperExecutionContext executionContext, Int32 i, Int32 count)
at JarodProject.Pages.Pages__Host.<ExecuteAsync>b__14_1() in C:\Users\kodie\source\repos\JarodSource\JarodProject\Pages\_Host.cshtml:line 30
at Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext.SetOutputContentAsync()
at JarodProject.Pages.Pages__Host.ExecuteAsync() in C:\Users\kodie\source\repos\JarodSource\JarodProject\Pages\_Host.cshtml:line 5
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageCoreAsync(IRazorPage page, ViewContext context)
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageAsync(IRazorPage page, ViewContext context, Boolean invokeViewStarts)
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderAsync(ViewContext context)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ViewContext viewContext, String contentType, Nullable`1 statusCode)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ViewContext viewContext, String contentType, Nullable`1 statusCode)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeNextResultFilterAsync>g__Awaited|29_0[TFilter,TFilterAsync](ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Rethrow(ResultExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.ResultNext[TFilter,TFilterAsync](State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeResultFilters>g__Awaited|27_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeNextResourceFilter>g__Awaited|24_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Rethrow(ResourceExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeFilterPipelineAsync>g__Awaited|19_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.<InvokeAsync>g__Awaited|17_0(ResourceInvoker invoker, Task task, IDisposable scope)
at Microsoft.AspNetCore.Routing.EndpointMiddleware.<Invoke>g__AwaitRequestTask|6_0(Endpoint endpoint, Task requestTask, ILogger logger)
at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore.MigrationsEndPointMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore.DatabaseErrorPageMiddleware.Invoke(HttpContext httpContext)
at Microsoft.AspNetCore.Diagnostics.EntityFrameworkCore.DatabaseErrorPageMiddleware.Invoke(HttpContext httpContext)
at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)

## Answer

**Marin Bratanov** answered on 16 Apr 2020

Hi Marco, Can you reproduce this problem with the attached sample? It seems to work fine for me and I am also adding the server console from three reloads where I don't see an error either. In general, this looks like a problem during disposing the component, and an underlying issue is that the framework lacks a proper hook for that. Dispose() does not function perfectly well for cleaning up, but there is no better hook in the framework (at the moment). You can read more about this here: [https://github.com/aspnet/AspNetCore/issues/13026.](https://github.com/aspnet/AspNetCore/issues/13026.) At the moment we simply don't have any hook or way to avoid this shortcoming. We have had a few similar reports and usually this exception does not break the app but only shows up on the server console. Hopefully, the framework will provide more suitable events in the future. That said, if you can reproduce this with this sample or any other simple runnable project, please send it my way so I can have a look. Regards, Marin Bratanov
