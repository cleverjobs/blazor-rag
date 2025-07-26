# Customize the Telerik FileManager

## Question

**RayRay** asked on 19 Jul 2022

Is there a way to customize the telerik filemanager? I need to hide the navigation pane (directories), the breadcrumbs and also customize the toolbar. (remove "Search", "New Folder," "Sort By", "Sort Order", and "View") Currently I am able to Hide the nav panel and the breadcrumbs through CSS, but the splitter is still forcing the content pane to be sized as though it is present.. I would also like to be able to select the grid as the default (and only) view available Any help would be appreciated.

## Answer

**Hristian Stefanov** answered on 20 Jul 2022

Hi Ray, Regarding the desired customizations we have open feature requests on our Public Feedback Portal: Customizable Toolbar (remove/add buttons) Add option to control the default view of the FileManager Once we implement the above features, the described customizations will become easily achievable without custom CSS. In the meantime, the sideways approach to customize the FileManager as wanted is to use custom CSS styles. I have prepared an example you can test to see the result: <style>.my-filemanager.k-toolbar> button [tabindex="0" ],.my-filemanager.k-toolbar.k-split-button,.my-filemanager.k-pane.k-filemanager-navigation,.my-filemanager.k-splitbar,.my-filemanager.k-breadcrumb,.my-filemanager.k-filemanager-search-tool,.my-filemanager.k-filemanager-details-toggle,.my-filemanager.k-button +.k-button-group { display: none;
} </style> <TelerikFileManager Class="my-filemanager" Height="400px" Data="@Files" @bind-Path="@FilePath" NameField="Name" SizeField="Size" PathField="Path" ExtensionField="Extension" IsDirectoryField="IsDirectory" HasDirectoriesField="HasDirectories" ItemsField="Items" DateCreatedField="DateCreated" DateCreatedUtcField="DateCreatedUtc" DateModifiedField="DateModified" DateModifiedUtcField="DateModifiedUtc" /> @code {
public List <HierarchicalFileEntry> Files=new List <HierarchicalFileEntry> ();
public string FilePath { get; set; }=string.Empty;

protected override async Task OnInitializedAsync()
{
Files=await GetHierarchicalFileEntries();
}

public class HierarchicalFileEntry
{
public string MyModelId { get; set; }
public string Name { get; set; }
public long Size { get; set; }
public string Path { get; set; }
public string Extension { get; set; }
public bool IsDirectory { get; set; }
public bool HasDirectories { get; set; }
public DateTime DateCreated { get; set; }
public DateTime DateCreatedUtc { get; set; }
public DateTime DateModified { get; set; }
public DateTime DateModifiedUtc { get; set; }
public List <HierarchicalFileEntry> MyDirectories { get; set; }
public List <HierarchicalFileEntry> Items { get; set; }
}

async Task<List <HierarchicalFileEntry>> GetHierarchicalFileEntries()
{
var root=new HierarchicalFileEntry()
{
MyModelId="1",
Name="Work Files",
IsDirectory=true,
HasDirectories=false,
DateCreated=new DateTime(2022, 1, 2),
DateCreatedUtc=new DateTime(2022, 1, 2),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine("Work Files"),
Size=3 * 1024 * 1024,
};

var dashboardDesign=new HierarchicalFileEntry()
{
MyModelId="2",
Name="Dashboard",
IsDirectory=false,
Extension=".png",
DateCreated=new DateTime(2022, 1, 10),
DateCreatedUtc=new DateTime(2022, 1, 10),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(root.Path, "Dashboard.png"),
Size=1024
};

var gridDesign=new HierarchicalFileEntry()
{
MyModelId="3",
Name="Design",
IsDirectory=false,
Extension=".png",
DateCreated=new DateTime(2022, 1, 12),
DateCreatedUtc=new DateTime(2022, 1, 12),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(root.Path, "Design.png"),
Size=1024
};

root.Items=new List <HierarchicalFileEntry> () { dashboardDesign, gridDesign };

List <HierarchicalFileEntry> files=new List <HierarchicalFileEntry> () { root };

return await Task.FromResult(files);
}
} Regards, Hristian Stefanov

