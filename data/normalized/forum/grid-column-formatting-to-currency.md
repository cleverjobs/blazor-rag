# Grid Column Formatting to Currency?

## Question

**Dea** asked on 23 Jun 2023

Weird one. I have a main grid and then a detail grid I display after user clicks on a cell value in Main grid. I have currency column sin both, Decimals. In the detail grid the Displayformat works and shows the currency formatting. in class: [DisplayFormat(DataFormatString="{0:C}")] public Decimal? M1_Amt { get; set; } Only difference between both grids is the main has GridColumn tags and the detail doesn't. Also tried the following in the main grids columntag: <GridColumn Field="@nameof(gdMappedUnMappedCostsOVHDR.M1_Amt)" Title="@M1_Title" DisplayFormat="{0:C}"> That displayformat does nothing! I am not sure why I cant get this to work? Anyone with some ideas?

## Answer

**Svetoslav Dimitrov** answered on 28 Jun 2023

Hello Deasun, Can you modify the code snippet from the Display Format documentation article so that the issue you are facing is reproducible? The snippet works with both the [DisplayAttribute] attribute and the DisplayFormat parameter on the Grid column. On my end, both seem to work as expected. Your cooperation is highly appreciated. Regards, Svetoslav Dimitrov
