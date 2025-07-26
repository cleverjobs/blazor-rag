# FileManager: support for multiple directories for single file

## Question

**Len** asked on 27 Mar 2023

Hi, I was hoping to use the FileManager component as a visual representation of a file hierarchy which is based on categories, instead of actual directories in a file system. From the examples I'm currently not able to figure out how to support a single file being part of multiple hierarchies. The features I'm hoping to implement through the FileManager component: 1. If my file has multiple categories/directories associated with it, I want the same file to be listed under each single category/directory. 2. If a directory is selected in the FileManager TreeView, I want the List/Grid to show all files under that directory and it's sub folders. I don't want to see the sub folders as icons in the Grid/List. Any ideas/examples on how to accomplish this? Kind regards.

## Answer

**Dimo** answered on 30 Mar 2023

Hello Lennert, The first point is achievable, if you add the same file item in multiple places in the FileManager Data inside different "folders" (categories). The second point is unclear to me, as it seems to contradict itself - "I want the List/Grid to show all files under that directory and it's sub folders. I don't want to see the sub folders as icons in the Grid/List. " If you meant to say "I don't want to see the sub folders in the TreeView", that's not possible, because the TreeView data and the Grid/ListView data must be consistent. In any case, the FileManager is designed to visualize file and folder structures. Any abstraction that is not exactly the same thing, must be adjusted to mimic an actual file system. Regards, Dimo Progress Telerik

### Response

**Lennert** commented on 31 Mar 2023

Hi Dimo, Thanks for your reaction. With point 2, I mean: The Treeview should show only folders. The Grid/List should show only files. If I select a folder in the Treeview, I want to see the complete collection of files from that subhierarchy (so the selected folder and all subfolders combined) in the Grid/List. That way only the Treeview is used to navigate the hierarchy. Like I mentioned, the hierarchy is more based on categories then on a file structure. I'm aware that what I'm asking isn't the default behavior of the component as it is designed like a File Explorer. I guess I can work out my own implementation by using the separate Treeview and grid/list components. Kind regards, Lennert

### Response

**Dimo** commented on 31 Mar 2023

Indeed, I also think it will be easier and better to assemble the TreeView, ListView and Grid "pieces" together with the required business logic, rather than "hack" the FileManager component.
