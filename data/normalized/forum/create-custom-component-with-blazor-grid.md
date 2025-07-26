# Create custom component with Blazor Grid

## Question

**Ste** asked on 15 Dec 2023

How would I create a custom reusable component using Blazor Grid? I have the following that I'd like to create a component from: <TelerikGrid Data="@InitialLendersData" EditMode="@GridEditMode.Incell" SelectionMode="@GridSelectionMode.Multiple" @bind-SelectedItems="@SelectedInitialLenders" Height="250px" Width="640px" OnEdit="@EditInitialLendersHandler" OnUpdate="@UpdateInitialLendersHandler"> <GridColumns> <GridColumn Field="@nameof(Lender.IsSelected)" Title="" Width="50px" TextAlign="@ColumnTextAlign.Center" Editable="false"> <Template> @{ EditedLender=context as Lender; <TelerikCheckBox @bind-Value="@EditedLender.IsSelected" OnChange="@ChangeSelectedHandler" /> } </Template> </GridColumn> <GridColumn Field="@nameof(Lender.Name)" Editable="false" /> <GridColumn Field="@nameof(Lender.Amount)" Width="160px" DisplayFormat="{0:C2}" TextAlign="@ColumnTextAlign.Right"> <EditorTemplate> @{ var item=context as Lender; <TelerikNumericTextBox @bind-Value="@item.Amount" DebounceDelay="0" Min=0 Max=999999999999 Arrows="false" Format="C2" Decimals="2"></TelerikNumericTextBox> } </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid> How do I pass in the data (InitialLendersData & SelectedInitialLenders) and references to the events (EditInitialLendersHandler, UpdateInitialLendersHandler & ChangeSelectedHandler) from the custom component? Is this possible?

## Answer

**Dimo** answered on 20 Dec 2023

Hi Stephen, Yes, this is possible. The required approach requires typical Blazor programming and is the same, no matter if you want to wrap and reuse our Grid or any other Razor component. You need to pass parameters from the parent component to the reusable component. I recommend the following resources: Create custom components and bind parameters - decide if you prefer one-way or two-way binding for the parameters (i.e. if you need the changes from the child component to propagate to the parent Blazor component events And here is a REPL example to get you started: [https://blazorrepl.telerik.com/mRvmQalu56opdFuF09](https://blazorrepl.telerik.com/mRvmQalu56opdFuF09) You may even create the reusable component to be generic, so that the Grid inside can work with different model types. Regards, Dimo Progress Telerik
