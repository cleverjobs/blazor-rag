# DropDownList in TelerikGrid EditorTemplate throws NullReferenceException

## Question

**And** asked on 30 May 2019

Hello, I have edited the code below to remove a lot of the non-relevant parts. In summary I have a TelerikDropDownList within a TelerikGrid EditorTemplate within a TelerikWindow. When I click "Add" in the grid a NullReferenceException exception is thrown (full Exception text at the bottom of the post). If I comment out the DropDownList control completely, the exception is not thrown when I click "Add". <TelerikWindow> <TelerikWindowContent> <TelerikGrid Data=@ScheduledJobs EditMode="inline"> <TelerikGridToolBar> <TelerikGridCommandButton Command="Add" Icon="add"></TelerikGridCommandButton> </TelerikGridToolBar> <TelerikGridColumns> <TelerikGridColumn Field=@nameof(ScheduledJob.JobActionName) Title="Action"> <EditorTemplate> @{ JobToEdit=context as ScheduledJob; <TelerikDropDownList DefaultItem="@DefaultJobAction" Data="@JobActions" bind-Value=@JobToEdit.JobAction ValueField="@nameof(JobAction.Id)" TextField="@nameof(JobAction.Name)"></TelerikDropDownList> } ... @functions { protected List<JobAction> JobActions=<code to populate JobActions list> protected DefaultJobAction=JobActions[0]; // I have debugged - this assigns a non-null object as expected protected JobToEdit JobToEdit; // has a field called JobAction of type JobAction } The full exception text is: System.NullReferenceException: Object reference not set to an instance of an object.
at string Telerik.Blazor.Common.TelerikSelectBase<TValue>.get_CurrentValueAsString()
at void Telerik.Blazor.Components.DropDownList.TelerikDropDownList<TItem, TValue>.BuildRenderTree(RenderTreeBuilder builder)
at Microsoft.AspNetCore.Components.ComponentBase()+(RenderTreeBuilder builder)=> { }
at void Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment)
at void Microsoft.AspNetCore.Components.Rendering.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry)
at void Microsoft.AspNetCore.Components.Rendering.Renderer.ProcessRenderQueue()

## Answer

**Andrew** answered on 30 May 2019

I cant edit my post so replying with a minor correction to the above: @functions { ... protected ScheduledJob JobToEdit; // has a field called JobAction of type JobAction }

### Response

**Marin Bratanov** answered on 30 May 2019

Hello Andrew, The following seems to work fine for me, could you compare against it to find the difference causing the isue? @using Telerik.Blazor.Components.Grid @using Telerik.Blazor.Components.DropDownList <style> .k-master-row { height: 200px; /* workaround for [https://feedback.telerik.com/blazor/1410958-prevent-dropdowns-from-being-clipped-limited-by-their-container](https://feedback.telerik.com/blazor/1410958-prevent-dropdowns-from-being-clipped-limited-by-their-container) */ } </style> <TelerikGrid Data=@MyData EditMode="inline" Pageable="true" Height="500px"> <TelerikGridColumns> <TelerikGridColumn Field=@nameof(SampleData.ID) Title="ID" /> <TelerikGridColumn Field=@nameof(SampleData.Name) Title="Name" /> <TelerikGridColumn Field=@nameof(SampleData.Role) Title="Position"> <EditorTemplate> @{ CurrentlyEditedEmployee=context as SampleData; <TelerikDropDownList bind-Value="CurrentlyEditedEmployee.Role" Data="@Roles" ValueField="Name" TextField="Name"></TelerikDropDownList> } </EditorTemplate> </TelerikGridColumn> <TelerikGridCommandColumn> <TelerikGridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</TelerikGridCommandButton> <TelerikGridCommandButton Command="Edit" Icon="edit">Edit</TelerikGridCommandButton> </TelerikGridCommandColumn> </TelerikGridColumns> <TelerikGridEvents> <EventsManager OnUpdate="@UpdateHandler"></EventsManager> </TelerikGridEvents> </TelerikGrid> @functions { public SampleData CurrentlyEditedEmployee { get; set; } public void UpdateHandler(GridCommandEventArgs args) { SampleData item=(SampleData)args.Item; //perform actual data source operations here //if you have a context added through an @inject statement, you could call its SaveChanges() method //myContext.SaveChanges(); var matchingItem=MyData.FirstOrDefault(c=> c.ID==item.ID); if (matchingItem !=null ) { matchingItem.Name=item.Name; matchingItem.Role=item.Role; } } protected override void OnInit() { MyData=new List<SampleData>(); for ( int i=0; i <50; i++) { MyData.Add( new SampleData() { ID=i, Name="name " + i, Role=Roles[i % Roles.Count].Name }); } } //in a real case, keep the models in dedicated locations, this is just an easy to copy and see example public class SampleData { public int ID { get; set; } public string Name { get; set; } public string Role { get; set; } } public class MyRole { public int Id { get; set; } public string Name { get; set; } } public List<SampleData> MyData { get; set; } public static List<MyRole> Roles=new List<MyRole> { new MyRole {Id=1, Name="Manager" }, new MyRole {Id=2, Name="Employee" }, new MyRole {Id=3, Name="Contractor" } }; } Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 04 Jun 2019

Hello again Andrew, We had another report of similar behavior that led us to find a problem in the component, perhaps your scenario is similar. You can find more details and the bug page to follow in this post: [https://www.telerik.com/forums/uirhelper-navigateto-problem#yxxq9OCfm0ayb-iA79xcxA.](https://www.telerik.com/forums/uirhelper-navigateto-problem#yxxq9OCfm0ayb-iA79xcxA.) Regards, Marin Bratanov
