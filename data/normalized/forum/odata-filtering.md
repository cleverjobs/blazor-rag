# odata filtering

## Question

**Dav** asked on 16 Oct 2020

I have a grid that I have linked to an odata 4 source. I use request.ToODataString() to build the URL in the onread event. if no filter is defined it works fine /odata/BinMasterAllstock?$count=true&$skip=0&$top=100 as soon as any filter is set (or just the clear button of a filter drop down) the ToODataString does the following all filters including empty ones get included GET /odata/BinMasterAllstock?$count=true&$filter=((contains(NameParentParentLoc,%27%27)%20and%20contains(NameParentParentLoc,%27%27))%20and%20(contains(ZNo,%27%27)%20and%20contains(ZNo,%27%27))%20and%20(QtyOnHand%20eq%20%20and%20QtyOnHand%20eq%20)%20and%20(contains(Zdesc,%27%27)%20and%20contains(Zdesc,%27%27))%20and%20(contains(LotNo,%27%27)%20and%20contains(LotNo,%27%27))%20and%20(contains(Extra0,%27%27)%20and%20contains(Extra0,%27%27))%20and%20(contains(Extra1,%27%27)%20and%20contains(Extra1,%27%27))%20and%20(contains(Extra2,%27%27)%20and%20contains(Extra2,%27%27))%20and%20(contains(Extra3,%27%27)%20and%20contains(Extra3,%27%27))%20and%20(contains(Extra4,%27%27)%20and%20contains(Extra4,%27%27))%20and%20(contains(Extra50,%27%27)%20and%20contains(Extra50,%27%27))%20and%20(contains(NameParentLoc,%27a%27)%20and%20contains(NameParentLoc,%27%27)))&$skip=0&$top=100 Of course that is not well formed and a bad request is returned. What am I missing.

## Answer

**Svetoslav Dimitrov** answered on 19 Oct 2020

Hello David, As an attached file, you can see WASM Blazor application since I suggest that you are using the WASM flavor. For me, locally, when I run the application and apply a filter through the FilterMenu (FilterRow) it works as expected. An example URL built with the args.Request.ToODataString() in the OnRead event looks like: [https://demos.telerik.com/kendo-ui/service-v4/odata/Products?](https://demos.telerik.com/kendo-ui/service-v4/odata/Products?) $count=true&$filter=((contains(ProductName,%27Cha%27)))&$skip=0&$top=10 Could you modify the project so that the behavior you are experiencing is reproducible and we can further investigate? That being said, we have a Bug Report on our Feedback Portal that covers the situation when the ToODataString extension method throws a null reference exception in Service-side Blazor application. If you encounter the same error you could Vote for it and Follow the thread to receive email notifications on status updates. Regards, Svetoslav Dimitrov

### Response

**David Ocasio** answered on 20 Oct 2020

Actually it is not wasm it is server-side . I am starting using the server side and will eventually migrate it to wasm. to that point no direct database/entity framework calls are done in my code from the client side (running on server of course). rather they connect to an odata source to get the data. I will see if i can get a more generic test (or doctor yours) together and post it a little later this week . Question: Does the fact that I am doing it server side change anything in your reply. thanks for assistance.

### Response

**Edward** answered on 20 Oct 2020

I've run into the same exact problem. Attempting to sort a column results in a OData string that is full of filters, for which there is no reason as no filters are applied. If any of the fields are bound to an enum field, I get back a bad request with the message "The query specified in the URI is not valid. The string '' is not a valid enumeration type constant." Makes sense, since you can't parse empty string into an enum value. This needs to be addressed for sure.

### Response

**Edward** answered on 20 Oct 2020

Your published sample uses version 2.7.0 and ToODataString() works fine. Once you update to version 2.17.0, it is broken with exactly the same symptoms we are describing. So the problem is extremely easy to demonstrate. Clone your own sample project that shows how to use OData and update components to 2.17.0.

### Response

**Svetoslav Dimitrov** answered on 21 Oct 2020

Hello David and Edgar, As attached files, you can see a server-side project (what we use on blazor-ui public repository) which is updated to 2.17.0. For me locally it runs as expected, the request-toodatastring-result screenshot shows what I can see from the execution of the code and the rendered-grid is a screenshot that showcases the rendered result. Could you modify the application so that the behavior you are experiencing is reproducible? I am missing something? Regards, Svetoslav Dimitrov

### Response

**Edward** answered on 21 Oct 2020

This happens in a WASM project for me. All I did was literally take your sample OData project and updated components to 2.17.0. Here is the project zipped up for your reference.

### Response

**Edward** answered on 21 Oct 2020

Sorry, wouldn't let me attach the zip as it's bigger than 2mb. Here are the steps: 1. Refer to project [https://github.com/telerik/blazor-ui.git](https://github.com/telerik/blazor-ui.git) 2. Open project blazor-ui/grid/odata/WasmApp/ 3. Update Telerik components to version 2.17.0 4. Run the project and attempt sorting columns

### Response

**Svetoslav Dimitrov** answered on 21 Oct 2020

Hello Edward and David, Thank you for bringing this to our attention and for your efforts in recreating the issue. I have created a new Bug Report on our Feedback Portal, which you can see from this link. I have added both your Votes to raise the popularity of the item and you can Follow it to receive email notifications on status updates. If you have any additional feedback on the issue you might submit it to the public Bug Report. Regards, Svetoslav Dimitrov
