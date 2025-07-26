# Cannot insert GridCommandColumns into my <TelerikGridWrapper>

## Question

**Rol** asked on 21 Oct 2020

I use [Parameter] public RenderFragment GridCommandColumn { get; set; } and <GridCommandColumn> <GridCommandButton Command="Edit" Icon="edit" /> @GridCommandColumn </GridCommandColumn> I get the following compiler error: Unrecognized child content inside component 'TelerikGrid'. The component 'TelerikGrid' accepts child content through the following top-level items: 'GridAggregates', 'GridColumns', 'GridToolBar', ... I don't understand why the compiler says that @GridCommandColumn needs to be a TelerikGrid RenderFragment. I would think this is "my" RenderFragment, and the TelerikGrid would only see the rendered GridCommandButtons. Is there some way to let a parent component insert GridCommandColumns into my <TelerikGridWrapper>?

## Answer

**Roland** answered on 21 Oct 2020

Feel free to remove this post. My wrapper put <GridCommandColumn> outside <GridColumns>

### Response

**Marin Bratanov** answered on 21 Oct 2020

Hi Roland, I suspect the first issue is that the render fragment is already in a command column while it tries to be a command column already. If you define the render fragment inside the command column, it should have command buttons in there, not an entire command column. For example: Index.razor <MyTemplatedGrid> <Commands> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="edit"> Edit </GridCommandButton> </Commands> </MyTemplatedGrid> which uses the following component (where actual editing is not imlemented, but you can see the buttons work even without the data updates): MyTemplatedGrid.razor <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="400px">
<GridToolBar>
<GridCommandButton Command="Add" Icon="add">Add Employee</GridCommandButton>
</GridToolBar>
<GridColumns>
<GridColumn Field=@nameof(SampleData.ID) Title="ID" Editable="false" />
<GridColumn Field=@nameof(SampleData.Name) Title="Name" />
<GridCommandColumn> @Commands <GridCommandButton Command="Delete" Icon="delete">Delete</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton>
</GridCommandColumn>
</GridColumns>
</TelerikGrid>

@code { [ Parameter ] public RenderFragment Commands { get; set; } // in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; }
}

List<SampleData> MyData { get; set; } protected override void OnInitialized ( ) {
MyData=new List<SampleData>(); for ( int i=0; i <50; i++)
{
MyData.Add( new SampleData()
{
ID=i,
Name="Name " + i.ToString()
});
}
}
} Regards, Marin Bratanov
