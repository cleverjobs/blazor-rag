# Grid functionality - using display text instead of underlying values for columns

## Question

**Dan** asked on 19 Jul 2022

Started building my first app with Blazor Grid and running into some issues. Have several columns that need dropdownlist to display text instead of underlying number (eg select and display "Operations Department" instead of value of 3) The grid will not sort based on the Display Text but does so instead based on value. Same when trying to group using the field. Sort by the value in groups (and I see no way to change the sort order from ascending to descending on the groups too).

### Response

**Nadezhda Tacheva** commented on 22 Jul 2022

Hi Daniel, I suppose you are referring to a dropdownlist that will be visible in the edit mode of the corresponding column or when filtering it. Is that correct? The most suitable approach to proceed with will depend on the data you are using. For example, if you are using Enum, the Grid will by default display the named constants of the underlying numeric values. In this case, the Grid will also render DropDownList for editing and filtering Enums. The sorting will be performed based on the Enum numeric values. Take a look at the Filter and Edit Enum in Grid article. If you are binding the Grid to a complex model, you will need to use the corresponding templates to control how the Grid renders the data in display mode or when the user edits or filters (see Grid Templates ). In terms of sorting - I'd like to confirm your desired behavior to make sure we are on the same page. Can you please confirm if you are trying to achieve sorting by the value or the displayed text? As for sorting the grouped column, this functionality is not yet available, but it will be supported in future version of the product. You can vote for it and follow it here: Allow sorting the grouped column If you are facing any difficulties after revising the linked resources, please let me know. In this case, please share a runnable replication of the problematic scenario. Thus I can test your exact configuration on my end, advise what is missing and suggest an option to proceed. You can generate some dummy data just for testing purposes, I just need to know the type of data you are binding the Grid to and the exact way you are displaying it. Thank you in advance!

### Response

**Werdna** commented on 25 Jan 2023

"In terms of sorting - I'd like to confirm your desired behavior to make sure we are on the same page. Can you please confirm if you are trying to achieve sorting by the value or the displayed text?" Yes I have this same issue. I'd like to sort by the value of the displayed text and not the value stored in the field itself. In the original example, I'd like to sort by "Operations Department", (which is displayed because a Template is used), rather than the actual value of 3.

### Response

**Nadezhda Tacheva** commented on 30 Jan 2023

Hi Werdna, Thank you for sharing details on your desired result! Let me extend the currently discussed example and provide information on how to achieve this behavior. Let's say the Grid column is bound to a numeric field that represents the actual values. You then use a Template to get the corresponding string representation based on that value to display it in the Grid in a user-friendly way (similar to the second approach listed here - [https://docs.telerik.com/blazor-ui/knowledge-base/grids-foreign-key](https://docs.telerik.com/blazor-ui/knowledge-base/grids-foreign-key) ). The key part in this scenario is that the Grid is not aware of that string representation. The Grid column is bound to the actual value field. When the Template is used, the Grid no longer controls the rendering, the component is not aware of what one may render in this Template. Having the above in mind, such sorting based on the string values is not possible out of the box as the component itself does not know about these values. You can, however, customize the sorting to achieve your desired behavior. You can do that via the OnRead event. I will first share a couple of important resources to review prior to binding the Grid with OnRead: Fundamentals of OnRead Grid-specific OnRead article with examples In your case, you will have to check the SortDescriptors in the Sorts property of the DataSourceRequest. If there is an active sorting by the specific column, then implement custom sorting (order the items as needed) and provide the sorted data to the Grid via args.Data (together will all the other data operations such as filtering, etc.). Please try the approach following the above-listed instructions and let me know if you are facing any difficulties with the implementation. If so, please send us a runnable version of your progress so we can revise it and find out what is missing. Thank you in advance!
