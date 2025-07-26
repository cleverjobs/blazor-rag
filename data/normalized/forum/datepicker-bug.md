# datepicker bug

## Question

**Bru** asked on 19 Feb 2024

I use the TelerikDatePicker: I enter a date and I remove it again, then I click on the calendar icon and I receive an exception... Microsoft.AspNetCore.Components.Web.ErrorBoundary | Message: Unhandled exception rendering component: "Object reference not set to an instance of an object." System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TelerikDatePicker`1.get_AriaActiveDescendant() at Telerik.Blazor.Components.TelerikDatePicker`1.<>c__DisplayClass111_0.<BuildRenderTree>b__2(RenderTreeBuilder __builder2) at Microsoft.AspNetCore.Components.CascadingValue`1.Render(RenderTreeBuilder builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException)

## Answer

**Tsvetomir** answered on 21 Feb 2024

Hello Bruno, The occurrence of this error can be attributed to a race condition triggered by rapid, multiple UI refreshes. In this scenario, the DatePicker undergoes multiple recreations in quick succession. Consequently, the nested Calendar component is destroyed, rendering it inaccessible to the DatePicker and resulting in the observed exception. For further information about this problem, you can check our forum, where another customer is having the same issue as you. My colleague has provided some advice and the potential reasons that could be causing the problem. Regards, Tsvetomir Progress Telerik

### Response

**Dameon** commented on 16 Jul 2024

What is the root cause of the error occurring in the DatePicker component, and how can it be attributed to a race condition triggered by rapid UI refreshes, leading to the destruction of the nested Calendar component? basket random
