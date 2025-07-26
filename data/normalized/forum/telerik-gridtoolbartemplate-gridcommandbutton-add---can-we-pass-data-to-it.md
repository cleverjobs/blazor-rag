# Telerik GridToolBarTemplate GridCommandButton Add - Can we pass data to it?

## Question

**Gle** asked on 20 Dec 2024

I have a TelerikGrid that the first column will open a TelerikWindow with a TelerikUpload. This is so that the user can upload files to the server that will be associated with the object. The object being edited has values that depend on the file being uploaded. For example, the file being uploaded has a File Name. If the File Name already exists, I want to change the name of the file currently being uploaded to include the Revision number at the end of the file name. For example, we have a file on the server named TestFile.pdf, and I am uploading a file named TestFile.pdf. If TestFile.pdf exists, I want to check what the revision of the TestFile.pdf that's already uploaded is, and add it to the end of the file name (TestFile_rev0.pdf). That part is simple, because it's just manipulation of the saved file on the server. However, the new file being uploaded I want to then change the name of it to TestFile_rev1.pdf, and I can do that and save it to the server, but the object in the grid that's currently being added, I need to pass the data to that object being edited, however it will not pass the data. How can we do that? @page "/SDS"

@using SafetySite.Models;
@using Helpers

@inject SDSModel SDSModel
@inject UserModel UserModel
@inject NavigationManager NavigationManager <PageTitle> Safety Data Sheets </PageTitle> <TelerikGrid Data=@SDSItemsList FilterMode="GridFilterMode.FilterMenu" Sortable="true" EditMode="GridEditMode.Inline" Height="2000px"> <GridToolBarTemplate> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus" Enabled="@UserModel.CanEdit()"> Add SDS Sheet </GridCommandButton> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@(nameof(SDSModel.FileExists))" Title="File" Width="120px"> <EditorTemplate> @{
var item=context as SDSModel;
if(item !=null)
{ <TelerikButton OnClick="@(()=> ToggleUploadWindow(item))" Icon="@SvgIcon.Upload" Class="btn btn-sm btn-primary"> Upload File </TelerikButton> }
} </EditorTemplate> <Template> @{
var item=context as SDSModel;
if(item !=null)
{ <div class="text-center"> <TelerikButton OnClick="@(()=> NavigateToViewSDSFile(item.FileName!))" Class="navlinkgrow"> <div class="navlink-content"> <span class="@(item.FileExists ? " text-success ": " text-danger ")"> <i class="fa-duotone fa-solid fa-file-pdf fa-2x"> </i> </span> </div> </TelerikButton> </div> }
} </Template> </GridColumn> <GridColumn Field="@nameof(SDSModel.Title)" Title="Title" Editable="true" /> <GridColumn Field="@nameof(SDSModel.Revision)" Title="Revision" Editable="true" /> <GridColumn Field="@nameof(SDSModel.CurrentVersion)" Title="CurrentVersion" Editable="true"> <Template> @{
var item=context as SDSModel;
if (item !=null)
{ <input type="checkbox" checked="@item.CurrentVersion" disabled /> }
} </Template> </GridColumn> <GridColumn Field="@nameof(SDSModel.CreatedBy)" Title="Created By" Editable="false" /> <GridColumn Field="@nameof(SDSModel.EditedBy)" Title="Edited By" Editable="false" /> <GridColumn Field="@nameof(SDSModel.CreationDate)" Title="Creation Date" DisplayFormat="{0:yyyy-MM-dd}" Editable="false" /> <GridColumn Field="@nameof(SDSModel.EditedDate)" Title="Edit Date" DisplayFormat="{0:yyyy-MM-dd}" Editable="false" /> <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true" Enabled="@UserModel.CanEdit()" OnClick="@OnUpdate"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil" Enabled="@UserModel.CanEdit()"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="@SvgIcon.Trash" Enabled="@UserModel.CanEdit()" OnClick="@OnDelete"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true" Enabled="@UserModel.CanEdit()"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @* THIS TELERIK WINDOW OPENS A POPUP OF A TELERIK FILE MANAGER THAT ALLOWS FOR THE INDIVIDUAL TO PLACE A PDF ASSOCIATED WITH THAT ITEM INTO THE FOLDER *@<TelerikWindow Width="400px" Height="fit-content" Centered="true" @bind-Visible="@IsUploadFileWindowVisible"> <WindowTitle> <strong> Upload SDS File </strong> </WindowTitle> <WindowActions> <WindowAction Name="Close" OnClick="@(()=> IsUploadFileWindowVisible=!IsUploadFileWindowVisible)" /> </WindowActions> <WindowContent> <TelerikUpload Multiple="false" SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" OnSuccess="@OnFileUploadSuccess" AllowedExtensions="@AllowedExtensions" MaxFileSize="10485760" /> </WindowContent> </TelerikWindow> @code { private bool IsUploadFileWindowVisible { get; set; }=false; private List<SDSModel> SDSItemsList=new (); private SDSModel? CurrentItem { get; set; }=new SDSModel(); private List<string> AllowedExtensions=new List<string> { ".pdf" }; private bool CanSaveUpload { get; set; }=false; private string SaveUrl=String.Empty; private string RemoveUrl=String.Empty; public void ToggleUploadWindow ( SDSModel item ) {
CurrentItem=item;
SaveUrl=$" {NavigationManager.BaseUri} api/Upload/SavePdf?rev={item.Revision} ";
RemoveUrl=$" {NavigationManager.BaseUri} api/Upload/RemovePdf";
IsUploadFileWindowVisible=!IsUploadFileWindowVisible;
} private void NavigateToViewSDSFile ( string fileName ) { if (! string.IsNullOrEmpty(fileName))
{ string fileUrl=$"/SafetyDataSheets/ {fileName} ";
NavigationManager.NavigateTo(fileUrl, forceLoad: true );
} else {
Console.WriteLine( "No document found for the specified file name." );
}
} private async Task OnFileUploadSuccess ( UploadSuccessEventArgs args ) { if (CurrentItem !=null && args.Files.Count> 0 )
{ var uploadedFile=args.Files[ 0 ]; string fileName=uploadedFile.Name; // Check if a file with the same name already exists in the database bool fileExists=await SDSModel.FileExistsAsync(fileName); if (fileExists)
{ var existingItem=await SDSModel.GetSDSItemByFileNameAsync(fileName); if (existingItem !=null )
{
existingItem.CurrentVersion=false; await SDSModel.UpdateOldSDSItemAsync(existingItem.FileName, UserModel.EmployeeID);

CurrentItem.Revision=existingItem.Revision + 1;
fileName=$" {Path.GetFileNameWithoutExtension(uploadedFile.Name)} _rev {CurrentItem.Revision} {Path.GetExtension(uploadedFile.Name)} ";
}
}

CurrentItem.FileName=fileName;
CurrentItem.FileExists=true;
CurrentItem.CurrentVersion=true;
}
} private async Task OnUpdate ( GridCommandEventArgs args ) { var item=args.Item as SDSModel; if (item !=null )
{
item.EditedBy=UserModel.EmployeeID; await SDSModel.SaveSDSItemAsync(item);
SDSItemsList=await SDSModel.GetSDSItemsAsync();
}
} private async Task OnDelete ( GridCommandEventArgs args ) { var item=args.Item as SDSModel; if (item !=null )
{ await SDSModel.DeleteSDSItemAsync(item);
SDSItemsList=await SDSModel.GetSDSItemsAsync();
}
} protected override async Task OnInitializedAsync () {
SDSItemsList=await SDSModel.GetSDSItemsAsync(); await base.OnInitializedAsync();
}

}

## Answer

**Glenn** answered on 23 Dec 2024

I was able to solve this problem. I realized that my CurrentItem was working as expected after some additional testing.

### Response

**Hristian Stefanov** commented on 24 Dec 2024

Hi Glenn, I'm glad to hear that you have quickly resolved the matter on your own. Thank you for sharing how things turned out publicly so other developers in the same situation can benefit from this. Kind Regards, Hristian
