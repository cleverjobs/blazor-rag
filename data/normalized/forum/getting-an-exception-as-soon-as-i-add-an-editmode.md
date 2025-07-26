# Getting an exception as soon as I add an EditMode

## Question

**Dav** asked on 30 Apr 2020

I have a very simple datagrid. I'm brand new to Telerik and Blazor. My grid works until I add in the EditMode enum. I get a null reference exception on my _Host.cshtml file at this line: 1. <component type="typeof(App)" render-mode="ServerPrerendered" /> Below is my whole .razor page. 01. @page "/crud" 02. 03. @using Portal.Data 04. @using Microsoft.Extensions.Logging; 05. 06. @inject LicenseService licenseService 07. @inject ILogger<LicenseInfo> MyLogger 08. 09. <h1>Crud</h1> 10. 11. <TelerikGrid Data="@licenseData" 12. AutoGenerateColumns="true" 13. EditMode="@GridEditMode.Popup"> 14. </TelerikGrid> 15. 16. @code 17. { 18. private List<Portal.Data.Licenses> licenseData { get; set; } 19. 20. private async Task<List<Licenses>> GetLicenseData() 21. { 22. var licenseData=await licenseService.GetLicensesAsync(); 23. return licenseData; 24. } 25. 26. protected override async Task OnInitializedAsync() 27. { 28. try 29. { 30. licenseData=await GetLicenseData(); 31. } 32. catch (Exception ex) 33. { 34. MyLogger.LogError(ex.Message); 35. } 36. } 37. }

## Answer

**David** answered on 30 Apr 2020

Looks like I needed to add this to my MainLayout.razor. <TelerikRootComponent> <div class="sidebar"> <NavMenu /> </div> <div class="main"> @Body </div> </TelerikRootComponent>
