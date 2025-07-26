# Webassembly: Nested Grid not primitive parameter cause call OnParametersSetAsync twice

## Question

**Ale** asked on 22 Oct 2020

<TelerikGrid Data="@CustomerViewModel.Customers" EditMode="@GridEditMode.Inline" Height="800px" Pageable="true" Sortable="true" SortMode="@SortMode.Single" OnUpdate="@(async args=> await CustomerViewModel.UpdateCustomerAsync(args))" OnDelete="@(async args=> await CustomerViewModel.DeleteCustomerAsync(args))" OnCreate="@(async args=> await CustomerViewModel.CreateCustomerAsync(args))"> <GridToolBar> <GridCommandButton Command="Add" Icon="Add">Add Customer</GridCommandButton> <GridSearchBox DebounceDelay="200"></GridSearchBox> </GridToolBar> <GridColumns> <GridColumn Field="@nameof(Customer.Name)" Title="Customer" /> <GridColumn Editable="false" Field="@nameof(Customer.Jurisdictions)" Title="Jur. Count" /> <GridColumn Editable="false" Field="@nameof(Customer.JurisdictionsWithPersonalForms)" Title="Jur. w/Personal forms" /> <GridColumn Editable="false" Field="@nameof(Customer.JurisdictionsWithCorporateForms)" Title="Jur. w/Corporate forms" /> <GridColumn Editable="false" Field="@nameof(Customer.JurisdictionsWithForms)" Title="Jur. with forms (total)" /> <GridColumn Editable="false" Field="@nameof(Customer.JurisdictionsWithLicense)" Title="Jur. License Count" /> <GridCommandColumn> <GridCommandButton Command="Edit" Icon="edit"></GridCommandButton> <GridCommandButton Command="Delete" Icon="delete"></GridCommandButton> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"></GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"></GridCommandButton> @*<GridCommandButton Title="Jurisdictions" OnClick="JurisdictionsShow">Jurisdictions</GridCommandButton>*@</GridCommandColumn> </GridColumns> <DetailTemplate> @{ Customer customer=context as Customer; <CustomerJurisdictionsGrid CustomerId="@customer.Id" OnDeleteCallback="@OnDeleteCustomerCallback" /> } </DetailTemplate> </TelerikGrid> nested <TelerikGrid Data="@ViewModel.CustomerJurisdictions" Pageable="true" Sortable="true" PageSize="20" SortMode="@SortMode.Single" Height="800px" OnDelete="@(async args=> await ViewModel.DeleteCustomerJurisdictionAsync(args))"> <GridColumns> <GridColumn Field="@nameof(CustomerJurisdiction.JurisName)" Title="Name"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.PersFormsCount)" Title="Personal Forms"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.CorpFormsCount)" Title="Corporate Forms"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.JurisTypeDescription)" Title="Type"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.JurisStateDescription)" Title="State"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.JurisCountryDescription)" Title="Country"></GridColumn> <GridColumn Field="@nameof(CustomerJurisdiction.LastUpdated)" Title="Last Updated"></GridColumn> <GridCommandColumn> <GridCommandButton Command="Delete" Icon="delete"></GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code { [Parameter] public int CustomerId { get; set; } [Parameter] public EventCallback<CustomerEventArgs> OnDeleteCallback { get; set; } protected override async Task OnParametersSetAsync() { Console.WriteLine(ViewModel); await ViewModel.LoadCustomerJurisdictionsAsync(CustomerId); } } so basically if thу parameter to the nested grid is not primitive, OnParametersSetAsync will be fired twice, would appreciate for the work around

## Answer

**Marin Bratanov** answered on 23 Oct 2020

Hello Aleksandr, I am attaching a few samples I made that seem to work as expected for me - the OnParametersSetAsync event of the child component in the DetailTemplate is called only once - both in the basic scenario where an int (a primitive type) is used like in the provided snippets, and also when a string is used which is not primitive. I am attaching a screen recording of the WebAssembly case for the string too. If comparing against those samples does not help you solve this, I can suggest the following: see if adding counters/flags and maybe overriding ShouldRender for that component will let you get the rendering and performance you seek see if there are larger changes at hand - for exapmle, event handlers and other application code re-rendering the entire grid, or something similar that causes a re-render (such as changing the parameter value inside the child component) Regards, Marin Bratanov

### Response

**Aleksandr** answered on 23 Oct 2020

i repeated your example and it works exactly as expected (please see 1.jpg) <DetailTemplate> @{ Customer customer=context as Customer; <CustomerJurisdictionsGrid CustomerId="@customer.Id" CustomerName="@customer.Name" /> } </DetailTemplate> but if we try to put an object or callback (see 2.jpg) the diff in code is just <DetailTemplate> @{ Customer customer=context as Customer; <CustomerJurisdictionsGrid CustomerId="@customer.Id" OnDeleteCallback="@OnCustomerJurisdictionDeleted" /> } </DetailTemplate>

### Response

**Marin Bratanov** answered on 23 Oct 2020

Hi Aleksandr, On my end, the event callback is the cause, without it I don't observe this behavior - with or without the two parameters (int and string). Could you confirm if this is what you see in the new samples I'm attaching? Does removing the event callback fix this issue for you? Can you reproduce it without it? Regards, Marin Bratanov

### Response

**Aleksandr** answered on 23 Oct 2020

removing callback will fix the issue, but instead of callback you can put something else, for example the sub model of ViewModel, etc

### Response

**Aleksandr** answered on 23 Oct 2020

