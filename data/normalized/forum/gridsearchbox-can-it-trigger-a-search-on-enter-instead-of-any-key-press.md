# GridSearchBox can it trigger a search on ENTER instead of any key press?

## Question

**RobRob** asked on 06 Mar 2023

Hi, Is is possible to configure the GridSearchBox in the TelerikGrid Toolbar, so that it searches when the user presses ENTER/RETURN instead of after every key press?

## Answer

**Dimo** answered on 09 Mar 2023

Hello Rob, Currently, the GridSearchBox always triggers search during typing. You have two options: If you want to reduce the number of search requests during typing, increase the DebounceDelay of the GridSearchBox component. Replace the GridSearchBox with a TelerikTextBox and then you will have full control over the behavior. Regards, Dimo Progress Telerik

### Response

**Rob** commented on 09 Mar 2023

Thanks Dimo, Unfortunately, I cannot replace the GridSearchBox as that is an internal component to your library, which gives it access to internal features of the Grid. Specifically the CommandName of the TableCommandEventArgs class. In replacing the text box, we lose all the integrated functionality for filtering/sorting that the GridSearchBox provides, with no way to reproduce them. Regards, Rob

### Response

**Dimo** commented on 09 Mar 2023

@Rob - the "access to intenal features" is a bit over-stated. The GridSearchBox helps build filter descriptors for the SearchFilter property of the Grid state. These filter descriptors are then used in the Grid data request. This routine is exactly what the second link shows how to implement manually. So it is possible to replace the default search box component without losing functionality. You can even mimic the HTML rendering with the icons if you like. Why do you need the TableCommandEventArgs CommandName?

### Response

**Rob** commented on 09 Mar 2023

Thanks for the reply @dimo. I am incredibly happy using the GridSearchBox to automatically find columns or optionally take a list of columns to search on. This is exactly the functionality I want to use. Only I would like it triggered by an Enter key rather than automatically after key presses. The link you provided is very good at implementing this for one use case and I am sure with some tweaking I could make it work in a more generic manner. My initial investigation into this issue lead into the source for the Telerik Grid to see how it is being done at the moment. I was hoping to extend the existing functionality with wrappers the Telerik editions. if we have to do it as part of the OnRead event, then so be it. Regards, Rob

### Response

**Adam** commented on 05 Mar 2025

@Dimo you mentioned mimicking the appearance of the GridSearchBox on a TelerikTextBox. Can you elaborate on how to do that?
