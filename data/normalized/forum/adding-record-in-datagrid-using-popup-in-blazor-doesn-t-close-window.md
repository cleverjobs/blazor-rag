# Adding record in DataGrid using Popup in Blazor doesn't close window

## Question

**TT** asked on 08 Aug 2024

Dear, I have a small test application that uses the telerik DataGrid in Blazor. For adding records to the dataGrid I use the Popup window. When doing that and pressing the "update" button once, the popup window doesn't close but my record has been added and the reload of the DataGrid has happend. Why doesn't it close ? Kind Regards

### Response

**Dimo** commented on 08 Aug 2024

Hello, please compare your setup with the one in our Grid Popup Editing documentation examples and also Grid Popup Editing online demo. Are you using a separate custom popup for the edit form? If yes, you need to close it manually. If you need further assistance, please send us a small runnable example for inspection. Also, ask the license holder at your company to assign you a license. This will make your Telerik account compliant with our license agreement, and you also will be able to submit support tickets when necessary.

### Response

**T** commented on 09 Aug 2024

Hi Dimo, I created my test based on the example from the site(Grid Popup Editing documentation examples -> Basics). Also good to know is that when click the "update" button a second time. He tries to add it again. Kind Regards Thomas

### Response

**Dimo** commented on 09 Aug 2024

Thomas, please send a small runnable example for inspection.

### Response

**T** commented on 09 Aug 2024

Hi Dimo, Can you tell me on what the "Add record" popup waits for closing ? Kind Regards.

### Response

**Dimo** commented on 09 Aug 2024

@Thomas Here is how it works: The Grid has built-in commands buttons. The command buttons can execute built-in commands. Each command fires an event ( OnEdit, OnUpdate, OnCreate, etc.). If the event is not cancelled, the command updates the Grid state. The built-in edit popup's visibility depends on the current Grid state - the popup is visible if EditItem or InsertedItem is not null. So, if you are managing the Grid editing state programmatically, review the KB article about programmatic Grid editing.
