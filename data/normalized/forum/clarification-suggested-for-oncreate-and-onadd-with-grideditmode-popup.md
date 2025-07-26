# clarification suggested for OnCreate and OnAdd with GridEditMode.Popup

## Question

**Cha** asked on 17 Jan 2025

Hi, I was working through converting a grid to TelerikGrid, referencing this document page: [https://www.telerik.com/blazor-ui/documentation/components/grid/editing/popup](https://www.telerik.com/blazor-ui/documentation/components/grid/editing/popup) Using GridEditMode.Popup. Edit and Delete functionality was working. New record functionality, however, was not. It was triggering the correct dialog editing, but wouldn't trigger a dialog for adding a new record. Instead it would fire my database code to add a record, with null data being passed. I eventually figured out the example uses the OnCreate event, and I was using the OnAdd event. This wasn't obvious to me, and there didn't seem to be anything in the documentation indicating you have to use OnCreate for the dialog to appear? I then found this page which has more details on the events: [https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview](https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview) In the events section of the page, it states: - OnAdd - fires when the Add command button for a newly added item is clicked. The event is cancellable. OnCreate - fires when the Save command button for a newly added item is clicked. Cancellable (cancelling it keeps the grid in Insert mode). - This isn't helpful either, and I'd go so far as to say it's incorrect? If you have a GridCommandbutton like this: <GridToolBarTemplate> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus"> Add New </GridCommandButton> </GridToolBarTemplate> And you are handling the OnAdd event, the event fires without giving the user a popup, and the data passed in the event is a null item. If you are handling the OnCreate event, the user gets a popup, however the button to "add" is actually Update: As you can see, there's neither an Add button to click or a Save button to click. Perhaps this documentation is correct for other edit modes, but it seems to be misleading or flat out incorrect for Popup mode? On a side note, the documentation also seems to switch back and forth between saying CUD and CRUD. I can sort of understand why you omit the Read part, but it makes the documentation confusing and I'm not sure you correctly use CUD and CRUD in all the right places. Furthermore, every other database documentation I've seen says CRUD, Read or not!

## Answer

**Dimo** answered on 17 Jan 2025

Hi Charles,>> there didn't seem to be anything in the documentation indicating you have to use OnCreate for the dialog to appear OnCreate is not required for the popup edit form to appear for new items: [https://blazorrepl.telerik.com/QJaPbBFB46tWVsbI19](https://blazorrepl.telerik.com/QJaPbBFB46tWVsbI19) The OnCreate handler is used for saving the populated new item to the database and/or the existing Grid Data collection. One possible reason for the Grid popup edit form to not appear is runtime exception or cancelled OnAdd event. Feel free to send your test page over for inspection.>> OnAdd - fires when the Add command button for a newly added item is clicked Indeed, this statement can be interpreted like the new item was already added, which is not true. Sorry about the confusion. The Grid editing documentation is one of the oldest parts of the documentation as a whole and is in a need of a revamp. This is due in the near future. I just added the CUD vs CRUD consideration as a sub-task.>> Save vs Update button text The button text depends on localization strings. We use the same key for new and existing items and I raised a discussion in the team whether to change the default "Update" to "Save" or to add one more localization string. In the meantime, developers can customize the button text in several ways: Popup Form Buttons Template Full localization with resx files Partial localization without resx files Popup Form Template Regards, Dimo Progress Telerik

### Response

**Charles** commented on 17 Jan 2025

Hi, thanks for the quick reply. You are correct, OnCreate is not required. HOWEVER If you handle OnAdd, it fires before the dialog is shown, with invalid data, which will likely lead to an exception. Firing before there's data isn't helpful? If you handle OnCreate, the dialog shows, when the user clicks the appropriate button, the data is passed to the event handler. So, in effect, OnCreate is required for the popup to appear if you want to use the data. And, who isn't interested in the data? You missed my point about the documentation that says: - OnCreate - fires when the Save command button for a newly added item is clicked. Cancellable (cancelling it keeps the grid in Insert mode). - I'm using an "Add" command button, and handling the OnCreate event, which does precisely what I require. The events page doc: [https://www.telerik.com/blazor-ui/documentation/components/grid/events](https://www.telerik.com/blazor-ui/documentation/components/grid/events) Doesn't give any detail on what triggers each "CUD" event. Instead it refers back to: [https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview](https://www.telerik.com/blazor-ui/documentation/components/grid/editing/overview) Which is where I got the above reference: - OnAdd - fires when the Add command button for a newly added item is clicked. The event is cancellable. OnCreate - fires when the Save command button for a newly added item is clicked. Cancellable (cancelling it keeps the grid in Insert mode). - I'm using an "Add" command button, and handling the OnAdd event simply doesn't work. Using a "Save" command button doesn't make sense when adding a new record? <GridToolBarTemplate> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus"> Add New </GridCommandButton> </GridToolBarTemplate> I realize documentation is hard. And keeping it updated with enhancements is even harder. But that's what customers are paying for, right? :) That's why I'm pointing this out, so that the next developer doesn't lose a few hours of work time trying to figure out why it's not behaving the documentation says. Regards, Charles

### Response

**Dimo** commented on 17 Jan 2025

Yes, OnAdd fires before the popup edit form is shown and this is by design. OnAdd is similar to OnEdit, but for new items. You can use OnAdd mainly to set default values for the new item or cancel the operation and prevent the popup from showing. I am not sure what do you mean by "OnAdd fires with invalid data". The event fires with a new empty model instance, which is by design too.>> So, in effect, OnCreate is required for the popup to appear if you want to use the data. And, who isn't interested in the data? No, OnCreate is not required for the popup to appear. And yes, OnCreate is required if you want to add new items, just like OnUpdate is required if you want to modify existing items. OnCreate and OnUpdate are the bridge between the UI and the data layer. OnAdd and OnEdit are usually confined to the UI and business logic.>> OnCreate - fires when the Save command button for a newly added item is clicked. Cancellable (cancelling it keeps the grid in Insert mode). The Save command button is the button that reads "Update". There is a difference between command and button, and between command name and button label. I acknowledged that this may have caused confusion and we will fix that.

### Response

**Charles** commented on 17 Jan 2025

- Yes, OnAdd fires before the popup edit form is shown and this is by design. OnAdd is similar to OnEdit, but for new items. You can use OnAdd mainly
to set default values for the new item or cancel the operation and
prevent the popup from showing. I am not sure what do you mean by "OnAdd fires with invalid data". The event fires with a new empty model instance, which is by design too. - Is this helpful information in the documentation anywhere? It makes a lot of sense and would have saved me a lot of time if I had found it beforehand.

### Response

**Dimo** commented on 17 Jan 2025

Regrettably, no, but this thread is now part of the task description to revamp the whole Grid Editing documentation.

### Response

**Dimo** commented on 11 Mar 2025

@Charles, the revamped Grid CRUD documentation is now live. Let me know if you have any feedback.
