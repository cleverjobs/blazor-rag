# TelerikGrid Cutting Off Input With EditorTemplate

## Question

**Cur** asked on 31 Jan 2024

We modified the code in the InCell Editing demo ( Blazor Components Demos and Examples - Telerik UI for Blazor ) with the Telerik REPL tool to include an EditorTemplate for the UnitPrice column. If we type in the column quickly and press tab to exit the field the input is cutoff. ie; we type 155 and the value shown in the grid after the update is 15. We have recorded a video showing the problem but we are unable to upload here. In our own sample application that we built to isolate the problem we saw the same behavior with TelerikTextBoxes and TelerikNumericTextBoxes. Is this a known problem with a known solution? The code used for the EditorTemplate <GridColumn Field=@nameof( ProductDto. UnitPrice ) DisplayFormat="{0:C}" Title="Unit Price" Width="150px"> <EditorTemplate> @{ var item=context as ProductDto; if (item !=null ) { <TelerikNumericTextBox @bind-Value="@item.UnitPrice" /> } } </EditorTemplate> </GridColumn>

## Answer

**Hristian Stefanov** answered on 05 Feb 2024

Hi Curtis, Thank you for explaining in such detail what you are experiencing. The behavior you've described seems attributed to the " DebounceDelay " parameter. Inputs like the "TelerikNumericTextBox" have a default debounce delay of " 150ms ". In some cases, that default value may cause undesired delays. To address this, I recommend setting the " DebounceDelay " parameter to " 0 ": <GridColumn Field=@nameof(ProductDto.UnitPrice) DisplayFormat="{0:C}" Title="Unit Price" Width="150px"> <EditorTemplate> @{
var item=context as ProductDto;
if (item !=null)
{ <TelerikNumericTextBox DebounceDelay="0" @bind-Value="@item.UnitPrice" /> }
} </EditorTemplate> </GridColumn> I have adjusted the demo to illustrate the impact of the debounce delay in this REPL link. As a result, it seems that no characters are removed during typing. Could you run and test the REPL to see whether the result you get is the same? Regards, Hristian Stefanov Progress Telerik
