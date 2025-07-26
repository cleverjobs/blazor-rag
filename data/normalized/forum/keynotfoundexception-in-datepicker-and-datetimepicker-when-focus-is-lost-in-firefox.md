# KeyNotFoundException in DatePicker and DateTimePicker when focus is lost in Firefox

## Question

**Tho** asked on 16 Mar 2023

Hi, when using the DatePicker or DateTimePicker in my project i get the following error when focus is lost in Firefox: Uncaught (in promise) Error: System.Collections.Generic.KeyNotFoundException: Arg_KeyNotFoundWithKey, inputElementValue
at System.Collections.Generic.Dictionary`2[[System.String, System.Private.CoreLib, Version=7.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Text.Json.JsonElement, System.Text.Json, Version=7.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51]].get_Item(String )
at Telerik.Blazor.Components.Common.DateInputs.DateInput`1[[System.DateTime, System.Private.CoreLib, Version=7.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].DateInput_Focus(Dictionary`2 args)
at Microsoft.JSInterop.Infrastructure.DotNetDispatcher.InvokeSynchronously(JSRuntime , DotNetInvocationInfo& , IDotNetObjectReference , String )
at Microsoft.JSInterop.Infrastructure.DotNetDispatcher.BeginInvokeDotNet(JSRuntime , DotNetInvocationInfo , String ) How to reproduce: I use VS2022 .NET 7, Telerik Blazor 4.1.0 Just create a Blazor WASM Client project. Add the DatePicker. Publish with AOT and run in Firefox. Current culture is set to german. Simply set the focus on the datepicker, then hit "Tab"-key to switch to another component. Then I get the above error. When using Chrome, this does not happen. Also tested on different machines. Error occurs only in Firefox. If you need more information please let me know. Regards, Thomas

### Response

**Domingos Portela** commented on 17 Mar 2023

I have he same problem.

### Response

**Domingos Portela** commented on 17 Mar 2023

I also already solved the problem. I had forgotten to change the javascript version.

## Answer

**Thomas** answered on 16 Mar 2023

Hi again, sorry to have bothered you with this error. It seems to clear all caches in Firefox and reloading the whole page did the trick in the end. I tried it several times before but now it worked somehow. Regards, Thomas
