# How to prevent adding and removing columns in the spreadsheet component

## Question

**Dou** asked on 27 Jun 2025

I need to lock down the spreadsheet and prevent the user from adding or removing columns. I'd like to hide the highlighted items in the context menu below. How can I accomplish this?

## Answer

**Ivan Danchev** answered on 29 Jun 2025

Hello Doug, The Spreadsheet does not have a parameter dedicated to disabling/enabling the context menu options you listed, but you can hide them with CSS: <style>.k-menu-item:has (.k-menu-link.k-svg-i-table-column-insert-left ),.k-menu-item:has (.k-menu-link.k-svg-i-table-column-insert-right ),.k-menu-item:has (.k-menu-link.k-svg-i-table-column-delete )
{ display: none;
}
</style> Here's an example that shows the effect of the CSS rule posted above: [https://blazorrepl.telerik.com/wzaqQZwc20hdvW6f24](https://blazorrepl.telerik.com/wzaqQZwc20hdvW6f24) Regards, Ivan Danchev Progress Telerik

### Response

**Doug** commented on 30 Jun 2025

Perfect, thank you!
