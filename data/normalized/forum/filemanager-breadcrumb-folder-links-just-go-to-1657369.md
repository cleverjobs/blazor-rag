# FileManager Breadcrumb folder links just go to "#"

## Question

**Han** asked on 05 Jul 2024

The FileManager breadcrumb links for previous folders don't seem to work like I would expect. Instead of opening the folder that was clicked on, it appears that the breadcrumb link leads to "#". Is there some kind of configuration that I'm missing? I attached my example source code which the issue. Please help to take a look and advise! Blazor web app, WebAssembly interactive render mode, .NET8.0 FileManagerBreadcrumb Thank you so much for your help!

### Response

**Hristian Stefanov** commented on 05 Jul 2024

Hi Hang, Thank you for attaching your project. However, I am unable to review any of the files due to permission restrictions on my office machine. To assist you better, please provide a runnable reproduction of the problem via the REPL platform. This will allow me to inspect the code and observe the behavior firsthand. I also attempted to replicate the issue using our FileManager demo, and the breadcrumb feature appears to function correctly there. I look forward to your response. Kind Regards, Hristian

### Response

**Hang** commented on 05 Jul 2024

When I added code to the REPL Platform and ran, its turn in to many errors even though I copy the code exactly on this link File Manager Overview. I also see the code example on REPL about File Manager when I got support from your team on another topic, but the breadcrumb works perfectly. I think the issue just happens outside REPL and in the real project Blazor. Can you use Visual Studio and create a new Blazor web app, using .net 8.0, interactive render mode is WebAssembly, then add the code in File Manager Overview? When you start the project, click on the breadcrumb. I think you can reproduce the issue.

### Response

**Hristian Stefanov** commented on 05 Jul 2024

Hi Hang, I carefully tested the example in a separate .NET 8 project, and the breadcrumb functionality works correctly on my end. If you are using .NET 8 interactivity per component in your project, ensure that all components are wrapped within the TelerikRootComponent. This is documented here: Using TelerikRootComponent with Per Page/Component Interactivity. You can have a look at it for more details. Please let me know if this applies to your case. Kind Regards, Hristian

### Response

**Hang** commented on 06 Jul 2024

