# Bind TelerikDropDownList to List of tuple

## Question

**Cla** asked on 23 Mar 2021

I'm trying to bind a TelerikDropDownList to a list of tuple, but without success. <TelerikDropDownList Data="@Items" TextField="Text" ValueField="Value" @bind-Value="@Value"></TelerikDropDownList> @code { private List<(string Text, int Value)> Items { get; set; } private int Value {get;set;} protected override void OnInitialized() { base.OnInitialized(); CreditSafeContractNotificationTypes=new List<(string Text, int Value)>() { ("Text1", 0), ("Text2", 1), }; } } in chrome console i obtain this error: Microsoft.AspNetCore.Components.WebAssembly.Rendering.WebAssemblyRenderer[100] Unhandled exception rendering component: Object reference not set to an instance of an object. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikDropDownList`2[[System.ValueTuple`2[[System.String, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].<OnParametersSetAsync>b__57_1(ListDataItem item) at System.Linq.Enumerable.TryGetFirst[ListDataItem](IEnumerable`1 source, Func`2 predicate, Boolean& found) at System.Linq.Enumerable.FirstOrDefault[ListDataItem](IEnumerable`1 source, Func`2 predicate) at Telerik.Blazor.Components.TelerikDropDownList`2.<OnParametersSetAsync>d__57[[System.ValueTuple`2[[System.String, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() at Telerik.Blazor.Components.Common.TelerikSelectBase`2.<SetParametersAsync>d__133[[System.ValueTuple`2[[System.String, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]], System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Int32, System.Private.CoreLib, Version=5.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]].MoveNext() What's wrong? Thanks

## Answer

**Claudio** answered on 23 Mar 2021

wrong code paste, replace CreditSafeContractNotificationTypes with Items the problem still remain

### Response

**Marin Bratanov** answered on 24 Mar 2021

Hello Claudio, The DropDownList component supports binding to a list of primitive values (numbers, strings, guids, enums), or to an instance of a model. You can find these two approaches in the following article: [https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind.](https://docs.telerik.com/blazor-ui/components/dropdownlist/data-bind.) A tuple is not a supported data type that the component can use. Regards, Marin Bratanov
