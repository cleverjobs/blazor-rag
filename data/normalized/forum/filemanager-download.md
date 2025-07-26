# FileManager Download

## Question

**ITIT** asked on 02 Jul 2024

Could you please provide an actual implementation (not just a dummy implementation) of how to download a file with the FileManager (FlatFileService only)? Specifically, how do you read for example a .pdf file into a stream within the DownloadAsync(FileManagerDownloadEventArgs args) method? My problem is that everytime I call something like File.ReadAllBytes(item.Path), it halts unexpectedly and does not continue the processing, thus leaving me in a loading loop. Cheers!

## Answer

**Dimo** answered on 04 Jul 2024

Hello, My assumption is that the item.Path in ReadAllBytes() is incomplete. Probably the app needs to combine the file path with some base path in order to produce the full path to the file that starts from the file system root. A good exercise is to experiment and read the file contents of any file on the file system, because the required implementation is not related to the FileManager component. The code below works in a Blazor Server app and uses the files inside wwwroot. @using Microsoft.AspNetCore.StaticFiles
@using System.IO

@inject NavigationManager NavigationManager

<h2>Flat Data</h2> <p> Path: @FlatDirectoryPath </p> <TelerikFileManager Data="@FlatData" @bind-Path="@FlatDirectoryPath" NameField="@(nameof(FileEntry.Name))" SizeField="@(nameof(FileEntry.Size))" PathField="@(nameof(FileEntry.Path))" ExtensionField="@(nameof(FileEntry.Extension))" IsDirectoryField="@(nameof(FileEntry.IsDirectory))" HasDirectoriesField="@(nameof(FileEntry.HasDirectories))" DateCreatedField="@(nameof(FileEntry.DateCreated))" DateCreatedUtcField="@(nameof(FileEntry.DateCreatedUtc))" DateModifiedField="@(nameof(FileEntry.DateModified))" DateModifiedUtcField="@(nameof(FileEntry.DateModifiedUtc))" ParentIdField="@(nameof(FlatFileEntry.ParentId))" OnDownload="@OnFileManagerDownload" Height="350px"> </TelerikFileManager> @code {
private string FlatDirectoryPath { get; set; }=string.Empty;

private List<FlatFileEntry> FlatData { get; set; }=new List<FlatFileEntry>();

private const int ActionDelay=1;

private static string StartPath { get; set; }=null!;

private async Task OnFileManagerDownload ( FileManagerDownloadEventArgs args ) { var file=(FileEntry)args.Item; var filePathWithoutStartSeparator=file.Path.IndexOf(Path.DirectorySeparatorChar)==0? file.Path.Substring( 1 ) : file.Path; var fullFilePath=Path.Combine(StartPath, filePathWithoutStartSeparator); var fileBytes=await System.IO.File.ReadAllBytesAsync(fullFilePath); var fileStream=new MemoryStream(fileBytes);

args.FileName=file.Name;
args.Stream=fileStream;
args.MimeType="application/octet-stream"; // default var mimeProvider=new FileExtensionContentTypeProvider();
string? mimeType;
mimeProvider.TryGetContentType(file.Extension, out mimeType); if (! String.IsNullOrEmpty(mimeType))
{
args.MimeType=mimeType;
}
}

protected override async Task OnInitializedAsync ( ) { StartPath=Path.Combine(Directory.GetCurrentDirectory(), "wwwroot" ); await LoadFlatDataAsync(); await base.OnInitializedAsync();
}

#region Flat File Data

private async Task LoadFlatDataAsync ( ) { if (FlatData==null || FlatData.Count==0 )
{
FlatData=await ReadFlatDataAsync();
}
}

private async Task<List<FlatFileEntry>> ReadFlatDataAsync ( ) { await Task.Delay(ActionDelay); return ReadCustomFlatData();
}

public List<FlatFileEntry> ReadCustomFlatData ( ) { var entries=new List<FlatFileEntry>(); var rootPath=Path.Combine(StartPath); var rootDirectory=new DirectoryInfo(rootPath); var files=rootDirectory.EnumerateFiles();
foreach ( var file in files)
{ var entry=ConvertToFlatEntry(file, null );
entries.Add(entry);
} var directories=rootDirectory.EnumerateDirectories();
foreach ( var directory in directories)
{
PopulateFlatEntryItemsRecursive(entries, directory, null );
} return entries;
}

private void PopulateFlatEntryItemsRecursive ( List<FlatFileEntry> entries, DirectoryInfo directoryInfo, string? parentId ) { var directoryEntry=ConvertToFlatEntry(directoryInfo, parentId);
entries.Add(directoryEntry); var files=directoryInfo.EnumerateFiles();

foreach ( var file in files)
{ var entry=ConvertToFlatEntry(file, directoryEntry.Id);
entries.Add(entry);
} var directories=directoryInfo.EnumerateDirectories();

foreach ( var directory in directories)
{
PopulateFlatEntryItemsRecursive(entries, directory, directoryEntry.Id);
}
}

private static FlatFileEntry ConvertToFlatEntry ( DirectoryInfo directory, string? parentId ) { var entry=new FlatFileEntry ( ) {
ParentId=parentId,
Name=directory.Name,
IsDirectory=true,
HasDirectories=directory.GetDirectories().Count()> 0,
DateCreated=directory.CreationTime,
DateCreatedUtc=directory.CreationTimeUtc,
DateModified=directory.LastWriteTime,
DateModifiedUtc=directory.LastWriteTimeUtc, // trim the real path to avoid exposing it Path=directory.FullName.Substring(directory.FullName.IndexOf(StartPath) + StartPath.Length),
Extension=directory.Extension,
Size=2 * 1024 * directory.GetFiles().LongCount()
}; return entry;
}

private static FlatFileEntry ConvertToFlatEntry ( FileInfo file, string? parentId ) { var entry=new FlatFileEntry ( ) {
ParentId=parentId,
Name=Path.GetFileNameWithoutExtension(file.FullName),
IsDirectory=false,
HasDirectories=false,
DateCreated=file.CreationTime,
DateCreatedUtc=file.CreationTimeUtc,
DateModified=file.LastWriteTime,
DateModifiedUtc=file.LastWriteTimeUtc, // trim the real path to avoid exposing it Path=file.FullName.Substring(file.FullName.IndexOf(StartPath) + StartPath.Length),
Extension=file.Extension,
Size=file.Length
}; return entry;
}

#endregion Flat File Data

#region Class Definitions

public class FlatFileEntry: FileEntry {
public string? ParentId { get; set; }
}

public class FileEntry {
public string Id { get; set; }=Guid.NewGuid().ToString();

public string Name { get; set; }=null!;

public long Size { get; set; }

public string Path { get; set; }=null!;

public string Extension { get; set; }=string.Empty;

public bool IsDirectory { get; set; }

public bool HasDirectories { get; set; }

public DateTime DateCreated { get; set; }

public DateTime DateCreatedUtc { get; set; }

public DateTime DateModified { get; set; }

public DateTime DateModifiedUtc { get; set; }
}

#endregion Class Definitions
} Regards, Dimo Progress Telerik
