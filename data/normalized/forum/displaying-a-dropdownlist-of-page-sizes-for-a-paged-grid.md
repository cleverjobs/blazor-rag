# Displaying a DropDownList of Page Sizes for a Paged Grid

## Question

**Ran** asked on 27 Oct 2021

I see that there is a way to set and show a list of PageSizes in a dropdown list on the Pager control. Is there a way to do that for a paged Grid control?

### Response

**Randy** commented on 27 Oct 2021

Nevermind, I found it <GridSettings> <GridPagerSettings PageSizes="@PageSizes" /> </GridSettings>
