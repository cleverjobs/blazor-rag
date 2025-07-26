# Customize the Grid selection

## Question

**Sat** asked on 09 Feb 2022

Is there a way I can replace the checkbox with button for the selection of the row in the grid? Blazor DataGrid Demos - CheckBox Only Selection | Telerik UI for Blazor

## Answer

**Marin Bratanov** answered on 10 Feb 2022

Hi Satish, You can: remove the built-in selection column add a column of your own that has no Field set use its Template to add the desired button use the OnClick of the button with a lambda to pass the current row model and update the selected items collection yourself Regards, Marin Bratanov Progress Telerik

### Response

**Satish** commented on 16 Feb 2022

Thank you Marin. Can you tell me how to customize the grid header color?

### Response

**Marin Bratanov** commented on 17 Feb 2022

You can use the browser dev tools to inspect the rendered HTML and the CSS rules that apply to it ( this can be a good starting point) and then devise the CSS rules that will provide you with the desired coloring.

### Response

**Satish** commented on 17 Feb 2022

HI Marin, If I have the following in my Razor component, it works, but when moved to site.css file, it doesn't. <style>.k-grid-header { background:red;
} </style>

### Response

**Marin Bratanov** commented on 17 Feb 2022

This is likely due to the order and specificity of the selectors. Try making yours heavier.
