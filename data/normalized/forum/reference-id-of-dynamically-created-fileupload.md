# reference ID of dynamically created fileupload

## Question

**And** asked on 29 Nov 2022

I have a blazor server script that dynamically generates several TelerikUpload controls to upload documents for different purposes. All controls use the same OnSelect function to handle the uploaded file. when a user uploads a file using one of these controls, I need the OnSelect or onUpload function to rename the uploaded file based on which TelerikUpload control was triggered. How can I reference the ID of the dynamically generated TelerikUpload that triggered the OnSelect or onUpload function so that I can rename the file as needed? Thank you!

## Answer

**Svetoslav Dimitrov** answered on 02 Dec 2022

Hello Andres, As this is a public forum, I would like to spread the solution from our private discussion so more people can benefit from it here. You can use a lambda expression for the OnSelect event to provide some additional information that would allow you to differentiate the exact component. Below, I have added a very basic example, where I loop through a List of ints that represents the IDs: @foreach ( int id in ListOfIds)
{
<TelerikUpload OnSelect="@((UploadSelectEventArgs e)=> OnSelectHandler(e, id))">
</TelerikUpload>
}

@code { private List <int> ListOfIds { get; set; }=new List<int>()
{ 1, 2, 3 }; async Task OnSelectHandler ( UploadSelectEventArgs e, int id ) { // cancel the event on some condition - more than two new files are added if (e.Files.Count> 2 )
{
e.IsCancelled=true;
} foreach ( var item in e.Files)
{
Console.WriteLine( $"OnSelect: {item.Name} " );
}
}
} Regards, Svetoslav Dimitrov Progress Telerik
