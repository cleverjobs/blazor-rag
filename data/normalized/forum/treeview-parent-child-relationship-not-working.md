# Treeview parent/child relationship not working

## Question

**Rob** asked on 29 Aug 2022

I created a treeView but for some reason, the data children are not included in the drop-down but separate. How would I set this up to have the children fall under their parent? <TelerikTreeView Data="@FlatData" @bind-ExpandedItems="@ExpandedItems"> <TreeViewBindings> <TreeViewBinding ParentIdField="FlatData.Parent" /> </TreeViewBindings> </TelerikTreeView> @code { IEnumerable<TreeItem> FlatData { get; set; } IEnumerable<object> ExpandedItems { get; set; }=new List<TreeItem>(); private void CreateDeviceTreeList() { List<TreeItem> items=new List<TreeItem>(); int count=0; foreach(var a in devices.Items) { items.Add(new TreeItem(){ Id=count, Parent=null, Text=a.Name, HasChildren=true }); count++; items.Add(new TreeItem(){ Id=count, Parent=count-1, Text=a.Group, HasChildren=false }); count++; items.Add(new TreeItem(){ Id=count, Parent=count-1, Text=a.Sensor, HasChildren=false }); count++; } FlatData=items; ExpandedItems=FlatData.Where(x=> x.HasChildren==true).ToList(); StateHasChanged(); } protected async override void OnInitialized() { CreateDeviceTreeList(); } }

## Answer

**Dimo** answered on 01 Sep 2022

Hello Robert, ParentIdField="FlatData.Parent" means that TreeItem has a FlatData property, which is an object and it has a nested Parent property. That is obviously not that case, so you need ParentIdField="Parent" Regards, Dimo Progress Telerik
