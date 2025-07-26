# Clear AutoFitAllColumnsAsync settings, allow to mantain widths settled on the columns

## Question

**Cla** asked on 19 Jul 2022

I have a Grid, for each column i set the width setting the property Width="@DescriptionWidth" When the grid is not in filter mode (FilterMode=GridFilterMode.None) i call AutoFitColumnsWidthAsync to autofit the columns. When it is in filter mode i would like to have a bigger column size to allow the filter render correctly, so i set the DescriptionWidth property who is binded to the Width of the column, but it not work if previously was called AutoFitColumnsWidthAsync. There is a way to clear the settings done by AutoFitColumnsWidthAsync and allow to keep the binded property width? Here a sample code: [https://blazorrepl.telerik.com/wmYrFDYh20r6bnFB33](https://blazorrepl.telerik.com/wmYrFDYh20r6bnFB33) Thanks

## Answer

**Dimo** answered on 21 Jul 2022

Hi Claudio, You will need to recreate the Grid in this scenario. After you execute AutoFitColumnsWidthAsync (), the columns no longer allow width changes via the Grid declaration. Regards, Dimo
