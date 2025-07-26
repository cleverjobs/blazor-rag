# Grid: Auto-Hide vertical Scrollbar

## Question

**Hen** asked on 10 Feb 2023

I know how to hide the Scrollbar completely for the whole time but I just want to hide it if the current rows do not fit in the grid. That must be a common question but I have not found an answer yet....

### Response

**Hristian Stefanov** commented on 15 Feb 2023

Hi Hendrik, The easiest way to hide the scrollbar conditionally is to apply the CSS style wrapped in an if block that checks for the number of rows. Here is a sample of how the structure looks: @if (//Check the number of rows)
{
<style>
@*Custom CSS style for hiding the scrollbar*@</style>
} Still, I'm not sure I completely understand the goal here. Can you please share a bit more information about the scenario? What is the idea of hiding the scrollbar when the rows do not fit the Grid? How could we access these rows without being able to scroll to them without a scrollbar? I look forward to hearing from you.

### Response

**Hendrik** commented on 15 Feb 2023

Thank you Hristian. Of course I want to hide the Scrollbar only if the row fit in the height of the grid ! I said the opposite but that was a mistake. Now I am looking for the answer to check if the rows fit inside the grid and no scrollbar is needed. I guess I have to calculate number of rows * height of the row <heuight of the grid, but there could be uneven heights of the rows due to multilines... I thought that would be a pretty common problem that is already solved a lot of times...

### Response

**Yanislav** commented on 20 Feb 2023

Hello Hendrik, I assume that you've already reviewed the "How to Remove the Vertical Grid Scrollbar" KB article. It describes how you can remove the scrollbar. The suggested approach will remove the scrollbar when it is not needed as in the following example: [https://blazorrepl.telerik.com/wxkGGOYV42te5z9w20](https://blazorrepl.telerik.com/wxkGGOYV42te5z9w20) As you can see on the second page the scrollbar is not displayed. Using this approach you should not set a Grid height, as Grid cells might be misaligned with the header and footer cells. This behavior can be noticed in the shared example. To avoid this and set the height of the Grid, you have to get the height of the Grid content and the height of all rows. Thus you can compare them. If the height of the row is smaller - apply custom CSS that hides the scrollbar and removes the header and footer padding. To achieve this you have to execute a JS script each time the rows inside the viewport of the Grid are changed. Here is an example: [https://blazorrepl.telerik.com/QxOmmkOi36RxVMii15](https://blazorrepl.telerik.com/QxOmmkOi36RxVMii15) I hope this helps.
