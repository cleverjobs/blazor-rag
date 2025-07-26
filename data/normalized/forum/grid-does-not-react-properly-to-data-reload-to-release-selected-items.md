# Grid does not react properly to data reload to release selected items

## Question

**Ale** asked on 17 Mar 2023

<TelerikGrid Data="@Service.ProductSubmissions" Resizable="true" SelectionMode="GridSelectionMode.Multiple" FilterMode="@GridFilterMode.FilterMenu" EditMode="@GridEditMode.Inline" Height="100%" Pageable="true" Sortable="true" Groupable="false" SortMode="@SortMode.Single" OnEdit="@GridRowEdit" OnCreate="@(async args=> await Service.CreateAsync(args))" OnUpdate="@(async args=> await Service.UpdateAsync(args))" @bind-SelectedItems="@Service.SelectedItems" @bind-Page="@Service.GridPageIndex" PageSize="@Service.GridPageSize" PageSizeChanged="@Service.PagerPageSizeChanged" @ref="@Grid"> on update: Console.WriteLine("before update request"); Console.WriteLine($"selected items count before: {SelectedItems.Count()}"); var updateResponse=await _productSubmissionService.UpdateAsync(
new ProductSubmissionUpdateRequestModel(submissionModel, new List <int> (), SelectedItems.Select(_=> _.Id).ToList(), null)); Console.WriteLine($"selected items count after: {SelectedItems.Count()}"); Console.WriteLine("update request - done");

await FinalizeUpdate(updateResponse);

Console.WriteLine("finalize update"); Console.WriteLine($"selected items count after 2: {SelectedItems.Count()} | Any {(SelectedItems.Any() ? 1 : 0)}"); if ( SelectedItems.Any() )
{ Console.WriteLine("has selected items"); //SelectedItems=Enumerable.Empty <ProductSubmissionModel> ();

await GetSubmissions(_productState.Value.ProductId.Value);

Console.WriteLine("reload - done");
} await FinalizeUpdate(updateResponse); - just replace updated model so the sequence: - have several items selected - update one item - reload all data to the grid (according to the doc, if the source if observable (it is public ObservableCollection<ProductSubmissionModel> ProductSubmissions { get; set; }), Selected items collection should be released) - edit another item (single, grid does not show that any selected (visually)) - but we still see that we have selected, see count before 1, still have after request, see after 1, and just after second collection change, the grid has all dataset recalculated & compared & released Selected items, see after update 2 so, selected items have to be released after the dataset reload, but it did not happen var submissions=await _productSubmissionService.GetAsync(productId, _versionId);
await IfHasFiles(submissions);
Console.WriteLine("exit GetSubmissions");
ProductSubmissions=new ObservableCollection <ProductSubmissionModel> (submissions);

### Response

**Aleksandr** commented on 17 Mar 2023

@Telerik how does it work if we use OnRead? do you use observable under the hood?

## Answer

**Aleksandr** answered on 17 Mar 2023

so, grid does not detect changes (does not manage selected items collection) when we replace data source, if we do clear & add range, the list of selected items seems correct
