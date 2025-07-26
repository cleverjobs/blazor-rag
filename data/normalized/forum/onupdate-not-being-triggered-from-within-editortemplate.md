# OnUpdate Not Being Triggered from within EditorTemplate

## Question

**Dou** asked on 16 Aug 2020

I can successfully trigger the OnUpdate event from a simple GridColumn Field update with Incell editing but not when using an EditorTemplate. Any ideas what I'm doing wrong or missing? <TelerikGrid Data=@ItemsOC EditMode="@GridEditMode.Incell" OnUpdate="@UpdateHandler"> <GridColumns> <!-- This column DOES NOT trigger OnUpdate when edited. --> <GridColumn Field="Quantity" Title="EDIT Quantity"> <EditorTemplate> @{ ItemToEdit=context as Item; <TelerikNumericTextBox @bind-Value="@ItemToEdit.Quantity" Format="F2" /> } </EditorTemplate> </GridColumn> <!-- This column DOES trigger OnUpdate when edited. --> <GridColumn Field="Quantity" /> <GridColumn Field="Description" /> <GridColumn Field="Cost" /> <GridColumn Field="SubTotal" /> </GridColumns> </TelerikGrid> Doug

## Answer

**Marin Bratanov** answered on 16 Aug 2020

Hi Doug, When using the editor template, the grid can't know what's happening in there, so the app (the template) must take care to close the cell for editing and to update the data. You can read more about this and find examples in the Notes section of the InCell editing article: [https://docs.telerik.com/blazor-ui/components/grid/editing/incell#notes](https://docs.telerik.com/blazor-ui/components/grid/editing/incell#notes) Regards, Marin Bratanov

### Response

**Doug** answered on 16 Aug 2020

Thanks Marin. That got me on track! Doug
