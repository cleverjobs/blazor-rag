# How to create ...(Three Dots) in GridColumn

## Question

**Pet** asked on 06 Sep 2024

Hello Telerik, <TelerikGrid @ref="@GridRef" Data="@Generators" Pageable="true" Sortable="true" FilterMode="GridFilterMode.FilterMenu" Resizable="true" Reorderable="true"> @* **************************************** Tool Bar **************************************** *@<GridToolBarTemplate> @* ******** Excel Button *@<GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileExcel"> Export to Excel </GridCommandButton> @* ******** AutoFill Button *@<TelerikButton OnClick="AutoFitAllColumns"> AutoFit All Columns </TelerikButton> @* ******** Clear All filters Button *@<TelerikButton ThemeColor="primary" OnClick="@ClearGridFilter"> Clear Filters </TelerikButton> </GridToolBarTemplate> <GridExport> <GridExcelExport FileName="@strExcelFileName" AllPages="@blnExportAllPages" OnBeforeExport="@(()=> { strExcelFileName=CreateExcelFileName(); } )" /> </GridExport> @* **************************************** Columns **************************************** *@<GridColumns> @* Gen Number is a HyperLink to the Generator Details Page *@<GridColumn Field="@nameof(ModtblGenerator.GenName)" Title="Generator Name" /> <GridColumn Field="@nameof(ModtblGenerator.GenNum)" Title="Gen Number" /> <GridColumn Field="@nameof(ModtblGenerator.Street)" Title="Street" /> <GridColumn Field="@nameof(ModtblGenerator.City)" Title="City" /> <GridColumn Field="@nameof(ModtblGenerator.Province)" Title="Province" /> <GridColumn Field="@nameof(ModtblGenerator.Country)" Title="Country" /> <GridColumn Field="@nameof(ModtblGenerator.PostalCode)" Title="Postal Code" /> <GridColumn Field="@nameof(ModtblGenerator.WasteClasses)" Title="Waste Classes" Filterable="false" /> </GridColumns> </TelerikGrid>

## Answer

**Tsvetomir** answered on 06 Sep 2024

Hello Peter, Thank you for the provided screenshot and clear explanation of the result you are looking for. Typically, the described behavior depends on the ability of the cell text to wrap or not. To gather more information and see an approach that will help you to achieve the desired outcome, refer to our KB article: Prevent the Grid from wrapping text in multiple lines and show ellipsis. I hope the provided information in the article helps you to move forward. If you face any difficulties with it, let me know. Regards, Tsvetomir Progress Telerik

### Response

**Peter** commented on 06 Sep 2024

Tsvetomir, thank you! I appreciate it.

### Response

**Peter** commented on 06 Sep 2024

Tsvetomir, Is it possible to make the HeaderClass on RowRender as well? I didn't see anything like that in the KB. <GridColumn Field="@nameof(ModtblGenerator.GenName)" Title="Generator Name" HeaderClass="header" /> <GridColumn Field="@nameof(ModtblGenerator.GenNum)" Title="Gen Number" HeaderClass="header" /> <GridColumn Field="@nameof(ModtblGenerator.Street)" Title="Street" HeaderClass="header" /> <GridColumn Field="@nameof(ModtblGenerator.City)" Title="City" HeaderClass="header" /> <GridColumn Field="@nameof(ModtblGenerator.Province)" Title="Province" HeaderClass="header" /> <GridColumn Field="@nameof(ModtblGenerator.WasteClasses)" Title="Waste Classes" HeaderClass="header" Filterable="false"/>

### Response

**Tsvetomir** commented on 11 Sep 2024

Hello Peter, The HeaderClass parameter main purpose is to apply a custom CSS class to the header cell of the column. So, the idea for setting the class of the column header cell in the event that is focusing the rendering of the rows seems invalid. With that being said, can you provided more information by answering the following: What is the main purpose to set the HeaderClass in the OnRowRender event? What is the idea to set the class though some Grid event? Is there any issue to set it through the HeaderClass parameter of the GridColumns? This will help me to better understand your scenario and provide you a more specific information about your requirements. Regards, Tsvetomir
