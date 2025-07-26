# Virtualization

## Question

**Rob** asked on 14 Dec 2021

Hi. Trying to use virtualization in the Combobox with a remote data source, but the DataSourceRequest.Page in OnRead is always 0. How to fix that?

## Answer

**Hristian Stefanov** answered on 17 Dec 2021

Hi Robert, The remote data source provides PageSize and Skip for the ComboBox virtualization. These properties give the information for the scrolling state. You can find more details in our article for working with remote data. There is one more thing to mention - ComboBox virtualization has a limitation. When the initially selected item/items are on a page different than the first one, opening the dropdown list will not scroll the list to the selected item. Based on the above specifics, you can test our Remote Data example. If you see unexpected behavior, please send us a small runnable sample that shows the issue. Thank you. Regards, Hristian Stefanov

### Response

**Robert** commented on 14 Jan 2022

The example doesn't use PageSize or Skip.

### Response

**Hristian Stefanov** commented on 19 Jan 2022

Hi Robert, I tested the Remote Data example, and I get correctly the PageSize / Skip. Please run the above example in debug mode and enter the OnRead handler - " GetRemoteData(ComboBoxReadEventArgs e) ". Try to scroll, and see how the event arguments are providing the current PageSize / Skip. Let me know if the result you get is different.

### Response

**Robert** commented on 19 Jan 2022

Yes, they are provided, but the example doesn't apply them. If page size is 20 and skip is 5, what am I supposed to do? If page size is 20 and skip is 25, what am I supposed to do?

### Response

**Hristian Stefanov** commented on 24 Jan 2022

Hi Robert, The PageSize/Skip provided from the OnRead arguments are already applied to the component. This happens automatically when you scroll. The OnRead arguments show the result of your current scroll action. When you receive the current PageSize/Skip as a result of your action, you can do whatever your scenario requires with the provided data. Regards, Hristian Stefanov

### Response

**Robert** commented on 24 Jan 2022

Ok, I see. The example uses the built in functionality via ToDataSourceResultAsync My situation is different. I have an OData back end and thus cannot use this built-in behavior. I'd like some more information about how to apply PageSize/Skip in my request to the back end.

### Response

**Robert** commented on 24 Jan 2022

Never mind, found out about DataSourceRequest.ToODataString()
