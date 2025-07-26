# FileManager Virtual Loading

## Question

**And** asked on 20 May 2022

Hello, Is there any way to load the data in the FileManager control virtually. I would prefer to not have to traverse the entire file system to provide the folder/file structure. Can the OnRead method be used to provide just the data needed for the current view? Thank You, -Andy

## Answer

**Stamo Gochev** answered on 25 May 2022

Hello, The "OnRead" handler can be used for achieving a final result similar to virtual loading. Another approach is to change the "Data" collection on some actions like when the "PathChanged" event is triggered (e.g. navigation). In general, the FileManager does not need to load all the data as it only displays a view for a certain folder only and a particular level for the treeview, thus you can limit the data in such a way that suits your needs. If you are looking for a specific way of virtualization (e.g. virtualizing the navigation treeview separately from the list/grid), can you elaborate more on the expected final result? Is there a demo (even from a 3rd-party source) that you can show, where I can check out the expected behavior? You can also send a REPL example with your current configuration if the above is not possible, so I can have a look at what is not working and make further suggestions. Regards, Stamo Gochev

### Response

**Smita** commented on 20 Sep 2022

We also have same requirement. We want to show child files when user clicks on folder. Can you provide sample code to implement PathChanged event you mentioned above?

### Response

**Stamo Gochev** commented on 23 Sep 2022

The main idea behind using the "PathChanged" event is to get a hook for when a new folder is selected (clicked) and set new data to the "Data" parameter of the FileManager. Here is a sample snippet that illustrates this: <TelerikFileManager Height="400px" Data="@Data" Path="@DirectoryPath" PathChanged="@OnPathChanged" ...>
</TelerikFileManager>

@code { public string DirectoryPath { get; set; } public void OnPathChanged ( string newPath ) {
DirectoryPath=newPath; // custom implementation here var newData=ProcessData(newPath); ... Data=newData;

StateHasChanged();
}
} The "ProcessData" method is expected to contain a custom implementation of how the new data is obtained based on the changed file path. Note that this implementation is dependent on whether hierarchical or flat data binding is used, so I cannot provide a generic example. In addition, the concrete code might depend on other factors (e.g. how you operate with the file system), but you can try the concept and adapt it to your specific needs.
