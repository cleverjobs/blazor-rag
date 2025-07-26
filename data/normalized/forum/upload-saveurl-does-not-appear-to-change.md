# Upload SaveUrl does not appear to change

## Question

**Ric** asked on 07 Oct 2024

I am working on a Blazor Auto application using the Upload component to upload images for a product for various properties in a SaaS type system. I found that when I adjust the save point in the application at runtime the SaveUrl does not seem to retain the value. For example: SaveImageUrl=$"api/property/{TenantSelectionService.SelectedTenant.Id}/product-types/{TypeCode}/images"; <TelerikUpload AllowedExtensions="@(new List<string>() {".jpg ", ".jpeg ", ".webp " })" SaveUrl="@SaveImageUrl" WithCredentials="true" OnUpload="@OnUploadAsync"> This is set in two locations, OnAfterRender as well as OnTenantSelectionChanged event. When using this method, it appears that the Upload component does not retain the SaveUrl for some reason. When examining the JavaScript, the URL is always blank. I did manage to alter the URL to a static version and pass data as a header. Is this something that can be looked into or maybe I am doing it wrong.

## Answer

**Dimo** answered on 10 Oct 2024

Hello Rick, As a first troubleshooting step, please render the SaveUrl value next to the Upload component to verify that it's changed as expected. <div> @SaveImageUrl </div> <TelerikUpload SaveUrl="@SaveImageUrl" /> An important thing to keep in mind is that SaveUrl and RemoveUrl cannot be changed between file selection and file upload, although I am not sure if this is your scenario. Check the attached working app. Regards, Dimo Progress Telerik
