# Issue with Dispose and TreeView

## Question

**Joh** asked on 20 Apr 2021

Hi, We are using among other components the TreeView component for showing an hierarchical view of an organization and that works fine in most cases, there is however an issue that happens when the users are quick to navigate between views and we get an error: crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Cannot read property 'addEventListener' of null TypeError: Cannot read property 'addEventListener' of null After some investigation of the code and how the TreeView works we can see that this probably happens due to that the OnAfterRenderAsync of the TreeView runs InitTreeView which calls JSInterop to set event handling for example: this.element.addEventListener(h, this.onKeyDown), this.element.addEventListener(f, this.onMouseDown), this.options.draggable && this.createDraggable() but since this is run in OnAfterRenderAsync it may happen even after the component is disposed and removed from the DOM so the elements are no longer available and the error occurs. Is this a known issue and is there a way to handle it? Best regards Johan

### Response

**Marin Bratanov** commented on 20 Apr 2021

Hi Johan, Could you check if the scenario and issue described here are what you are having: [https://feedback.telerik.com/blazor/1466134-navigating-and-disposing-a-treeview-throws-errors-in-a-webassembly-app-unknown-edit-type-0?](https://feedback.telerik.com/blazor/1466134-navigating-and-disposing-a-treeview-throws-errors-in-a-webassembly-app-unknown-edit-type-0?) If not, how is the treeview related to the navigation, and when is the error thrown? Also, does this happen with the latest version (2.23.0 at the time of writing)? Regards, Marin Bratanov

### Response

**Johan** commented on 20 Apr 2021

Hi Marin, Thank you for the quick answer! We don't get the same error as in the mentioned issue (unknown-edit-type-0), our treeview is used in a component which is used in a page and the only relation to navigation is that when a user navigates the page gets disposed along with the components in it. We are using the latest version, 2.23.0. The error is thrown after a navigation has happened and the component is disposed, but since the OnAfterRenderAsync already has been called and not completed the error is thrown when the TreeView tries to bind the events to an html-element that no longer exists. The issue only happens if the user don't wait until the page is fully rendered before they click on another page/view but since that can happen quite often this issue is causing problems. Best regards Johan

### Response

**Marin Bratanov** commented on 20 Apr 2021

Hi Johan, Can you send me a sample that shows the error you get? That scenario (a treeview being disposed during navigation) cases the error described in the Feedback Portal page I linked. Regards, Marin Bratanov Progress Telerik

### Response

**Johan** commented on 27 Apr 2021

Hi Marin, Unfortunately I don't have the time at the moment to create a sample project for the issue, we have decided to not use the treeview at the moment since it doesn't work but I will get back to this issue when I have the time to create a viable solution that shows the problem. Best regards Johan

### Response

**Marin Bratanov** commented on 27 Apr 2021

Hi Johan, If you do manage to create a reproducible sample, please send it over. Without being able to reliably reproduce a bug, I could only guess and that's not very efficient. Best regards, Marin

### Response

**Adam** commented on 06 Jan 2022

Were there any solutions to this issue? I believe we are having the same issue on 2.30.0. In our case if our project runs as native wasm (from index.html in root of client project) it works. When I change the project to spin up as blazor server hybrid (runs from _host.cshtml in server project, server project runs client App.razor as server prerendered) we see the errors you described. We are just starting to build out our project and had a TelerikTextBox on the index.razor page for testing. If I remove it the error goes away when starting up the app. I'm guessing it is related to the above mention that if the page navigation is changing before OnAfterRenderAsync completes it throws the exception. It could be server prerendering is causing the error or an authorization cycle. In either case, could the telerik blazor library be updated to null check this condition so it doesn't throw an exception when the thing it is expecting doesn't exist anymore? If components are being disposed then it shouldn't be throwing exceptions because that kills the app when the JSRuntimeInterop throws back the exception. I also don't have a slimmed down project to post. I'll try to test adding Telerik Blazor to the sample Hybrid Blazor project here: [https://itnext.io/blazor-switching-server-and-webassembly-at-runtime-d65c25fd4d8](https://itnext.io/blazor-switching-server-and-webassembly-at-runtime-d65c25fd4d8) Github project: [https://github.com/jdtcn/HybridBlazor](https://github.com/jdtcn/HybridBlazor) crit: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100]
Unhandled exception rendering component: Cannot read properties of null (reading 'addEventListener')
TypeError: Cannot read properties of null (reading 'addEventListener')
at e.value ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17566)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17566))
at new e ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17449)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17449))
at r ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:1:23547)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:1:23547))
at Object.r ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:18067)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:18067))
at [https://localhost:44349/_framework/blazor.webassembly.js:1:3332](https://localhost:44349/_framework/blazor.webassembly.js:1:3332)
at new Promise ( <anonymous> )
at Object.beginInvokeJSFromDotNet ([https://localhost:44349/_framework/blazor.webassembly.js:1:3306)](https://localhost:44349/_framework/blazor.webassembly.js:1:3306))
at Object.Rt [as invokeJSFromDotNet] ([https://localhost:44349/_framework/blazor.webassembly.js:1:59738)](https://localhost:44349/_framework/blazor.webassembly.js:1:59738))
at _mono_wasm_invoke_js_blazor ([https://localhost:44349/_framework/dotnet.6.0.1.ynjylm5yl3.js:1:194546)](https://localhost:44349/_framework/dotnet.6.0.1.ynjylm5yl3.js:1:194546))
at wasm://wasm/009705ea:wasm-function[219]:0x1a129
Microsoft.JSInterop.JSException: Cannot read properties of null (reading 'addEventListener')
TypeError: Cannot read properties of null (reading 'addEventListener')
at e.value ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17566)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17566))
at new e ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17449)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:17449))
at r ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:1:23547)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:1:23547))
at Object.r ([https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:18067)](https://blazor.cdn.telerik.com/blazor/2.30.0/telerik-blazor.min.js:61:18067))
at [https://localhost:44349/_framework/blazor.webassembly.js:1:3332](https://localhost:44349/_framework/blazor.webassembly.js:1:3332)
at new Promise ( <anonymous> )
at Object.beginInvokeJSFromDotNet ([https://localhost:44349/_framework/blazor.webassembly.js:1:3306)](https://localhost:44349/_framework/blazor.webassembly.js:1:3306))
at Object.Rt [as invokeJSFromDotNet] ([https://localhost:44349/_framework/blazor.webassembly.js:1:59738)](https://localhost:44349/_framework/blazor.webassembly.js:1:59738))
at _mono_wasm_invoke_js_blazor ([https://localhost:44349/_framework/dotnet.6.0.1.ynjylm5yl3.js:1:194546)](https://localhost:44349/_framework/dotnet.6.0.1.ynjylm5yl3.js:1:194546))
at wasm://wasm/009705ea:wasm-function[219]:0x1a129
at Microsoft.JSInterop.JSRuntime. <InvokeAsync> d__16`1[[System.Object, System.Private.CoreLib, Version=6.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext()
at Telerik.Blazor.Components.Common.TextBoxBase.InitJsComponentAsync()
at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderInternalAsync(Boolean firstRender)
at Telerik.Blazor.Components.Common.TextBoxBase.OnAfterRenderAsync(Boolean firstRender)
at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle, ComponentState owningComponentState)

### Response

**Marin Bratanov** commented on 06 Jan 2022

HI Adam, Disposing components, especially when JS Interop needs to be used then, has always had issues in Blazor, mostly due to the lack of a real "unmount" lifecycle hook, and doing things through IDisposable has had issues (see here, here and here for examples of one of the problems that one can hit when you try to improve some things there). That said - yes, we would like to improve things, but to see if your case is the same as this issue we know of, we need to know the exact scenario. If you cannot confirm this yourself (and use the workaround proposed there if this is what you hit), I would suggest opening a support ticket so you can attach a project we can run and observe the error. This will let us see where it is stemming from and whether it is this issue, or a new one should be logged. To also answer your question on whether this was ever solved - this thread has not been solved to my knowledge because we never got a reproducible to see what's going on, and we haven't gotten to fixing that known error condition.

### Response

**Johan** commented on 13 Jan 2022

Hi, Unfortunatelly we never got back to this since we decided to not use the TreeView due to that it didn't work so we created our own component for it and then this issue was placed in the backlog. Best regards Johan
