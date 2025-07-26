# How to set the color picker width to fit-content of cell template.

## Question

**Bee** asked on 21 Mar 2022

Attached is the screen shot which shows both Color palette and Color picker in the cell template of the grid. How can I set the Color picker width similar to the Color palette. I have tried setting the class of the Color picker to be width 100 % or fit-content or stretch. But none of them seem to be working. Attached image file marks the color picker in red and color palette in blue. The color picker should have width similiar to the palatte. Below is the code and css style. <GridColumn Field="Color" Title="Color" Width="100px" TextAlign="ColumnTextAlign.Center" FieldType="@(typeof(string))"> <Template> @{
@colorUpdate.ColorCode; <TelerikColorPicker @bind-Value="colorUpdate.ColorCode" ValueFormat="ColorFormat.Hex" Class="k-colorpicker"> <ColorPickerViews> <ColorPickerGradientView ShowOpacityEditor="false" Format="ColorFormat.Hex"> </ColorPickerGradientView> </ColorPickerViews> </TelerikColorPicker> <TelerikColorPalette Colors="@ColorList" TileHeight="25px" TileWidth="25px"> </TelerikColorPalette> } </Template> </GridColumn> .k-colorpicker { width: stretch; /*tried using 100% or fit-content */ }.k-colorpicker.k-selected-color { width: stretch; /*tried using 100% or fit-content */ } span.k-colorpicker { width: stretch; /*tried using 100% or fit-content */ } Thank you for your help. Beena.

## Answer

**Dimo** answered on 24 Mar 2022

Hi Beena, width:100% is enough and should work: <div style="width: 200px; border: 1px solid red;"> <TelerikColorPicker @bind-Value="@Value" Class="expand-color" /> </div> <style>.k-colorpicker.expand-color { width: 100%;
} </style> @code {
string Value { get; set; }="#282f89";
} Regards, Dimo
