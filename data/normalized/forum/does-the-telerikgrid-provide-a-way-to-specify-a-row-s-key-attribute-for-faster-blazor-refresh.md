# Does the TelerikGrid provide a way to specify a row's @key attribute for faster blazor refresh

## Question

**Mar** asked on 19 Apr 2024

I think I may have posted this question perhaps incorrectly in Technical Support, but let's try here anyways. I have data I display in a grid that get's re-fetched from the server every second. In Microsoft's QuickGrid, there is an ItemKey attribute that lets you specify a row entries Key so that Blazor can perform it's diff operation more effectively: <QuickGrid Items="@_Items" ItemKey="(item)=> item.Guid" Theme=""> I'm now wanting to switch the QuickGrid out with Telerik's Grid, but can't seem to find any mention of this feature. Does Telerik provide the ability to specify a row's key (so as to improve blazor's diffing algorithm) and if not what is recommended for scenarios where the grid's data is to be re-fetched every second? Much thanks Marcin

## Answer

**Dimo** answered on 24 Apr 2024

Hello Marcin, I am copy-pasting my ticket response, so that other developers can benefit from it too:===We use @key internally in our source code as a best practice, but currently don't expose a way for developers to define a custom @key. I just raised a discussion with the developers if this is something we could consider as a future enhancement. If we agree on that, I will log a public feature request on your behalf and you will receive an email notification. Currently we use the data item object as a @key, which relies on a reference comparison. This may be OK or even desirable in general, but may not be effective in your case, if you reload the data from the database often and the data item references change every time. That's why a possible way to rely on a value-type comparison across rebinds is to override the Equals method of the Grid model class. Here is an example: [https://blazorrepl.telerik.com/mIEoQyFv171mC31G57](https://blazorrepl.telerik.com/mIEoQyFv171mC31G57) In addition, all general performance optimization techniques apply: Use paging or virtual scrolling. Use a smaller PageSize - it's applicable to both paging and row virtualization. Use virtual columns, if the number of columns is too large. We have some more performance tips here.===Regards, Dimo Progress Telerik
