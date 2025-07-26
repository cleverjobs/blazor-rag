# FileManager OnRead Event

## Question

**TimTim** asked on 15 May 2023

[https://docs.telerik.com/blazor-ui/components/filemanager/events#read-event](https://docs.telerik.com/blazor-ui/components/filemanager/events#read-event) The documentation says the event can be used "for example, to retrieve only a small number of items to improve the backend performance." This is exactly the scenario I have with many files and folders. However, the event only seems to fire one time when the control is initialized. What is the purpose of this event, since data can be read programmatically with the OnInitializedAsync or OnModelInit events? Is there any way to set the data to the current path's folders/files and use the read event when the user navigates (up or down) to a new folder? Thanks

## Answer

**Nadezhda Tacheva** answered on 18 May 2023

Hi Tim, You are correct, at this stage, the OnRead event does not cover all possible scenarios for a true load on demand. In a future version of UI for Blazor, we will update the component to fire OnRead event upon more user actions such as changing the path or expanding the TreeView. Then, it will be possible to handle the event to pass only the set of items that are relevant for the chosen directory, for example. You may track the progress of this enhancement here: Trigger OnRead event for more actions. I added your vote there to increase the popularity of the item as we prioritize the requests based on the community demand and we use the gathered votes to evaluate that. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Tim** commented on 18 May 2023

Thank you!
