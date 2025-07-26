# Limit Multiselected to single selection?

## Question

**Dav** asked on 11 Jun 2021

We have have built a multiselect into a window component that can be pop-up on the host page. We have a few instances where we only want the user to be able to select one item and we would like to pass a parm into our component to limit the multiselect to one item. Is that possible?

## Answer

**Marin Bratanov** answered on 14 Jun 2021

Hi David, You can add a parameter to your custom component and change between a DropdownList and a Multiselect. Alternatively, you can use that flag in the ValueChanged event of the multiselect to prevent the selection of a second option. Regards, Marin Bratanov

### Response

**Bon** commented on 02 Jun 2024

Very disappointing answer. There is logically no difference between a single and multi select list except for the number of items you can select. They should be the same control and you should be able to easily set the max number of selected items.

### Response

**Nadezhda Tacheva** commented on 05 Jun 2024

Hi Bon, I noticed that the jQuery version of the MultiSelect has a maxselecteditems configuration that allows restricting the selected items count. Once the maximum is reached, however, the popup does not open. The user has to first delete a selected item in order to open the popup and select a new item. Let me know if this is the behavior you are looking for. If you want to support single selection only and allow the user to open the popup to directly change the selected item, I recommend using the ValueChanged event to manage the selection. Here is a basic example: [https://blazorrepl.telerik.com/wSOqaJFm54dsPcQO56.](https://blazorrepl.telerik.com/wSOqaJFm54dsPcQO56.)
