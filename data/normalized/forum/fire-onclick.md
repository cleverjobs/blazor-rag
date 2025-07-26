# Fire OnClick?

## Question

**Ila** asked on 02 Mar 2021

Is there a way to fire the OnClick event ?

## Answer

**Marin Bratanov** answered on 02 Mar 2021

Hello Ilan, This was posted in the Upload component forum, but it does not have an OnClick event (you can see its list of events in the documentation ). Could you confirm what component you are using and what you are trying to achieve? Regards, Marin Bratanov

### Response

**Ilan** answered on 03 Mar 2021

I'm using the Upload component, I would like to open the choose file window automatically

### Response

**Marin Bratanov** answered on 03 Mar 2021

Hi Ilan, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1475231-trigger-file-select-dialog-from-my-own-button.](https://feedback.telerik.com/blazor/1475231-trigger-file-select-dialog-from-my-own-button.) The thread also offers a solution you can use right now. Regards, Marin Bratanov

### Response

**Ilan** answered on 03 Mar 2021

How can I call this from within a c# method? That didn't work for me: public async Task OnLogoClick() { var script="$('.k-upload input').click()"; await JS.InvokeVoidAsync(script); }

### Response

**Marin Bratanov** answered on 03 Mar 2021

Hello Ilan, You can use the JavScript Interop that the framework provides: [https://docs.microsoft.com/en-us/aspnet/core/blazor/call-javascript-from-dotnet?view=aspnetcore-5.0](https://docs.microsoft.com/en-us/aspnet/core/blazor/call-javascript-from-dotnet?view=aspnetcore-5.0) Regards, Marin Bratanov

### Response

**Ilan** answered on 03 Mar 2021

I've tried that but got Microsoft.JSInterop.JSException: '$ is not defined _Host.cshtml window.customUploadClick=function () { $('.k-upload-button input').trigger('click'); return "done"; } Interop public async Task<string> Upload() { return await _js.InvokeAsync<string>("customUploadClick"); } What am I missing?

### Response

**Ilan** answered on 03 Mar 2021

jquery was missing, my bad

### Response

**Marin Bratanov** answered on 03 Mar 2021

If you don't use jQuery already you don't have to add it, I've updated the other example with plain dom methods: @inject IJSRuntime _js

<script suppress-error="BL9992"> window.customUploadClick=function ( ) { document.querySelector( ".k-upload-button input" ).click();
}
</script> <TelerikButton OnClick="@InvokeSelectClick"> invoke click </TelerikButton> <TelerikUpload> </TelerikUpload> @code{ async Task InvokeSelectClick()
{ await _js.InvokeVoidAsync( "customUploadClick" );
}
} --Marin
