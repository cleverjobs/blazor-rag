# Accessing Controller from Blazor Page not working in Azure Web App

## Question

**Chr** asked on 16 Mar 2023

Any idea why this would work when running locally but returns "Unauthorized" when running in a Azure Web App? Using AAD for authentication and the Blazor Upload calls to the same controller work fine. I tried to get the User Token when the app starts, but it is null. HttpClient client=ClientFactory.CreateClient(); var response=await client.PostAsJsonAsync<UploadDataViewModel>(ToAbsoluteUrl("api/IntUpload/savenotes"), _model); if (response.IsSuccessStatusCode) { ShowNotification("success", "Notes file was successfully recorded."); } else { ShowNotification("error", "Notes file failed to upload."); } This is what I'm using for authentication in the Program.cs file: builder.Services.AddAuthentication(OpenIdConnectDefaults.AuthenticationScheme) .AddMicrosoftIdentityWebApp(builder.Configuration.GetSection("AzureAd"))
