# Search any file in the nested folders of selected folder in FileManager blazor

## Question

**Tas** asked on 09 Apr 2025

Hi Team, Currently I can only search files in the current selected folder. But is there a way to search any file in the nested folders of selected folder in FileManager blazor?

## Answer

**Anislav** answered on 09 Apr 2025

Yes, the built-in search functionality in the FileManager only filters files within the currently selected folder. The current folder is reflected in both the tree view on the left and the breadcrumb navigation at the top. The contents of this folder are always displayed. With that in mind, how would you expect the FileManager to behave when multiple files with the same name are found in different folders? Displaying contents from multiple folders simultaneously is not supported. A possible alternative is to implement a custom search tool with an autocomplete textbox. As the user types, you could display a list of matching files from all folders, along with their full paths. When a file is selected, you can programmatically update the FileManager’s Path to the file’s folder and either: Pre-select the file using the SelectedItems property, or Filter the displayed contents by excluding other files in the directory via the FileManager's Data property. Regards, Anislav Atanasov

### Response

**Dimo** answered on 09 Apr 2025

Hello Tasnim, The FileManager persists the search string when the user navigates from one folder to another, so that only the matching items display. You may be expecting all search results to show in the same view ("folder") like in desktop file explorers, but I am afraid this is not how the component is designed. On a side note, please ask the license holder at your company to assign you one of the available Telerik licenses. This will: Make your account compliant with our license agreement. Allow you to download and use your own license key. Allow you to access to technical support by Telerik. The third bullet item is optional, but the first item is required. The second one is required if you are using Telerik UI for Blazor version 8.x. Regards, Dimo

### Response

**Anislav** commented on 09 Apr 2025

Dimo, The FileManager does not search in all folders. It searches only within the current folder, as stated in the documentation: Telerik FileManager Search. I also reviewed the component's code, and it confirms the behavior described in the documentation. Regards, Anislav Atanasov

### Response

**Dimo** commented on 09 Apr 2025

@Anislav - right, my previous statement was misleading, so I reworded it.
