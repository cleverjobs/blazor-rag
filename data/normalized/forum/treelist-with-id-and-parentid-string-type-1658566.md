# TreeList with Id and parentId string type

## Question

**Mic** asked on 17 Jul 2024

Hi, I have a treelist where the parentID is a GUID so it is defined as a string. The child items don't appears. It seems that string is not supported in ParentID. Any turn around for that? Best regards.

## Answer

**Dimo** answered on 19 Jul 2024

Hello Michel, The TreeView item relationships can work with Guid and string too. Please make sure that: The ID and parent ID values are set correctly in the data. The IdField and ParentIdField parameters are configured correctly. <TelerikTreeList Data="@TreeListData" IdField="@nameof(SampleModel.Id)" ParentIdField="@nameof(SampleModel.ParentId)" Pageable="true" Sortable="true"> <TreeListColumns> <TreeListColumn Field="@nameof(SampleModel.Id)" /> <TreeListColumn Field="@nameof(SampleModel.ParentId)" /> <TreeListColumn Field="@nameof(SampleModel.Name)" Expandable="true" /> </TreeListColumns> </TelerikTreeList>

@code {
private List<SampleModel> TreeListData { get; set; }=new ();

private List<string> SearchableFields=new List<string> { nameof(SampleModel.Name) };

protected override void OnInitialized ( ) { for (int i=1; i <=9; i++)
{
TreeListData.Add( new SampleModel ( ) {
Name=$ "Name {i}" });
} for (int i=0; i <TreeListData.Count; i++)
{ if (i> 2 )
{ TreeListData[i].ParentId=TreeListData[i % 3 ].Id; }
}
}

public class SampleModel {
public string Id { get; set; }=Guid.NewGuid().ToString();
public string? ParentId { get; set; }
public string Name { get; set; }=string.Empty;
}
} Regards, Dimo
