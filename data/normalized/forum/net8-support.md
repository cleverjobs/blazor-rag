# Net8 support?

## Question

**Den** asked on 06 Oct 2023

I tried following the [https://www.telerik.com/blogs/net-8-release-candidate-delivers-smoother-out-box-experience-blazor](https://www.telerik.com/blogs/net-8-release-candidate-delivers-smoother-out-box-experience-blazor) On trivial pages it works ok, but if i add something like the example from the wizard [https://demos.telerik.com/blazor-ui/wizard/overview](https://demos.telerik.com/blazor-ui/wizard/overview) then it throws when it swaps from server to wasm: warn: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer[ 100 ]
Unhandled exception rendering component: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: https: //docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration System.Exception: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: https: //docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragment.OnInitializedAsync()
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
fail: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[ 111 ]
Unhandled exception in circuit 'vu1d5OeY0l1wssueGrhRNuYFT4GHFJylXQODsHtTPgI'.
System.Exception: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: https: //docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragment.OnInitializedAsync()
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
warn: Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer[ 100 ]
Unhandled exception rendering component: Cannot access a disposed object.
System.ObjectDisposedException: Cannot access a disposed object.
at Microsoft.AspNetCore.Components.RenderTree.ArrayBuilder` 1. GrowBuffer(Int32 desiredCapacity)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InsertNewFrame(DiffContext& diffContext, Int32 newFrameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.AppendDiffEntriesForRange(DiffContext& diffContext, Int32 oldStartIndex, Int32 oldEndIndexExcl, Int32 newStartIndex, Int32 newEndIndexExcl)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.ComputeDiff(Renderer renderer, RenderBatchBuilder batchBuilder, Int32 componentId, ArrayRange` 1 oldTree, ArrayRange` 1 newTree)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()
fail: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[ 111 ]
Unhandled exception in circuit 'vu1d5OeY0l1wssueGrhRNuYFT4GHFJylXQODsHtTPgI'.
System.ObjectDisposedException: Cannot access a disposed object.
at Microsoft.AspNetCore.Components.RenderTree.ArrayBuilder` 1. GrowBuffer(Int32 desiredCapacity)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.InsertNewFrame(DiffContext& diffContext, Int32 newFrameIndex)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.AppendDiffEntriesForRange(DiffContext& diffContext, Int32 oldStartIndex, Int32 oldEndIndexExcl, Int32 newStartIndex, Int32 newEndIndexExcl)
at Microsoft.AspNetCore.Components.RenderTree.RenderTreeDiffBuilder.ComputeDiff(Renderer renderer, RenderBatchBuilder batchBuilder, Int32 componentId, ArrayRange` 1 oldTree, ArrayRange` 1 newTree)
at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() which is a really weird error, since I do have that, and the trivial examples work (like changing the button in Counter.cs to a TelerikButton) sometimes the error origins on the client instead: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100]
Unhandled exception rendering component: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration)
System.Exception: A Telerik component on the requested view requires a TelerikRootComponent to be added to the root of the MainLayout component of the app. Read more at: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration)
at Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragment.OnInitializedAsync()
at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()
fr @blazor.web.js:1
(anonymous) @invoke-js.ts:176
El @invoke-js.ts:276
$func350 @00b1e17a:0x1faed
$func246 @00b1e17a:0x1bf8a
$func239 @00b1e17a:0xf171
$func273 @00b1e17a:0x1d1af
$func3183 @00b1e17a:0xe7ef0
$func2504 @00b1e17a:0xbdcfe
$func2510 @00b1e17a:0xbe4bd
$func2534 @00b1e17a:0xc0b04
$mono_wasm_invoke_method_bound @00b1e17a:0xa524
Module._mono_wasm_invoke_method_bound @dotnet.native.8.0.0-...9.4.qccqbfnfqo.js:8
Sr @invoke-cs.ts:273
(anonymous) @invoke-cs.ts:247
beginInvokeDotNetFromJS @blazor.web.js:1
invokeDotNetMethodAsync @blazor.web.js:1
invokeMethodAsync @blazor.web.js:1
refreshRootComponents @blazor.web.js:1
refreshAllRootComponents @blazor.web.js:1
documentUpdated @blazor.web.js:1
ai @blazor.web.js:1
await in ai (async)
(anonymous) @blazor.web.js:1
Ae @blazor.web.js:1
ri @blazor.web.js:1 Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at r.bindPickerEvents ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1133819)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1133819)) at r.setOptions ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132575)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132575)) at new s ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132083)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132083)) at new r ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1125051)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1125051)) at e.initComponent ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1077272)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1077272)) at e.initDatePicker ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1124871)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1124871)) at [https://localhost:7226/_framework/blazor.web.js:1:3244](https://localhost:7226/_framework/blazor.web.js:1:3244) at new Promise (<anonymous>) at v.beginInvokeJSFromDotNet ([https://localhost:7226/_framework/blazor.web.js:1:3201)](https://localhost:7226/_framework/blazor.web.js:1:3201)) at Object.Ur [as invokeJSJson] ([https://localhost:7226/_framework/blazor.web.js:1:146334)](https://localhost:7226/_framework/blazor.web.js:1:146334)) Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener') TypeError: Cannot read properties of null (reading 'addEventListener') at r.bindPickerEvents ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1133819)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1133819)) at r.setOptions ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132575)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132575)) at new s ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132083)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1132083)) at new r ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1125051)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1125051)) at e.initComponent ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1077272)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1077272)) at e.initDatePicker ([https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1124871)](https://localhost:7226/_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js:50:1124871)) at [https://localhost:7226/_framework/blazor.web.js:1:3244](https://localhost:7226/_framework/blazor.web.js:1:3244) at new Promise (<anonymous>) at v.beginInvokeJSFromDotNet ([https://localhost:7226/_framework/blazor.web.js:1:3201)](https://localhost:7226/_framework/blazor.web.js:1:3201)) at Object.Ur [as invokeJSJson] ([https://localhost:7226/_framework/blazor.web.js:1:146334)](https://localhost:7226/_framework/blazor.web.js:1:146334)) at Microsoft.JSInterop.JSRuntime.<InvokeAsync>d__16`1[[Microsoft.JSInterop.Infrastructure.IJSVoidResult, Microsoft.JSInterop, Version=8.0.0.0, Culture=neutral, PublicKeyToken=adb9793829ddae60]].MoveNext() at Microsoft.JSInterop.JSRuntimeExtensions.InvokeVoidAsync(IJSRuntime jsRuntime, String identifier, Object[] args) at Telerik.Blazor.Components.Common.Pickers.TelerikPickerBase`1.<InitPicker>d__127[[System.Nullable`1[[System.DateTime, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Telerik.Blazor.Components.Common.Pickers.TelerikPickerBase`1.<OnAfterRenderAsync>d__123[[System.Nullable`1[[System.DateTime, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState) ie, copy demo code to some page in the client. add <h1> @(RuntimeInformation.ProcessArchitecture==Architecture.Wasm ? "Wasm" : "Server") </h1> add @attribute [RenderModeAuto] Tried various combinations of setting RenderMode in .razor file or in app.razor, same problem

### Response

**Dennis** commented on 06 Oct 2023

The problem is the date selector <TelerikForm Model="this"> <FormItems> <FormItem LabelText="Birth Date" Field="@nameof(DateOfBirth)" /> </FormItems> </TelerikForm> @code {
public DateTime? DateOfBirth { get; set; }

## Answer

**Dimo** answered on 10 Oct 2023

Hello Dennis, This is related to a general .NET8 Blazor problem. You can read more at [https://github.com/dotnet/aspnetcore/issues/50724](https://github.com/dotnet/aspnetcore/issues/50724) We are still evaluating the best way to proceed in terms of built-in behavior and documentation, but overall, you will need to set @attribute [RenderModeServer] for the whole app, including the layout file(s). Regards, Dimo Progress Telerik

### Response

**Dennis** commented on 12 Oct 2023

As I understand what you write, the `InteractiveAuto` and `InteractiveWebAssembly` scenarios are currently unsupported by Telerik? Will they be supported before 8 rtm?

### Response

**Dimo** commented on 12 Oct 2023

All interactive modes should work, given that the render mode is the same in the component hierarchy from the layout file (where the TelerikRootComponent is) to the innermost .razor component where our popup-based component is (e.g. ComboBox, DatePicker, Window, etc.)

### Response

**Dennis** commented on 13 Oct 2023

global InteractiveWebAssembly or InteractiveAuto does not work with the TelerikRootComponent around the layout . It does work if I have the global at the default (static), and then a TelerikRootComponent per interactive component. But HotReload is even more flaky than normal.

### Response

**Dennis** commented on 16 Oct 2023

Nope, still cannot get it to work properly, even with those restrictions... If I have a component with TelerikRootComponent, and it looses focus it rerenders. Weather component: @inject WeatherService WeatherService

@rendermode DefaultRenderMode <TelerikRootComponent> <PageTitle> Weather </PageTitle> <h1> Weather </h1> <TelerikDropDownList TItem="int" TValue="int" Data="@_listSizes" @bind-Value="@_listSize" OnChange="UpdateForecasts"> </TelerikDropDownList> @if (_forecasts==null)
{ <p> <em> Loading.... </em> </p> }
else
{ <table class="table"> <thead> <tr> <th> Date </th> <th> Temp. (C) </th> <th> Temp. (F) </th> <th> Summary </th> </tr> </thead> <tbody> @foreach (var forecast in _forecasts)
{ <tr> <td> @forecast.Date.ToShortDateString() </td> <td> @forecast.TemperatureC </td> <td> @forecast.TemperatureF </td> <td> @forecast.Summary </td> </tr> } </tbody> </table> } </TelerikRootComponent> @code {
private WeatherForecast[]? _forecasts;

protected override Task OnInitializedAsync()=> _forecasts !=null ? Task.CompletedTask : UpdateForecasts();

private async Task UpdateForecasts()
{
_forecasts=null;
_forecasts=await WeatherService.UpdateForecasts(_listSize);
}

private readonly IEnumerable <int> _listSizes=[1,3,5,7];
private int _listSize=1;
} page: @page "/allweather" <Weather /> <Weather /> <Weather /> if I pick something in the dropdown in the first one, and then click anywhere on the page that isnt that component it reloads the list with a new set of random elements It works as expected without telerik components

### Response

**Dimo** commented on 18 Oct 2023

Blurring the DropDownList fires OnChange again and this executes UpdateForecasts (). This event handling is by design and in this case you can use ValueChanged instead of OnChange. Alternatively, implement a check in UpdateForecasts () to see if the new value is actually different from the previous one. I should also point out that putting <TelerikRootComponent> inside a non-layout component and using it multiple times on the page is a recipe for unwanted side effects and specifically, incorrect popup and dropdown position.
