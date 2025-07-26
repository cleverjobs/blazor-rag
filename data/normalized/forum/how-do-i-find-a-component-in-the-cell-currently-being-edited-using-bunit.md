# How do I find a component in the cell currently being edited using bUnit?

## Question

**Hol** asked on 05 Jun 2025

I have a Blazor grid for a collection of key-value pairs where the edit template for one cell has a ComboBox with a list of the possible keys. The requirement is that each key can only be used once. My grid's OnEdit handler is: private void OnEdit ( GridCommandEventArgs e ) {
MyModel model=(MyModel)e.Item; if (e.Field==nameof (MyModel.KeyTypeId))
{
IEnumerable<byte> typeIdsInUse=Data.Select(x=> x.KeyTypeId).Except([model.KeyTypeId]).ToArray();
KeyTypesForDropDown=KeyTypes!.Where(x=> !typeIdsInUse.Contains(x.KeyTypeId)).ToList(); if (KeyTypesForDropDown.Count==0 )
{
Notification.Show( "There are no more keys available to add.", ThemeConstants.Notification.ThemeColor.Warning);
e.IsCancelled=true;
}
}
} My problem is that I can't figure out how to find this ComboBox in the grid cell during my test in order to validate that its data is correct. This is how far I got: GridCommandEventArgs args=new ()
{
Item=new MyModel(),
}; await grid.InvokeAsync(()=> grid.Instance.OnAdd.InvokeAsync(args)); await grid.InvokeAsync(()=> grid.Instance.OnCreate.InvokeAsync(args)); var state=grid.Instance.GetState();
state.OriginalEditItem=state.EditItem=(MyModel)args.Item; await grid.Instance.SetStateAsync(state);
grid.Render(); var rows=grid.FindComponent<GridRowCollection<MyModel>>();
rows.Render(); state=grid.Instance.GetState(); state.EditField=nameof(MyModel.KeyTypeId); await grid.Instance.SetStateAsync(state); grid.Render(); rows.Render(); var row=rows.FindComponent<GridRow<MyModel>>(); Assert.True(row.HasComponent<GridEditCell<MyModel>>()); Can you help me to find the edit cell and ComboBox? Thanks!

## Answer

**Dimo** answered on 10 Jun 2025

