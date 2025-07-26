# iOS error with TelerikColorPicker

## Question

**And** asked on 22 Apr 2025

I'm using the TelerikColorPicker in my Maui Blazor hybrid code like this: <TelerikColorPicker @bind-Value="@_color" View="@Telerik.Blazor.ColorPickerView.Palette" AdaptiveMode="@Telerik.Blazor.AdaptiveMode.Auto" />...
@code { private string? _color; } This works fine in Windows. However, it throws an error in iOS: null is not an object (evaluating 'this.element.addEventListener')
bindEvents@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063454
@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063348
initPopupNavigationService@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054798
s@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054360
@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:23:2177305
@app://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:695018
@app://0.0.0.1/_framework/blazor.webview.js:1:2891
Promise@[native code]
beginInvokeJSFromDotNet@app://0.0.0.1/_framework/blazor.webview.js:1:2859
@app://0.0.0.1/_framework/blazor.webview.js:1:47081
@user-script:1:4:75
forEach@[native code]
@user-script:1:4:45 And also in Android: [INFO:CONSOLE(1)] "Cannot read properties of null (reading 'addEventListener')
TypeError: Cannot read properties of null (reading 'addEventListener')
at e.NavigationService.bindEvents ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063455)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063455))
at new e.NavigationService ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063338)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1063338))
at s.initPopupNavigationService ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054775)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054775))
at new s ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054334)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:1054334))
at e.initComponent ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:23:2177300)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:23:2177300))
at e.initColorPicker ([https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:695018)](https://0.0.0.1/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js:1:695018))
at [https://0.0.0.1/_framework/blazor.webview.js:1:2891](https://0.0.0.1/_framework/blazor.webview.js:1:2891)
at new Promise ( <anonymous> )
at y.beginInvokeJSFromDotNet ([https://0.0.0.1/_framework/blazor.webview.js:1:2848)](https://0.0.0.1/_framework/blazor.webview.js:1:2848))
at External.__callback ([https://0.0.0.1/_framework/blazor.webview.js:1:47076)](https://0.0.0.1/_framework/blazor.webview.js:1:47076))
at Microsoft.JSInterop.JSRuntime. <InvokeAsync> d__16`1[[System.Object, System.Private.CoreLib, Version=9.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext()
at Telerik.Blazor.Components.TelerikColorPicker.InitColorPicker()
at Telerik.Blazor.Components.TelerikColorPicker.OnAfterRenderAsync(Boolean firstRender)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)", source: [https://0.0.0.1/_framework/blazor.webview.js](https://0.0.0.1/_framework/blazor.webview.js) (1) The error is coming from async Task TelerikColorPicker.InitColorPicker() Has anyone seen anything like this? Thanks Andrew

## Answer

**Anislav** answered on 22 Apr 2025

The sample you provided should be working. I tested it using the following REPL: [https://blazorrepl.telerik.com/mfEewcPy10jEalCo17,](https://blazorrepl.telerik.com/mfEewcPy10jEalCo17,) and it worked fine. What version of Telerik UI for Blazor are you using? Regards, Anislav Atanasov

### Response

**Andrew** commented on 22 Apr 2025

I'm using 8.1.1 <PackageReference Include="Telerik.UI.for.Blazor" Version="8.1.1" />

### Response

**Andrew** commented on 22 Apr 2025

In my debugging, the issue seems to be around the AdaptiveMode attribute. If I don't explicitly set it or set it to None (the default), the error doesn't occur. AdaptiveMode=Auto works on Windows but not on Android or iOS devices (again, this is in a Maui Blazor hybrid app). I'm guessing that AdaptiveMode=Auto has to set up some extra functionality to resize the control if the screen size changes. This set up seems to be expecting an element in the DOM that doesn't exist.

### Response

**Anislav** commented on 22 Apr 2025

What you're saying is reasonable. You can report a bug on the following page: [https://feedback.telerik.com/blazor.](https://feedback.telerik.com/blazor.) I also recommend trying to downgrade by 1–2 versions to check whether this is a recently introduced bug. Regards, Anislav Atanasov
