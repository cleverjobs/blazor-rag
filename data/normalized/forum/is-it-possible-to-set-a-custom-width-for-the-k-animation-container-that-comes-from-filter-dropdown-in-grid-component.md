# Is it possible to set a custom width for the k-animation-container that comes from filter dropdown in grid component?

## Question

**Grz** asked on 29 Mar 2022

Hello, I'd like to apply custom width on the dropdown element for the filter row in grid component. The last column in our project is wide enough for the cell content but not wide enough for the filter row dropdown. I was wondering if it'd be possible to target a `.k-animation-container` element that is connected to the dropdown. Here's a demo that shows the issue. Result I'd like to get: Kind regards, Greg

## Answer

**Dimo** answered on 01 Apr 2022

Hi Greg, The easiest way to expand the dropdown is to use this CSS rule: .k-animation-container { min-width: 200px;
} However, it will affect ALL Telerik popups on the page or in the app, depending on where you put it. This may cause undesired side effects. A better and more reliable solution will be one of the following: Use wider columns, possibly with horizontal scrolling. Use a filter row template (FilterCellTemplate), which will allow you to configure the Width in the DropDownList's PopupSettings Use a FilterMenu instead of a FilterRow. Regards, Dimo

### Response

**Grzegorz** commented on 01 Apr 2022

Hi Dimo, Thanks! That's what I thought. The root cause of the issue are too small columns in my example. I will use wider columns.
