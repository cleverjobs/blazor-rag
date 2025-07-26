# Reduce the Row height by reducing the free space at the top and bottom of the row, without changing the font size?

## Question

**Yur** asked on 17 Nov 2021

I use Grid together with Grid ToolBar with default settings. But my users complain that the row height is noticeably higher than the height of the Grid ToolBar. Excessive line height reduces the amount of useful information on the page and this is bad. There is a lot of extra free space in the Grid row at the top and bottom. Changing the rowhight parameter does not give the desired result. Is there an easy way to reduce the Row height by removing excess free space at the top and bottom of the row, without changing the font size?

### Response

**NiV-L-A** commented on 18 Jul 2023

I only add that the link " how to easily calculate it." gives access denied. Thank you.

### Response

**Dimo** commented on 19 Jul 2023

The link currently works on my side in two different browsers. In any case, you can search for "css specificity wars" in Google Images and you will see the information in lots of other places.

## Answer

**Dimo** answered on 17 Nov 2021

Hi Yuri, The Grid data cells have paddings and line-height that you can override to reduce their height. At some point, the cell height may depend on command buttons, because they are higher than plain text. Command buttons have vertical margins, paddings and line-height that affect the cell height. The easiest and fastest way to tweak a component appearance is: Inspect the HTML output and applied CSS styles with the browser's DOM inspector. Find out all elements and styles that affect the appearance you want to change. Sometimes an element may apply default browser styles. Know about CSS Specificity and how to easily calculate it. Apply your custom CSS styles with higher specificity. The following example is extreme, because it reduces the cell and button height to a minimum. The only thing it doesn't touch is font-size. However, it demonstrates the idea. Another important thing to keep in mind is how CSS Isolation (scoped styles) works with Blazor components, if you are using this feature. div.k-grid td,.k-grid td.k-command-cell { padding-top: 0; padding-bottom: 0; line-height: 1;
}.k-grid td.k-command-cell.k-button { margin: 0; padding-top: 0; padding-bottom: 0; line-height: 1; height: auto; /* for icon buttons */ } Finally, you can set a custom Class for the Grid and use it instead of ".k-grid", if you want to target specific Grid instances. Regards, Dimo Progress Telerik

### Response

**Yuri** commented on 17 Nov 2021

Thanks, but it looks like it only works in the direction of increase I tried out three options on the standard example Grid Option 1 Default Option 2 Decrease – no visible changes <style> .k-grid td { padding: 1px 1px; } </style> Option 3 Magnification - changes are noticeable <style> .k-grid td { padding: 50px 50px; } </style>

### Response

**Dimo** commented on 17 Nov 2021

In this case the table cells are expanded by the buttons. You need to reduce their size as well. Buttons have margins, paddings, line-height and font-size. You can inspect the HTML output and styles in the browser's DOM inspector, and decide what to override to match your preferences.

### Response

**Yuri** commented on 17 Nov 2021

Thank you, but can you tell me the easiest way to change the margins at the top and bottom for the standard "Edit" "Delete" buttons for this example

### Response

**Dimo** commented on 18 Nov 2021

Check my edited answer above.

### Response

**Yuri** commented on 18 Nov 2021

Thank you very much. This is almost what I need, but there is one strange effect I have set the style <style> div.k-grid td, .k-grid td.k-command-cell { padding-top: 1px; padding-bottom: 1px; line-height: 1px; } .k-grid td.k-command-cell .k-button { margin: 1px; padding-top: 1px; padding-bottom: 1px; line-height: 1px; } I got a result that suits me (16 lines per page) But if I remove the text "Edit" on the edit button, the changes I need will disappear (I will get only 11 lines on the page)

What additional changes do I need to make?

### Response

**Dimo** commented on 22 Nov 2021

This is because icon buttons (with no text) have an explicit height style to match regular text buttons. Have you tried using the browser's DOM inspector to find this out? Let me know if our built-in styling is difficult to inspect, or if our blog post is difficult to follow. A height: auto; style in the button rule above will override the theme style immediately.

### Response

**Yuri** commented on 22 Nov 2021

In my case, it was enough for me to add font-size to the style you proposed .k-grid td.k-command-cell .k-button { margin: 1px; padding-top: 1px; padding-bottom: 1px; line-height: 1px; font-size: 10px; } Thanks for the helpful clarifications
