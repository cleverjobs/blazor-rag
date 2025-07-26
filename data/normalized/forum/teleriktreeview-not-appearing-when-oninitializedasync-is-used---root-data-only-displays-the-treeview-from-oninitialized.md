# TelerikTreeView not appearing when OnInitializedAsync is used - root data only displays the TreeView from OnInitialized

## Question

**Kel** asked on 25 Oct 2021

Designed using the HierarchicalData load on demand example, but I can only get the TelerikTreeView to display when I load the root data manually from OnInitialized. I've even tried calling StateHasChanged in OnInitializedAsync after LoadRootHierarchical has completed. Is there an issue with TelerikTreeView and async?

## Answer

**Hristian Stefanov** answered on 28 Oct 2021

Hi Kelly, Thank you for sharing with me what you are experiencing in detail. I have prepared for you a sample project that shows all the examples from our Treeview Load on Demand documentation with OnInitializedAsync methods. It seems that on my end, the TreeView displays as expected with async methods. Could you use the attached sample as a reference to see if the result you get is the same? One more thing that comes to my mind is that you might need an "if-else" block around the TreeView to make sure the data is loaded before rendering. This can be a reason for the described issue if you are using Flat Data Load on Demand. However, this approach is showcased on the second razor page in the attached project. I hope this helps. Please let me know if you need any further information. Regards, Hristian Stefanov Progress Telerik

### Response

**Kelly** commented on 03 Nov 2021

Thanks Hristian, I found some success, but seems like there may still be an issue. My use case is with an API call to populate the TreeView. What's the significance of inserting "await Task.Delay(50);"? See my test results below (3 LoadRootHierarchical variations): protected override async Task OnInitializedAsync ( ) { await LoadRootHierarchical();
} // This method works (no API - root data populated with fixed values) private async Task LoadRootHierarchical ( ) {
HierarchicalData=new List<TreeViewItem>();

HierarchicalData.Add( new TreeViewItem
{
DisplayName="John Doe",
ObjectName="User",
SectionDocuments=new List<TreeViewItem>(),
Icon="user",
Id=5217 // an identifier for use in the service call for child items });
} // This does NOT display the TreeView (retrieved from an API Http service call) private async Task LoadRootHierarchical ( ) {
HierarchicalData=new List<TreeViewItem>(); int userId=5217;
UserData=await _users.GetById(Endpoints.UsersEndpoint, userId);

HierarchicalData.Add( new TreeViewItem
{
DisplayName=UserData.UserName,
ObjectName="User",
SectionDocuments=new List<TreeViewItem>(),
Icon="user",
Id=UserData.UserId // an identifier for use in the service call for child items });
} // This method works (retrieved from an API Http service call) ... but only when "await Task.Delay(50);" is added private async Task LoadRootHierarchical ( ) { await Task.Delay( 50 );
HierarchicalData=new List<TreeViewItem>(); int userId=5217;
UserData=await _users.GetById(Endpoints.UsersEndpoint, userId);

HierarchicalData.Add( new TreeViewItem
{
DisplayName=UserData.UserName,
ObjectName="User",
SectionDocuments=new List<TreeViewItem>(),
Icon="user",
Id=UserData.UserId // an identifier for use in the service call for child items });
}

### Response

**Hristian Stefanov** commented on 08 Nov 2021

Hi Kelly, Indeed, the behavior is strange, and the method should work without the delay. The provided Task.Delay in the attached project in my last answer was just for the purpose of the example to show an async method. I also tested with an example with HTTP call and it works as expected on my end. To avoid guessing, could you isolate the scenario you have in a small runnable project and send it? This will allow me to see the reported behavior first hand on my machine and investigate further. Additionally, one thing you can try if you didn't is to wrap the TreeView syntax with an @if(HierarchicalData !=0) block. Thank you, and I look forward to your reply.
