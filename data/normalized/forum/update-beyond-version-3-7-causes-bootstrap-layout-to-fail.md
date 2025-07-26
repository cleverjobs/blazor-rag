# Update beyond version 3.7 causes bootstrap layout to fail

## Question

**Ric** asked on 01 Dec 2023

Upgrading the version of Telerik.Blazor.UI used beyond 3.7 causes all pages to change the layout order. See the attached screenshots. I am only using bootstrap for the row and column layout. It seems to put full width controls at the top and then controls that should be partial width. But it also makes those controls full width. I've tried bringing everything up to date in terms of the Theme, bootstrap css etc. but still no joy. I don't have the time to rewrite all the layouts in this app to use just Telerik controls. Suggestions welcome. Thanks Richard

## Answer

**Richard** answered on 04 Dec 2023

Same as this issue: [https://feedback.telerik.com/blazor/1601597-form-reorders-items-and-custom-markup](https://feedback.telerik.com/blazor/1601597-form-reorders-items-and-custom-markup)

### Response

**Dimo** answered on 06 Dec 2023

Hi Richard, I assume that you have custom HTML markup or Razor components inside the <FormItems> tag. Please refer to this documentation article, which describes what caused the change and how to migrate: Template for all Form items The essence is that the old approach worked "by chance" in the past without official support. At some point we had to drop it in order to provide other requested features. The short description of what to do now is "move all custom content from <FormItems> to <FormItemsTemplate>". In general, we don't recommend using custom markup and child components anywhere inside our components, except for officially documented templates. The only reason the old approach worked is because we can't impose restrictions on the content inside Blazor RenderFragments that we sometimes use for non-template purposes. I am sorry if the change will require development resource to migrate. Regards, Dimo Progress Telerik

### Response

**Richard** commented on 06 Dec 2023

Hi Dimo, I've been through the 'how to migrate' pages and other associated links. For anyone else with this issue I found that so long as all fields are in the following structure <FieldItems><FieldGroup><FieldItem><Template> for each section of the form then adding this generic code as the FormItemsTemplate speeds up the migration. <FormItemsTemplate Context="formContext"> @foreach (IFormItemBase item in formContext.Items) { if (item is IFormGroup) // only if using FormGroups { var groupItem=(IFormGroup)item; <TelerikFormGroupRenderer Group="@groupItem"> <Template Context="groupContext"> @foreach (IFormItem singleItem in groupContext.Items) { <TelerikFormItemRenderer Item="@singleItem" /> } </Template> </TelerikFormGroupRenderer> } else { <TelerikFormItemRenderer Item="@(item as IFormItem)" /> } } </FormItemsTemplate>
