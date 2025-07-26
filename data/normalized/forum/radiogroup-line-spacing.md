# RadioGroup Line Spacing

## Question

**Chr** asked on 21 Feb 2023

How can I reduce the line spacing when a horizontal radiogroup wraps in a DIV?

## Answer

**Ivan Zhekov** answered on 22 Feb 2023

Hi, Christopher. The radio list uses flex box for laying out its items. As such, you simply need to customize the vertical spacing (or row spacing). .k-radio-list.k-list-horizontal {
row-gap: 4px;
} Putting everything together: [https://dojo.telerik.com/@joneff/AGiZOjOL](https://dojo.telerik.com/@joneff/AGiZOjOL) Regards, Ivan Zhekov
