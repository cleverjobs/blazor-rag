# How to check form dirty state in <EditForm>?

## Question

**Shu** asked on 28 Mar 2022

I am using EditForm in one of my module. Based on form state viz., dirty, touched I want to perform some operations, how can I get those events with EditForm ?

## Answer

**Marin Bratanov** answered on 28 Mar 2022

Hi Shubham, You can click Follow on this page to know when such an event becomes available where you could raise the dirty flag: [https://feedback.telerik.com/blazor/1508940-add-onupdate-event.](https://feedback.telerik.com/blazor/1508940-add-onupdate-event.) For the time being the only way would be to do it yourself with the EditContext and its FieldChanged event. Regards, Marin Bratanov Progress Telerik
