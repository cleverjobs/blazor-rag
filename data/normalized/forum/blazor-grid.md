# blazor grid

## Question

**kha** asked on 01 Jan 2020

hello i have a couple of questions about blazor grid 1) i added a grid column called actions it contains some buttons to navigate but when i add Reorderable="true" to TelerikGrid im able to change position of this column which i dont want to so i added Reorderable="false" to my action column and it worked i cant change it's position anymore but i can drag my other columns and put it before my action column so it gets affected by the reorderable column and its position gets changed but i dont want to 2) i also used Sortable="true" and FilterMode="@GridFilterMode.FilterMenu" in my TelerikGrid tag but it doesnt get filtered nor sorted i see the red arrow for sort but it doesnt sort and also ui for filter is completely ok but it doesnt filter either aldo the Data im passing to grid is List<SomeDto>

## Answer

**Marin Bratanov** answered on 01 Jan 2020

Hi Khashayar, To each question: reordering adjacent columns affects a column that is not reorderable - this is expected and documented ( docs link ). There is no way to not let a column be affected by other columns, unless it is frozen but that would change the UX in a different direction. the grid not filtering or sorting - I am not aware of such problems in the component and at this point I can only advise that you compare against our demos (link to filtering, link for sorting ) to see what is the difference causing the problem on your end. If this does not help, please open a support ticket so you can send me a sample project that demonstrates the problem which will let me investigate and offer a more concrete answer. In the meantime the only other idea that comes to mind is to make sure that you are not using the OnRead event of the grid, as this is the only case where the grid stops performing the data operations (such as filtering and sorting) for you, and you must implement them. Regards, Marin Bratanov

### Response

**Arjun** commented on 02 Sep 2024

Hi Telerik team, regarding reordering adjacent columns affects a column that is not reorderable As this preview ,w hen i add Reorderable="true" to TelerikGrid im able to change position of this column which i dont want to so i added Reorderable="false" to my action column and it worked i cant change it's position anymore but i can drag my other columns and put it before my action column so it gets affected by the reorderable column and its position gets changed .

### Response

**Dimo** commented on 03 Sep 2024

@Arjun - indeed, we have a feature request about this scenario - prevent reordering and changing the index of a Grid column. The linked page contains a possible workaround. I already voted for the feature request on your behalf and you can follow it for status updates. On a side note, I see that your company has several unassigned licenses. Please ask your license holder to assign you a license, so that your account is in good standing and compliant with our license agreement.

### Response

**khashayar** answered on 08 Jan 2020

thanks, and also i wanted to know is there a way to manulay refresh data of virtualized grid ?

### Response

**Marin Bratanov** answered on 08 Jan 2020

Hello Khashayar, Let's continue the discussion about this in your other thread on the same subject where you can find an example I made for you: [https://www.telerik.com/forums/telerikgrid-onread](https://www.telerik.com/forums/telerikgrid-onread) Regards, Marin Bratanov
