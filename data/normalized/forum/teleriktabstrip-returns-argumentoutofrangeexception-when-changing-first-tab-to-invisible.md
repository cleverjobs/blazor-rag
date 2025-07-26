# TelerikTabStrip returns ArgumentOutOfRangeException when changing first tab to invisible

## Question

**Thi** asked on 29 Aug 2022

Telerik Blazor version: 3.4.0, 3.5.0 I'm currently encountering a bug within Telerik Blazor with the TabStrip component. If the first Tab of the TabStrip's visibility is set to false, the component throws an exception: ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index') With some debugging, I found what went wrong within Telerik's code. But first, the scenario: Setup Create a TelerikTabStrip with three TabStripTab components inside: A, B, C. Scenario A Tab A: Visible=false Tab B: Visible=true Tab C: Visible=true Scenario B Tab A: Visible=true Tab B: Visible=false Tab C: Visible=true Result Scenario B works fine. Scenario A does not. Why? Basically, it looks like this happens: Tab=> SetParameters()=> VisibleChanged=true (because that parameter is set)=> TabStrip.OnTabVisibiltyChanged=> IsTabActive=true (because it's the first tab)=> FindFocusable=> this method has only one tab in the list (the first tab) and not the other two tabs because it's still early in the component lifecycle=> FindIndex can't find a tab that is visible and not disabled=> returns index -1=> this is out of range and throws an exception Why scenario B works: Tab A=> SetParameters()=> VisibleChanged=false (because the parameter is not changed to the default)=> basically done Tab B=> SetParameters()=> VisibleChanged=true (because we changed that)=> TabStrip.OnTabVisibilityChanged=> IsTabActive=false (not the first tab, so not active)=> basically done @page "/TabStripTest" <PageTitle>Telerik tabs error</PageTitle>

<TelerikTabStrip @ref="_stripRef">
<TabStripTab Title="A" Visible="true">
Tab A
</TabStripTab>

<TabStripTab Title="B" Visible="false">
Tab B
</TabStripTab>

<TabStripTab Title="C" Visible="true">
Tab C
</TabStripTab>
</TelerikTabStrip>

@code { private TelerikTabStrip _stripRef;
} Full stacktrace: System.ArgumentOutOfRangeException: Index was out of range. Must be non-negative and less than the size of the collection. (Parameter 'index')
at Telerik.Blazor.Components.TelerikTabStrip.FocusActiveTab()
at Telerik.Blazor.Components.TelerikTabStrip.set_CurrentActiveTabIndex(Int32 value)
at Telerik.Blazor.Components.TelerikTabStrip.Telerik.Blazor.Components.TabStrip.ITabContainer.OnTabVisibleChanged(ITab tab)
at Telerik.Blazor.Components.TabStripTab.OnParametersSetAsync()
at Microsoft.AspNetCore.Components.ComponentBase.CallOnParametersSetAsync()
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.HandleException(Exception exception)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.HandleExceptionViaErrorBoundary(Exception error, ComponentState errorSourceOrNull)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.AddToPendingTasks(Task task, ComponentState owningComponentState)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.SetDirectParameters(ParameterView parameters)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InitializeNewComponentFrame(DiffContext& diffContext, Int32 frameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InitializeNewSubtree(DiffContext& diffContext, Int32 frameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InsertNewFrame(DiffContext& diffContext, Int32 newFrameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InsertNewFrame(DiffContext& diffContext, Int32 newFrameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.AppendDiffEntriesForRange(DiffContext& diffContext, Int32 oldStartIndex, Int32 oldEndIndexExcl, Int32 newStartIndex, Int32 newEndIndexExcl)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.ComputeDiff(Renderer renderer, RenderBatchBuilder batchBuilder, Int32 componentId, ArrayRange`1 oldTree, ArrayRange`1 newTree)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.HandleException(Exception exception)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessPendingRender()
at Microsoft.AspNetCore.Components.RenderTree.Renderer.AddToRenderQueue(Int32 componentId, RenderFragment renderFragment)
at Microsoft.AspNetCore.Components.ComponentBase.StateHasChanged()
at Microsoft.AspNetCore.Components.ComponentBase.CallOnParametersSetAsync()
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.HandleException(Exception exception)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.HandleExceptionViaErrorBoundary(Exception error, ComponentState errorSourceOrNull)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.AddToPendingTasks(Task task, ComponentState owningComponentState)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.SupplyCombinedParameters(ParameterView directAndCascadingParameters)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.SetDirectParameters(ParameterView parameters)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderRootComponentAsync(Int32 componentId, ParameterView initialParameters)
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.CreateInitialRenderAsync(Type componentType, ParameterView initialParameters)
at Microsoft.AspNetCore.Components.Rendering.HtmlRenderer.RenderComponentAsync(Type componentType, ParameterView initialParameters)
at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext. <> c__11`1.<<InvokeAsync> b__11_0>d.MoveNext()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.ViewFeatures.StaticComponentRenderer.PrerenderComponentAsync(ParameterView parameters, HttpContext httpContext, Type componentType)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ComponentRenderer.PrerenderedServerComponentAsync(HttpContext context, ServerComponentInvocationSequence invocationId, Type type, ParameterView parametersCollection)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ComponentRenderer.RenderComponentAsync(ViewContext viewContext, Type componentType, RenderMode renderMode, Object parameters)
at Microsoft.AspNetCore.Mvc.TagHelpers.ComponentTagHelper.ProcessAsync(TagHelperContext context, TagHelperOutput output)
at Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner. <RunAsync> g__Awaited|0_0(Task task, TagHelperExecutionContext executionContext, Int32 i, Int32 count)
at TelerikTabStripBug.Pages.Pages__Host.ExecuteAsync() in C:\Users\Thimo.Koolen\source\repos\TelerikTabStripBug\TelerikTabStripBug\Pages\_Host.cshtml:line 6
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageCoreAsync(IRazorPage page, ViewContext context)
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderPageAsync(IRazorPage page, ViewContext context, Boolean invokeViewStarts)
at Microsoft.AspNetCore.Mvc.Razor.RazorView.RenderAsync(ViewContext context)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ViewContext viewContext, String contentType, Nullable`1 statusCode)
at Microsoft.AspNetCore.Mvc.ViewFeatures.ViewExecutor.ExecuteAsync(ViewContext viewContext, String contentType, Nullable`1 statusCode)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeNextResultFilterAsync> g__Awaited|30_0[TFilter,TFilterAsync](ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Rethrow(ResultExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.ResultNext[TFilter,TFilterAsync](State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.InvokeResultFilters()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeNextResourceFilter> g__Awaited|25_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Rethrow(ResourceExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.InvokeFilterPipelineAsync()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeAsync> g__Logged|17_1(ResourceInvoker invoker)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeAsync> g__Logged|17_1(ResourceInvoker invoker)
at Microsoft.AspNetCore.Routing.EndpointMiddleware. <Invoke> g__AwaitRequestTask|6_0(Endpoint endpoint, Task requestTask, ILogger logger)
at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware.Invoke(HttpContext context)

## Answer

**Svetoslav Dimitrov** answered on 01 Sep 2022

Hello Thimo, Thank you for the in-depth explanation. I have reproduced the behavior and, indeed, this is a bug. As a small token of appreciation, I have added Telerik Points to your account. That being said, I have opened a new Bug Report on your behalf - The TabStrip throws ArgumentOutOfRangeException if the first tab is not Visible. I have added your vote for it and you are automatically subscribed to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik
