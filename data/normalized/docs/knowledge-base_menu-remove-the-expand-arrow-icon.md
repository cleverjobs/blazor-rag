
## Environment
<table>
<tbody>
<tr>
<td>Product</td>
<td>Menu for Blazor</td>
</tr>
</tbody>
</table>

## Description

When there is more than one item under a menu item an arrow icon is displayed to indicate additional items are below it. Sometimes it may be desirable to remove the icon from the top-level menu item.

## Solution

Use the following CSS to set the display to none.

```` CSS
.k-menu-expand-arrow {
	display: none;
}
````
