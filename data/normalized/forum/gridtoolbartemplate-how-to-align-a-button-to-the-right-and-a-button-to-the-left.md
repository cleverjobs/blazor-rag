# GridToolBarTemplate how to align a button to the right and a button to the left

## Question

**LeeLee** asked on 06 Aug 2024

I have the following code for my GridToolBarTemplate. We want the ExportToExcel formated to the far right while the Resub, Cancel and Cleare stay to the left. How is this done? <GridToolBarTemplate> <GridCommandButton Command="Resubmit" Enabled="@IsResubmitEnabled" Icon="@SvgIcon.Redo" OnClick="TransactionsGrid_ResubmitButton_ClickAsync"> RESUBMIT </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" OnClick="TransactionsGrid_CancelButton_Click"> CANCEL </GridCommandButton> <GridCommandButton Command="Clear" Icon="@SvgIcon.ArrowRotateCcw" OnClick="TransactionsGrid_ClearButton_Click"> CLEAR </GridCommandButton> <GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileExcel"> Export to Excel </GridCommandButton> </GridToolBarTemplate>

## Answer

**Lee** answered on 06 Aug 2024

<div style="margin-left:auto"> <GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileExcel">Export to Excel</GridCommandButton> <label class="k-checkbox-label"><TelerikCheckBox @bind-Value="@ExportAllPages" />Export All Pages</label> </div>

### Response

**Hristian Stefanov** commented on 07 Aug 2024

Hi Lee, It seems that you have resolved the matter on your own. I'm glad to hear this. Sharing an update here is appreciated, as other developers with the same scenario can benefit from it. Kind Regards, Hristian
