# Error on DatePicker component for Blazor

## Question

**Alf** asked on 12 Jul 2023

Getting error when clicking on calendar icon in TelerikDatePicker in a Blazor Web Server app: Error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikDatePicker`1.get_AriaActiveDescendant() at Telerik.Blazor.Components.TelerikDatePicker`1.<BuildRenderTree>b__154_1(RenderTreeBuilder __builder2) at Microsoft.AspNetCore.Components.CascadingValue`1.Render(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException) Doesn't happen to all DatePickers, only on certain ones. Also, this only happens when the app is published to IIS on Windows Server 2019. This does not happen when running in development in Visual Studio 2022 Professional. Using Telerik UI for Blazor v3.5

### Response

**Alexey** commented on 31 May 2024

I have the same issue. I use TelerikDateTimePicker inside a form. When I try to clean up TelerikDateTimePicker using keyboard backspace and then click mouse by Calendar icon I get error: System.NullReferenceException: Object reference not set to an instance of an object.

### Response

**Dimo** commented on 03 Jun 2024

@Alexey The information from my other response in this thread applies. We are not able to reproduce the error on our side, so if you need further assistance, please send us an isolated runnable example that we can troubleshoot.

## Answer

**Dimo** answered on 14 Jul 2023

Hello Alfredo, This error can occur due to a race condition, which is caused by fast multiple UI refreshes. As a result, the DatePicker is recreated several times one after the other, which destroys the nested Calendar component, and the DatePicker cannot find it. This causes the exception. In general, the AriaActiveDescendant getter in our source code looks like this: private string AriaActiveDescendant=> IsPopupVisible ? CalendarRef.CurrentCellId : null; IsPopupVisible is defined like this: private bool IsPopupVisible=> PopupRef?.Visible==true; IsPopupVisible is not mentioned in the stack trace and CurrentCellId is always a Guid. So the error can occur only if PopupRef is defined and visible, but the CalendarRef is null. I have seen this error a couple of times in the past and the developers were doing something like this: Fast double refresh of the UI. For example, executing StateHasChanged inside an EventCallback, which leads to double StateHasChanged. (Blazor calls StateHasChanged after EventCallbacks automatically). Subscribing to an event handler in such a way, so that it was getting called multiple times one after the other. In one case, a customer confirmed that the DatePicker exception occurred when some code of another non-Telerik event hander was executed, but that's all I know - the customer seems to have resolved the problem on their own. So my advice is to review the app logic, which revolves around the DatePicker and its value, as well as other related app event handlers. Try to find what is causing the multiple UI refreshing. Then, either reduce the number of UI refreshes, or insert a delay between them. Regards, Dimo

### Response

**Ted** commented on 12 Mar 2025

We are experiencing this exact issue, and your advice is NOT helpful, at all, Dimo. This needs to be fixed at the Telerik end please, to make sure this race condition cannot happen! This is happening in Telerik Blazor v6, v7 and v8 under .NET 8 and 9. It's ridiculous to expect clients to try to figure out a bug like this. Please fix!

### Response

**Dimo** commented on 13 Mar 2025

@Ted - this issue is now fixed and the changes will take effect in our next release.

### Response

**Vlad** commented on 24 Apr 2025

@Dimo Was it part of 8.1.1 release or will it be in the next one?

### Response

**Dimo** commented on 25 Apr 2025

@Vlad - the fix will be included in the coming release in mid-May 2025.

### Response

**Ted** commented on 25 Apr 2025

@Dimo Thank you for getting a fix in! We'll look forward to testing it out in the next release.
