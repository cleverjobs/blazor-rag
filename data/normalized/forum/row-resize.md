# Row resize?

## Question

**Dou** asked on 21 Sep 2020

Is there a way to allow the user to resize row height? I have a column that could contain a lot of data and I'd like to set the initial row height but allow the user to expand it (in addition to expanding the column width) if they need to see all the text.

## Answer

**Marin Bratanov** answered on 22 Sep 2020

Hello Doug, You can set the RowHeight to the desired pixel value (note that browsers will ignore values lower than what they would have rendered based on the content). Alternatively, you can use a template and put a <div> element in the cell that will render the desired height and contents. Regards, Marin Bratanov

### Response

**Doug** answered on 22 Sep 2020

Right, but does that mean it's not possible to have a user-resizable row height, i.e. the user can drag the height of the row bigger or smaller?

### Response

**Marin Bratanov** answered on 22 Sep 2020

Hello Doug, Yes, a user-draggable row edge is not possible. Each row cannot store its own height for the grid - they are all supposed to be the same (barring any rendering difference the browser does based on the content). Thus, a feature in the grid would be ambiguous - would it try to resize only the current row and if so - how should it read and store it? Or, would it try to resize all rows - in such a case the user experience will be quite strange with everything in the grid zooming in and out. Have you seen a grid somewhere in the web do that? Spreadsheet components tend to have such functionality, but they are rather different from a grid in many ways. Regards, Marin Bratanov

### Response

**Doug** answered on 22 Sep 2020

Looks like a spreadsheet component would work for me but since there's not currently one available for Blazor I'll figure out another way. Thanks for your response.

### Response

**Marin Bratanov** answered on 22 Sep 2020

You can Follow its implementation here: [https://feedback.telerik.com/blazor/1442151-spreadsheet-component.](https://feedback.telerik.com/blazor/1442151-spreadsheet-component.) I've added your Vote to raise its priority. For the time being, you can consider encapsulating the Kendo for jQuery widget as explained there. Regards, Marin Bratanov