basically i need to establish communication between page & nested grid to be able to update the main greed if for example the item from the nested was removed. we can do it two way: - have callback - or put the sub model to the nested grid & have internal event handlelling but this cause double run of OnParametersSetAsync

### Response

**Aleksandr** answered on 25 Oct 2020

more over - when details are shown, any event in a parent grid row lead to details reload :-(

### Response

**Aleksandr** answered on 25 Oct 2020

if we have grid of 10 rows & 5 of them are expanded, clicking at the button on the parent grid will raise event propagation for each, terrible CustomerViewModel JurisdictionsShow blazor.webassembly.js:1 CustomerAvailableJurisdictionsViewModel PopUpShowAsync blazor.webassembly.js:1 CustomerAvailableJurisdictionsViewModel LoadJurisdictions blazor.webassembly.js:1 DoWorkShow blazor.webassembly.js:1 1 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[100] Start processing HTTP request GET [http://localhost:5001/api/customer/5/availablejurisdictions](http://localhost:5001/api/customer/5/availablejurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[100] Sending HTTP request GET [http://localhost:5001/api/customer/5/availablejurisdictions](http://localhost:5001/api/customer/5/availablejurisdictions) blazor.webassembly.js:1 CustomerJurisdictionViewModel OnParametersSetAsync blazor.webassembly.js:1 CustomerJurisdictionViewModel LoadCustomerJurisdictionsAsync blazor.webassembly.js:1 DoWorkShow blazor.webassembly.js:1 2 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[100] Start processing HTTP request GET [http://localhost:5001/api/customer/5/jurisdictions](http://localhost:5001/api/customer/5/jurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[100] Sending HTTP request GET [http://localhost:5001/api/customer/5/jurisdictions](http://localhost:5001/api/customer/5/jurisdictions) blazor.webassembly.js:1 CustomerJurisdictionViewModel OnParametersSetAsync blazor.webassembly.js:1 CustomerJurisdictionViewModel LoadCustomerJurisdictionsAsync blazor.webassembly.js:1 DoWorkShow blazor.webassembly.js:1 3 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[100] Start processing HTTP request GET [http://localhost:5001/api/customer/6/jurisdictions](http://localhost:5001/api/customer/6/jurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[100] Sending HTTP request GET [http://localhost:5001/api/customer/6/jurisdictions](http://localhost:5001/api/customer/6/jurisdictions) blazor.webassembly.js:1 CustomerJurisdictionViewModel OnParametersSetAsync blazor.webassembly.js:1 CustomerJurisdictionViewModel LoadCustomerJurisdictionsAsync blazor.webassembly.js:1 DoWorkShow blazor.webassembly.js:1 4 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[100] Start processing HTTP request GET [http://localhost:5001/api/customer/7/jurisdictions](http://localhost:5001/api/customer/7/jurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[100] Sending HTTP request GET [http://localhost:5001/api/customer/7/jurisdictions](http://localhost:5001/api/customer/7/jurisdictions) blazor.webassembly.js:1 CustomerJurisdictionViewModel OnParametersSetAsync blazor.webassembly.js:1 CustomerJurisdictionViewModel LoadCustomerJurisdictionsAsync blazor.webassembly.js:1 DoWorkShow blazor.webassembly.js:1 5 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[100] Start processing HTTP request GET [http://localhost:5001/api/customer/15/jurisdictions](http://localhost:5001/api/customer/15/jurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[100] Sending HTTP request GET [http://localhost:5001/api/customer/15/jurisdictions](http://localhost:5001/api/customer/15/jurisdictions) blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[101] Received HTTP response headers after 311.525ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[101] End processing HTTP request after 312.7ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[101] Received HTTP response headers after 294.95ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[101] End processing HTTP request after 296.1749ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[101] Received HTTP response headers after 290.9249ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[101] End processing HTTP request after 292.05ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[101] Received HTTP response headers after 285.2199ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[101] End processing HTTP request after 286.74ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.ClientHandler[101] Received HTTP response headers after 264.67ms - 200 blazor.webassembly.js:1 info: System.Net.Http.HttpClient.ICustomerApiService.LogicalHandler[101] End processing HTTP request after 265.7349ms - 200 blazor.webassembly.js:1 DoWorkHide blazor.webassembly.js:1 4 blazor.webassembly.js:1 CustomerAvailableJurisdictionsViewModel PopUpShowAsync WindowJurisdictionsPopUpVisible: True 4blazor.webassembly.js:1 CustomerJurisdictionViewModel OnParametersSetAsync blazor.webassembly.js:1 HideSpinner blazor.webassembly.js:1 3 blazor.webassembly.js:1 HideSpinner blazor.webassembly.js:1 2 blazor.webassembly.js:1 HideSpinner blazor.webassembly.js:1 1 blazor.webassembly.js:1 HideSpinner blazor.webassembly.js:1 0

### Response

**Aleksandr** answered on 25 Oct 2020

please see the video, i am just clicking on textbox Video

### Response

**Aleksandr** answered on 26 Oct 2020

so found a workaround, removed callback, firing event through app service bus between components, works perfectly

### Response

**Marin Bratanov** answered on 28 Oct 2020

Hello Aleksandr, The short answer is that this behavior is expected. I made the following KnowledgeBase article that explains the situation in more detail and also offers a different approach towards changing this behavior: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-detailtemplate-renders](https://docs.telerik.com/blazor-ui/knowledge-base/grid-detailtemplate-renders) Regards, Marin Bratanov