Hi Holly, The Telerik Blazor ComboBox is a generic component with two @typeparam 's. To reference it, you need to specify the type of the ComboBox model and the type of the ComboBox Value: var row=rows.FindComponent<GridRow<MyGridModel>>(); var cell=row.FindComponent<GridEditCell<MyGridModel>>(); var comboBoxes=cell.FindComponents<TelerikComboBox<MyComboBoxModel, int>>(); Assert.True(row.HasComponent<GridEditCell<MyGridModel>>());
Assert.Empty(comboBoxes); The bad thing is that the above code does not throw exceptions, but there is no ComboBox found, so the second Assert "passes". At the same time, the ComboBox is rendered, which can be easily verified with: var all=cell.FindAll( "*" );
Console.WriteLine( string.Join( " - ", all)); // outputs // AngleSharp.Html.Dom.HtmlTableDataCellElement - AngleSharp.Html.Dom.HtmlSpanElement - AngleSharp.Html.Dom.HtmlInputElement - AngleSharp.Html.Dom.HtmlSpanElement - AngleSharp.Html.Dom.HtmlSpanElement - AngleSharp.Svg.Dom.SvgSvgElement - AngleSharp.Svg.Dom.SvgElement - AngleSharp.Html.Dom.HtmlButtonElement - AngleSharp.Html.Dom.HtmlSpanElement - AngleSharp.Svg.Dom.SvgSvgElement - AngleSharp.Svg.Dom.SvgElement The GridEditCell component renders a RenderFragment, which contains the ComboBox: <td>
@if (Column.EditorTemplate !=null )
{ @Column.EditorTemplate(Item); } else { // render the default cell editor for the column field type }
</td> However, I am not sure how to obtain the ComboBox instance. I believe this is a bUnit support question, not a Telerik support question. On a side note, you can test if the ComboBox Data and Value are correct without the actual ComboBox instance. Just test what the app provides the correct values to these two parameters. Regards, Dimo Progress Telerik

### Response

**Holly** commented on 10 Jun 2025

Thanks for responding! I should have clarified: The line Assert.True(row.HasComponent<GridEditCell<MyModel>>()) fails, so I can't even look in it to find the ComboBox markup.

### Response

**Dimo** commented on 11 Jun 2025

Here is a complete test that passes on my side and shows what I managed to achieve. On a side note, it's highly recommended to be more specific about what blockers you hit when requesting assistance. This will spare extra message round-trips and double work. @using Telerik.Blazor.Components.Grid

@inherits TelerikTestContext

@code {
public class Product {
public int Id { get; set; }
public int? CategoryId { get; set; }
public string Name { get; set; }=string.Empty;

public Product Clone ( ) { return new Product ( ) {
Id=Id,
CategoryId=CategoryId,
Name=Name
};
}
}

public class Category {
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
}

[Fact]
public async Task Grid_renders_edit_cell ( ) {
List<Product> GridData=new ( ) { new ( ) { Id=1, CategoryId=1, Name="Product 1" } };
List<Category> CategoryData=new ( ) { new ( ) { Id=1, Name="Category 1" } }; var grid=Render(@<TelerikGrid Data="@GridData" EditMode="@GridEditMode.Incell"> <GridColumns> <GridColumn Field="@nameof(Product.Name)" /> <GridColumn Field="@nameof(Product.CategoryId)" Title="Category"> <Template> @{ var dataItem=(Product)context; }
@CategoryData.Find(x=> x.Id==dataItem.CategoryId)?.Name </Template> <EditorTemplate> @{ var dataItem=(Product)context; } <TelerikComboBox Data="@CategoryData" @bind-Value="@dataItem.CategoryId" ValueField="@nameof(Category.Id)" TextField="@nameof(Category.Name)" /> </EditorTemplate> </GridColumn> </GridColumns> </TelerikGrid>); var gridComponent=grid.FindComponent<TelerikGrid<Product>>(); var firstDataItem=GridData.First(); var gridState=gridComponent.Instance.GetState();
gridState.EditField=nameof(Product.CategoryId);
gridState.OriginalEditItem=firstDataItem;
gridState.EditItem=firstDataItem.Clone(); await gridComponent.Instance.SetStateAsync(gridState);

gridComponent.Render(); var rows=gridComponent.FindComponent<GridRowCollection<Product>>(); var row=rows.FindComponent<GridRow<Product>>(); var cell=row.FindComponent<GridEditCell<Product>>(); var comboBoxes=cell.FindComponents<TelerikComboBox<Category, int>>(); // will be empty although the ComboBox is rendered var comboBoxElement=cell.FindAll( "span.k-combobox" ); // will find the element Assert.NotNull(cell);
Assert.Contains( "k-combobox", comboBoxElement.First().ClassName);
}
}

### Response

**Holly** commented on 11 Jun 2025

Oh! I didn't realize you could go straight to edit mode with a blank item, although it seems obvious now in hindsight. I was trying to go through the entire Add process and I got stuck when the GridContentCell wasn't replaced with the GridEditCell. I'm not sure why your call to FindComponents() returned an empty collection, but I got my ComboBox through that route. Thanks so much for your help!

### Response

**Dimo** commented on 12 Jun 2025

That's interesting. Can you send me the complete test, so that I can run it on my side? Thank you in advance!

### Response

**Holly** commented on 12 Jun 2025

OK, give me a little time to strip out the proprietary stuff and I'll put it into a GitHub repo.

### Response

**Holly** commented on 13 Jun 2025

I have attached a zip file of the code in my support ticket instead.
