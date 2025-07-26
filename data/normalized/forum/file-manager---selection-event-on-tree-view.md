# File manager - Selection event on tree view

## Question

**Han** asked on 18 Sep 2024

Hi. I have a requirement I'm stumped with. I want to get the folder name when click on the tree view. I found that Telerik has SelectedItemsChanged but it only works for the files/folders on content view. I can't think of any way to do this - is it possible? Thanks, Hang Pham

### Response

**Hang** commented on 19 Sep 2024

[https://demos.telerik.com/blazor-ui/filemanager/selection](https://demos.telerik.com/blazor-ui/filemanager/selection) I attached the link demo for clearer

## Answer

**Dimo** answered on 20 Sep 2024

Hello Hang, Please use the FileManager PatchChanged event. It fires when the user clicks on TreeView items. See the FileManager Events example. Regards, Dimo Progress Telerik
