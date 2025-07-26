# Errors after upgrade

## Question

**IonIon** asked on 07 Apr 2020

After upgrade to 2.10.0, the ComboBox control with OnRead event, I get the error: Uncaught (in promise) Error: System.ArgumentException: There is no event handler associated with this event. EventId: '38'. (the number differs between errors) The page "blinks" and the control fills with an empty Guid (SelectedPersonId type) The post to the server is performed correctly This worked with 2.9.0 js: <script src="[https://kendo.cdn.telerik.com/blazor/2.10.0/telerik-blazor.min.js"](https://kendo.cdn.telerik.com/blazor/2.10.0/telerik-blazor.min.js") defer></script> razor: <TelerikComboBox Data="PersonSearchResult" OnRead="@SearchPersons" Filterable="true" TextField="FullName" ValueField="Id" @bind-Value="SelectedPersonId" Width="400px"> </TelerikComboBox> and cs: private async Task SearchPersons(ComboBoxReadEventArgs args) { if (args.Request.Filters.Count> 0) { var filter=args.Request.Filters[0] as FilterDescriptor; var search=filter.Value.ToString(); if (search.Length>=2) { PersonSearchResult=await Post<List<PersonModel>>("api/person/person-search", search, true); } } }

## Answer

**Svetoslav Dimitrov** answered on 10 Apr 2020

Hello Ion, Thank you for participating in our Blazor community. I cannot seem to reproduce the issue so I am sending you a demo project (see attached file) which references to 2.10.0. The only notable difference is that i do not use a request to a database. Having said that, you can open a support ticket so we can further investigate the issue you have encountered, or post here the change that would break this app so I can investigate. Regards, Svetoslav Dimitrov

### Response

**Ion** answered on 14 Apr 2020

Hi Svetoslav, Thanks for your reply. There are few differences between your project and my project: - I have a client-side blazor app, not server-side. - My Telerik package is trial. - I perform a request to the server to get the data. I tested with a client-side data source and the control is working. So, the remote data request seems to be the problem. Anyway, the request is performing fine, but the response could not be processed by the ComboBox control. As a detail, the autocomplete control has the same behavior. Ion

### Response

**Svetoslav Dimitrov** answered on 17 Apr 2020

Hello Ion, The fact that you are using Trial Telerik UI for Blazor would not affect the behavior of the components. As attached file you can see a Client-side application with ComboBox taking data from a service. The project references Preview 3 of the Framework and Telerik UI for Blazor 2.10.0. You could compare the differences and follow-up in our conversation as to what to change in order to reproduce the error you are experiencing. Regards, Svetoslav Dimitrov

### Response

**Ion** answered on 21 Apr 2020

Hello again, Thank you for you sample, it help me to hind the mistake, by comparison. I had a wrapper over GetFromJsonAsync method: AppState.IsDataLoading=true;//this property makes a StateHasChanged call, to display a loading progress somewhere in the page<br> var result=await Http.GetFromJsonAsync<TResponse>(url); <br>AppState.IsDataLoading=false;//a new call of StateHasChanged, to hide the progress control<br> return result; ---- LegalCourtSearchResult=await Get<List <LegalCourtModel>>(url); Because of calling the StateHasChanged before the result assignment, the control does not work properly. I will change the progress mechanism to work properly. Thanks! Ion

### Response

**Svetoslav Dimitrov** answered on 22 Apr 2020

Hello Ion, I am glad to hear that you found the issue and the solution for it! Hope that you are having great experience using Telerik UI for Blazor! Regards, Svetoslav Dimitrov
