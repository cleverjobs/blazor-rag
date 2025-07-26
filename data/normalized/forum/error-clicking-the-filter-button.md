# Error clicking the filter button

## Question

**Ber** asked on 22 Mar 2021

Hi, I get an error when I click the filter button in this situation: I have a colum with enum datatype. I filter the column on 1 of the enumeration values. After changing the filters, I save the gridstate to local storage. I use the system.text.json to serialize the gridstate. After refreshing the page, the filter loads correctly, the data is filtered on the database and the filter button is marked as used. When I click the button to change the filter, I get following error: Unhandled exception in circuit '{CircuitId}'. (System.InvalidCastException: Unable to cast object of type 'System.Int16' to type 'System.Int32'. at Telerik.Blazor.Components.Common.Editors.TelerikEnumEditor.get_CurrentValue() at Telerik.Blazor.Components.Common.Editors.TelerikEnumEditor.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue()) Thanks

## Answer

**Bert** answered on 25 Mar 2021

I made a small workaround for this problem. After deserialisation of the gridstate, I convert the short (Int16) values to Int32 values. This is the extension I use: public static void ReplaceEnumDatatype<T>(this GridState<T> gridstate) { gridstate.FilterDescriptors.ToList().ForEach(f=> { if (f is FilterDescriptor fd) { if (fd.Value.GetType()==typeof(short)) { fd.Value=Convert.ChangeType(fd.Value, typeof(Int32)); } } if (f is CompositeFilterDescriptor cfd) { cfd.FilterDescriptors.ToList().ForEach(fd=> { if (fd is FilterDescriptor fdc) { if (fdc.Value?.GetType()==typeof(short)) { fdc.Value=Convert.ChangeType(fdc.Value, typeof(Int32)); } } }); } }); }

### Response

**Stamo Gochev** answered on 25 Mar 2021

Hello Bert, The behavior you are experiencing sounds unexpected, but as we are not aware of such a bug, can you send me a runnable example that demonstrates the issue, so I can investigate it? For some reason, the "int" type is converted to a "short" value, so I will use the page you are going to send in order to determine if this is caused by a configuration (or serialization) issue or whether it is an actual bug. Regards, Stamo Gochev

### Response

**Bert** answered on 25 Mar 2021

Hi Stamo, when I have a enumeration field in the grid, I see the value in the filterdescription is deserialized with system.text.json as an Int16 value. When clicking on the filter button in the grid, the grid tries to convert the filterdescriptor value to an int32, which fails. This is a small bug I believe, there is no reason why a Int16 can not be converted to a Int32. I tried to add my source files, but it's not allowed.How can I send some files to you? Best regards

### Response

**Stamo Gochev** answered on 26 Mar 2021

Hello, You can organize the necessary files into a folder and then archive them in a ".zip" format, so they can be attached to the ticket. If this still doesn't work, you can paste the text of the files in a similar way as you did with the response from 25 Mar 2021 and I will use them as a reference to create a runnable example. On a side note - System.Text.Json has some known problems with serializing/deserializing certain types, so what I can suggest you try meanwhile is to use a different type of serializer for the scenario. Regards, Stamo Gochev Progress Telerik

### Response

**Bert** answered on 26 Mar 2021

Hi Stamo, I will send you the files later, today I'm not in the office. The problem starts with the deserialisation with json.text, it converts enums to Int16 instead of Int32. I also tried Json.net, but then I get other problems. With my extension, i converts the short values in the filters to int32, and then there is no problem. Is it possible to do the right conversion/casting inside the grid component? Thanks, Best regards Bert Degrave

### Response

**René** answered on 30 Mar 2021

I can confirm that with Enum Columns the described InvalidCastException is being thrown when "FilterMenuType.Menu" is used. If "FilterMenuType.CheckBoxList" is used instead, there is no Exception being thrown but there is some other misbehaviour: The Filter Icon in the column header is marked as "Filtered" and the data is correctly filtered but if the Filter-Icon is clicked no checkbox is marked in the popup. The filter can be cleared though and some other filtering can be applied. Regards, René

### Response

**Stamo Gochev** answered on 31 Mar 2021

