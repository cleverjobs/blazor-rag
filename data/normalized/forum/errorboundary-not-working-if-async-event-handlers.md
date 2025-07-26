# ErrorBoundary not working if async event handlers

## Question

**Cae** asked on 09 Feb 2024

Hi, This seems to effect most telerik components, but if for example using a TelerikCheckBox and the ValueChanged event is an async function, then the error boundry wont catch the exception. This works from basic checkboxes or if not using async. Example: <div> Telerik checkbox (does NOT display any error): <TelerikCheckBox TValue="bool" ValueChanged="@OnCheck" /> </div> <div> Basic checkbox (displays the error): <input type="checkbox" @onchange="@OnCheck" /> </div> @{
async Task OnCheck()
{
throw new Exception("Something went wrong!");
}
} MainLayout: <ErrorBoundary> <ChildContent> <div class="page"> <div class="sidebar"> <NavMenu /> </div> <main> <div class="top-row px-4"> <a href="[https://learn.microsoft.com/aspnet/core/"](https://learn.microsoft.com/aspnet/core/") target="_blank"> About </a> </div> <article class="content px-4"> <TelerikRootComponent> @Body </TelerikRootComponent> </article> </main> </div> </ChildContent> <ErrorContent> ERROR!!! </ErrorContent> </ErrorBoundary>

## Answer

**Dimo** answered on 14 Feb 2024

Hello Caesar, Indeed, we are aware of such an issue with our ValueChanged handlers, or to be more precise, all PropertyChanged handlers. Here are a few public items logged for similar scenarios: [https://feedback.telerik.com/blazor/search?searchterm=errorboundary](https://feedback.telerik.com/blazor/search?searchterm=errorboundary) The exact reason and possible fix are still unknown, as the ErrorBoundary documentation is scarce. Our assumption is that when we use internally JSInterop with regard to the event firing, ErrorBoundary is unable to catch the exception, because it happens outside the .NET component tree. Regards, Dimo Progress Telerik

### Response

**Caesar** commented on 15 Feb 2024

Well, from what I can see in your source code, this has a natural explanation. These events are handled by TelerikInputBase.TriggerChange, but that function is not async, and it does throw away the task that invokes the external event: _=OnChange.InvokeAsync(value); Should be: await OnChange.InvokeAsync(value); And async all the way up to the triggering event.

### Response

**Dimo** commented on 19 Feb 2024

Thanks for the follow-up. I forwarded this to our developers and will update this thread once I get their opinion.

### Response

**Dimo** commented on 20 Feb 2024

P.S. We tested the suggested change ( await OnChange.InvokeAsync(value); ) in our source code together with the Razor markup above. There was no difference in the app behavior and the ErrorBoundary was still unable to detect the exception. There must be something else in play, but we are not sure what exactly. If you can make the ErrorBoundary work with a modified version of our source code, you can open a private ticket and show us. We will be interested to take a look how you achieved it.

### Response

**Caesar** commented on 22 Feb 2024

Well, this is a little bit strange. If I make a custom checkbox component like this: <input type="checkbox" @onchange="@OnCheckboxChange" /> @code {
[Parameter]
public EventCallback <object> ValueChanged { get; set; }

async Task OnCheckboxChange()
{
await this.ValueChanged.InvokeAsync(true);
}
} That does work! If I remove the async code above, it does not work, this was expected. From what I can see, this is basically what the code looks like in your code, so I changed to async/await all the way in your code also, but it still does not work. Or is there some javascript involved that breaks this?

### Response

**Caesar** commented on 22 Feb 2024

Even stranger... If I put the exact code above in your project as a Component, it does not work. If the exact code above is inside my project, it does work. So something works differently only if the component is in your project...

### Response

**Dimo** commented on 23 Feb 2024

Hm, yes, I agree this looks quite peculiar indeed. Thank you for these updates - I added your observations to our internal GitHub issue, so that the devs take them into account. I also awarded you some Telerik points.
