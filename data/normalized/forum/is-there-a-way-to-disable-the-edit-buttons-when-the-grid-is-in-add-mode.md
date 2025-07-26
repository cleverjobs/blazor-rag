# Is there a way to disable the "Edit" buttons when the Grid is in Add mode?

## Question

**Gar** asked on 22 Dec 2019

Marin, Is there a way to disable the "Edit" buttons when the Grid is in Add mode? I would also like to disable some other navigation links on the page when the grid is in "Add" mode. I have set a "GridIsDirty" variable when I'm in Edit mode to take care of this for edits. If it's not possible, do you have a work around for this by any chance? Thanks Marin,

## Answer

**Marin Bratanov** answered on 23 Dec 2019

Hi Gary, Perhaps the easiest approach I can think of is using the popup editing model as it shows a modal window so the user can't touch the page behind it: [https://demos.telerik.com/blazor-ui/grid/editing-popup.](https://demos.telerik.com/blazor-ui/grid/editing-popup.) You can also customize it, for example: [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form.) Another approach is to raise flags in the grid events and add conditional logic around the command buttons that uses those flags, something similar to the second example here: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create.](https://docs.telerik.com/blazor-ui/knowledge-base/grid-change-editable-attribute-update-create.) Below is an example I made for you based on that, where I highlighted the key points. Would it be OK with you if I moved this thread to the public forums, as I feel like this snippet may be useful to other people? <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="500px" OnUpdate="@UpdateHandler" OnCancel="@( ()=> isEditable=true )" OnCreate="@( ()=> isEditable=true )">
<GridColumns>
<GridColumn Field=@nameof (SampleData.ID) Title="ID" />
<GridColumn Field=@nameof (SampleData.Name) Title="Name" />
<GridCommandColumn>
<GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton>
<GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> @if (isEditable) { <GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton> } </GridCommandColumn>
</GridColumns>
<GridToolBar>
<GridCommandButton Command="Add" Icon="add" OnClick="@( ()=> isEditable=false )">Add Employee</GridCommandButton>
</GridToolBar>
</TelerikGrid>

@code { bool isEditable { get; set; }=true; void OnCancel ( GridCommandEventArgs e ) { isEditable=true; } public void UpdateHandler ( GridCommandEventArgs args ) { isEditable=true; //unrelated CRUD operations. // TODO: inserts and deletes are not implemented in this sample for brevity SampleData item=(SampleData)args.Item; var matchingItem=MyData.FirstOrDefault(c=> c.ID==item.ID); if (matchingItem !=null )
{
matchingItem.Name=item.Name;
}
} protected override void OnInitialized ( ) {
MyData=new List<SampleData>(); for ( int i=0; i <50; i++)
{
MyData.Add( new SampleData()
{
ID=i,
Name="name " + i
});
}
} //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; }
} public List<SampleData> MyData { get; set; }
} Regards, Marin Bratanov

### Response

**Gary** answered on 23 Dec 2019

Marin, I don't mind if you move it to the public forum. I hope it helps someone! You know, I didn't realize how easy this was. I just didn't understand that I could add an event "OnClick" to the "Add" command button. That makes it all so easy. I thought the default command button events were limited to (OnUpdate, OnDelete, OnCreate, OnEdit and OnCancel) based on this article [https://docs.telerik.com/blazor-ui/components/grid/editing/overview#grid-crud-operations-overview.](https://docs.telerik.com/blazor-ui/components/grid/editing/overview#grid-crud-operations-overview.) My mistake. I appreciate your help sir. Happy Holidays!

### Response

**Marin Bratanov** answered on 23 Dec 2019

Thank you, Gary. The thread is now public at: [https://www.telerik.com/forums/is-there-a-way-to-disable-the-edit-buttons-when-the-grid-is-in-add-mode](https://www.telerik.com/forums/is-there-a-way-to-disable-the-edit-buttons-when-the-grid-is-in-add-mode) Regards, Marin Bratanov
