# How to create new file in Blazor FileManager

## Question

**Tas** asked on 07 Apr 2025

Hi Team, I know that we can create a new folder in Blazor FileManager using OnModelInit and OnCreate. But in my application, I want to have 2 buttons: 1 for New Folder and other for New file. Is there a way to achieve it? I have already tried using below code. But I do not get the popup for New File: <FileManagerToolBarCustomTool> <TelerikButton OnClick="@(()=>OnModelInitHandler("file"))">New File</TelerikButton> </FileManagerToolBarCustomTool> <FileManagerToolBarCustomTool> <TelerikButton OnClick="@OnNewFileClicked"> New File </TelerikButton> </FileManagerToolBarCustomTool> private void OnNewFileClicked () { var item=new HierarchicalFileEntry();
item.Name=$"New file";
item.Size=0;
item.Extension=".json";
item.Path=Path.Combine(DirectoryPath, item.Name);
item.IsDirectory=false;
item.HasDirectories=false;
}

## Answer

**Anislav** answered on 07 Apr 2025

You should not call the OnModelInit handler directly. OnModelInit is an event triggered by the FileManager when a new file or folder is about to be created by the FileManager, allowing you to modify its properties before it's added. Instead, for your custom button, you should handle its OnClick event, create a new HierarchicalFileEntry instance, add it to the data source bound to the FileManager, and then notify the FileManager to refresh (rebind) its data. I’ve prepared a sample demonstrating this approach: [https://blazorrepl.telerik.com/wzOyErli00JOqWJL22](https://blazorrepl.telerik.com/wzOyErli00JOqWJL22) Regards, Anislav Atanasov

### Response

**Anislav** commented on 08 Apr 2025

Tasnim, does the proposed solution work for you?

### Response

**Tasnim** commented on 08 Apr 2025

It worked. But now when I try to rename that file, the OnUpdate event is not triggered. So I am unable to rename it. Can you help me with this?

### Response

**Anislav** commented on 08 Apr 2025

I gave it a try, and the OnUpdate event is fired successfully, triggering its handler. It can be implemented like this: private async Task OnUpdateHandler ( FileManagerUpdateEventArgs args ) { var item=args.Item as HierarchicalFileEntry; var name=item.Name ?? string.Empty; var extension=item.Extension ?? string.Empty; var fullName=extension.Length> 0 && name.EndsWith(extension) ?
name : $" {name} {extension} "; var updatedItem=FileManagerData.FirstOrDefault(x=> x.MyModelId==item.MyModelId);

updatedItem.Name=item.Name;
updatedItem.Path=Path.Combine(DirectoryPath, fullName);
} Here is a complete example: [https://blazorrepl.telerik.com/mfkoOMbO45LOcgNZ07](https://blazorrepl.telerik.com/mfkoOMbO45LOcgNZ07) Regards, Anislav Atanasov

### Response

**Anislav** commented on 23 Apr 2025

Were you able to get it working?

### Response

**Tasnim** commented on 24 Apr 2025

Yes its working. Thank you for the help
