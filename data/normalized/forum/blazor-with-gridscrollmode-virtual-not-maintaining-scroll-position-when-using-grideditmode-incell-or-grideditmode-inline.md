# Blazor with GridScrollMode.Virtual not maintaining scroll position when using GridEditMode.Incell or GridEditMode.Inline

## Question

**Bra** asked on 14 Mar 2023

When a Blazor TelerikGrid component is configured to use virtual scrolling (GridScrollMode.Virtual) in combination with Inline or Incell editing, the scroll position will always jump to the top after exiting the cell edit. This snippet shows the issue: [https://blazorrepl.telerik.com/GHudPSlF1136joxn59](https://blazorrepl.telerik.com/GHudPSlF1136joxn59) To replicate, scroll down a bit, edit a cell and the grid scroll position will jump to the top.

## Answer

**Dimo** answered on 16 Mar 2023

Hello Bram, The scroll offset change occurs, because the Grid data is fully replaced in the OnUpdate handler. You can update the local data collection explicitly, so that you don't have to reload the whole data. There is also a related bug that you may want to keep an eye on. private async Task UpdateItem ( GridCommandEventArgs args ) { var updatedItem=args.Item as ProductDto; var originalItemIndex=GridData.FindIndex(x=> x.ProductId==updatedItem.ProductId);
GridData[originalItemIndex]=updatedItem; ProductService.UpdateProduct((ProductDto)args.Item); //await LoadData(); } Regards, Dimo

### Response

**Bram** commented on 16 Mar 2023

Ok, this solves my issue. It might be convenient (and more performant) to have the index available in the GridCommandEventArgs or maybe in the GridState.

### Response

**Dimo** commented on 16 Mar 2023

If you aim for performance, you can store the original edit item in the OnEdit handler and then simply modify it in OnUpdate. It's not straight-forward and efficient to provide a reliable index value for each item, as it will change after data operations (sorting, filtering, paging, grouping). We will have to do a lot more work in such cases.

### Response

**Bram** commented on 16 Mar 2023

I had an intermediate solution where I updated the edit item from the grid state. I'm not sure which solution I like best, depends on the use case I guess. var updatedItem=args.Item as ProductDto;
var currentGridState=GridComponent.GetState();
currentGridState.OriginalEditItem.UpdateFromObject(updatedItem); // method to update all properties
ProductService.UpdateProduct(updatedItem);
