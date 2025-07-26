# Renaming a newly created folder, keeps the old folder and creates a new folder with the new name FileManager

## Question

**Tas** asked on 17 Apr 2025

Hi Team, Steps: 1. Click on New folder and create a new folder with name "ABC" (OnCreateHandler method is called to which is attached to OnCreate event) 2. Right click on folder "ABC" and click on rename and rename it as "XYZ" 3. On enter click, it retains the old folder "ABC" and creates a new folder with name "XYZ". (Again OnCreateHandler method is called instead of OnUpdateHandler) Can you please help me understand if it is a bug with FileManager or is something wrong at my end. <TelerikFileManager @ref="FileManagerRef" Data="@FileManagerData" @bind-Path="@DirectoryPath" IdField="MyModelId" Height="400px" NameField="Name" PathField="Path" ExtensionField="Extension" IsDirectoryField="IsDirectory" HasDirectoriesField="HasDirectories" DirectoriesField="MyDirectories" ItemsField="Items" SelectedItems="@SelectedItems" SelectedItemsChanged="@((IEnumerable<HierarchicalFileEntry> selectedFiles)=> OnSelect(selectedFiles))" OnCreate="@OnCreateHandler" OnUpdate="@OnUpdateHandler" OnDelete="@OnDeleteHandler" />

## Answer

**Tsvetomir** answered on 22 Apr 2025

Hi Tasnim, Thank you for the provided information about your scenario. The described behavior seems to be related to a known bug in the FileManager component that has already been fixed in our latest version (8.1.1). To test the behavior in the latest version that includes the fix, I've prepared a REPL example for you. To benefit from that fix, I recommend upgrading to our latest version. I hope the provided information serves you well. Regards, Tsvetomir Progress Telerik
