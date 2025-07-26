# MultiSelect doesn't render properly with large lists

## Question

**Cha** asked on 02 Feb 2022

Hello, I have a rather long list of items (> 400) that users will multiselect from. I was hoping the TelerikMultiSelect control would work for this, as it's the only Blazor control I've found so far that comes close to providing the required functionality. However, it doesn't seem to be rendering properly, and it doesn't provide a way to scroll beyond one page worth of data. First of all, it only draws the "drop down" for 8 items, even though the list renders far beyond the drop down, causing a poor visual rendition of the list. This is just a snippet, as the list goes down beyond the bottom of the browser page: The component should know how long to render the "drop down" based on the number of items in the list? I tried setting a MinHeight, which increased the length of the list, but that only changed where the visual cutoff occurs, as it still cuts off. Secondly, there's no way to scroll beyond one page worth. When the control scrolls off the page in the browser, the list collapses, making it impossible to scroll even to the 'Bs'. I think I can make this work by making use of filters and setting the MinHeight so that it extends beyond the controls below it, however this doesn't seem like the right way to do it. I'm open to other ideas. Thanks!

## Answer

**Marin Bratanov** answered on 02 Feb 2022

Hello Charles, It looks like the Telerik stylesheet is missing or does not load for some reason - thus the styling of the component is off, and you see such an issue. Double check that you have the stylesheet included as described here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets.](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#client-assets.) Regards, Marin Bratanov

### Response

**Charles** commented on 02 Feb 2022

Thanks. You're correct, the stylesheet wasn't referenced. Now a bunch of other visual things changed that I have to fix too!

### Response

**Charles** commented on 02 Feb 2022

Specifically, all of my TelerikDateTimePickers changed to Width=100%. The documentation says the default is 280px? The browser dev tools indicate this is coming from the all.css for kendo-theme-default: I'm using Telerik.UI.for.Blazor 3.0.1 from NuGet. Is this my doing? I can override it, but this doesn't seem right.

### Response

**Radko** commented on 07 Feb 2022

Hello Charles, Indeed, starting with Telerik.UI.for.Blazor 3.0.0, inputs and pickers have their width set to 100%, and overriding it through the Width parameter is the way to set the desired width that fits your needs. As for our documentation mentioning 280px as an exact preset width - apologies for the caused confusion, we will edit this. Thank you for noticing! Regards, Radko Stanev