Hi, @Bert - Were you able to isolate the issue on a sample page in order to paste the code here, so I can inspect it? @René - As you are reporting an additional issue with "FilterMenuType.CheckBoxList", can you open a separate support ticket and provide a runnable example, so the issue can be investigated? Regards, Stamo Gochev

### Response

**Bert** answered on 31 Mar 2021

Hi Stamo and René, Sorry for my late reply. In another part of my project, I defined a Int64 Enumeration. I also got this error with this enumeration. I temporarily changed the enum to Int32 I cannot upload a zip file in reply to this post=> I will paste my code. I used the telerik persist_selection example to make this sample. @page "/" @using Telerik.Blazor.Components; @using Telerik.DataSource; @using Telerik.DataSource.Extensions; @using Blazored.LocalStorage; @using System.Text; @using System.Text.Json; @using VBS.Shared.Attributes; @inject ILocalStorageService _LocalStorage <TelerikGrid @ref="@_TblTasksGrid" Data=@GridData SelectionMode="GridSelectionMode.Multiple" SelectedItemsChanged="@((IEnumerable<Employee> employeeList)=> OnSelect(employeeList))" SelectedItems="@PersistedSelectedItems" FilterMode="@GridFilterMode.FilterMenu" OnStateInit="@((GridStateEventArgs<Employee> args)=> OnStateInitHandler(args))" OnStateChanged="@((GridStateEventArgs<Employee> args)=> OnStateChangedHandler(args))" @bind-Page="@CurrentPage" PageSize="@PageSize" Pageable="true"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field=@nameof(Employee.EmployeeId) /> <GridColumn Field=@nameof(Employee.Name) /> <GridColumn Field=@nameof(Employee.Team) /> <GridColumn Field=@nameof(Employee.TestEnum) /> </GridColumns> </TelerikGrid> @if (PersistedSelectedItems !=null) { <ul> @foreach (Employee employee in PersistedSelectedItems.OrderBy(e=> e.EmployeeId)) { <li> @employee.EmployeeId </li> } </ul> } @code { public List<Employee> PersistedSelectedItems { get; set; }=new List<Employee>(); int CurrentPage { get; set; } int PageSize { get; set; }=5; private TelerikGrid<Employee> _TblTasksGrid { get; set; } private GridState<Employee> _TblTasksGridState { get; set; } private DataSourceRequest _TblTasksRequest { get; set; } protected void OnSelect(IEnumerable<Employee> employees) { IEnumerable<Employee> CurrentPageEmployees=GridData.Skip(PageSize * (CurrentPage - 1)).Take(PageSize); if (employees==null || employees.Count()==0) { //the user de-selected all items with the header checkbox PersistedSelectedItems=PersistedSelectedItems.Except(CurrentPageEmployees).ToList(); } else { //handle any deselected items var UnselectedEmployees=CurrentPageEmployees.Except(employees); PersistedSelectedItems=PersistedSelectedItems.Except(UnselectedEmployees).ToList(); //add any new items if they were not selected already foreach (var item in employees) { if (!PersistedSelectedItems.Contains(item)) { PersistedSelectedItems.Add(item); } } } } async Task OnStateInitHandler(GridStateEventArgs<Employee> args) { try { if (_TblTasksGridState==null) { string json=await _LocalStorage.GetItemAsStringAsync("GridSaveStateTblTasks"); _TblTasksGridState=JsonSerializer.Deserialize<GridState<Employee>>(json, new JsonSerializerOptions() { PropertyNameCaseInsensitive=true }); //_TblTasksGridState.ReplaceEnumDatatype<Employee>(); // _TblTasksGridState=await _LocalStorage.GetItemAsync<GridState<TblTask>>("GridSaveStateTblTasks"); } if (args !=null) { args.GridState=_TblTasksGridState; } else { await _TblTasksGrid.SetState(_TblTasksGridState); } } catch (Exception exc) { //Logger.Error(LogExtensions.Exc(exc)); } finally { } } async void OnStateChangedHandler(GridStateEventArgs<Employee> args) { try { string json=JsonSerializer.Serialize(args.GridState); await _LocalStorage.SetItemAsync<string>("GridSaveStateTblTasks", json); } catch (InvalidOperationException e) { // JavaScript interop calls cannot be issued at this time. This is because the component is being statically rendered. When prerendering is enabled, JavaScript interop calls can only be performed during the OnAfterRenderAsync lifecycle method. //if (!e.Message.Contains("JavaScript interop calls cannot be issued at this time")) // Logger.Error(LogExtensions.Exc(e)); } catch (Exception exc) { //Logger.Error(LogExtensions.Exc(exc)); } finally { } } //data binding and sample data public List<Employee> GridData { get; set; } protected override void OnInitialized() { GridData=new List<Employee>(); for (int i=0; i <5; i++) { GridData.Add(new Employee() { EmployeeId=i, Name="Employee " + i.ToString(), Team="Team " + i % 3, TestEnum=(Test)i }); } } public class Employee { public int EmployeeId { get; set; } public string Name { get; set; } public string Team { get; set; } public Test TestEnum { get; set; } } public enum Test: Int32 { Value0=0, Value1=1, Value2=2, Value3=3, Value4=4, Value5=5, } }

### Response

**Stamo Gochev** answered on 02 Apr 2021

Hello, As the ILocalStorage implementation was not present on my side, I was able to run the page by adding a custom implementation for localStorage that works with the browser counterpart. The problem still appears to be caused by the serialization/deserialization implementation of System.Text.Json and its issues listed in: [https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-migrate-from-newtonsoft-how-to?pivots=dotnet-5-0#types-without-built-in-support](https://docs.microsoft.com/en-us/dotnet/standard/serialization/system-text-json-migrate-from-newtonsoft-how-to?pivots=dotnet-5-0#types-without-built-in-support) This results in the filter not having the correct type (as it is not deserialized correctly). What I can suggest is to manually handle the serialization/deserialization by using a serializer that supports Type conversion. Another approach is to manually set the "MemberType" of the filter as it is not available from the deserialization: async Task OnStateInitHandler ( GridStateEventArgs<Employee> args ) { try { if (_TblTasksGridState==null )
{ //string json=await _LocalStorage.GetItemAsStringAsync("GridSaveStateTblTasks"); string json=await _LocalStorage.GetItem<string>( "GridSaveStateTblTasks" );
_TblTasksGridState=JsonSerializer.Deserialize<GridState<Employee>>(json, new JsonSerializerOptions() { PropertyNameCaseInsensitive=true }); //_TblTasksGridState.ReplaceEnumDatatype<Employee>(); var filter=_TblTasksGridState.FilterDescriptors.ElementAtOrDefault( 3 ); if (filter !=null )
{ var filters=(filter as CompositeFilterDescriptor)?.FilterDescriptors; for ( int i=0; i <filters?.Count(); i++)
{ var childFilter=filters[i]; (childFilter as FilterDescriptor).MemberType=typeof (Int32); }
}
...
}
...
}
} The above snippet assumes that there is already a filter on the "TestEnum" column and sets the "MemberType" for the filters. You can modify it accordingly (adding checks for non-existent filters, the correct "MemberType", etc.) Regards, Stamo Gochev

### Response

**René** commented on 11 Oct 2022

Hello Stamo, your workaround does not work for me since setting the MemberType to Int32 results in an exception when trying to change the filter after loading state. The following works though: // Convert all Int16 to Int32 since we are not using any Int16. All occurrances come from Enums wrongly deserialized as Int16 foreach ( var filterDescriptor in state.FilterDescriptors)
{ var filters=(filterDescriptor as CompositeFilterDescriptor)?.FilterDescriptors; for ( int i=0; i <filters?.Count(); i++)
{ var childFilter=filters[i] as FilterDescriptor; if (childFilter?.Value !=null && childFilter.Value is short )
{ // childFilter.MemberType=typeof(int); // above line throws Error: System.NullReferenceException: Object reference not set to an instance of an object. // at Telerik.Blazor.Common.Filter.FilterOperatorFactory.GetFilterOperatorsForType(Type type, ITelerikStringLocalizer localizer) childFilter.Value=Convert.ToInt32(childFilter.Value);
}
}
} Regards, René

### Response

**Bert** answered on 02 Apr 2021

Hi Stamo, Thanks for the reply. You are right the problem is coming from the deserialization. I also tested JSon.net to serialize/deserialize, but then I get a lot of other problems. I will try to change my workaround extension a little bit to change the filter to the datatype of the enumeration. Best regards, Bert Degrave
