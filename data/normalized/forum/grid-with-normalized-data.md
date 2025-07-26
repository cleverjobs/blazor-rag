# Grid with Normalized Data

## Question

**Dav** asked on 19 Jun 2022

Is there a way to leverage the Grid with normalized data? I've tried looping through the fields to generate the columns, that's fine. But when it comes to editing them, I can't specify the field in the column as the model doesn't have those properties. This then leads to the field never having a value in the OnEdit callback. I know I can work around it using OnBlur of all of the input fields, but that's really annoying. Any suggestions? I've added sample JSON of what it sort of looks like at the bottom. "lineItems": [
{ "id": 5, "sortOrder": 2, "columns": [
{ "id": 77, "fieldId": 1, "value": "Test 1", "lineItemId": 5 },
{ "id": 78, "fieldId": 7, "value": "Centerspread", "lineItemId": 5 },
{ "id": 79, "fieldId": 8, "value": "02/02/2022", "lineItemId": 5 },
{ "id": 80, "fieldId": 9, "value": "28/02/2022", "lineItemId": 5 },
{ "id": 81, "fieldId": 11, "value": "4/C", "lineItemId": 5 },
{ "id": 82, "fieldId": 13, "value": "600", "lineItemId": 5 },
{ "id": 83, "fieldId": 24, "value": "01/10/2022", "lineItemId": 5 },
{ "id": 84, "fieldId": 26, "value": "Magazine", "lineItemId": 5 },
{ "id": 85, "fieldId": 27, "value": "Test 1", "lineItemId": 5 },
{ "id": 86, "fieldId": 37, "value": "Internal notes, they are a thing!", "lineItemId": 5 }
]

## Answer

**Dimo** answered on 22 Jun 2022

Hello David, Indeed, the Grid data operations can only work if the component is bound to a collection of C# objects with property names that you can specify for each GridColumn Field. Otherwise the column is treated as "unbound" and you will need to take care of sorting, filtering and editing completely manually via custom code. I hope you can create some view model that can meet this requirement. Regards, Dimo Progress Telerik

### Response

**David** commented on 22 Jun 2022

Thanks for the information. Unfortunately, it's based on a normalized template in the database and can change at the drop of a hat. I was able to get it working by creating a dynamic Template and EditTemplate. Cheers