Hi Hristian, I read the document and add IconType and EnableRtl to the TelerikRootComponent, the breadcrumb can work, but the url is changed (link is cleared and # is added). Do you know why and how to fix it? Current url: After click on breadcrumb: Regards, Hang Pham

### Response

**Hristian Stefanov** commented on 10 Jul 2024

Hi Hang, Thank you for getting back to me with additional information. I'm still unable to reproduce the "#" locally on my machine. Therefore, could you try to isolate the behavior in a runnable sample and send it to me for inspection? Kind Regards, Hristian

### Response

**Justin** commented on 30 Sep 2024

Dear Hristian, I, too, am experiencing issues with the breadcrumbs control when using the Telerik File Manager component. When implementing the PathChanged event handler, I see when clicking the items in the TreeView, the directory path is being correctly passed to the OnPathChanged handler. However, when clicking on items in the breadcrumb control, the patch passed to the OnPathChanged handler is empty. With regards to the URL being localhost:44369/#, this appears to be standard, as the same occurs when viewing the first sample on the following page: Blazor FileManager Overview - Telerik UI for Blazor This is a slightly frustrating issue; it would be great if someone had a fix. Regards, Justin

### Response

**Hristian Stefanov** commented on 01 Oct 2024

Hi Justin, I tried reproducing the problem using our overview demo, and it seems that clicking on the breadcrumb items correctly updates the newPath in the OnPathChanged handler. Here is the sample I used for testing: REPL link. Please run it and see if you get the same result. Kind Regards, Hristian

### Response

**Justin** commented on 02 Oct 2024

Hi Hristian, Thank you for your prompt response. The sample code also worked fine when running within my Blazor project. This indicated that something in my implementation was causing an issue. For my code, I accept a folder path as a parameter and then get a list of folders and files from this path. The path is based on the following format: "\\SERVERNAME\FOLDERNAME_1/FOLDERNAME_2" After troubleshooting, I realized the issue was related to the path starting with "\\". I was able to recreate the issue in the sample code by updating the path to start with "//", as listed below: private string RootPath { get; set; }="//root-folder-path"; private string DirectoryPath { get; set; }="//root-folder-path"; I guess the difference here is based on whether the web service runs in a Windows or Linux environment. As a workaround, I created a drive mapping. In my case, setting the RootPath to be as follows resolved the issue: "O:\FolderName_1\FolderName_2" P.S. Because I'm using backslashes, I created a verbatim string literal to avoid issues related to the \ being an escape character. So: private string RootPath { get; set; }=@"O:\FolderName_1\FolderName_2"; private string DirectoryPath { get; set; }=@"O:\FolderName_1\FolderName_2"; Regards, Justin

### Response

**Justin** commented on 03 Oct 2024

Hi Hristian, On reflection, the mapped drive option won't work as my website runs under a service account. Is there any option to enable the use of "\\" in the path? Regards, Justin

### Response

**Hristian Stefanov** commented on 03 Oct 2024

Hi Justin, I can confirm that the parameter is designed to accept " // " as a valid path, so replacing " \\ " is required at the moment. However, supporting " \\ " as well seems like a potential enhancement. I'll bring this up with our team and follow up with you by mid-next week at the latest to let you know if this feature can be implemented in the future. Kind Regards, Hristian

### Response

**Justin** commented on 04 Oct 2024

Thank you, Hristian. I will keep an eye out for this update. The file manager control is a perfect option for my project, so adding "\\" support would be great (if possible). Regards, Justin

### Response

**Hristian Stefanov** commented on 04 Oct 2024

Hi Justin, Just a quick update. I already forwarded the information to our team, and it is one of the main points for our next weekly meeting. Kind Regards, Hristian

### Response

**Hristian Stefanov** commented on 09 Oct 2024

Hi Justin, Following our meeting, the request for supporting "\\" has been validated as a good idea. I’ve gone ahead and submitted a feature request on your behalf to our Public Feedback Portal: FileManager Breadcrumb Support Double Backslash ("\\"). As the request’s creator, you are automatically subscribed and will receive email updates regarding its status in the future. Kind Regards, Hristian

### Response

**Justin** commented on 17 Oct 2024

Thank you, Hristian. I appreciate your support on this. I noticed the feature request has Hang listed as the submitter rather than myself. It's not an issue; I just wanted to point it out. Regards, Justin

### Response

**Hristian Stefanov** commented on 17 Oct 2024

Hi Justin, Thank you for pointing me out about the submitter. I did it by mistake, but it doesn't matter for the item. Kind Regards, Hristian

### Response

**Jason** commented on 19 Dec 2024

Is there a workaround for this?

### Response

**Hristian Stefanov** commented on 20 Dec 2024

Hi Jason, If we develop a workaround in the meantime before the feature is implemented, I will promptly share it in the public item 's comment section. Kind Regards, Hristian

### Response

**Jason** commented on 08 Jan 2025

Thank you for the explanation. However, wouldn't this be a bug not a feature? The Filemanager does not say its full functionality is only limited to unix servers and the breadcrumb function does not work with windows servers unless you are using a local file system which is probably not going to be the standard. Is there a way to hide the bread crumb?

### Response

**Hristian Stefanov** commented on 09 Jan 2025

Hi Jason, You can easily hide the breadcrumb using the CSS provided in the example below. As for why this is considered a feature rather than a bug: a bug implies that the functionality was intended to work with double backslashes but is currently broken. In this case, however, the functionality was never designed to support double backslashes, making it a missing feature rather than a defect. @using System.IO <style>.k-filemanager-content.k-breadcrumb { display: none;
} </style> <TelerikFileManager Data="@FileManagerData" @bind-Path="@DirectoryPath" Height="400px" OnCreate="@OnCreateHandler" OnUpdate="@OnUpdateHandler" OnModelInit="@OnModelInitHandler" OnDownload="@OnDownloadHandler" OnDelete="@OnDeleteHandler"> </TelerikFileManager> @code {
private List <FlatFileEntry> FileManagerData=new List <FlatFileEntry> ();

private string RootPath { get; set; }="root-folder-path";
private string DirectoryPath { get; set; }="root-folder-path";

private async Task OnCreateHandler(FileManagerCreateEventArgs args)
{
// the new item data is hardcoded for the purpose of the example
var newFolder=args.Item as FlatFileEntry;

var parent=GetParent(newFolder, DirectoryPath);

newFolder.Id=DirectoryPath + newFolder.Name.ToString();
newFolder.ParentId=parent !=null ? parent.Id : null;
newFolder.IsDirectory=true;
newFolder.HasDirectories=false;
newFolder.DateCreated=DateTime.Now;
newFolder.DateCreatedUtc=DateTime.Now;
newFolder.DateModified=DateTime.Now;
newFolder.DateModifiedUtc=DateTime.Now;
newFolder.Path=Path.Combine(DirectoryPath, newFolder.Name);
newFolder.Extension=null;

var parentDirectory=GetDirectory(DirectoryPath) ?? GetParent(newFolder, DirectoryPath);

if (parentDirectory !=null)
{
// simulate add in file system
newFolder.ParentId=parentDirectory.Id;
FileManagerData.Add(newFolder);
parentDirectory.HasDirectories=FileManagerData.Count(x=> x.ParentId==parentDirectory.Id)> 0;
}
else
{
// create a folder in the root dir
FileManagerData.Add(newFolder);
}

RefreshData();
}

private FlatFileEntry GetDirectory(string path)
{
var directory=FileManagerData.FirstOrDefault(x=> x.IsDirectory && x.Path==path);

return directory;
}

private FlatFileEntry GetParent(FlatFileEntry currItem, string currDirectory)
{
var parentItem=FileManagerData
.FirstOrDefault(x=> x.IsDirectory==true && x.Path==currDirectory);

return parentItem;
}

private async Task OnUpdateHandler(FileManagerUpdateEventArgs args)
{
var item=args.Item as FlatFileEntry;

if (item.IsDirectory)
{
// prevent renaming of directories. If you allow that, make sure
// to also update the Path of the children
}
else
{
// the name prop is updated, but update the path to the file as well
var name=item.Name ?? string.Empty;
var extension=item.Extension ?? string.Empty;
var fullName=extension.Length> 0 && name.EndsWith(extension) ?
name : $"{name}{extension}";

var updatedItem=FileManagerData.FirstOrDefault(x=> x.Id==item.Id);

updatedItem.Name=item.Name;
updatedItem.Path=Path.Combine(DirectoryPath, fullName);
Console.WriteLine(updatedItem.Path);
}
}

private async Task OnDownloadHandler(FileManagerDownloadEventArgs args)
{
var selectedItem=args.Item as FlatFileEntry;

//the Filemanager does not have the actual file.
//To download it, find the selected file through args.Item and
//assign the actual file to the argument as follows:

//args.Stream=the file stream of the actual selected file;
//args.MimeType=the mime type of the actual file, so it can be downloaded;
//args.FileName=allows overriding the name of the downloaded file;
}

private async Task OnDeleteHandler(FileManagerDeleteEventArgs args)
{
var currItem=args.Item as FlatFileEntry;

var itemToDelete=FileManagerData.FirstOrDefault(x=> x.Id==currItem.Id);

FileManagerData.Remove(itemToDelete);

RefreshData();
}

private FlatFileEntry OnModelInitHandler()
{
var item=new FlatFileEntry();
item.Name=$"New folder";
item.Size=0;
item.Path=Path.Combine(DirectoryPath, item.Name);
item.IsDirectory=true;
item.HasDirectories=false;
item.DateCreated=DateTime.Now;
item.DateCreatedUtc=DateTime.Now;
item.DateModified=DateTime.Now;
item.DateModifiedUtc=DateTime.Now;

return item;
}

private void RefreshData()
{
FileManagerData=new List <FlatFileEntry> (FileManagerData);
}

// fetch the FileManager data
protected override async Task OnInitializedAsync()
{
FileManagerData=await GetFlatFileEntries();
}

// a model to bind the FileManager. Should usually be in its own separate location.
public class FlatFileEntry
{
public string Id { get; set; }
public string ParentId { get; set; }
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
}

// the next lines are hardcoded data generation so you can explore the FileManager freely

private async Task<List <FlatFileEntry>> GetFlatFileEntries()
{

var workFiles=new FlatFileEntry()
{
Id="1",
ParentId=null,
Name="Work Files",
IsDirectory=true,
HasDirectories=true,
DateCreated=new DateTime(2022, 1, 2),
DateCreatedUtc=new DateTime(2022, 1, 2),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine(RootPath, "Work Files"),
Size=3 * 1024 * 1024
};

var Documents=new FlatFileEntry()
{
Id="2",
ParentId=workFiles.Id,
Name="Documents",
IsDirectory=true,
HasDirectories=false,
DateCreated=new DateTime(2022, 1, 2),
DateCreatedUtc=new DateTime(2022, 1, 2),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine(workFiles.Path, "Documents"),
Size=1024 * 1024
};

var Images=new FlatFileEntry()
{
Id="3",
ParentId=workFiles.Id,
Name="Images",
IsDirectory=true,
HasDirectories=false,
DateCreated=new DateTime(2022, 1, 2),
DateCreatedUtc=new DateTime(2022, 1, 2),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine(workFiles.Path, "Images"),
Size=2 * 1024 * 1024
};

var specification=new FlatFileEntry()
{
Id="4",
ParentId=Documents.Id,
Name="Specification",
IsDirectory=false,
HasDirectories=false,
Extension=".docx",
DateCreated=new DateTime(2022, 1, 5),
DateCreatedUtc=new DateTime(2022, 1, 5),
DateModified=new DateTime(2022, 2, 3),
DateModifiedUtc=new DateTime(2022, 2, 3),
Path=Path.Combine(Documents.Path, "specification.docx"),
Size=462 * 1024
};

var report=new FlatFileEntry()
{
Id="5",
ParentId=Documents.Id,
Name="Monthly report",
IsDirectory=false,
HasDirectories=false,
Extension=".xlsx",
DateCreated=new DateTime(2022, 1, 20),
DateCreatedUtc=new DateTime(2022, 1, 20),
DateModified=new DateTime(2022, 1, 25),
DateModifiedUtc=new DateTime(2022, 1, 25),
Path=Path.Combine(Documents.Path, "Monthly report.xlsx"),
Size=538 * 1024
};

var dashboardDesign=new FlatFileEntry()
{
Id="6",
ParentId=Images.Id,
Name="Dashboard Design",
IsDirectory=false,
HasDirectories=false,
Extension=".png",
DateCreated=new DateTime(2022, 1, 10),
DateCreatedUtc=new DateTime(2022, 1, 10),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(Images.Path, "Dashboard Design.png"),
Size=1024
};

var gridDesign=new FlatFileEntry()
{
Id="7",
ParentId=Images.Id,
Name="Grid Design",
IsDirectory=false,
HasDirectories=false,
Extension=".jpg",
DateCreated=new DateTime(2022, 1, 12),
DateCreatedUtc=new DateTime(2022, 1, 12),
DateModified=new DateTime(2022, 2, 13),
DateModifiedUtc=new DateTime(2022, 2, 13),
Path=Path.Combine(Images.Path, "Grid Design.jpg"),
Size=1024
};

var files=new List <FlatFileEntry> ()
{
workFiles,

Documents,
specification,
report,

Images,
dashboardDesign,
gridDesign
};

return files;
}
} Kind Regards, Hristian

### Response

**Justin** commented on 09 Jan 2025

Hi Hristian, Thank you for providing the CSS to hide the breadcrumb. I will test this out and see if I want to use it until the feature has been implemented. Out of interest, do you think it would make sense to add a parameter to the TelerikFileManager to hide the breadcrumb if not required? Something like HideBreadcrumb="true," with the default being HideBreadcrumb="false." Regards, Justin

### Response

**Hristian Stefanov** commented on 10 Jan 2025

Hi Justin, I don’t believe a dedicated parameter for hiding the breadcrumb is necessary, as it can already be accomplished easily with just a single line of CSS. Adding such a parameter wouldn’t simplify the process for developers but would unnecessarily expand the API. Kind Regards, Hristian

### Response

**Justin** commented on 10 Jan 2025

Hi Hristian. Thank you for the reply. I understand the logic, and that thought crossed my mind. As you mentioned, the CSS is simple, as long as I remember it! haha Regards, Justin
