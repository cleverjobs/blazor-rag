# Preserve line feeds in grid cell

## Question

**Dou** asked on 17 Mar 2023

I'm displaying text in a grid cell that contains line feeds and like normal those line feeds get removed when rendered. The conventional wisdom to preserve line feeds is to apply CSS, something like "white-space: pre-wrap". However when I do that in a Telerik grid cell via .k-grid td, .k-grid .k-table-td { white-space: pre-wrap; } The rendered td element gets unnecessarily tall, wasting space. I saw this post: [https://www.telerik.com/forums/multi-line-text-in-grid-cell](https://www.telerik.com/forums/multi-line-text-in-grid-cell) And with that I was able to get the end result to look okay using this: <Template> @(new MarkupString((context as LocationDto).RMRAddress?.DisplayText.Replace(Environment.NewLine, "<br/>"))) </Template> But I really don't like having to use a markup string like that. Is there a way to apply CSS to the grid cell to preserve the line feeds without creating the unnecessary height? See the attached screenshot. Yellow highlight shows the wasted space I'm referring to. Thanks.

## Answer

**Yanislav** answered on 21 Mar 2023

Hello Doug, I've applied the "white-space" CSS rule you shared in a sample application. When I inspect the Grid cell, it seems that the content height is too big. Most likely an empty line is inserted by the "white-space" CSS property. I was able to find a way to remove the empty line. Here are the steps you can take to implement the workaround: Declare a column template. Wrap the text in a <p> tag and apply the pre-wrap rule to the paragraph instead of overriding the default cell styles. I've prepared a REPL example to demonstrate the approach. I hope you find it useful. Please let me know if you have any questions or if you need further assistance. Regards, Yanislav Progress Telerik

### Response

**Doug** commented on 21 Mar 2023

Thanks Yanislav, Maybe this issue isn't specific to Telerik but I appreciate your response. Use of a <p> tag helps but it still appears to make the content height taller than it needs to be. <GridColumn Field="RMRAddress.DisplayText" Title="RMR Address <p>"> <Template> <p style="white-space:pre-wrap">@((context as LocationDto).RMRAddress?.DisplayText)</p> </Template> </GridColumn> As opposed to using a markup string from my original post: Using a markup string isn't the end of the world so I'll move forward with that but thanks for your response.

### Response

**Yanislav** commented on 24 Mar 2023

Hello Doug, Using a markup string is a valid solution, and I'm glad that you're able to move forward with it. Please don't hesitate to reach out if you have any further questions or concerns. Have a great day!
