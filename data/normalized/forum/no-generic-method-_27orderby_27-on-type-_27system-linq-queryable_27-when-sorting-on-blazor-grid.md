# No generic method 'OrderBy' on type 'System.Linq.Queryable' when sorting on Blazor Grid

## Question

**SLSL** asked on 19 Dec 2019

My project is using the client/webassembly template and I get this error when I sort on the Grid. I am using CSLA business objects to bind to the grid by the way. It should just work since it derives from IEnumerable<T>. The TelerikBlazorApp project sample uses a plain List<WeaterForecast> so I wonder why it doesn't work with the CSLA BusinessList. Thanks. blazor.webassembly.js:1 WASM: ﻿Unhandled exception rendering component: h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: System.InvalidOperationException: No generic method 'OrderBy' on type 'System.Linq.Queryable' is compatible with the supplied type arguments and arguments. No type arguments should be provided if the method is non-generic. h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at System.Linq.Expressions.Expression.FindMethod (System.Type type, System.String methodName, System.Type[] typeArgs, System.Linq.Expressions.Expression[] args, System.Reflection.BindingFlags flags) <0x2a500d8 + 0x0012e> in <c9598198a7e340e28f933e3bfe55dba1>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at System.Linq.Expressions.Expression.Call (System.Type type, System.String methodName, System.Type[] typeArguments, System.Linq.Expressions.Expression[] arguments) <0x2a4fde8 + 0x00046> in <c9598198a7e340e28f933e3bfe55dba1>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.DataSource.SortDescriptorCollectionExpressionBuilder.Sort () <0x2d18610 + 0x00142> in <b8e61d62238c4666b5ff65df7544c779>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.DataSource.Extensions.QueryableExtensions.Sort (System.Linq.IQueryable source, System.Collections.Generic.IEnumerable`1[T] sortDescriptors) <0x2d18370 + 0x00014> in <b8e61d62238c4666b5ff65df7544c779>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.DataSource.Extensions.QueryableExtensions.CreateDataSourceResult[TModel,TResult] (System.Linq.IQueryable queryable, Telerik.DataSource.DataSourceRequest request, System.Func`2[T,TResult] selector) <0x2a47060 + 0x002fe> in <b8e61d62238c4666b5ff65df7544c779>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.DataSource.Extensions.QueryableExtensions.ToDataSourceResult (System.Linq.IQueryable queryable, Telerik.DataSource.DataSourceRequest request) <0x2a2e2a8 + 0x0000a> in <b8e61d62238c4666b5ff65df7544c779>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.DataSource.Extensions.QueryableExtensions.ToDataSourceResult (System.Collections.IEnumerable enumerable, Telerik.DataSource.DataSourceRequest request) <0x2a2d980 + 0x0000e> in <b8e61d62238c4666b5ff65df7544c779>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Data.TelerikDataSource.ProcessData (System.Collections.IEnumerable data) <0x2a2d850 + 0x0000a> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.TelerikGridBase`1[TItem].ProcessDataInternal () <0x2a2d590 + 0x0001c> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.TelerikGridBase`1[TItem].ProcessData () <0x2a72220 + 0x00156> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.TelerikGridBase`1[TItem].OnSort (Telerik.Blazor.Components.Grid.IGridHeader header) <0x2a71000 + 0x00104> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion (System.Threading.Tasks.Task task) <0x25a24e8 + 0x000e6> in <cbf249d7f04d4fa18d15bfae8ef7f389>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.Grid.GridHeaderRowBase`1[TItem].OnHeaderSort (Telerik.Blazor.Components.Grid.IGridHeader header) <0x2d06328 + 0x0014a> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion (System.Threading.Tasks.Task task) <0x25a24e8 + 0x000e6> in <cbf249d7f04d4fa18d15bfae8ef7f389>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Telerik.Blazor.Components.Grid.GridHeaderBase`1[TItem].ToggleSort () <0x2d05308 + 0x00100> in <a910a49758ca4acf83cce1dc84471cb6>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion (System.Threading.Tasks.Task task) <0x25a24e8 + 0x000e6> in <cbf249d7f04d4fa18d15bfae8ef7f389>:0 h.printErr @blazor.webassembly.js:1 blazor.webassembly.js:1 WASM: at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask (System.Threading.Tasks.Task taskToHandle) <0x25a9440 + 0x000c2> in <cbf249d7f04d4fa18d15bfae8ef7f389>:0 h.printErr @blazor.webassembly.js:1

## Answer

**Marin Bratanov** answered on 19 Dec 2019

Hi, This looks like an issue with the linker - the WASM flavor has been plagued by problems related to LINQ extension methods (which we need and use) and the linker consistently destroys them. At most versions (excluding 2.5.0) the workaround is to disable the linker (see the csproj snippet at the end): [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-side-project-considerations.) Could you upgrade to 2.5.1 and try that to see if it helps? Regards, Marin Bratanov

### Response

**SL** answered on 19 Dec 2019

Thank you that solved the problem. I was using the default Blazor webassembly template from VS 2019 and it did not have this option.

### Response

**Phil** answered on 09 Jan 2020

Hello, I am getting the same errors that SL got when I try to sort a column using a Telerik grid. My grid comes straight from an example on the Telerik website so I don't think that is the issue. I am using the latest version (2.5.1) and I have followed all of the steps in the article that you posted including disabling the linker in the csproj file. Also, I am using Blazor client side. Do you have any other suggestions / potential fixes for this issue? I can provide more information just let me know what you need. Thanks!

### Response

**Marin Bratanov** answered on 09 Jan 2020

Hi Phil, The only case that I know of this happening is when the linker has stripped out the extension methods we have and need. Thus, disabling the linker should fix it. Can you confirm there isn't a typo somewhere (like the name of the tag that disables the linker)? Can you try a project created with our VS extensions (see here to get them, here on how to create one) - the Grid and Menu example works fine for me, both in its client and server flavors. If neither of this helps, please open a support ticket and send me a sample that show the problem so I can look into it and avoid guessing. Regards, Marin Bratanov

### Response

**Phil** answered on 09 Jan 2020

Hey Marin, So I was able to get everything working by creating a new solution using the Telerik extension. I was comparing that new solution to my old one and was unable to find any differences unfortunately. I checked and the tag that disables the linker was spelled correctly too. Anyway I just decided to move my files into the new solution and use that. Thanks!

### Response

**Marin Bratanov** answered on 09 Jan 2020

Hi Phil, It's good to hear you have this working now. My best guess now (considering that the projects are identical) is that something that was built badly (probably with a linker on) lingered in the bin or obj folders, and you kept getting that cached build which errored out. You could deleted the bin and obj folders from the problematic project and rebuild to see if that was the case. Regards, Marin Bratanov
