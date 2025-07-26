# Loader is not showing

## Question

**Dav** asked on 18 Nov 2020

01. @if (_isLoading) 02. { 03. <TelerikLoader Class="loader-indicator" 04. Type="@LoaderType.ConvergingSpinner" 05. Size="@LoaderSize.Large" 06. Visible="true"></TelerikLoader> 07. } 08. else 09. { 10. <TelerikGrid Data="@_identities" 11. AutoGenerateColumns="true" 12. PageSize="50" 13. ScrollMode="@GridScrollMode.Virtual" 14. Height="460px" 15. RowHeight="60"> 16. <GridToolBar> 17. <GridSearchBox /> 18. </GridToolBar> 19. </TelerikGrid> 20. } 21. 22. @code { 23. List<IdentityDTO> _identities; 24. public bool _isLoading { get; set; } 25. 26. protected override async Task OnInitializedAsync() 27. { 28. await LoadData(); 29. 30. } 31. async Task LoadData() 32. { 33. _isLoading=true; 34. _identities=await _service.GetIdentities(); 35. _isLoading=false; 36. } 37. } Am I missing something basic here? Why wouldn't the loader be showing?

## Answer

**David** answered on 18 Nov 2020

Ok I'm definitely missing something. I copied/pasted the source from the documentation and it still doesn't show. 01. @if (IsLoading) 02. { 03. <TelerikLoader /> 04. } 05. else 06. { 07. @Data 08. } 09. 10. @code { 11. public bool IsLoading { get; set; } 12. public string Data { get; set; } 13. 14. protected override async Task OnInitializedAsync() 15. { 16. await LoadData(); 17. } 18. 19. async Task LoadData() 20. { 21. IsLoading=true; 22. await Task.Delay(2000); 23. IsLoading=false; 24. Data="Your data goes here"; 25. } 26. }

### Response

**David** answered on 18 Nov 2020

I created a brand new Telerik Blazor App from the VS template, and the sample code I posted above from the Loader demo page works. So it's something in my app :(

### Response

**Lonwabo** answered on 19 Nov 2020

I am having the same issue. I have an existing project that I upgraded to .net 5 and Blazor UI 2.19.0. It works on a brand new project but not on my existing one.

### Response

**Nadezhda Tacheva** answered on 19 Nov 2020

Hello David, Lonwabo, Attached you will find a demo Blazor application in which I have used the Telerik Loader component (can be found on Fetch data page). Could you please run that project locally and see if it works as expected for you? If it does, my suggestion will be to try the following options: Option 1 Compare it with your project setup and see if any differences cause the issues Option 2 Check stylesheets references - As at this stage I am not aware if your project uses static assets or a CDN, make sure you have the correct stylesheets reference in ~/Pages/_Host.cshtml file of your project. You may find the following article helpful in that case - [https://docs.telerik.com/blazor-ui/themes/overview.](https://docs.telerik.com/blazor-ui/themes/overview.) I'm also providing an article for upgrading Telerik UI for Blazor if needed - [https://docs.telerik.com/blazor-ui/upgrade/overview.](https://docs.telerik.com/blazor-ui/upgrade/overview.) *Note: It is crucial to have the correct stylesheet reference as the Loader is a relatively new component, released in version 2.17.0. Therefore, if your project has a bit older, not updated stylesheet reference that might cause the described issue. Option 3 If options 1 and 2 do not solve the problem, please go ahead and modify the application I have sent so that the issue is reproducible. Thus, we will be able investigate further and assist better. Regards, Nadezhda

### Response

**David** answered on 19 Nov 2020

Thanks for the reply, Nadezhda. It was indeed missing CSS classes that was the issue. I somehow got my CSS files messed up and the classes that render the Loader were not there. After I added a "stock" CSS file from Telerik and referenced that it worked. DOH!

### Response

**Fadhilah** commented on 14 Sep 2022

are you able to share the missing CSS or how you added the stock CSS file? my loader is missing after upgrading to telerik 3.5.0... i've added the css but doesnt seem like its working...

### Response

**Nadezhda Tacheva** commented on 15 Sep 2022

Hi Fadhilah, I already posted a reply in your private ticket, so we can revise the issue there. However, just adding a comment here as well with some clarifications on this discussion. The current thread covers a scenario in which the application uses old stylesheet where the styles for the Loader component are missing because the component was not yet released when the stylesheet was generated. For example, if the Loader is released in version 2.17.0 and the application uses the theme compatible with version 2.16.0, the Loader styles will be missing there since this component was not available at all in UI for Blazor 2.16.0. Upgrading from version 3.4.0 to 3.5.0 should not introduce such a risk as the component was released a long time ago. However, it is crucial that the application uses the correct client assets for the specific version, so the components can look and behave as expected. If you are using the correct CSS file, you should not explicitly add the component styles, they should already be in the stylesheet.

### Response

**Lonwabo** answered on 19 Nov 2020

Thank you, I had to pull latest from kendo-themes on github. I use a custom theme and css was not up to date.

### Response

**Nadezhda Tacheva** answered on 20 Nov 2020

Hello David, Lonwabo, I am happy to find out you both managed to resolve the issue. Please do not hesitate to contact us if you need any further assistance. Regards, Nadezhda

### Response

**Conie** answered on 07 Jan 2021

Zip file is Empty

### Response

**Nadezhda Tacheva** answered on 12 Jan 2021

Hi Conie, It seems there is an issue with opening the zip file on some machines (I tested on a couple, on some the file couldn't be opened, on others it worked as expected). Nevertheless, I'm attaching the file again, so you can check it. Regards, Nadezhda
