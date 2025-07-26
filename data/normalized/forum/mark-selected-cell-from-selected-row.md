# Mark selected cell from selected row

## Question

**Cip** asked on 07 Jan 2021

Hi everyone, Is it possible somehow on a selected row to mark the selected cell when the user clicks on it? Best regards, Cipri

## Answer

**Marin Bratanov** answered on 07 Jan 2021

Hello Cipri, You can follow the cell selection feature here: [https://feedback.telerik.com/blazor/1451980-multiple-cell-selection-not-full-row](https://feedback.telerik.com/blazor/1451980-multiple-cell-selection-not-full-row) You can also follow the ability to focus a particular cell in the grid here: [https://feedback.telerik.com/blazor/1495333-method-to-focus-a-cell](https://feedback.telerik.com/blazor/1495333-method-to-focus-a-cell) Regards, Marin Bratanov

### Response

**Ciprian Daniel** answered on 07 Jan 2021

Hi Marin, The possibility to select a cell was implemented for the ASP.NET MVC UI [https://demos.telerik.com/aspnet-mvc/grid/selection](https://demos.telerik.com/aspnet-mvc/grid/selection) and also for Kendo UI using jQuery [https://demos.telerik.com/kendo-ui/grid/selection](https://demos.telerik.com/kendo-ui/grid/selection) I wasn't sure if what I wanted on my first question was clear for you that's why I gave you those examples. On the other hand selecting a cell is not exactly what we want but selecting a row and on that row selecting a cell so in this situation in our case selecting a row and selecting a cell should coexist. I don't know if that is or would be possible. Best regards, Cipri

### Response

**Marin Bratanov** answered on 07 Jan 2021

Hi Cipri, The feature request for cell selection is exactly the same feature you linked. Row selection and cell selection are alternatives, they could not work together because they would result in ambiguity - the same action (click on a row) will do different things - should it select the row, or should it select the cell? If you want them together, use the row selection and add cell templates that perform the logic you need. If you want to point a user to a specific cell in a row (whether it is selected or not), a method to focus it would let you do that - and that's the second feature request I linked. Regards, Marin Bratanov
