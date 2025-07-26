# Breadcrumb does not show the complete path FileManager

## Question

**Tas** asked on 11 Apr 2025

Hi Team, In my application, on page initialization I have to set the default path for FileManager (It can be any nested path in the root folder depending on the selection from user). After setting the path on OnInitialized, it opens the relevant path but the breadcrumb does not show the complete path. My path is: Home/FileStorage/Folder2 Current: Expected: My code: <TelerikFileManager @ref="FileManagerRef" Data="@FileManagerData" Path="@DirectoryPath" Height="400px" NameField="Name" PathField="Path" ExtensionField="Extension" IsDirectoryField="IsDirectory" HasDirectoriesField="HasDirectories" DirectoriesField="MyDirectories" ItemsField="Items" SelectedItems="@SelectedItems" SelectedItemsChanged="@((IEnumerable<HierarchicalFileEntry> selectedFiles)=> OnSelect(selectedFiles))" OnModelInit="@OnModelInitHandler" OnCreate="@OnCreateHandler" PathChanged="@OnPathChanged" /> protected override void OnInitialized () {
DirectoryPath="Home/FileStorage/Folder2" }

## Answer

**Anislav** answered on 11 Apr 2025

I tried an example where I set the Path of the FileManager to a nested subfolder, and it worked as expected. Here's a link to the example: [https://blazorrepl.telerik.com/mJOePFkq49hTLc0g33](https://blazorrepl.telerik.com/mJOePFkq49hTLc0g33) My assumption is that there might be a mismatch in the folder names or path structure on your end. Regards, Anislav Atanasov

### Response

**Tasnim** commented on 11 Apr 2025

I have checked the path it is correct. Also I have also tried doing the exact same way as you did in your sample. Still getting the same issue. One observation I had is that after the screen is loaded, if I click on the main folder in the left-hand side TreeView then the correct path reflects on breadcrumb. Can you guide me if I can do something using this?

### Response

**Anislav** commented on 11 Apr 2025

I see that you have a handler for the PathChanged event—there may be an issue with its implementation. You can prepare a minimal example of your code that reproduces the issue and share it via [https://blazorrepl.telerik.com/](https://blazorrepl.telerik.com/) so we can better evaluate what might be going wrong. Otherwise, it's difficult to guess the cause. In any case, it does seem likely to be related to your implementation. Regards, Anislav Atanasov

### Response

**Tasnim** commented on 11 Apr 2025

Its taking time to update the UI. I have added Task.Delay and then StateHasChanged() to fix this. Thanks for your help.
