# Passing and extracting extra values in the post

## Question

**Bit** asked on 19 Jun 2020

From the example: In the api handler, what is the preferred way to read the value in "SomeFormField" from the request? Is it in the Body collection of the Request? @inject NavigationManager NavigationManager <TelerikUpload SaveUrl="@SaveUrl" RemoveUrl="@RemoveUrl" OnUpload="@OnUploadHandler"> </TelerikUpload> @code { async Task OnUploadHandler(UploadEventArgs e) { e.RequestData.Add("SomeFormField", "SomeFormValue"); // for example, user name e.RequestHeaders.Add("CustomHeader", "SomeHeaderValue"); // for example, authentication token // you can add more than one } // a sample way of generating the URLs to the endpoint public string SaveUrl=> ToAbsoluteUrl("api/upload/save"); public string RemoveUrl=> ToAbsoluteUrl("api/upload/remove");

## Answer

**BitShift** answered on 19 Jun 2020

Nevermind, I figured it out. Just had to add another paramter to the api controller method for SaveUrl eg. this [HttpPost] public async Task<IActionResult> Save(IEnumerable<IFormFile> files) Needs to be this [HttpPost] public async Task<IActionResult> Save(IEnumerable<IFormFile> files, string YourExtraValue)

### Response

**Zack** answered on 27 Jul 2020

To get extra values in and out of the request, this is what we ended up having to do. Telerik, please update the post if there are better ways. ------- For including extra params in the request, we had to add [FromForm] to the param to get it to work. To get values back from the response, we changed the response to a string and parsed e.Request.ResponseText in the OnSuccessHandler.

### Response

**Marin Bratanov** answered on 27 Jul 2020

Hi Zack, The exact configuration of the endpoint depends on the endpoint, and not on our component, so there might be many valid scenarios and attributes. That said, we have basic examples in the docs: sending data in OnUpload (the second snippet, see also the Controller tab for a sample ASP.NET Core 3 controller action), and receiving information from the endpoint in OnSuccess (the second snippet, again with the Controller tab). Generally, what you mentioned sounds like a correct approach, and you should use the endpoints and setup for them that is suitable for your environment. What we have in the docs are merely samples of one way to do this, out of many. Regards, Marin Bratanov

### Response

**Zack** answered on 27 Jul 2020

Thank you, Marin. For us, we are using Blazor WebAssembly client hosted on ASP.NET Core 3.1 (VS 2019 blazorwasm template with --no-restore --pwa true --hosted true -au SingleOrg). I would have preferred to do something like pass a File business object to the server upload controller and get a saved business model back. I suppose we can make some wrappers to get that effect but I was a little tight on time for the solution.

### Response

**Marin Bratanov** answered on 27 Jul 2020

Hi Zack, If you add appropriate form fields in the Blazor code in OnUpload, ASP.NET should be able to parse them to a model. Alternatively, a JSON serializable model should be able to go into a field in the web request/response and to get extracted and deserialized - both on the Blazor side,and on the controller side. Regards, Marin Bratanov
