# I need a Grid cell template that will make certain cells bold based on a boolean value.

## Question

**Adr** asked on 18 Jun 2021

I have the need to display certain grid values bold as to highlight them to the user. I have created a template like so: <GridColumn Field="@(nameof(ManufacturerSettingsInfo.Region1))" Width="80px" Filterable="false" Groupable="false"> <Template> @{
var row=context as ManufacturerSettingsInfo;
if (true)
{ <span style="font-weight:bold;"> @(Converter.ConvertToBlankOrFormattedDecimal(row.Region1)) </span> }
else
{ <span> @(Converter.ConvertToBlankOrFormattedDecimal(row.Region1)) </span> }
} </Template> </GridColumn> However the cells with the font-weight bold styling do not show up as bold and look the same as the other cells. N.B. I am able to change the font-size but I can't seem to change the font-weight. Do you know how I can achieve this? UPDATE: This is working as expected, it was an issue with my CSS not using the correct font-family for a bold font face.
