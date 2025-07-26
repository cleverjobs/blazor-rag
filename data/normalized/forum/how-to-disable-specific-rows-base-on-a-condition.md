# How to disable specific rows base on a condition.

## Question

**Zei** asked on 27 Aug 2022

I am using CRUD operations where my grid has default data so, when it is displayed, will have two rows . I can add , edit and delete more rows but, I can not edit or delete the default specfic rows that I got: USER001 and USER002 can not be edited or deleted. How can I disable those two rows?

## Answer

**Dimo** answered on 31 Aug 2022

Hi Zeina, Render the Edit and Delete commands conditionally inside the GridCommandColumn. Another option is to cancel the OnEdit event to prevent editing (e.g. if you are using in-cell editing). Regards, Dimo
