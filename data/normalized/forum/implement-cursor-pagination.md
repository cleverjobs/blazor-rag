# Implement cursor pagination

## Question

**Cla** asked on 23 Jan 2024

hi, i would like to know if the grid support server side cursor pagination (keyset pagination) instead of the standard offset pagination who use page number to navigate through the pages, and an example to implement it. Thanks

## Answer

**Nadezhda Tacheva** answered on 26 Jan 2024

Hi Claudio, If I properly understand, you are looking for an option to change the Grid pages via keyboard. Is that correct? If this is the case, you can currently achieve that if you enable the Grid keyboard navigation by setting the Navigable property to "true". The Grid supports keyboard navigation for the integrated pager element. You can find the list of shortcuts here: [https://demos.telerik.com/blazor-ui/pager/keyboard-navigation.](https://demos.telerik.com/blazor-ui/pager/keyboard-navigation.) Regards, Nadezhda Tacheva Progress Telerik

### Response

**Claudio** commented on 31 Jan 2024

Hi Nadezhda, my question is about an alternative pagination method called "cursor pagination" or "keyset pagination", instead of the classic offset pagination. You can find some info here: [https://betterprogramming.pub/understanding-the-offset-and-cursor-pagination-8ddc54d10d98](https://betterprogramming.pub/understanding-the-offset-and-cursor-pagination-8ddc54d10d98) In summary, the current grid pagination is offset based so it need the page number and the page size, the cursor pagination instead take as parameters the cursor value (calculated on the sort field value) and the page size.

### Response

**Nadezhda Tacheva** commented on 01 Feb 2024

Hi Claudio, Thank you for the clarification! Now I understand your requirement. Cursor paging is possible with custom coding. Here is how to implement such pagination: Bind the Grid with its OnRead event. In this way, you will have full control over the data request and the returned data. If needed, cache the returned data ( DataSourceResult.Data ) to a Razor component variable. In this way, you will know what items the user is seeing, which is first and which is last. If needed, disable the built-in Grid paging and use the Grid ToolBar for custom paging UI. You can also use any custom UI outside the Grid. In the OnRead handler, analyze the values in the DataSourceRequest object ( args.Reques t). If needed, change them before querying the data source, based on values from the custom paging UI. To achieve cursor paging in the data source, you need to pass a filter criterion in the read request. To do this, set the appropriate filter descriptor(s) in the DataSourceRequest object in the OnRead event handler. Here is a basic sample: [https://blazorrepl.telerik.com/cIamabvH40AGkKNi16.](https://blazorrepl.telerik.com/cIamabvH40AGkKNi16.) I hope this will help you move forward with your application.

### Response

**Claudio** commented on 02 Feb 2024

Thanks Nadezhda, this can be done using virtual scroll?

### Response

**Claudio** commented on 07 Feb 2024

Hi Nadezhda, i successfully implemented cursor pagination with toolbar buttons but i would like to use virtual scroll so the user can navigate through the pages without select previous or next button but only scrolling the grid. Can you provide me an example with virtual scroll? I think it would be great to add there cursor paging sample code in the grid documentation.

### Response

**Nadezhda Tacheva** commented on 12 Feb 2024

Hi Claudio, I am glad that you managed to successfully implement cursor pagination with toolbar buttons. The code I shared is just a basic sample of potential implementation. The UI for changing the pages may vary depending on the desired result. This is essentially a custom solution and as such, it should not be included in the official Grid documentation. The scenario generally falls outside of the standard support scope but I can assist by providing some guidance. When virtual scrolling is used, the OnRead event fires each time when the user scrolls. You can catch if the user is scrolling up or down (and how much) if you check the Skip property of the DataSourceRequest object and compare it to the previous Skip value, which you will need to store somewhere.

### Response

**Claudio** commented on 13 Feb 2024

Thanks Nadezhda for your support. I'm trying to implement cursor paging with virtual scroll with the info you provided me. I can determine the direction of the scroll as you suggested (comparing the skip value with the previous one) but i have some doubt about loading data: the data requested on the OnRead are always contiguous? because if not i think i can't use virtual scroll. With the cursor pagination i have implemented i have the info about first, last, previous and next page (or window) of data. Now, first and last are absolute positions, but previous and next are relative to the current position (current page or current window of data). Scrolling with virtual scroll will request always contiguous data? For example if i have total items count=100 and a PageSize=20, moving the scroll down in a single step from the beginning to the end, will raise all the pages with multiple OnRead request (with Skip=0, Skip=20, Skip=40, Skip=60, Skip=80) or it can raise a single OnRead with Skip=80?

### Response

**Nadezhda Tacheva** commented on 16 Feb 2024

Hi Claudio, Whether the requested records will be contiguous depends on how much the user scrolls. With OnRead and virtual scrolling enabled, the Grid tracks how much the user scrolls and calculates the position using the page size and row height, so it can fetch the relevant set of records for that position. To answer your question shortly, the OnRead will fire once when you scroll and the request will contain a Skip value corresponding to the scroll position. I hope this helps you move forward with the implementation.