### Response

**Ray** commented on 20 Jul 2022

That works great for hiding the items - THANK YOU! Is there a way to default to the Grid view for the control or do I need to wait for the feature request?

### Response

**Hristian Stefanov** commented on 22 Jul 2022

Hi Ray, As a sideways approach, until the feature gets implemented, there is one that came to my mind. You can use a Javascript function to click the Grid view button on the initial load. Here is an example I have prepared for you to run and test: @inject IJSRuntime js <style>.my-filemanager.k-toolbar> button [tabindex="0" ],.my-filemanager.k-toolbar.k-split-button,.my-filemanager.k-pane.k-filemanager-navigation,.my-filemanager.k-splitbar,.my-filemanager.k-breadcrumb,.my-filemanager.k-filemanager-search-tool,.my-filemanager.k-filemanager-details-toggle,.my-filemanager.k-button +.k-button-group { display: none;
} </style> <TelerikFileManager Class="my-filemanager" Height="400px" Data="@Files" @bind-Path="@FilePath" NameField="Name" SizeField="Size" PathField="Path" ExtensionField="Extension" IsDirectoryField="IsDirectory" HasDirectoriesField="HasDirectories" ItemsField="Items" DateCreatedField="DateCreated" DateCreatedUtcField="DateCreatedUtc" DateModifiedField="DateModified" DateModifiedUtcField="DateModifiedUtc" /> @*In a normal app, this function should be in the _Layout.cshtml file*@<script suppress-error="BL9992"> function gridDefault ( ) { document.querySelector( '.my-filemanager div + .k-button-group> button' ).click();
} </script> @code {
public List <HierarchicalFileEntry> Files=new List <HierarchicalFileEntry> ();
public string FilePath { get; set; }=string.Empty;

protected override async Task OnInitializedAsync()
{
Files=await GetHierarchicalFileEntries();
} protected override void OnAfterRender(bool firstRender)
{
js.InvokeVoidAsync("gridDefault");
base.OnAfterRender(firstRender);
} public class HierarchicalFileEntry
{
public string MyModelId { get; set; }
public string Name { get; set; }
public long Size { get; set; }
public string Path { get; set; }
public string Extension { get; set; }
public bool IsDirectory { get; set; }
public bool HasDirectories { get; set; }
public DateTime DateCreated { get; set; }
public DateTime DateCreatedUtc { get; set; }
public DateTime DateModified { get; set; }
public DateTime DateModifiedUtc { get; set; }
public List <HierarchicalFileEntry> MyDirectories { get; set; }
public List <HierarchicalFileEntry> Items { get; set; }
}

async Task<List <HierarchicalFileEntry>> GetHierarchicalFileEntries()
{
var root=new HierarchicalFileEntry()
{
MyModelId="1",
Name="Work Files",
IsDirectory=true,
HasDirectories=false,
DateCreated=new DateTime(2022, 1, 2),
DateCreatedUtc=new DateTime(2022, 1, 2),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine("Work Files"),
Size=3 * 1024 * 1024,
};

var dashboardDesign=new HierarchicalFileEntry()
{
MyModelId="2",
Name="Dashboard",
IsDirectory=false,
Extension=".png",
DateCreated=new DateTime(2022, 1, 10),
DateCreatedUtc=new DateTime(2022, 1, 10),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(root.Path, "Dashboard.png"),
Size=1024
};

var gridDesign=new HierarchicalFileEntry()
{
MyModelId="3",
Name="Design",
IsDirectory=false,
Extension=".png",
DateCreated=new DateTime(2022, 1, 12),
DateCreatedUtc=new DateTime(2022, 1, 12),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(root.Path, "Design.png"),
Size=1024
};

root.Items=new List <HierarchicalFileEntry> () { dashboardDesign, gridDesign };

List <HierarchicalFileEntry> files=new List <HierarchicalFileEntry> () { root };

return await Task.FromResult(files);
}
}
