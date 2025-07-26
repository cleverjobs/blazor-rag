# Custom popup editor for grid similar to "Form Editor".

## Question

**Ken** asked on 12 May 2019

Is it possible to build something using the Modal window perhaps where I could build a custom popup editor? I have a complex edit form with quite a few fields and dynamic behavior (fields hidden based on selection values). It looks like I could implement this with the form editor, I was wondering if I could do something with a popup to avoid a lot of scrolling that is required with the form editor solution. Thanks, Kenny

## Answer

**Marin Bratanov** answered on 13 May 2019

Hi Kenny, You can: start with a custom form editor example: [https://demos.telerik.com/blazor-ui/grid/editing-custom-form](https://demos.telerik.com/blazor-ui/grid/editing-custom-form) once this works as expected, put the custom form inside a modal Window component: [https://demos.telerik.com/blazor-ui/window/modal](https://demos.telerik.com/blazor-ui/window/modal) bind its Visible property to the presences of the currently edited model, or to other custom logic, or show it according to other events: [https://docs.telerik.com/blazor-ui/components/window/overview](https://docs.telerik.com/blazor-ui/components/window/overview) Regards, Marin Bratanov

### Response

**Kenny** answered on 15 May 2019

Hi Marin, This solution works great! Only problem I am having is that after create, the gid does not refresh to show the new item. I am calling: GridData.Add(itemToAdd); to add the item to the grid in the create. It doesn't show up. If I refresh the page it does show up. I tried adding StateHasChanged, no difference. Is there some way I can force the Grid to refresh? Thanks, Kenny

### Response

**Marin Bratanov** answered on 15 May 2019

Hi Kenny, Thank you for reporting this. Indeed, the grid does not react to the data change immediately, some other data source operation is needed at the moment (like changing the current page, for example). You can Follow its status in the following page: [https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change.](https://feedback.telerik.com/blazor/1409112-the-grid-does-not-update-on-data-source-change.) Regards, Marin Bratanov
