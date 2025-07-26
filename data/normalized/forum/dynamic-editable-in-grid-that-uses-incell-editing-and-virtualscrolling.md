# dynamic editable in grid that uses InCell editing and VirtualScrolling

## Question

**Mir** asked on 16 Sep 2020

Hi, I am currently trying to use a dynamic editable in my grid but it doesn't work although I followed the directions in this post: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create](https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create) <GridColumn Field="@(nameof(Menge))" Title="Menge" Width="100px" Editable="@(Current?.PositionsTyp !=PositionsTyp.Hierarchiestufe)"> <EditorTemplate> @{ Current=context as Item; <div>@Current.Menge</div> } </EditorTemplate> </GridColumn> Should it work for InCell editing and virtual scrolling mode too? Thanks in advance!

## Answer

**Marin Bratanov** answered on 16 Sep 2020

Hello Miriam, You can try adding the conditional logic in the EditorTemplate itself - in this case you won't have to use the Editable parameter of the column - the template itself can decide whether to keep showing the "read" value, or to offer an actual editor. This is the first approach from the article and the one I'd recommend. The second is more suitable for InLine and PopUp editing as they render a lot of things (the entire row and an entire popup) while the InCell editing only updates the current cell. Regards, Marin Bratanov

### Response

**Miriam** answered on 17 Sep 2020

Ok, I actually tried to implement the GridColumn conditionally in the EditorTemplate but I always get an Exception: InvalidOperationException: Object of type 'Telerik.Blazor.Components.GridColumn' does not have a property matching the name 'Value'. So, it doesn't work. And the other option: Editable="@( CurrentlyEditedEmployee?.ID> 0 )" doesn't work either because CurrentlyEditedEmployee is always null.

### Response

**Miriam** answered on 17 Sep 2020

<GridColumn Field="Menge" Title="Menge" Width="100px"> <EditorTemplate> @{ Current=context as Item; if (Current?.Typ !=Typ.H) { <GridColumn Field="Menge" Editable="true"> <div>@Current.Menge</div> </GridColumn> } } </EditorTemplate> </GridColumn> System.InvalidOperationException: Object of type 'Telerik.Blazor.Components.GridColumn' does not have a property matching the name 'ChildContent'. How do I have to use the EditorTemplate?

### Response

**Marin Bratanov** answered on 17 Sep 2020

Hi Miriam, You can review the documentation of the editor template to see how to use it: [https://docs.telerik.com/blazor-ui/components/grid/templates/editor.](https://docs.telerik.com/blazor-ui/components/grid/templates/editor.) You place markup and editor components there, not another grid column. You can find an example of conditional markup in the first snippet of this KB: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create.) As for the error - it is described here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-no-childcontent.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-no-childcontent.) Regards, Marin Bratanov

### Response

**Miriam** answered on 21 Sep 2020

The solution looks like this: 01. <GridColumn Field="Menge" Title="Menge" Width="100px"> 02. <EditorTemplate> 03. @{ 04. Current=context as Item; 05. if (Current?.PositionsTyp !=PositionsTyp.Hierarchiestufe) 06. { 07. <TelerikNumericTextBox T="decimal?" @bind-Value="@Current.Menge" OnChange="@ChangeMengenHandler" Decimals="3"> 09. </TelerikNumericTextBox> 10. } 11. } 12. </EditorTemplate> 13. </GridColumn>

### Response

**Miriam** answered on 21 Sep 2020

And this: 01. public async Task ChangeMengenHandler( object theUserInput) 02. { 03. var gridCommandEventArgs=new GridCommandEventArgs 04. { 05. Item=CurrentLV 06. }; 07. 08. await UpdateHandler(gridCommandEventArgs); 09. } 10. 11. public async Task UpdateHandler(GridCommandEventArgs args) 12. { 13. var viewModel=args.Item as Item; 14. 15. /* some operations + saving */ 19. 21. 22. var index=GridItems.FindIndex(item=> item.LId==viewModel.LId); 23. 24. GridItems[index].Menge=Convert.ToDecimal(viewModel.Menge?.AsNumberFormatted()); 28. 29. StateHasChanged(); 30. }
