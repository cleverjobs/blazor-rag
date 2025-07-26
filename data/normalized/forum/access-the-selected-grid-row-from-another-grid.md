# Access the selected grid row from another grid

## Question

**Dou** asked on 09 May 2023

I have a grid that displays financial information nicely. However, I need a second grid to access the selected row from the first grid so that it can display further details. First (fully functioning) grid in brief: <TelerikGrid Data="@vm.Model.CO_DetailsList" @ref="grid" EditMode="@Telerik.Blazor.GridEditMode.Incell"> <GridColumns> <GridColumn Field="@nameof(CO_Details.Seg0)" Title="Fund" Width="70px"> <EditorTemplate> <TelerikComboBox Data="@vmSeg0.Model" TextField="Value" ValueField="Value" TItem="GL_Seg0RO" TValue="string" @bind-Value="vm.Model.CO_DetailsList[index].Seg0"> <ComboBoxSettings> <ComboBoxPopupSettings MaxHeight="@seg0CmbHeight" /> </ComboBoxSettings> </TelerikComboBox> </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid>

## Answer

**Dimo** answered on 10 May 2023

Hi Doug, Set the SelectedItems parameter of the first Grid, and if needed, use the SelectedItemsChanged handler. Grid Selection documentation (also see the other two articles in the feature section). Regards, Dimo Progress Telerik
