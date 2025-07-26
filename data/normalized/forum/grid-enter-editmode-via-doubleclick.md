# Grid: Enter EditMode via DoubleClick

## Question

**Hen** asked on 12 Aug 2022

I am kind of new to Telerik and Blazor. I try to read all the documentation, but I still can not figure out how to solve this: I only want to enter the InCell-Edit-Mode when I am doubleclicking on the specific cell. Is that possible ?

## Answer

**Dimo** answered on 12 Aug 2022

It's possible to enter incell edit mode only on double-click. Note that the component has not been designed with this in mind, so the solution is not very elegant or flexible. For example, users will expect non-editable cells to trigger selection, but this is not possible, as we discussed in the other thread.

### Response

**Hendrik** commented on 12 Aug 2022

Thank you for the solution. It seems to be what I was looking for. But I do not get the point that is not possible as feature. I know a lot of grids from the !=Blazor-World (and the Blazor-Grid from Syncfusion) and that is always a standard. What if I want to use the Grid on a Touch-Display ? Do I always get the Enter-Mode when I try to scroll with my fingers hitting a cell ?

### Response

**Dimo** commented on 15 Aug 2022

On a touch device, we rely on two distinct gestures - tapping will enter edit mode, while swiping will scroll. I see some vendors use single click to edit, and some use double click. We have opted for a single click for all our Grid components from the past and present. Single click is more common in web environment and also, it will be consistent with single taps on touch devices.

### Response

**Dimo** answered on 16 Aug 2022

Hi again, Hendrik, We revisited this topic in our team and decided to open a public feature request about in-cell editing via double clicks on your behalf. There is still no specific time frame for implementation, but we acknowledge the validity of such scenario in contemporary context. Regards, Dimo

### Response

**Hendrik** commented on 17 Aug 2022

That sounds great !
