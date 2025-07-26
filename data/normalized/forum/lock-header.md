# Lock header

## Question

**Ila** asked on 03 Jun 2021

Is there a way to lock (freeze) the header row?

## Answer

**Eric R | Senior Technical Support Engineer** answered on 07 Jun 2021

Hi Ilan, Thank you for your using the UI for Blazor forums. However, there isn't enough information to fully understand the question. Let me explain more below. Explanation Generally, the header row is not required to lock for vertical scrolling within the grid as shown in the Grid - Freeze Columns demo. This is because only the content of the grid is vertically scrollable. For more details on column locking, see the Grid Frozen Columns article. Additionally, there is a feature named "row pinning" which is not available in Blazor. To see this in action, refer to the React Grid - Locked Rows demo. This enables locking a certain row within view. Although, I am not certain this is what you're looking for. Potential Workaround If the built-in header row locking isn't suitable for your scenario, i.e. for page scrolling and not just scrolling within the grid, it may be possible to make the header row frozen during page scroll by applying CSS to the HTML header element. See the following code snippet for how to do this. Note that the exact configuration depends on the scenario and the position of the other elements on the page and will require some adjustments. <style>.k-grid-header-wrap { position: sticky; top: 500px; left: 400px;
} </style> Wrapping Up If the above information and potential workaround doesn't meet your needs, I will need to understand the scenario better. In this case, I ask that you provide more information on the requirement and the Grid markup and code-behind for review. In the meantime, please let me know if you need any additional information. Thank you. Regards, Eric R | Senior Technical Support Engineer

### Response

**Sam** commented on 08 Sep 2023

I think the requestor was very clear in their request -- Is there a way to freeze (make sticky) the header row in a BlazorTelerik Grid? Your solution for React is irrelevant and the "potential workaround" doesn't work. So, I will ask the original question again: Is there a way to freeze (make sticky) the header row in a BlazorTelerik Grid?

### Response

**Dimo** commented on 12 Sep 2023

@Sam - Normally, CSS provides the position:sticky style for such scenarios and this is what Eric is talking about in the "Workaround" section above. However, this style has multiple requirements to work, and the Grid cannot comply with all of them out-of-the-box due to its HTML markup and CSS styling. It is possible to override the Grid styling and stick the header during page scrolling. However, side effects may occur and we don't support this officially.

### Response

**Sam** commented on 12 Sep 2023

Thanks. I was able to get this solution working using the css position:sticky. I should have updated my request.
