# Razor Components

## Question

**Sha** asked on 05 Nov 2019

Is there documentation covering using UI for Blazor as Razor Components mixed within Razor Pages and MVC? Currently the focus of the docs seem to only cover Blazor only type apps? Admin edit: Here is a link to an example: [https://github.com/telerik/blazor-ui/tree/master/common/razor-components](https://github.com/telerik/blazor-ui/tree/master/common/razor-components)

## Answer

**Marin Bratanov** answered on 05 Nov 2019

Hello Shannon, We have the following KB article that explains the basics, even though it was written several Previews of the framework earlier. The current latest (3.1 Preview 2) changes the way razor components are to be references (from an HTML helper to a tag helper), and we are working on a release that offers compatibility with Preview 2 as I am writing this. It is projected to go live tomorrow (barring any unforseen showstoppers) and I'd suggest testing out the approach from the article with the new info (see here ) and our new release (2.3.0). Regards, Marin Bratanov

### Response

**Shannon** answered on 05 Nov 2019

Thank you Marin, for the quick reply. Looking forward to trying out 3.1 Preview 2. It has some nice enhancements. Please post back once the release has been posted. I did find this KB discussing how to use UI for Blazor with Razor Components: [https://docs.telerik.com/blazor-ui/knowledge-base/blazor-in-asp-net](https://docs.telerik.com/blazor-ui/knowledge-base/blazor-in-asp-net)

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hi Shannon, Indeed, this is the KB I intended to link. Why the link is not in my post is beyond me :) The 2.3.0 release that supports .NET Core 3.1 Preview 2 is now available. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hello again, I just tested the setup and I feel like Blazor components in a Razor page are now broken. Even the standard Counter component no longer works. I see no SignalR messages going back and forth which indicates that somehow Blazor simply does not work anymore in this setup - only the server pre-rendering produces some initial markup but that's not enough. I am attaching the project I tested with in case I am missing something that you can notice. Regards, Marin Bratanov

### Response

**Shannon** answered on 07 Nov 2019

When you say it doesn't work, you mean Razor Components of any kind or Kendo UI Components?

### Response

**Shannon** answered on 07 Nov 2019

I have a fiarly large project using Razor Pages and upgraded everything including Blazor UI 2.3.0 and have no issues. Did you upgrade the Runtime?

### Response

**Marin Bratanov** answered on 07 Nov 2019

Hi Shannon, To answer each question in turn Which components don't work for me - on my end no Blazor components work in the test Razor page I made. Not even a simple button. This, of course, carries over the same issue to the Telerik Blazor components. The Kendo widgets are jQuery based so they should keep working in a razor page like they did before. Upgrading the Runtime - I am at .NET Core 3.1. Preview 2, and I created a brand new project with the latest references (both of Blazor and of the Telerik components). It is attached to my previous post ( direct link ). Does this run for you? Did I miss anything obvious? Can you send me a simple app that runs? If you can run my sample or make a simple example that works, I'd encourage you to open a pull request with it in this repo: [https://github.com/telerik/blazor-ui.](https://github.com/telerik/blazor-ui.) Regards, Marin Bratanov

### Response

**Shannon** answered on 08 Nov 2019

First thing I notice is that the project is using the client version of Blazor. By app is an MVC/Pages app. Yours is a client side Blazor app. Pretty sure things like SignalR do not work in the version you are using.

### Response

**Shannon** answered on 08 Nov 2019

Update, I need to do a PR. Will be several hours before I get time to do the PR. I did get things working.

### Response

**Shannon** answered on 08 Nov 2019

Created a working PR with the example. Order seems to be important in the Configure Services. Layout was also changed. BlazorGridData does not exist so used a Window to show a working Telerik Component

### Response

**Marin Bratanov** answered on 08 Nov 2019

Hello Shannon, Thank you for the pull request, your Telerik points are updated. I had missed initializing the Blazor hub on the client, it was not needed explicitly the last time I made such a sample for the KB. It also seems that the framework has issues in the way parameters are passed - it seems to have been reported and is considered resolved by MS, but it still manifests. So, I added comments and examples about it in the sample. The problem is not that the sample data from the razor page does not exist, but that passing it as a parameter to a component breaks the component tree. For anyone else looking for such an example - here's a link: [https://github.com/telerik/blazor-ui/tree/master/common/razor-components.](https://github.com/telerik/blazor-ui/tree/master/common/razor-components.) I also added it to the opener post. Regards, Marin Bratanov

### Response

**Shannon** answered on 08 Nov 2019

Just a note that this will work @(await Html.RenderComponentAsync<SomeComponent>(RenderMode.Server, new { Object=Model.Object, Username=username }))

### Response

**Marin Bratanov** answered on 08 Nov 2019

Hello Shannon, On my end it throws the same error. In the sample in the repo, I tried @(await Html.RenderComponentAsync<Counter>(RenderMode.Server, new { Customers=Model.BlazorGridData.Take(4) })) and @(await Html.RenderComponentAsync<Counter>(RenderMode.ServerPrerendered, new { Customers=Model.BlazorGridData.Take(4) })) and both threw the same error that I get from <component type="typeof(Counter)" render-mode="ServerPrerendered" param-Customers="@Model.BlazorGridData.Take(4)" /> Does this work for you on that sample? Regards, Marin Bratanov

### Response

**Shannon** answered on 08 Nov 2019

No, it does not work in the sample. Strange thing in my large app it is working. In the js console I see this error. Error: The list of component records is not valid.

### Response

**Shannon** answered on 08 Nov 2019

Created another PR using an anonymous object. Created a simple list not using a Telerik Component. Seems like you may have a bug related to sequence numbers.

### Response

**Marin Bratanov** answered on 08 Nov 2019

Hi Shannon, This error is why I did not include parameters to any of the components in the sample, and why you could not get our grids working initially, and I referenced those issues in the comments in the code. The sequence numbers that throw errors are not something in our control, we don't set them anywhere (I don't think we even can set them). It seems that this is the sequencing of components that the framework uses for its diff engine, and the same problem arises not just with our components, but also with the Counter component from the current sample: [https://github.com/telerik/blazor-ui/blob/master/common/razor-components/razor-pages/Pages/Index.cshtml#L32.](https://github.com/telerik/blazor-ui/blob/master/common/razor-components/razor-pages/Pages/Index.cshtml#L32.) I will try to find something else on this matter, but I don't think it is a bug in our components at this stage, it looks like a generic framework problem because the stack trace of the error does not contain anything related to Telerik. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 08 Nov 2019

On my end even this simple list component throws exceptions, even when it is the only Razor component on the page, without any Telerik components in it. I closed the current pull request because it does not fix the current problems, and I exposed the information about this framework issue better in the readme file. Regards, Marin Bratanov
