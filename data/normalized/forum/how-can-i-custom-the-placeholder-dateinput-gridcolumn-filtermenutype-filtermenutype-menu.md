# How can I custom the placeholder (DateInput) "GridColumn FilterMenuType="@FilterMenuType.Menu""

## Question

**Jur** asked on 09 Jul 2024

Hi everyone! I hace this Rowfilter This is the Telerik Code <GridColumn FilterMenuType="@FilterMenuType.Menu" Field="@nameof(HechoDirectoClienteViewModel.FechaVencimiento)" Title="Fecha vencimiento" TextAlign="ColumnTextAlign.Right" Resizable="true" Sortable="true" Width="170px" HeaderClass="center-wrap"> <Template> @((context as HechoDirectoClienteViewModel)?.FechaVencimiento?.ToString("dd/MM/yyyy")) </Template> </GridColumn> It is possible changue the DateFormat "y/M/yyyy" to this "dd/MM/yyyy?

## Answer

**Tsvetomir** answered on 12 Jul 2024

Hello Jurgen, Thank you for the clear explanation of the result you want to achieve. Indeed, it is possible to customize the date format in the filter menu. To achieve that, use the FilterEditorFormat parameter and set it to the desired format. To see the approach first-hand, refer to Customize The Filter Editors section in our documentation. Regards, Tsvetomir Progress Telerik
